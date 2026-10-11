// A thin iOS shell around the built page. The page's files are copied into the app under www/. A small http server inside the
// app (class Loopback) serves them at http://127.0.0.1:41730/ to a WKWebView, with byte ranges, which video needs. It listens on
// the loopback address only, so nothing outside the phone can reach it, and its port is fixed, so the page's origin, and with it
// everything the page keeps in Cache Storage, stays the same from one launch to the next. A loopback address is a potentially
// trustworthy origin under the Secure Contexts rules, which camera access, workers and Cache Storage ask for, and Cache Storage
// takes its http addresses as names (at app://localhost/ it refuses them, so the larger model could not be kept there).
// If the server cannot start, the shell falls back to a URL scheme handler that serves the same files at app://localhost/.
// The shell grants the page's camera request (iOS 15 and later); the system asks the person first, with the sentence in
// Info.plist. Every three seconds it writes what the page reports about itself (window.__selftest, the screen it shows) to
// Documents/state.json, and the page's console errors to Documents/log.txt, where the simulator's data container shows them.
// Launch arguments for tests: -q <query string for index.html>, -url <any address instead>, -app (use app://localhost/),
// -probe <path of a script in the bundle to add to the page after it loads>, -js <script to run six seconds after it loads>.
// Build for the simulator: see ci/native/ios.sh (swiftc, no Xcode project).

import Network
import UIKit
import WebKit

let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]

func note(_ s: String) {
    let line = String(format: "%.1f ", Date().timeIntervalSince1970) + s + "\n"
    print(line, terminator: "")
    let url = docs.appendingPathComponent("log.txt")
    if let h = try? FileHandle(forWritingTo: url) {
        h.seekToEndOfFile()
        h.write(line.data(using: .utf8)!)
        h.closeFile()
    } else {
        try? line.write(to: url, atomically: true, encoding: .utf8)
    }
}

let contentTypes: [String: String] = [
    "html": "text/html", "js": "text/javascript", "mjs": "text/javascript", "json": "application/json",
    "webmanifest": "application/manifest+json", "wasm": "application/wasm", "png": "image/png", "jpg": "image/jpeg",
    "jpeg": "image/jpeg", "webm": "video/webm", "mp4": "video/mp4", "woff2": "font/woff2", "css": "text/css",
    "svg": "image/svg+xml", "txt": "text/plain", "md": "text/plain", "csv": "text/csv",
]

func byteRange(_ s: String, count: Int) -> ClosedRange<Int>? {
    guard s.hasPrefix("bytes="), count > 0 else { return nil }
    let parts = s.dropFirst(6).split(separator: "-", omittingEmptySubsequences: false)
    guard parts.count == 2 else { return nil }
    if parts[0].isEmpty, let n = Int(parts[1]) { return max(0, count - n)...(count - 1) }
    guard let a = Int(parts[0]), a < count else { return nil }
    let b = Int(parts[1]) ?? (count - 1)
    return a...min(b, count - 1)
}

// The page's files over http on 127.0.0.1 only: GET and HEAD, byte ranges, one request for each connection.
final class Loopback {
    let root: URL
    let port: UInt16
    let queue = DispatchQueue(label: "org.seenback.loopback")
    var listener: NWListener?
    var reported = false
    var up = false
    var onStart: ((Bool) -> Void)?

    init(root: URL, port: UInt16) {
        self.root = root.standardizedFileURL
        self.port = port
    }

    var address: String { return "http://127.0.0.1:\(port)/" }

    // Calls back once on the main queue: true when the listener is ready, false when it could not start within three seconds.
    func start(_ done: @escaping (Bool) -> Void) {
        onStart = done
        listen(attempt: 1)
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) { [weak self] in self?.report(false) }
    }

    func report(_ ok: Bool) {
        DispatchQueue.main.async { [weak self] in
            guard let self = self, !self.reported else { return }
            self.reported = true
            self.onStart?(ok)
        }
    }

    func listen(attempt: Int) {
        guard let p = NWEndpoint.Port(rawValue: port) else { note("loopback: no port \(port)"); report(false); return }
        let params = NWParameters.tcp
        params.allowLocalEndpointReuse = true
        let l: NWListener
        do {
            if attempt == 1 {
                params.requiredLocalEndpoint = NWEndpoint.hostPort(host: NWEndpoint.Host("127.0.0.1"), port: p)
                l = try NWListener(using: params)
            } else {
                params.requiredInterfaceType = .loopback
                l = try NWListener(using: params, on: p)
            }
        } catch {
            note("loopback: attempt \(attempt) could not make a listener: \(error)")
            if attempt == 1 { listen(attempt: 2) } else { report(false) }
            return
        }
        l.stateUpdateHandler = { [weak self] st in
            guard let self = self else { return }
            switch st {
            case .ready:
                note("loopback: listening at \(self.address) (attempt \(attempt))")
                self.up = true
                self.report(true)
            case .failed(let e):
                note("loopback: attempt \(attempt) failed: \(e)")
                l.cancel()
                if self.up {
                    self.queue.asyncAfter(deadline: .now() + 1) { self.listen(attempt: attempt) }
                } else if attempt == 1 {
                    self.listen(attempt: 2)
                } else {
                    self.report(false)
                }
            default:
                break
            }
        }
        l.newConnectionHandler = { [weak self] c in self?.serve(c) }
        listener = l
        l.start(queue: queue)
    }

    // After the app comes back to the foreground: start again if the system has closed the listener while it was suspended.
    func revive() {
        queue.async { [weak self] in
            guard let self = self, let l = self.listener else { return }
            if case .ready = l.state { return }
            note("loopback: listener was not ready on return to the foreground; starting it again")
            l.cancel()
            self.listen(attempt: 1)
        }
    }

    func serve(_ c: NWConnection) {
        c.start(queue: queue)
        read(c, Data())
    }

    func read(_ c: NWConnection, _ buf: Data) {
        c.receive(minimumIncompleteLength: 1, maximumLength: 65536) { [weak self] data, _, isComplete, error in
            guard let self = self else { c.cancel(); return }
            var b = buf
            if let d = data { b.append(d) }
            if let r = b.range(of: Data("\r\n\r\n".utf8)) {
                self.respond(c, String(decoding: b.subdata(in: 0..<r.lowerBound), as: UTF8.self))
            } else if error != nil || isComplete || b.count > 65536 {
                c.cancel()
            } else {
                self.read(c, b)
            }
        }
    }

    func respond(_ c: NWConnection, _ head: String) {
        let lines = head.components(separatedBy: "\r\n")
        let first = (lines.first ?? "").split(separator: " ").map(String.init)
        guard first.count >= 2 else { c.cancel(); return }
        let method = first[0]
        var path = first[1]
        if let q = path.firstIndex(where: { $0 == "?" || $0 == "#" }) { path = String(path[..<q]) }
        path = path.removingPercentEncoding ?? path
        if path.isEmpty || path.hasSuffix("/") { path += "index.html" }
        var range: String? = nil
        for line in lines.dropFirst() {
            let kv = line.split(separator: ":", maxSplits: 1).map { $0.trimmingCharacters(in: .whitespaces) }
            if kv.count == 2 && kv[0].lowercased() == "range" { range = kv[1] }
        }
        let rel = path.hasPrefix("/") ? String(path.dropFirst()) : path
        let file = root.appendingPathComponent(rel).standardizedFileURL
        var status = 200
        var reason = "OK"
        var body = Data()
        var headers: [(String, String)] = [("Access-Control-Allow-Origin", "*"), ("Cache-Control", "no-cache")]
        if method != "GET" && method != "HEAD" {
            status = 405; reason = "Method Not Allowed"; body = Data("method not allowed".utf8)
            headers.append(("Content-Type", "text/plain"))
        } else if !file.path.hasPrefix(root.path + "/"), file.path != root.path {
            status = 404; reason = "Not Found"; body = Data("not found".utf8)
            headers.append(("Content-Type", "text/plain"))
        } else if let data = try? Data(contentsOf: file, options: .mappedIfSafe) {
            headers.append(("Content-Type", contentTypes[file.pathExtension.lowercased()] ?? "application/octet-stream"))
            headers.append(("Accept-Ranges", "bytes"))
            body = data
            if let rs = range, let r = byteRange(rs, count: data.count) {
                body = data.subdata(in: r.lowerBound..<(r.upperBound + 1))
                headers.append(("Content-Range", "bytes \(r.lowerBound)-\(r.upperBound)/\(data.count)"))
                status = 206; reason = "Partial Content"
            }
        } else {
            note("404 \(path)")
            status = 404; reason = "Not Found"; body = Data("not found".utf8)
            headers.append(("Content-Type", "text/plain"))
        }
        var h = "HTTP/1.1 \(status) \(reason)\r\n"
        for (k, v) in headers { h += k + ": " + v + "\r\n" }
        h += "Content-Length: \(body.count)\r\nConnection: close\r\n\r\n"
        if method == "HEAD" || body.isEmpty {
            c.send(content: Data(h.utf8), completion: .contentProcessed { _ in c.cancel() })
        } else {
            c.send(content: Data(h.utf8), completion: .contentProcessed { _ in })
            c.send(content: body, completion: .contentProcessed { _ in c.cancel() })
        }
    }
}

final class Files: NSObject, WKURLSchemeHandler {
    let root: URL
    init(root: URL) { self.root = root }

    func webView(_ webView: WKWebView, start task: WKURLSchemeTask) {
        guard let url = task.request.url else { return }
        var path = url.path
        if path.isEmpty || path.hasSuffix("/") { path += "index.html" }
        let rel = path.hasPrefix("/") ? String(path.dropFirst()) : path
        let file = root.appendingPathComponent(rel)
        guard let data = try? Data(contentsOf: file, options: .mappedIfSafe) else {
            note("404 \(path)")
            let r = HTTPURLResponse(url: url, statusCode: 404, httpVersion: "HTTP/1.1", headerFields: ["Content-Type": "text/plain"])!
            task.didReceive(r)
            task.didReceive(Data("not found".utf8))
            task.didFinish()
            return
        }
        let type = contentTypes[file.pathExtension.lowercased()] ?? "application/octet-stream"
        var headers = ["Content-Type": type, "Access-Control-Allow-Origin": "*", "Cache-Control": "no-cache", "Accept-Ranges": "bytes"]
        var status = 200
        var body = data
        if let range = task.request.value(forHTTPHeaderField: "Range"), let r = byteRange(range, count: data.count) {
            body = data.subdata(in: r.lowerBound..<(r.upperBound + 1))
            headers["Content-Range"] = "bytes \(r.lowerBound)-\(r.upperBound)/\(data.count)"
            status = 206
        }
        headers["Content-Length"] = String(body.count)
        let r = HTTPURLResponse(url: url, statusCode: status, httpVersion: "HTTP/1.1", headerFields: headers)!
        task.didReceive(r)
        task.didReceive(body)
        task.didFinish()
    }

    func webView(_ webView: WKWebView, stop task: WKURLSchemeTask) {}

}

final class VC: UIViewController, WKScriptMessageHandler, WKUIDelegate, WKNavigationDelegate {
    var web: WKWebView!
    var timer: Timer?
    var probe: String?
    var probed = false
    var js: String?
    var jsDone = false
    var loop: Loopback?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .black
        let cfg = WKWebViewConfiguration()
        let www = Bundle.main.resourceURL!.appendingPathComponent("www")
        cfg.setURLSchemeHandler(Files(root: www), forURLScheme: "app")
        cfg.allowsInlineMediaPlayback = true
        cfg.mediaTypesRequiringUserActionForPlayback = []
        let uc = WKUserContentController()
        uc.add(self, name: "log")
        let hook = """
        (function () {
          var post = function (k, a) {
            try {
              var s = Array.prototype.map.call(a, function (x) { try { return typeof x === 'string' ? x : JSON.stringify(x); } catch (e) { return String(x); } }).join(' ');
              window.webkit.messageHandlers.log.postMessage(k + ' ' + s.slice(0, 600));
            } catch (e) {}
          };
          ['error', 'warn'].forEach(function (k) { var o = console[k]; console[k] = function () { post(k, arguments); return o.apply(console, arguments); }; });
          window.addEventListener('error', function (e) { post('pageerror', [e.message + ' @' + e.filename + ':' + e.lineno]); });
          window.addEventListener('unhandledrejection', function (e) { var r = e.reason; post('rejection', [String(r && (r.stack || r.message) || r)]); });
        })();
        """
        uc.addUserScript(WKUserScript(source: hook, injectionTime: .atDocumentStart, forMainFrameOnly: true))
        cfg.userContentController = uc
        web = WKWebView(frame: view.bounds, configuration: cfg)
        web.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        web.uiDelegate = self
        web.navigationDelegate = self
        if #available(iOS 16.4, *) { web.isInspectable = true }
        view.addSubview(web)
        let args = ProcessInfo.processInfo.arguments
        func arg(_ k: String) -> String? {
            if let i = args.firstIndex(of: k), i + 1 < args.count { return args[i + 1] }
            return nil
        }
        let q = arg("-q").map { "?" + $0 } ?? ""
        probe = arg("-probe")
        js = arg("-js")
        if let full = arg("-url") {
            go(full)
        } else if args.contains("-app") {
            go("app://localhost/index.html" + q)
        } else {
            let l = Loopback(root: www, port: 41730)
            loop = l
            l.start { [weak self] ok in
                if !ok { note("loopback did not start; serving the page at app://localhost/ instead") }
                self?.go((ok ? l.address : "app://localhost/") + "index.html" + q)
            }
        }
        timer = Timer.scheduledTimer(withTimeInterval: 3, repeats: true) { [weak self] _ in self?.poll() }
    }

    func go(_ target: String) {
        note("open " + target)
        if let u = URL(string: target) { web.load(URLRequest(url: u)) } else { note("not an address: " + target) }
    }

    func poll() {
        let js = "JSON.stringify({st: window.__selftest || null, sb: !!window.__seenBack,"
            + " screen: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.screen : null,"
            + " src: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.src : null,"
            + " big: window.__bigProbe || null,"
            + " md: !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia),"
            + " href: location.href, secure: window.isSecureContext, coi: window.crossOriginIsolated, ua: navigator.userAgent})"
        web.evaluateJavaScript(js) { r, e in
            if let s = r as? String {
                try? s.write(to: docs.appendingPathComponent("state.json"), atomically: true, encoding: .utf8)
            } else if let e = e {
                note("poll error " + e.localizedDescription)
            }
        }
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        note("console " + String(describing: message.body))
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        note("page finished " + (webView.url?.absoluteString ?? ""))
        if let p = probe, !probed, p.range(of: "^[A-Za-z0-9_./-]+$", options: .regularExpression) != nil {
            probed = true
            DispatchQueue.main.asyncAfter(deadline: .now() + 4) { [weak self] in
                let js = "(function(){var s=document.createElement('script');s.src='" + p + "';document.head.appendChild(s);})()"
                self?.web.evaluateJavaScript(js) { _, e in note("probe " + p + " injected" + (e.map { " with error " + $0.localizedDescription } ?? "")) }
            }
        }
        if let j = js, !jsDone {
            jsDone = true
            DispatchQueue.main.asyncAfter(deadline: .now() + 6) { [weak self] in
                self?.web.evaluateJavaScript(j) { r, e in
                    note("js -> " + String(describing: r) + (e.map { " with error " + $0.localizedDescription } ?? ""))
                }
            }
        }
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        note("navigation failed " + error.localizedDescription)
    }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
        note("provisional navigation failed " + error.localizedDescription)
    }

    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        note("the web content process ended")
    }

    @available(iOS 15.0, *)
    func webView(_ webView: WKWebView, requestMediaCapturePermissionFor origin: WKSecurityOrigin, initiatedByFrame frame: WKFrameInfo,
                 type: WKMediaCaptureType, decisionHandler: @escaping (WKPermissionDecision) -> Void) {
        note("camera request from " + origin.protocol + "://" + origin.host + " granted")
        decisionHandler(.grant)
    }
}

final class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        let w = UIWindow(frame: UIScreen.main.bounds)
        w.rootViewController = VC()
        w.makeKeyAndVisible()
        window = w
        note("launched")
        return true
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        (window?.rootViewController as? VC)?.loop?.revive()
    }
}

UIApplicationMain(CommandLine.argc, CommandLine.unsafeArgv, nil, NSStringFromClass(AppDelegate.self))
