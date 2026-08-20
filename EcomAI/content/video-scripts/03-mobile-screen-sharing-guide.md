# EcomAI — Screen Recording Guide: Show Mobile App on Laptop

**Goal:** In the videos, show the EcomAI **mobile app** running on your phone, displayed on your laptop screen, while you record the whole thing (for the "mobile app coming soon" teaser + future mobile demos).

---

## Option 1 — iPhone → Mac (Best, easiest, built-in)

### QuickTime (no extra install)
1. Open **QuickTime Player** on Mac
2. Menu → **File → New Movie Recording**
3. Next to record button, click **▼** → select your **iPhone** as camera
4. iPhone screen appears on Mac → ready to record
5. Red record button → captures your phone screen + (if you pick mic) your voice
6. Works over USB or Wi-Fi (USB = no lag, use for demos)

### iPhone Mirroring (macOS Sequoia+ / Apple Silicon)
1. iPhone and Mac on same Apple ID + Wi-Fi/Bluetooth
2. Click **iPhone Mirroring** app on Mac
3. Phone screen appears, controllable from Mac
4. Record the Mac window with **Cmd+Shift+5** (built-in screen recorder)

---

## Option 2 — Android → Mac

### scrcpy (free, best quality, low lag)
```bash
brew install scrcpy          # + brew install android-platform-tools for adb
# Enable Developer Options + USB debugging on Android
adb devices                  # confirm device
scrcpy                       # phone screen on Mac window
```
- Record with Mac's **Cmd+Shift+5** (select the scrcpy window)
- USB = near-zero lag. Wi-Fi works too (`scrcpy --tcpip`)
- Also lets you control the phone from the keyboard/mouse — clean for demos

### LetsView / ApowerMirror (no cable, wireless)
1. Install **LetsView** on Mac + app on Android
2. Same Wi-Fi → mirror phone to Mac window
3. Record with Mac screen recorder
- Easier but slightly more lag. Fine for a quick teaser.

---

## Option 3 — Record phone directly, then splice (no laptop needed)

If you only need a short "app on phone" clip:
1. Use **iOS built-in screen recorder** (Control Center → record) or Android's
2. Record 15–30 sec of the app on the phone
3. In CapCut / iMovie, overlay that clip on the main video (corner phone mockup)

Best for the "mobile app teaser" — phone-in-hand style shot reads as authentic.

---

## Recommended setup for YOUR videos

| Video | Setup |
|---|---|
| Investor/team video — mobile teaser | Option 1 (QuickTime) or Option 3 (phone clip spliced) |
| Customer video — mobile teaser | Option 3 — short phone clip feels real |
| Future: live mobile demo | Option 1 (iPhone) or Option 2 (Android scrcpy) |

## Tips

- **USB over Wi-Fi** for anything live — no lag, no drops
- Record **voice on Mac mic** (QuickTime/mic input) so narration is clean
- In the teaser, say: *"Mobile app — poora business phone se, notifications aapko drive karenge"* while scrolling the app
- Keep mobile teaser ≤ 15 sec — it's a promise, not a demo (app coming soon)
- Use the existing app screenshots in `content/video-scripts/` as placeholder if app not ready yet