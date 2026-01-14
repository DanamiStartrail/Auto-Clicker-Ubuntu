import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# --- KONFIGURASI ---
delay = 0.1  # Jeda waktu antar klik (detik). 0.1 berarti 10 klik per detik.
button = Button.left
start_stop_key = KeyCode(char='c') # Tekan tombol 'c' untuk START/STOP
exit_key = KeyCode(char='e')       # Tekan tombol 'e' untuk EXIT program

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

print("--- Auto Clicker Ready ---")
print(f"Tekan '{start_stop_key.char}' untuk Start/Stop")
print(f"Tekan '{exit_key.char}' untuk Keluar")

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("[Status] Berhenti")
        else:
            click_thread.start_clicking()
            print("[Status] Berjalan...")
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("Program Ditutup.")

with Listener(on_press=on_press) as listener:
    listener.join()
