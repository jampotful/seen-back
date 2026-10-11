// A thin iOS shell around the built page. The page's files are copied into the app under www/ and served to a WKWebView
// at app://localhost/ by a URL scheme handler (with byte ranges, which video needs), so nothing is fetched from the network
// except what the page itself fetches from other origins (the larger model's parts). The host "localhost" makes the origin a
// potentially trustworthy one under the Secure Contexts rules, which camera access, workers and Cache Storage ask for.
// The shell grants the page's camera request (iOS 15 and later); the system asks the person first, with the sentence in
// Info.plist. Every three seconds it writes what the page reports about itself (window.__selftest, the screen it shows) to
// Documents/state.json, and the page's console errors to Documents/log.txt, where the simulator's data container shows them.
// Launch arguments for tests: -q <query string for index.html>, -url <any address instead>.
// Build for the simulator: see ci/native/ios.sh (swiftc, no Xcode project).

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

final class Files: NSObject, WKURLSchemeHandler {
    let root: URL
    init(root: URL) { self.root = root }

    static let types: [String: String] = [
        "html": "text/html", "js": "text/javascript", "mjs": "text/javascript", "json": "application/json",
        "webmanifest": "application/manifest+json", "wasm": "application/wasm", "png": "image/png", "jpg": "image/jpeg",
        "jpeg": "image/jpeg", "webm": "video/webm", "mp4": "video/mp4", "woff2": "font/woff2", "css": "text/css",
        "svg": "image/svg+xml", "txt": "text/plain", "md": "text/plain", "csv": "text/csv",
    ]

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
        let type = Files.types[file.pathExtension.lowercased()] ?? "application/octet-stream"
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

    func byteRange(_ s: String, count: Int) -> ClosedRange<Int>? {
        guard s.hasPrefix("bytes="), count > 0 else { return nil }
        let parts = s.dropFirst(6).split(separator: "-", omittingEmptySubsequences: false)
        guard parts.count == 2 else { return nil }
        if parts[0].isEmpty, let n = Int(parts[1]) { return max(0, count - n)...(count - 1) }
        guard let a = Int(parts[0]), a < count else { return nil }
        let b = Int(parts[1]) ?? (count - 1)
        return a...min(b, count - 1)
    }
}

final class VC: UIViewController, WKScriptMessageHandler, WKUIDelegate, WKNavigationDelegate {
    var web: WKWebView!
    var timer: Timer?

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
        var target = "app://localhost/index.html"
        if let i = args.firstIndex(of: "-q"), i + 1 < args.count { target += "?" + args[i + 1] }
        if let i = args.firstIndex(of: "-url"), i + 1 < args.count { target = args[i + 1] }
        note("open " + target)
        if let u = URL(string: target) { web.load(URLRequest(url: u)) } else { note("not an address: " + target) }
        timer = Timer.scheduledTimer(withTimeInterval: 3, repeats: true) { [weak self] _ in self?.poll() }
    }

    func poll() {
        let js = "JSON.stringify({st: window.__selftest || null, sb: !!window.__seenBack,"
            + " screen: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.screen : null,"
            + " src: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.src : null,"
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
}

UIApplicationMain(CommandLine.argc, CommandLine.unsafeArgv, nil, NSStringFromClass(AppDelegate.self))
