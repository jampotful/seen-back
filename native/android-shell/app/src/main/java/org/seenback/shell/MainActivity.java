package org.seenback.shell;

// A thin Android shell around the built page. The page's files are packed in the APK under assets/www and served to
// the WebView at https://appassets.androidplatform.net/ (a secure origin that never reaches the network), so the page
// keeps camera access, workers, WebAssembly and Cache Storage. The shell grants the page's camera request once the
// person has granted the app's own camera permission. Every three seconds it writes what the page reports about itself
// (window.__selftest, the screen it shows) to files/state.json, which a debug build lets `adb shell run-as` read.
// Intent extras for tests: "q" (a query string for index.html), "url" (any address instead), "js" (run after the page loads).

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.webkit.ConsoleMessage;
import android.webkit.PermissionRequest;
import android.webkit.ServiceWorkerClient;
import android.webkit.ServiceWorkerController;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import org.json.JSONTokener;

import java.io.ByteArrayInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class MainActivity extends Activity {
    static final String TAG = "SeenBack";
    static final String HOST = "appassets.androidplatform.net";
    static final String STATE_JS = "JSON.stringify({st: window.__selftest || null, sb: !!window.__seenBack,"
            + " screen: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.screen : null,"
            + " src: (window.__seenBack && window.__seenBack.S) ? window.__seenBack.S.src : null,"
            + " href: location.href, secure: window.isSecureContext, coi: window.crossOriginIsolated, ua: navigator.userAgent})";

    WebView web;
    final Handler handler = new Handler(Looper.getMainLooper());
    PermissionRequest pending;
    boolean jsDone;

    @Override
    protected void onCreate(Bundle saved) {
        super.onCreate(saved);
        WebView.setWebContentsDebuggingEnabled(true);
        web = new WebView(this);
        setContentView(web);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);

        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView v, WebResourceRequest r) {
                return serve(r.getUrl());
            }

            @Override
            public void onPageFinished(WebView v, String url) {
                Log.i(TAG, "page finished " + url);
                final String js = getIntent().getStringExtra("js");
                if (js != null && !jsDone) {
                    jsDone = true;
                    handler.postDelayed(() -> web.evaluateJavascript(js, r -> Log.i(TAG, "js -> " + r)), 6000);
                }
            }

            @Override
            public void onReceivedError(WebView v, WebResourceRequest r, WebResourceError e) {
                Log.w(TAG, "load error " + r.getUrl() + " " + e.getErrorCode() + " " + e.getDescription());
            }

            @Override
            public void onReceivedHttpError(WebView v, WebResourceRequest r, WebResourceResponse resp) {
                Log.w(TAG, "http " + resp.getStatusCode() + " " + r.getUrl());
            }
        });
        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onConsoleMessage(ConsoleMessage m) {
                Log.i(TAG + "Console", m.messageLevel() + " " + m.message() + " @" + m.sourceId() + ":" + m.lineNumber());
                return true;
            }

            @Override
            public void onPermissionRequest(PermissionRequest req) {
                runOnUiThread(() -> grant(req));
            }
        });
        ServiceWorkerController.getInstance().setServiceWorkerClient(new ServiceWorkerClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebResourceRequest r) {
                return serve(r.getUrl());
            }
        });

        String q = getIntent().getStringExtra("q");
        String url = "https://" + HOST + "/index.html" + (q != null && !q.isEmpty() ? "?" + q : "");
        String full = getIntent().getStringExtra("url");
        if (full != null && !full.isEmpty()) url = full;
        Log.i(TAG, "open " + url);
        web.loadUrl(url);
        handler.postDelayed(this::poll, 3000);
    }

    WebResourceResponse serve(Uri u) {
        if (!HOST.equals(u.getHost())) return null;
        String p = u.getPath();
        if (p == null || p.isEmpty()) p = "/";
        if (p.endsWith("/")) p += "index.html";
        Map<String, String> headers = new HashMap<>();
        headers.put("Access-Control-Allow-Origin", "*");
        headers.put("Cache-Control", "no-cache");
        String type = mime(p);
        String enc = type.startsWith("text/") || type.endsWith("json") ? "utf-8" : null;
        try {
            InputStream in = getAssets().open("www" + p);
            return new WebResourceResponse(type, enc, 200, "OK", headers, in);
        } catch (IOException e) {
            Log.w(TAG, "404 " + p);
            return new WebResourceResponse("text/plain", "utf-8", 404, "Not Found", headers,
                    new ByteArrayInputStream("not found".getBytes(StandardCharsets.UTF_8)));
        }
    }

    static String mime(String p) {
        String e = p.substring(p.lastIndexOf('.') + 1).toLowerCase(Locale.ROOT);
        switch (e) {
            case "html": return "text/html";
            case "js": case "mjs": return "text/javascript";
            case "json": return "application/json";
            case "webmanifest": return "application/manifest+json";
            case "wasm": return "application/wasm";
            case "png": return "image/png";
            case "jpg": case "jpeg": return "image/jpeg";
            case "webm": return "video/webm";
            case "mp4": return "video/mp4";
            case "woff2": return "font/woff2";
            case "css": return "text/css";
            case "svg": return "image/svg+xml";
            case "txt": case "md": return "text/plain";
            case "csv": return "text/csv";
            default: return "application/octet-stream";
        }
    }

    void grant(PermissionRequest req) {
        if (checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
            req.grant(req.getResources());
            Log.i(TAG, "page's camera request granted");
        } else {
            pending = req;
            requestPermissions(new String[]{Manifest.permission.CAMERA}, 1);
        }
    }

    @Override
    public void onRequestPermissionsResult(int code, String[] perms, int[] results) {
        if (pending == null) return;
        if (results.length > 0 && results[0] == PackageManager.PERMISSION_GRANTED) {
            pending.grant(pending.getResources());
            Log.i(TAG, "camera permission given; page's request granted");
        } else {
            pending.deny();
            Log.i(TAG, "camera permission refused; page's request denied");
        }
        pending = null;
    }

    void poll() {
        web.evaluateJavascript(STATE_JS, v -> {
            try {
                Object o = new JSONTokener(v).nextValue();
                String s = String.valueOf(o);
                write("state.json", s);
                Log.i(TAG, "state " + s.substring(0, Math.min(240, s.length())));
            } catch (Exception e) {
                Log.w(TAG, "poll " + e);
            }
            handler.postDelayed(this::poll, 3000);
        });
    }

    void write(String name, String s) {
        try (FileOutputStream o = openFileOutput(name, MODE_PRIVATE)) {
            o.write(s.getBytes(StandardCharsets.UTF_8));
        } catch (IOException e) {
            Log.w(TAG, "write " + e);
        }
    }
}
