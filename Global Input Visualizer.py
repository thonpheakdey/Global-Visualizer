import tkinter as tk
from tkinter import scrolledtext
import time
from pynput import keyboard, mouse
import os

class InputVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Input Mini - THON PHEAKDEY")
        self.root.geometry("500x350") 
        self.root.configure(bg='#0a0a0a')
        self.root.attributes('-topmost', True)
        
        # --- ICON SETUP ---
        # Looking for your specific icon file
        icon_file = "tpkicon.ico"
        if os.path.exists(icon_file):
            try:
                self.root.iconbitmap(icon_file)
            except Exception as e:
                print(f"Icon error: {e}")
        
        self.pressed_keys = {}
        self.mouse_buttons = {}

        self.setup_ui()
        
        # Start Listeners
        self.key_listener = keyboard.Listener(on_press=self.global_press, on_release=self.global_release)
        self.key_listener.start()
        
        self.mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)
        self.mouse_listener.start()
        
        self.root.bind("<Configure>", self.on_resize)
        self.update_loop()

    def setup_ui(self):
        # Header for Clock and Name
        self.info_frame = tk.Frame(self.root, bg='#0a0a0a')
        self.info_frame.pack(fill=tk.X, side=tk.TOP)
        
        self.clock_label = tk.Label(self.info_frame, text="00:00:00", fg="#00ffcc", bg="#0a0a0a", font=("Consolas", 10, "bold"))
        self.clock_label.pack(side=tk.LEFT, padx=10, pady=2)

        # YOUR NAME
        self.name_label = tk.Label(self.info_frame, text="THON PHEAKDEY", fg="#00ffcc", bg="#0a0a0a", font=("Arial", 9, "bold"))
        self.name_label.pack(side=tk.RIGHT, padx=10, pady=2)

        # Log and Mouse Container
        self.top_container = tk.Frame(self.root, bg='#0a0a0a')
        self.top_container.pack(fill=tk.X, padx=5, pady=2)

        # Activity Log (History Box)
        self.history_log = scrolledtext.ScrolledText(self.top_container, height=4, bg="#111", fg="#00ffcc", font=("Consolas", 8), state='disabled', borderwidth=0, highlightthickness=1, highlightbackground="#333")
        self.history_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Mouse Canvas
        self.mouse_canvas = tk.Canvas(self.top_container, width=80, height=60, bg='#0a0a0a', highlightthickness=0)
        self.mouse_canvas.pack(side=tk.RIGHT, padx=5)
        
        self.mouse_buttons['left'] = self.mouse_canvas.create_rectangle(5, 5, 35, 55, fill='#1a1a1a', outline='#333')
        self.mouse_buttons['right'] = self.mouse_canvas.create_rectangle(45, 5, 75, 55, fill='#1a1a1a', outline='#333')
        self.mouse_buttons['middle'] = self.mouse_canvas.create_rectangle(35, 15, 45, 40, fill='#333', outline='#555')

        # Keyboard Canvas
        self.canvas = tk.Canvas(self.root, bg='#0a0a0a', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def log_event(self, message):
        self.history_log.config(state='normal')
        self.history_log.insert(tk.END, f"{time.strftime('%H:%M:%S')} > {message}\n")
        self.history_log.see(tk.END)
        self.history_log.config(state='disabled')

    def draw_layout(self):
        self.canvas.delete("all")
        w, h = self.root.winfo_width(), self.root.winfo_height()
        sw, sh = w / 500, h / 350
        
        def skey(name, x, y, width=32, height=30, font_size=7):
            rx, ry, rw, rh = x*sw, y*sh, width*sw, height*sh
            r = self.canvas.create_rectangle(rx, ry, rx+rw, ry+rh, fill='#1a1a1a', outline='#333', width=1)
            t = self.canvas.create_text(rx+rw/2, ry+rh/2, text=name.upper(), fill='#777', font=('Arial', int(font_size*sw), 'bold'))
            self.pressed_keys[name.lower()] = (r, t)

        skey('esc', 10, 5, 35, 20, 6)
        
        # Row 1
        keys1 = ['`','1','2','3','4','5','6','7','8','9','0','-','=']
        for i, k in enumerate(keys1): skey(k, 10 + i*34, 30)
        skey('back', 452, 30, 38, 30, 6)
        
        # Row 2
        skey('tab', 10, 65, 45)
        keys2 = ['q','w','e','r','t','y','u','i','o','p','[',']','\\']
        for i, k in enumerate(keys2): skey(k, 60 + i*34, 65)
        
        # Row 3
        skey('caps', 10, 100, 55)
        keys3 = ['a','s','d','f','g','h','j','k','l',';',"'"]
        for i, k in enumerate(keys3): skey(k, 70 + i*34, 100)
        skey('enter', 444, 100, 46)

        # Row 4
        skey('shift', 10, 135, 75)
        keys4 = ['z','x','c','v','b','n','m',',','.','/']
        for i, k in enumerate(keys4): skey(k, 90 + i*34, 135)
        skey('del', 430, 135, 60)

        # Row 5
        skey('ctrl', 10, 170, 45); skey('win', 60, 170, 40); skey('alt', 105, 170, 40)
        skey('space', 150, 170, 190)
        skey('alt', 345, 170, 40); skey('win', 390, 170, 40); skey('ctrl', 435, 170, 55)

    def get_key_name(self, key):
        try:
            if hasattr(key, 'vk') and key.vk is not None:
                vk = key.vk
                if vk == 27: return 'esc'
                if vk == 46: return 'del'
                if 65 <= vk <= 90 or 48 <= vk <= 57: return chr(vk).lower()
                vk_map = {192: '`', 189: '-', 187: '=', 219: '[', 221: ']', 220: '\\', 186: ';', 222: "'", 188: ',', 190: '.', 191: '/'}
                if vk in vk_map: return vk_map[vk]
            if hasattr(key, 'char') and key.char:
                if ord(key.char) < 32: return chr(ord(key.char) + 96).lower()
                return key.char.lower()
            k_name = str(key).lower().replace('key.', '')
            if 'delete' in k_name: return 'del'
            if 'backspace' in k_name: return 'back'
            for mod in ['ctrl', 'shift', 'alt', 'esc', 'tab', 'caps', 'win', 'enter', 'space']:
                if mod in k_name: return mod
            return k_name
        except: return None

    def global_press(self, key):
        name = self.get_key_name(key)
        if name in self.pressed_keys: 
            self.canvas.itemconfig(self.pressed_keys[name][0], fill='#00ffcc')
            self.canvas.itemconfig(self.pressed_keys[name][1], fill='#000')
            self.log_event(f"KEY: {name.upper()}")

    def global_release(self, key):
        name = self.get_key_name(key)
        if name in self.pressed_keys: 
            self.canvas.itemconfig(self.pressed_keys[name][0], fill='#1a1a1a')
            self.canvas.itemconfig(self.pressed_keys[name][1], fill='#777')

    def on_click(self, x, y, button, pressed):
        btn = str(button).split('.')[-1]
        if btn in self.mouse_buttons:
            self.mouse_canvas.itemconfig(self.mouse_buttons[btn], fill='#00ffcc' if pressed else '#1a1a1a')
            if pressed: self.log_event(f"MOUSE: {btn.upper()}")

    def on_scroll(self, x, y, dx, dy):
        self.mouse_canvas.itemconfig(self.mouse_buttons['middle'], fill='#00ffcc')
        self.root.after(100, lambda: self.mouse_canvas.itemconfig(self.mouse_buttons['middle'], fill='#333'))

    def on_resize(self, event=None):
        self.draw_layout()

    def update_loop(self):
        self.clock_label.config(text=time.strftime('%H:%M:%S'))
        self.root.after(1000, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = InputVisualizer(root)
    root.mainloop()