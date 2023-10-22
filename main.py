import tkinter as tk
from tkinter import ttk
import requests

ip = "http://192.168.1.222"

def getValue():
    r = requests.get(ip+"/get-values")
    return round(r.text, 4)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("My GUI")
        self.root.geometry("300x200")

        self.max_value = float('-inf')
        self.save_to_file = tk.BooleanVar(value=True)

        self.label = ttk.Label(self.root, text="Value: ", font=("Arial", 16))
        self.label.pack(pady=10)

        self.reset_button = ttk.Button(self.root, text="Reset Max Value", command=self.reset_max)
        self.reset_button.pack(pady=5)

        self.max_label = ttk.Label(self.root, text="Max Value: ", font=("Arial", 16))
        self.max_label.pack(pady=10)

        self.toggle_button = ttk.Checkbutton(self.root, text="Save to File", variable=self.save_to_file)
        self.toggle_button.pack(pady=5)

        self.update_value()

    def reset_max(self):
        self.max_value = float('-inf')

    def update_value(self):
        value = getValue()
        self.label.config(text=f"Value: {value}")

        self.max_value = max(self.max_value, value)
        self.max_label.config(text=f"Max Value: {self.max_value}")

        if self.save_to_file.get():
            with open("values.txt", "a") as f:
                f.write(str(value) + "\n")

        self.root.after(1000, self.update_value)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
