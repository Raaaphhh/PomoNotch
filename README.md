# PomoNotch 🍅

A Pomodoro timer that lives in your Mac's notch. Work sessions run in your terminal, and when it's time for a break, the notch expands with a countdown.

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

```bash
pomonotch              # 25 min work, 5 min break (default)
pomonotch --work 50 --break 10   # custom durations in minutes
```

When a break starts, the notch expands and displays the remaining time. It closes automatically when the break is over.

---

## Uninstall

```bash
curl -sSL https://raw.githubusercontent.com/Raaaphhh/PomoNotch/main/uninstall.sh | bash
```

---

## Requirements

- macOS 12 or later (MacBook Pro 2021+ with notch)
- Python 3.10 or later (inclus sur macOS)