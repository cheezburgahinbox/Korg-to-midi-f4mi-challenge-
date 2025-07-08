# rainbow road aka RBR
First project
# 🌈 Rainbow Road

**Convert KORG DS-10 `.sav` files into MIDI tracks** — extract full songs from your Nintendo DS and bring them into your DAW.

This project lets you drag and drop `.sav` files from the DS-10 synthesizer (emulated or original) and export them as `.mid` files you can play, remix, or sequence.

---

## Features

-  Extracts notes and tempo from `.sav` files
-  Converts full DS-10 songs into `.mid` format
-  Drag-and-drop and “Open With” support on Windows
-  Lightweight and fully open

---

## Usage

1. Install Python 3.8+ on your system.
2. Download or clone this repo.
3. Run the tool:

```bash
python RBR.py yourfile.sav
Or right-click your .sav file → Open with → RBR.py
It will generate a .mid file in the same folder.

dependincies
mido: install using pip
bash pip install mido in cmd
