# ⌨️ Input Mini - Global Input Visualizer
### Developed by **THON PHEAKDEY**

**Input Mini** is a lightweight, high-performance Windows application that provides a real-time visual overlay of your keyboard and mouse activity. Perfect for tutorial creators, gaming streamers, and software demonstrators.

---

## 🚀 Features

* **Universal Alphanumeric Support**: Advanced Virtual Key (VK) mapping ensures that `SHIFT + 1` correctly highlights the `1` key rather than just the symbol.
* **Compact UI**: Designed to fit a $500 \times 350$ footprint to save screen real estate.
* **Mouse Visualization**: Real-time display for Left Click, Right Click, and Scroll Wheel activity.
* **Activity Log**: A scrollable history window that logs key presses and mouse clicks with precise timestamps.
* **Always-on-Top**: The window stays pinned above other applications for easy viewing during recordings.
* **Custom Branding**: Includes a custom icon and developer signature.

---

## 🛠️ Technical Stack

* **Language**: Python 3.13
* **UI Framework**: Tkinter
* **Input Monitoring**: `pynput` library
* **Packaging**: PyInstaller

---

## 💻 Installation & Usage

### Method 1: Running the Executable (Recommended)
1. Download the `app.exe` from the [Releases](../../releases) section.
2. Ensure the `tpkicon.ico` file is in the same directory (unless using the bundled version).
3. Double-click `app.exe` to run.

### Method 2: Running from Source
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/input-mini.git](https://github.com/YOUR_USERNAME/input-mini.git)
   cd input-mini
