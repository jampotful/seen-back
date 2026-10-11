# Regards for Android: a debug build

`seen-back-debug.apk` is the Regards page of build 15 inside a plain Android WebView. The page's files are packed in the app, and the app serves them to its WebView from inside itself. It was built on a GitHub build machine from commit `acc7d9713a3fc006fa24ccf6680aefe9e8f7c62a` of https://github.com/jampotful/seen-back and signed there with a debug key that Gradle made for this one build. The key was thrown away with the machine, and it is in no repository.

The file is for trying the page on one's own phone. It is a debug build and has not been through Google Play or any other store.

| | |
|---|---|
| File | `seen-back-debug.apk`, 54,319,188 bytes |
| SHA-256 | `63ba89bb0b55c8ef4779fdc5cd42ce1f71797755c246b764d3e59328db6fc05c` |
| Page | build 15 |
| Commit | `acc7d9713a3fc006fa24ccf6680aefe9e8f7c62a` |
| Built | 2026-10-11T19:53:39Z (workflow run 12) |
| Needs | Android 7.0 or later, and the camera |

## Before it was published

The same build, with the page's check files added, ran in an Android 14 emulator on the build machine: the page's self-test finished with 98 checks and 0 failed. Then this file, without the check files, was installed in the same emulator, opened at its first screen and reached the camera after Begin. Apart from their signature files, the two APKs differ only in the check files; the comparison, the self-test's report and the screenshots are on the repository's `ci` branch under `runs/native/12-pub/android/`. Nothing here has run on a real phone.

## How to install it

1. On the phone, open this address in the browser: https://raw.githubusercontent.com/jampotful/seen-back/pub/app-android/seen-back-debug.apk
2. The browser downloads the file. It may warn that this kind of file can harm the device; choose to download it anyway.
3. Open the downloaded file. Android asks whether the browser may install unknown apps. Turn that on for the browser in the setting it shows, go back and press Install.
4. Google Play Protect is likely to warn that it does not recognize the app's developer, because a debug key belongs to no developer it knows, and it may offer to scan the app first. Its dialog has a way to install the app anyway, sometimes under "More details".
5. Open Regards. The first time you press Begin, Android asks for the camera.

The larger model (309,812,341 bytes) is not in the file. As on the web, the page offers to fetch it and then keeps it in the app's own storage.

## Updates

The app does not update itself. A newer build appears at the same address, signed with a different throwaway key, so Android will refuse to install it over this one: uninstall Seen Back first (the kept larger model goes with it), then install the new file.

To check a downloaded file on a computer, compare the output of `sha256sum seen-back-debug.apk` with the SHA-256 above, or with `built.json` beside it.
