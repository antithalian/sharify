# Sharify
---

Sharify is a super simple Python3 CLI tool for creating WiFi network QR codes. These can be used by any modern iPhone or Android device to connect to a WiFi network quickly and easily.

## Dependencies
---

Sharify currently has only two dependencies:
`python3` (any modern 3.x version should work) and `qrcode`, which is available on the PyPI. This list is not exhaustive, and, if I decide to work on the project more, will probably expand at least a bit.

## How do I use it?
---
Using sharify is pretty simple. It provides a Python CLI interface with argparse, so, on most systems, you can call it from within its directory by typing `python3 sharify.py network_type ssid -p password`
