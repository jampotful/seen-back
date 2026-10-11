# Native shells

This directory holds two thin native shells around the built page, one for Android and one for the iPhone. The scripts in `ci/native/` build them and run them on GitHub's build machines. Each shell carries a copy of the built page and serves it to the system's own web view from inside the app, so the page itself is unchanged. The Android shell is also published as a debug APK that a person can install on their own phone (see "The Android file"). Nothing here is signed for a store, and nothing here has run on a real phone: every result below comes from an Android emulator or an iPhone simulator on a build machine.

## What is here

| Path | What it is |
|---|---|
| `native/android-shell/` | A Gradle project (Android Gradle Plugin 8.7.3, compile and target SDK 35, minimum SDK 24, Java 17) with one activity in Java and no libraries. The activity shows a WebView and answers every request for `https://appassets.androidplatform.net/` from the files packed under `assets/www/` in the APK, with its own table of content types (the WebAssembly runtime's `.mjs` file is a module script, which must arrive with a JavaScript type). That address is a secure origin that never reaches the network, so the page keeps camera access, workers and Cache Storage. When the page asks for the camera, the shell asks the person for Android's camera permission and then grants the page's request. |
| `native/ios-shell/` | `main.swift` and `Info.plist`: a UIKit app with one WKWebView, compiled with `swiftc` for the iPhone simulator. There is no Xcode project in the repository; the steps for making one are below. A small http server inside the app (class `Loopback`, written with Apple's Network framework) serves the bundled files at `http://127.0.0.1:41730/`, with byte ranges for video. It listens on the loopback address only, so nothing outside the phone can reach it, and its port is fixed, so the page's origin, and with it what the page keeps in Cache Storage, stays the same from one launch to the next. A loopback address is potentially trustworthy under the Secure Contexts rules. If the server cannot start, the shell serves the same files at `app://localhost/` through a URL scheme handler, as it did before run 7. The shell grants the page's camera request after iOS has asked the person, with the sentence in `Info.plist`; `NSAllowsLocalNetworking` in `Info.plist` lets the web view load an `http` address on the loopback. |
| `ci/native/bundle.sh` | Copies the built page and what it fetches into one directory: `index.html`, `sw.js`, `selftest.js`, `manifest.webmanifest`, `vendor/`, `fonts/`, `icons/`, `labels/`, `models/pocket/`, and `models/naturalist/` (the larger model's rows and manifest; its 310 MB encoder still comes from the network, as on the web). For the checks it adds `test/assets/`, `test/rec/photos/` and `native-probe/big.js`; `TEST=0` leaves them out. The page fetches nothing under `data/`, so `data/` stays out. |
| `ci/native/android_build.sh`, `ci/native/android_emu.sh` | The Android job: build the page, bundle it, run `gradle assembleDebug`, then in an emulator open the app, run the page's self-test with the pocket recognizer, press Begin with the emulator's camera, and fetch the larger model through the page's own recognizer. |
| `ci/native/ios.sh` | The iOS job: build the page, compile the shell, copy the page into the app, sign it ad hoc, install it in an iPhone simulator and run the same self-test inside it. A label starting with `ios-big` runs the larger-model probe instead of the comparison run: once inside the app, and once with the same app pointed at the page served from the Mac. |
| `ci/native/android_pub_build.sh`, `ci/native/android_pub_emu.sh`, `ci/native/android_pub.sh`, `ci/native/android_pub_files.py` | The publishing job (see "The Android file"): two debug APKs from one build of the page, the self-test on the one with the check files, the published one opened in the emulator, and only after both have passed, the file on the branch `pub/app-android` with its `README.md` and `built.json`. |
| `ci/native/probe-big.js` | Used only by the checks. It fetches the larger model the way the consent sheet's "Get it" does (download, verify, keep, start the encoder) and then names four photos with it. |
| `.github/workflows/native.yml` | Starts the jobs on a push to `run/native/<label>`: a label starting with `pub` runs only the publishing job, one starting with `android` only the Android job, one starting with `ios` only the iOS job, and any other label both of the last two. |

The shells read a few launch options that only the checks use: the Android intent extras `q` (a query string for `index.html`), `url`, `js` and `probe`, and the iOS launch arguments `-q`, `-url`, `-app` (serve at `app://localhost/`), `-js` and `-probe`. Every three seconds each shell writes what the page reports about itself (`window.__selftest`, the screen it shows, `window.__bigProbe`) to a file in the app's own storage, which the checks read with `adb shell run-as` on Android and from the simulator's data container on iOS.

## The Android file

A push to `run/native/pub<anything>` builds the page from that commit and makes two debug APKs from that one build, signed with the same debug key, which Gradle makes on the build machine and which goes when the machine does. The first holds the check files (`test/assets/`, `test/rec/photos/`, `native-probe/`); the second is made with `TEST=0` and holds none. `ci/native/android_pub_build.sh` compares the two entry by entry and stops if they differ anywhere outside the check files and the signature files. In an Android 14 emulator the job then runs the page's self-test in the first APK, removes it, installs the second, opens it at its first screen and presses Begin with the emulator's camera. Only when the self-test has passed with no failed check and the second APK has shown its first screen at a secure origin and reached the camera does `ci/native/android_pub.sh` put the second APK on the branch `pub/app-android` as `seen-back-debug.apk`, with a `README.md` for the person installing it and a `built.json` (the commit, the page's build number from `src/cam.a.js`, the file's bytes and SHA-256, the time). It then fetches the file back from `raw.githubusercontent.com` at the branch's new commit and compares the checksum. The job uses only files in `native/`, `ci/native/`, the workflow, `ci/put_branch.sh` and `ci/return.sh`, so it runs from `main` as it does from a working branch.

The file's address for a phone is https://raw.githubusercontent.com/jampotful/seen-back/pub/app-android/seen-back-debug.apk , and the branch's `README.md` says how to install it. Each build is signed with a new throwaway key, so Android will not install a newer file over an older one; the app has to be removed first.

### Run 6 (`runs/native/6-pub/`, commit `731fcab`, label `pub-a`)

- **Build.** The page of build 9. The APK with the check files is 55,324,991 bytes and the published one 54,195,702 bytes; Gradle's second build, after `clean`, took 13 s. The comparison found 51 entries in the first and 36 in the second, all 36 identical in CRC-32 and size; the 15 entries found only in the first are all under `assets/www/test/` and `assets/www/native-probe/` (`android/pub-compare.txt`, `android/pub-build-log.txt`).
- **The self-test**, in the APK with the check files, in the same emulator as run 1 (Android 14, Android System WebView 113.0.5672.136): all 98 checks passed in 47.0 s, at a secure origin (`android/selftest-state.json`, `android/emu-log.txt`).
- **The published APK**, installed fresh in the same emulator, opened at the page's first screen at `https://appassets.androidplatform.net/index.html` with `isSecureContext` true, and Begin took it to the finder with the emulator's camera as its source (`android/pub-state-open.json`, `android/pub-state-begin.json`, `android/shots/5-pub-open.jpg`, `android/shots/6-pub-begin.jpg`; the gate's verdict is in `android/gate.json`).
- **Published.** `pub/app-android` at commit `a1331eb`: `seen-back-debug.apk` (54,195,702 bytes, SHA-256 `2aaaec28013c25f845b21e145809b94a118f94e13139996ed7ac0049dcd75a97`), `README.md`, `built.json`. The job read the file back from `raw.githubusercontent.com` at that commit and found the same checksum, with the type `application/octet-stream` (`android/pub-log.txt`). GitHub's push warned that the file is over its recommended 50 MB and accepted it.

## What ran, and what it showed

Results are on the `ci` branch under `runs/native/<run number>-android/` and `runs/native/<run number>-ios/`. Each holds the job's log, screenshots as JPEG, and the page's own report as JSON.

### Android: run 1 (`runs/native/1-android/`, commit `6c7868f`)

- **Build.** `ubuntu-latest` (4 cores, 16 GB), JDK 17.0.20.1, Gradle 8.10.2. `gradle assembleDebug` took 46 s. The debug APK is 55,827,719 bytes; it holds 50 files, 73,457,980 bytes before compression (`android/build-log.txt`). Gradle made the debug keystore on the build machine, and it was neither committed nor returned.
- **Emulator.** Android 14 (API 34, `google_apis`, x86_64) with 4 GB of memory, `-gpu swiftshader_indirect`, Android System WebView 113.0.5672.136 (`android/emu-log.txt`).
- **The opening screen** appears in full, with its typeface (`android/shots/1-open.jpg`). The page reports `isSecureContext` true and `crossOriginIsolated` false.
- **The page's self-test** (`?selftest=1&nosw=1` with `rec=models/pocket` and four photos from `test/rec/photos`) finished in 47.6 s: all 98 checks passed. WebGL 2 is present, float render targets work, and the renderer is "Android Emulator OpenGL ES Translator (Google SwiftShader)" (`android/selftest-state.json`, `android/shots/2-selftest-final.jpg`).
- **The pocket recognizer** became ready in 7.5 s (session 2.2 s, warm-up 4.5 s) on the WASM backend with one thread, and took 1.9, 1.2, 0.8 and 0.5 s for the four photos. It named these kinds: wader for `heron.png`, person for `portrait.jpg`, none for `wall.png`, plant for `garden.jpg`.
- **Begin with the emulator's camera.** The shell granted the page's camera request, and the page reached its finder screen with the camera as its source (`android/state-begin.json`, `android/shots/3-begin.jpg`, which shows the emulator's built-in camera scene through the page).
- **Console.** Two messages in all, both the browser's advice to set `willReadFrequently` on a canvas (`android/logcat-seenback.txt`).

The emulator runs on a server processor with hardware virtualization, so its times say nothing about a phone's.

### iOS: run 2 (`runs/native/2-ios/`, commit `8be197a`)

- **Build.** `macos-latest` (macOS 26.6.2, arm64, 7.5 GB), Xcode 26.6, iPhone simulator SDK 26.5. `swiftc` compiled `main.swift` without errors; the app was signed ad hoc and installed in an iPhone 17 simulator running iOS 26.5. The app is 71,992 kB on disk, and 54,406,286 bytes when zipped the way an `.ipa` is (`ios/log.txt`).
- **The opening screen** appears in full, with its typeface (`ios/shots/1-open.jpg`). The page reports `isSecureContext` true at `app://localhost/` and `crossOriginIsolated` false. Its user agent names "iPhone OS 18_7", although the simulator runs iOS 26.5.
- **The page's self-test inside the app** finished in 28.3 s: all 98 checks passed. WebGL 2 is present, float render targets work, the renderer is "Apple GPU", and the test video played as MP4 through the scheme handler (`ios/2-selftest-state.json`, `ios/shots/2-selftest-final.jpg`).
- **The pocket recognizer** became ready in 1.7 s on the WASM backend with one thread and took 0.64, 0.64, 0.65 and 0.52 s for the four photos, with the same four kinds as on Android.
- **For comparison**, the same app pointed at the page served from the Mac (`http://127.0.0.1:8781`) also passed all 98 checks (ready in 3.2 s, 0.6 to 0.8 s a photo; `ios/3-served-state.json`, `reports/ios-served.json`).
- **The app's own log** holds no console error or warning and no file it could not serve (`ios/app-log.txt`).
- **Not checked:** the simulator has no camera, so the camera request inside the iOS shell has not been tried. The simulator also borrows the Mac's memory, so a pass there does not show that a real iPhone holds the same load.

### The larger model inside the shells

**Android, run 3** (`runs/native/3-android/`, commit `92283a2`; the same build and emulator as run 1, whose self-test passed again with all 98 checks). The probe called the page's own `get()` for the larger model (`models/naturalist`) inside the WebView (`android/big-state.json`, `android/big-memory.txt`, `android/emu-log.txt`):

- The four parts, 309,812,341 bytes in all, came from `raw.githubusercontent.com`, were verified and kept, and the encoder started, 106.5 s after the call. Of that, starting the encoder took 43.3 s (session 8.1 s, warm-up 28.9 s); the rest was the download and its checks.
- `navigator.storage.estimate()` gave 126,612,835 bytes in use before (from the earlier steps of the same run) and 446,307,171 after, with a quota of 3,736,869,273 bytes.
- The four photos took 28.9 s (`heron.png`, wader), 25.7 s (`portrait.jpg`, other), 23.6 s (`garden.jpg`, plant) and 22.2 s (`wall.png`, other, with `sure` false) on the WASM backend with one thread.
- The WebView's renderer process reached 1,585 MB of resident memory at its peak, sampled every 4 s with `ps`; the app's own process reached 210 MB, and the emulator's available memory fell to 771 MB of its 4 GB. Logcat shows no process killed after the probe started, and the renderer kept one process id to the end.

**iOS, run 4** (`runs/native/4-ios/`, commit `a88469a`; the same build and simulator as run 2, whose self-test passed again with all 98 checks, the recognizer ready in 2.3 s). Inside the app at `app://localhost/`, the page cannot keep the larger model. The probe's call to `get()` failed 1.6 s after it began, with no part kept, and the page said "The larger model could not be kept on this device." The recognizer recorded the cause as `keep: Request url is not HTTP/HTTPS` (`ios/big-state.json`). The page names each kept part by an address under its own origin (`partKey` in `src/cam.rec.js`), and Cache Storage takes only `http` and `https` addresses as names, so every such name fails at `app://`. The page's own copies of the pocket model were not kept either: after the self-test the storage in use was 77 bytes (`before` in `ios/big-state.json`), where the Android shell showed 126,612,835 bytes at the same point. The page catches that failure without a word, and the pocket recognizer runs from the app's own files, which is why the self-test passes. `navigator.storage.estimate()` gave a quota of 10,307,921,511 bytes there. Two ways out, neither tried yet: the shell serves its files over `http://127.0.0.1` from a small server inside the app (a loopback address is a secure context, and the page's names would then be `http` addresses), or the page names its kept copies with an `https` address of its own choosing wherever its own address is not `http` or `https` (a change in `src/cam.rec.js`, which belongs to the recognizer's area).

**iOS, run 5** (`runs/native/5-ios/`, commit `7288841`). Inside the app at `app://localhost/` the probe failed again in the same way. Then the same app was pointed at the page served from the Mac at `http://127.0.0.1:8781`, a loopback address that stands in for a server inside the app (`ios/5-big-served-state.json`, `ios/5-big-served-memory.txt`, `ios/log.txt`):

- The four parts, 309,812,341 bytes, came from `raw.githubusercontent.com`, were verified and kept, and the encoder started, 17.5 s after the call; starting the encoder took 11.9 s of that (session 2.0 s, warm-up 6.5 s).
- `navigator.storage.estimate()` gave 61,956,931 bytes in use before and 381,643,630 after, with a quota of 10,307,921,511 bytes.
- The four photos took 9.6 s (`heron.png`, wader), 11.2 s (`portrait.jpg`, other), 8.8 s (`garden.jpg`, plant) and 7.0 s (`wall.png`, other, with `sure` false) on the WASM backend with one thread.
- The simulator's web content process reached 1,427 MB of resident memory on the Mac at its peak, sampled every 4 s with `ps`. The simulator has no memory limit of a phone's kind, so this does not show that an iPhone will allow it.

In the simulator, then, the same app holds and runs the larger model when the page's address is `http`. The next step for the iOS shell is the small server inside the app (or the page change above), checked again in the simulator and then on a real iPhone.

## Commands

Start the jobs on build machines (see the workflow's row above for what each label runs), wait, and read the results:

```
git push -f origin HEAD:refs/heads/run/native/<label>
bash ci/wait.sh <commit> <results expected> 540
git fetch origin ci && git show FETCH_HEAD:runs/native/<run number>-android/android/emu-log.txt
```

Publish the APK from `main` (one result, under `runs/native/<run number>-pub/`; the file appears on `pub/app-android` only if the gate passed):

```
git push -f origin origin/main:refs/heads/run/native/pub-<label>
bash ci/wait.sh <commit of main> 1 540
git fetch origin ci && git show FETCH_HEAD:runs/native/<run number>-pub/android/gate.json
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

A real iPhone runs only apps signed with a certificate that Apple has issued. For one's own phone, an Apple ID signed in to Xcode is enough: Xcode makes a free "Personal Team" for it. These steps make the Xcode project on the owner's Mac; none of them has been tried, because the build machine has no Apple ID and no phone, and this repository holds no signing identity.

1. **The page's files.** In a clone of the repository on the Mac, run `python3 -I build.py`, then `TEST=0 bash ci/native/bundle.sh native/ios-shell/www`. This makes `native/ios-shell/www`, which git ignores.
2. **The Apple ID.** Open Xcode, then Xcode, Settings, Accounts, press the plus sign and sign in with the Apple ID. A team named after the person, with "(Personal Team)" after it, appears.
3. **The project.** File, New, Project, iOS, App. Product Name `SeenBack`; Team: the Personal Team; Organization Identifier: something of the owner's own in reverse domain form (for example `com.example.yourname`), which makes the bundle identifier `com.example.yourname.SeenBack`; Interface: Storyboard; Language: Swift; no tests. Save it anywhere outside the repository.
4. **Remove what the template made.** In the project navigator, delete `AppDelegate.swift`, `SceneDelegate.swift`, `ViewController.swift` and `Main.storyboard` (Move to Trash). Keep `LaunchScreen.storyboard` and `Assets.xcassets`.
5. **Add the shell.** Drag `native/ios-shell/main.swift` from the repository into the project navigator, with the target `SeenBack` ticked. Leave copying off, so that the project uses the repository's file. Then drag the folder `native/ios-shell/www` in the same way and add it as a folder reference (a blue folder), so that the app holds `www/` with its paths unchanged; `main.swift` reads the page from there.
6. **The settings that the template set differently.** Select the project, the target `SeenBack`, the Build Settings tab, All. Set "Application Scene Manifest (Generation)" to No, and clear "UIKit Main Storyboard File Base Name". In the Info tab, delete "Application Scene Manifest" if it is still listed, and add two keys: "Privacy - Camera Usage Description" (`NSCameraUsageDescription`) with the sentence from `native/ios-shell/Info.plist`, and "App Transport Security Settings" (`NSAppTransportSecurity`) holding "Allow Local Networking" (`NSAllowsLocalNetworking`) set to YES. Under General, set Minimum Deployments to iOS 16.0 or later, and leave only iPhone under Supported Destinations.
7. **Signing.** In Signing and Capabilities, keep "Automatically manage signing" on, with the Personal Team. If Xcode says that the bundle identifier is taken, change the Organization Identifier part.
8. **The phone.** Connect the iPhone with a cable and trust the Mac on the phone. On the phone, turn on Developer Mode (Settings, Privacy and Security, Developer Mode; the phone restarts and asks once more). In Xcode, choose the iPhone as the run destination and press Run. The first launch stops with a message about an untrusted developer: on the phone, open Settings, General, VPN and Device Management, choose the Apple ID under Developer App, and trust it. Press Run again.
9. **On the phone.** The app opens at the page's first screen. Begin asks for the camera with the sentence from step 6. The larger model is fetched from the network when the person agrees, and kept in the app's own storage.

What the free tier allows, from Apple's page "Choosing a Membership" (developer.apple.com/support/compare-memberships, read on 11 October 2026): up to 10 App IDs and up to 3 devices, each expiring after 7 days; up to 3 apps on a device; provisioning profiles that expire 7 days after they are issued. After seven days the app no longer opens; connecting the phone and pressing Run again in Xcode signs and installs it anew. An app that is installed over itself in this way keeps its data, so the kept larger model should stay; that was not tried. Deleting the app deletes what it kept. The same page lists app distribution and App Store Connect, of which TestFlight is a part, among the benefits of the paid Apple Developer Program.

## The distance to the two stores

**Google Play.** What Google's help pages say (support.google.com/googleplay/android-developer, answers 6112435 and 14151465, read on 11 October 2026): a Play Console account costs US$25 once, and its holder must verify their identity with a government ID and a card in their legal name. A personal account created after 13 November 2023 must run a closed test with at least 12 testers, opted in for at least 14 days without a break, before it may apply to publish, and a new personal account must also show that it has an Android device through the Play Console app. The following come from general knowledge of Google's rules and were not read tonight: a new app is uploaded as an Android App Bundle signed with an upload key that the owner makes and keeps, and an app that asks for the camera needs a privacy policy and a completed Data safety form. The shell already targets API level 35. A release build needs a signing configuration in `app/build.gradle` and `gradle bundleRelease`; neither exists yet.

**The App Store.** The Apple Developer Program costs 99 USD a membership year, and Apple's page says that non-profit organizations, accredited educational institutions and government entities may be eligible for a fee waiver. Guideline 4.2 of the App Store Review Guidelines ("Minimum Functionality") says: "Your app should include features, content, and UI that elevate it beyond a repackaged website." That sentence was read tonight in copies of the guidelines reached through a web search; Apple's own page was not opened. The shell is the page in a web view, so a reviewer will judge what the page does: the camera's change of eyes, the recognizer that runs on the phone, and use without a network. Whether that passes review cannot be known from here. A camera app also needs the camera sentence (present in `Info.plist`), a privacy policy and the App Privacy answers in App Store Connect; those last two come from general knowledge of Apple's rules and were not read tonight. A build for the store also needs an Xcode project and an app icon set.

**Size, with and without the larger model.** Without the larger model, the debug APK of run 1 is 55,827,719 bytes, and the iOS app of run 2 is 54,406,286 bytes zipped. Both hold the check files (about 1.1 MB) and the larger model's rows (9.9 MB in `models/naturalist/`); the encoder of the pocket model is 40,978,137 bytes of that. Built into the app, the larger model would add its 309,812,341 bytes of encoder parts (from `models/naturalist/manifest.json`); no such build was made tonight, and how far those bytes compress was not measured. The shells as they stand keep the web page's behaviour: the larger model is downloaded once, with the person's consent, and kept in the web view's Cache Storage.

## What is open

- Nothing has run on a real phone. The camera inside the iOS shell, the memory a real phone gives the web view, and the time a photo takes on a phone are all unmeasured.
- In the emulator the app's camera permission was granted at install (`adb install -g`), so Android's own permission prompt and the shell's path through it were not seen.
- The page keeps its own copies of model files in Cache Storage. Inside a shell the files are already in the app, so a phone may hold them twice. On Android, 126,612,835 bytes were in use in the web view's storage after the self-test and Begin, before the larger model was fetched; what makes up that figure was not looked at.
- The service worker was switched off in every run (`nosw=1` in the self-test, and the opening screen was not checked for it). The Android shell answers the service worker's requests from the bundle as well; whether a service worker registers at `app://localhost/` on iOS was not tried. The shells do not need it for use without a network, because their files are in the app.
- The page's text still speaks of a download from the web where a shell already holds the files; no wording was changed, because the page is not this area's to change.
