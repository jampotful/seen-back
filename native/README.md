# Native shells

This directory holds two thin native shells around the built page, one for Android and one for the iPhone. The scripts in `ci/native/` build them and run them on GitHub's build machines. Each shell carries a copy of the built page and serves it to the system's own web view from inside the app, so the page itself is unchanged. Nothing here is signed for a store, and nothing here has run on a real phone: every result below comes from an Android emulator or an iPhone simulator on a build machine.

## What is here

| Path | What it is |
|---|---|
| `native/android-shell/` | A Gradle project (Android Gradle Plugin 8.7.3, compile and target SDK 35, minimum SDK 24, Java 17) with one activity in Java and no libraries. The activity shows a WebView and answers every request for `https://appassets.androidplatform.net/` from the files packed under `assets/www/` in the APK, with its own table of content types (the WebAssembly runtime's `.mjs` file is a module script, which must arrive with a JavaScript type). That address is a secure origin that never reaches the network, so the page keeps camera access, workers and Cache Storage. When the page asks for the camera, the shell asks the person for Android's camera permission and then grants the page's request. |
| `native/ios-shell/` | `main.swift` and `Info.plist`: a UIKit app with one WKWebView, compiled with `swiftc` for the iPhone simulator. There is no Xcode project yet. A URL scheme handler serves the bundled files at `app://localhost/`, with byte ranges for video. The host name `localhost` makes the origin potentially trustworthy under the Secure Contexts rules, and the page reported `isSecureContext` true there. The shell grants the page's camera request after iOS has asked the person, with the sentence in `Info.plist`. |
| `ci/native/bundle.sh` | Copies the built page and what it fetches into one directory: `index.html`, `sw.js`, `selftest.js`, `manifest.webmanifest`, `vendor/`, `fonts/`, `icons/`, `labels/`, `models/pocket/`, and `models/naturalist/` (the larger model's rows and manifest; its 310 MB encoder still comes from the network, as on the web). For the checks it adds `test/assets/`, `test/rec/photos/` and `native-probe/big.js`; `TEST=0` leaves them out. The page fetches nothing under `data/`, so `data/` stays out. |
| `ci/native/android_build.sh`, `ci/native/android_emu.sh` | The Android job: build the page, bundle it, run `gradle assembleDebug`, then in an emulator open the app, run the page's self-test with the pocket recognizer, press Begin with the emulator's camera, and fetch the larger model through the page's own recognizer. |
| `ci/native/ios.sh` | The iOS job: build the page, compile the shell, copy the page into the app, sign it ad hoc, install it in an iPhone simulator and run the same self-test inside it. A label starting with `ios-big` fetches the larger model instead of the comparison run. |
| `ci/native/probe-big.js` | Used only by the checks. It fetches the larger model the way the consent sheet's "Get it" does (download, verify, keep, start the encoder) and then names four photos with it. |
| `.github/workflows/native.yml` | Starts both jobs on a push to `run/native/<label>`. |

The shells read a few launch options that only the checks use: the Android intent extras `q` (a query string for `index.html`), `url`, `js` and `probe`, and the iOS launch arguments `-q`, `-url` and `-probe`. Every three seconds each shell writes what the page reports about itself (`window.__selftest`, the screen it shows, `window.__bigProbe`) to a file in the app's own storage, which the checks read with `adb shell run-as` on Android and from the simulator's data container on iOS.

## What ran, and what it showed

Results are on the `ci` branch under `runs/native/<run number>-android/` and `runs/native/<run number>-ios/`. Each holds the job's log, screenshots as JPEG, and the page's own report as JSON.

### Android: run 1 (`runs/native/1-android/`, commit `6c7868f`)

- **Build.** `ubuntu-latest` (4 cores, 16 GB), JDK 17.0.20.1, Gradle 8.10.2. `gradle assembleDebug` took 46 s. The debug APK is 55,827,719 bytes; it holds 50 files, 73,457,980 bytes before compression (`android/build-log.txt`). Gradle made the debug keystore on the build machine, and it was neither committed nor returned.
- **Emulator.** Android 14 (API 34, `google_apis`, x86_64) with 4 GB of memory, `-gpu swiftshader_indirect`, Android System WebView 113.0.5672.136 (`android/emu-log.txt`).
- **The opening screen** appears as on the web (`android/shots/1-open.jpg`). The page reports `isSecureContext` true and `crossOriginIsolated` false.
- **The page's self-test** (`?selftest=1&nosw=1` with `rec=models/pocket` and four photos from `test/rec/photos`) finished in 47.6 s: all 98 checks passed. WebGL 2 is present, float render targets work, and the renderer is "Android Emulator OpenGL ES Translator (Google SwiftShader)" (`android/selftest-state.json`, `android/shots/2-selftest-final.jpg`).
- **The pocket recognizer** became ready in 7.5 s (session 2.2 s, warm-up 4.5 s) on the WASM backend with one thread, and took 1.9, 1.2, 0.8 and 0.5 s for the four photos. It gave the same kinds as in the browsers: wader for `heron.png`, person for `portrait.jpg`, none for `wall.png`, plant for `garden.jpg`.
- **Begin with the emulator's camera.** The shell granted the page's camera request, and the page reached its finder screen with the camera as its source (`android/state-begin.json`, `android/shots/3-begin.jpg`, which shows the emulator's built-in camera scene through the page).
- **Console.** Two messages in all, both the browser's advice to set `willReadFrequently` on a canvas (`android/logcat-seenback.txt`).

The emulator runs on a server processor with hardware virtualization, so its times say nothing about a phone's.

### iOS: run 2 (`runs/native/2-ios/`, commit `8be197a`)

- **Build.** `macos-latest` (macOS 26.6.2, arm64, 7.5 GB), Xcode 26.6, iPhone simulator SDK 26.5. `swiftc` compiled `main.swift` without errors; the app was signed ad hoc and installed in an iPhone 17 simulator running iOS 26.5. The app is 71,992 kB on disk, and 54,406,286 bytes when zipped the way an `.ipa` is (`ios/log.txt`).
- **The opening screen** appears as in Safari (`ios/shots/1-open.jpg`). The page reports `isSecureContext` true at `app://localhost/` and `crossOriginIsolated` false. Its user agent names "iPhone OS 18_7", although the simulator runs iOS 26.5.
- **The page's self-test inside the app** finished in 28.3 s: all 98 checks passed. WebGL 2 is present, float render targets work, the renderer is "Apple GPU", and the test video played as MP4 through the scheme handler (`ios/2-selftest-state.json`, `ios/shots/2-selftest-final.jpg`).
- **The pocket recognizer** became ready in 1.7 s on the WASM backend with one thread and took 0.64, 0.64, 0.65 and 0.52 s for the four photos, with the same four kinds as on Android.
- **For comparison**, the same app pointed at the page served from the Mac (`http://127.0.0.1:8781`) also passed all 98 checks (ready in 3.2 s, 0.6 to 0.8 s a photo; `ios/3-served-state.json`, `reports/ios-served.json`).
- **The app's own log** holds no console error or warning and no file it could not serve (`ios/app-log.txt`).
- **Not checked:** the simulator has no camera, so the camera request inside the iOS shell has not been tried. The simulator also borrows the Mac's memory, so a pass there does not show that a real iPhone holds the same load.

### The larger model inside the shells

**Android, run 3** (`runs/native/3-android/`, commit `92283a2`; the same build and emulator as run 1, whose self-test passed again with all 98 checks). The probe called the page's own `get()` for the larger model (`models/naturalist`) inside the WebView (`android/big-state.json`, `android/big-memory.txt`, `android/emu-log.txt`):

- The four parts, 309,812,341 bytes in all, came from `raw.githubusercontent.com`, were verified and kept, and the encoder started, 106.5 s after the call. Of that, starting the encoder took 43.3 s (session 8.1 s, warm-up 28.9 s); the rest was the download and its checks.
- `navigator.storage.estimate()` gave 126,612,835 bytes in use before (from the earlier steps of the same run) and 446,307,171 after, with a quota of 3,736,869,273 bytes.
- The four photos took 28.9 s (`heron.png`, wader), 25.7 s (`portrait.jpg`, other), 23.6 s (`garden.jpg`, plant) and 22.2 s (`wall.png`, other, not sure) on the WASM backend with one thread.
- The WebView's renderer process reached 1,585 MB of resident memory at its peak, sampled every 4 s with `ps`; the app's own process reached 210 MB, and the emulator's available memory fell to 771 MB of its 4 GB. Nothing was killed and the page did not reload.

IOS_BIG_RESULTS

## Commands

Start both jobs on build machines (a label starting with `android` runs only the Android job, one starting with `ios` only the iOS job), wait, and read the results:

```
git push -f origin HEAD:refs/heads/run/native/<label>
bash ci/wait.sh <commit> <results expected> 540
git fetch origin ci && git show FETCH_HEAD:runs/native/<run number>-android/android/emu-log.txt
```

Build the APK on a computer with the Android SDK, JDK 17 and Gradle 8.10, and install it on a phone with USB debugging on:

```
python3 -I build.py
TEST=0 bash ci/native/bundle.sh native/android-shell/app/src/main/assets/www
mkdir -p native/android-shell/app/src/main/res/mipmap-xxxhdpi
cp icons/icon-192.png native/android-shell/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png
(cd native/android-shell && gradle assembleDebug)
adb install -r native/android-shell/app/build/outputs/apk/debug/app-debug.apk
```

Build the iOS shell for the simulator on a Mac with Xcode:

```
python3 -I build.py
APP=build-ios/SeenBack.app; mkdir -p "$APP"
xcrun --sdk iphonesimulator swiftc -swift-version 5 -module-name SeenBack -O -target arm64-apple-ios16.0-simulator \
  -sdk "$(xcrun --sdk iphonesimulator --show-sdk-path)" -o "$APP/SeenBack" native/ios-shell/main.swift
cp native/ios-shell/Info.plist "$APP/"; TEST=0 bash ci/native/bundle.sh "$APP/www"; codesign --force --sign - "$APP"
xcrun simctl install booted "$APP" && xcrun simctl launch booted org.seenback.shell
```

## A build for the owner's own iPhone

A real iPhone runs only apps signed with a certificate that Apple has issued. For the owner's own phone, an Apple ID signed in to Xcode on their Mac is enough (Xcode, Settings, Accounts; the free "Personal Team"). The steps:

1. In Xcode, make a new iOS App project with the UIKit interface. Delete its generated Swift files and its main storyboard, remove the scene and storyboard entries from the project's Info settings, add `native/ios-shell/main.swift`, and copy the keys of `native/ios-shell/Info.plist` into the Info settings, the camera sentence among them.
2. Make the page's files with `TEST=0 bash ci/native/bundle.sh www` and add the `www` directory to the project as a folder reference, so that its paths are kept.
3. Give the app a bundle identifier of the owner's own (for example one ending in `.seenback`), and choose the Personal Team under Signing and Capabilities.
4. Connect the iPhone, turn on Developer Mode on it (Settings, Privacy and Security), press Run, and on the first launch trust the developer on the phone (Settings, General, VPN and Device Management).

What the free tier allows, from Apple's page "Choosing a Membership" (developer.apple.com/support/compare-memberships, read on 11 October 2026): up to 10 App IDs and up to 3 devices, each expiring after 7 days; up to 3 apps on a device; provisioning profiles that expire 7 days after they are issued, so the app has to be built and installed from Xcode again every week. TestFlight, App Store Connect and the App Store need the Apple Developer Program.

The build machine cannot do this part: it has no Apple ID and no phone, and this repository holds no signing identity.

## The distance to the two stores

**Google Play.** What Google's help pages say (support.google.com/googleplay/android-developer, answers 6112435 and 14151465, read on 11 October 2026): a Play Console account costs US$25 once, and its holder must verify their identity with a government ID and a card in their legal name. A personal account created after 13 November 2023 must run a closed test with at least 12 testers, opted in for at least 14 days without a break, before it may apply to publish, and a new personal account must also show that it has an Android device through the Play Console app. The following come from general knowledge of Google's rules and were not read tonight: a new app is uploaded as an Android App Bundle signed with an upload key that the owner makes and keeps, and an app that asks for the camera needs a privacy policy and a completed Data safety form. The shell already targets API level 35. A release build needs a signing configuration in `app/build.gradle` and `gradle bundleRelease`; neither exists yet.

**The App Store.** The Apple Developer Program costs 99 USD a membership year, and Apple's page says that non-profit organizations, accredited educational institutions and government entities may be eligible for a fee waiver. Guideline 4.2 of the App Store Review Guidelines ("Minimum Functionality") says: "Your app should include features, content, and UI that elevate it beyond a repackaged website." I read that sentence in copies of the guidelines reached through a web search, and did not open Apple's page tonight. The shell is the page in a web view, so a reviewer will judge what the page does: the camera's change of eyes, the recognizer that runs on the phone, and use without a network. Whether that passes review cannot be known from here. A camera app also needs the camera sentence (present in `Info.plist`), a privacy policy and the App Privacy answers in App Store Connect; those last two come from general knowledge of Apple's rules and were not read tonight. A build for the store also needs an Xcode project, an app icon set and a launch screen made in Xcode.

**Size, with and without the larger model.** Without the larger model, the debug APK of run 1 is 55,827,719 bytes, and the iOS app of run 2 is 54,406,286 bytes zipped. Both hold the check files (about 1.1 MB) and the larger model's rows (9.9 MB in `models/naturalist/`); the encoder of the pocket model is 40,978,137 bytes of that. Built into the app, the larger model would add its 309,812,341 bytes of encoder parts (from `models/naturalist/manifest.json`); no such build was made tonight, and how far those bytes compress was not measured. The shells as they stand keep the web page's behaviour: the larger model is downloaded once, with the person's consent, and kept in the web view's Cache Storage.

## What is open

- Nothing has run on a real phone. The camera inside the iOS shell, the memory a real phone gives the web view, and the time a photo takes on a phone are all unmeasured.
- In the emulator the app's camera permission was granted at install (`adb install -g`), so Android's own permission prompt and the shell's path through it were not seen.
- The page keeps its own copies of model files in Cache Storage. Inside a shell the files are already in the app, so a phone may hold them twice; this was not measured.
- The service worker was switched off in every run (`nosw=1` in the self-test, and the opening screen was not checked for it). The Android shell answers the service worker's requests from the bundle as well; whether a service worker registers at `app://localhost/` on iOS was not tried. The shells do not need it for use without a network, because their files are in the app.
- The page's text still speaks of a download from the web where a shell already holds the files; no wording was changed, because the page is not this area's to change.
