# PomoNotch

A Pomodoro timer that lives in your Mac's notch. Work sessions run in your terminal, and when it's time for a break, the notch expands with a live countdown.

**Requires macOS 12+ with a notch (MacBook Pro 2021 or later)**

---

## Install

```bash
curl -sSL https://raw.githubusercontent.com/Raaaphhh/PomoNotch/main/install.sh | bash
```

Open a new terminal tab, then run:

```bash
pomonotch
```

---

## Usage

Launch PomoNotch from your terminal:

```bash
pomonotch
```

An interactive menu appears with three session options:

| Option | Focus | Break |
|---|---|---|
| Classic Pomodoro | 25 min | 5 min |
| Deep Work | 45 min | 15 min |
| Custom | your choice | your choice |

Navigate with arrow keys and confirm with `Enter`.

**During focus time**, the terminal shows a live countdown:
```
Only 24min 32s left before a 5min break
```

**When break time starts**, two things happen simultaneously:
- A sound plays to notify you
- The notch expands and displays the break countdown

The notch closes automatically when the break ends, and a second sound signals it's time to focus again. The cycle repeats indefinitely.

---

## Uninstall

Open a new terminal tab, then run:

```bash
curl -sSL https://raw.githubusercontent.com/Raaaphhh/PomoNotch/main/uninstall.sh | bash
```

---

## Requirements

- macOS 12 or later (MacBook Pro 2021+ with notch)
- Python 3.10 or later (included on macOS)


---

Made with ❤️ by raaaphhh