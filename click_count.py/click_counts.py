from pynput import mouse, keyboard
import tkinter as tk
import csv

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click and Key Counter")
        self.root.geometry("310x300")  # UI 사이즈 조절

        self.mouse_click_count = 0
        self.key_click_count = {
            "q": 0, "w": 0, "e": 0, "r": 0, "d": 0,
            "f": 0, "a": 0, "s": 0, "g": 0, "b": 0,
            "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
            "6": 0, "t": 0, "`": 0, "key.backspace": 0,
            keyboard.Key.tab: 0,
            keyboard.Key.ctrl_l: 0,
            keyboard.Key.space: 0,
            keyboard.Key.esc: 0,
            keyboard.Key.alt_l: 0
        }

        self.labels_mouse = tk.Label(root, text="Mouse Clicks: 0", font=("Helvetica", 12))
        self.labels_mouse.grid(row=0, columnspan=3, pady=10)

        self.labels_key = {}

        row = 1
        col = 0
        for key in self.key_click_count:
            label = tk.Label(root, text=f"{key}: 0", font=("Helvetica", 10))
            label.grid(row=row, column=col, padx=5, pady=2, sticky="w")
            self.labels_key[key] = label

            col += 1
            if col > 2:
                col = 0
                row += 1
        self.keyboard_listener_running = True  # 키보드 리스너 상태를 추적

        # UI 닫힐 때 저장 기능 연결
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        # 마우스 이벤트 리스너 시작
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_listener.start()

        # 키보드 이벤트 리스너 시작
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        self.keyboard_listener.start()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.mouse_click_count += 1
            self.labels_mouse.config(text=f"Mouse Clicks: {self.mouse_click_count}")
            self.save_data()

    def on_press(self, key):
        if self.keyboard_listener_running:  # 키보드 리스너가 실행 중일 때만 처리
            try:
                key_name = key.char
            except AttributeError:
                key_name = key

            if key_name in self.key_click_count:
                self.key_click_count[key_name] += 1
                self.labels_key[key_name].config(text=f"{key_name}: {self.key_click_count[key_name]}")
                self.save_data()

    def save_data(self):
        with open("click_counts.csv", mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Key", "Count"])
            for key, count in self.key_click_count.items():
                writer.writerow([key, count])

    def save_and_exit(self):
        self.save_data()
        self.keyboard_listener_running = False  # 키보드 리스너 중지
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
