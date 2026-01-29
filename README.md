# Auto Clicker for Ubuntu (Python)

A simple, lightweight auto-clicking script built with Python specifically for Linux users. It allows you to toggle automated clicking using keyboard hotkeys.

## ⚠️ Important: System Requirement
This script requires the **X11 (Xorg)** display server to detect keyboard hotkeys and control the mouse. It will **not work** on the default Wayland session found in newer Ubuntu versions (22.04+).

### How to Switch to Xorg:
1. **Log out** of your current session.
2. Click on your **Username**.
3. Click the **Gear Icon (⚙️)** in the bottom right corner of the screen.
4. Select **"Ubuntu on Xorg"**.
5. Log in as usual.

## Features
- **Toggle Start/Stop**: Use a customizable hotkey (default is `C`).
- **Safety Exit**: Close the program instantly with a hotkey (default is `E`).
- **Threaded Execution**: The script remains responsive while clicking is active.

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/DanamiStartrail/Auto-Clicker-Ubuntu.git](https://github.com/DanamiStartrail/Auto-Clicker-Ubuntu.git)
   cd Auto-Clicker-Ubuntu

2. **Install Dependencies**:
   
   It is recommended to use the system package manager for stability on Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3-pynput
- **Alternatively**, if you prefer using pip:
  ```bash
  pip install -r requirements.txt

## Usage
1. Run the script from your terminal
- **Copy the code**
  ```bash
  cd auto-clicker-ubuntu
  source venv/bin/activate
  python main.py
2. Position your mouse cursor where you want to click
3. Pres **C** to start/stop clicking
4. Pres **E** to terminate the program

## Configuration
You can adjust the clicking speed by editing the **delay** variabel in **main.py**:
* **delay = 0.1** (10 clicks per second)
* **delay = 0.01** (100 clicks per seconds)

## How to Acces the python program
- Use this code:
  ```bash
  cd auto-clicker-ubuntu
  nano main.py

## License
Distributed under the MIT License. See LICENSE for more information


## Disclaimer
Use this tool responsibly. The developer is not responsible for any bans or issues caused by using this script in games or third-party applications.
