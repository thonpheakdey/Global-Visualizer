# Input Mini - Global Visualizer
### Developed by THON PHEAKDEY

**Input Mini** is a lightweight, high-performance Windows application that visualizes keyboard and mouse inputs in real-time. Designed for streamers, tutorial creators, and developers.

## ✨ Features
* **Universal Key Mapping**: Correctly detects Shift/Ctrl combinations (e.g., Shift+1 shows as "1").
* **Compact Design**: Optimized 500x350 window size.
* **Mouse Tracking**: Visualizes Left, Right, and Middle clicks/scrolls.
* **Activity Log**: Real-time history of all inputs.
* **Always on Top**: Stays visible while you use other apps.

## 🚀 Installation
1. Download `app.exe` from the [Releases](../../releases) section.
2. Ensure `tpkicon.ico` is in the same folder (or use the standalone version).
3. Run and start tracking!

## 🛠️ Build from Source
If you want to compile it yourself:
```bash
pip install pynput tkinter
python -m PyInstaller --noconsole --onefile --add-data "tpkicon.ico;." --icon=tpkicon.ico app.py
