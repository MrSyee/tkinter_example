from glob import glob
import os
import queue
import random
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import cv2


class ImageLoader:
    def __init__(self):
        self.root_path = "./mpcontrol/data/pathmap/images"
        self.image_paths = sorted(glob(os.path.join(self.root_path, "*.png")))
        self.idx = 0
        self.max_idx = len(self.image_paths) - 1

    def reset_idx(self):
        self.idx = 0

    def increase_idx(self):
        for _ in range(self.max_idx):
            self.idx = min(self.idx + 1, self.max_idx)
            print(self.idx)
            time.sleep(0.2)

    def load(self):
        image = cv2.imread(self.image_paths[self.idx])
        return image.copy()


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multithreading GUI")
        self.root.geometry("1200x800")

        self.label1 = tk.Label(self.root, text="Hello There!")
        self.label1.pack(pady=20)

        self.button1 = tk.Button(
            self.root, command=lambda: threading.Thread(target=self.b1_click).start()
        )
        self.button1.configure(text="timer", background="Grey", padx=50)
        self.button1.pack(pady=20)

        self.button2 = tk.Button(self.root, command=self.b2_click)
        self.button2.configure(text="Pick Random Number", background="Grey", padx=50)
        self.button2.pack(pady=20)

        self.random_label = tk.Label(self.root, text="")
        self.random_label.pack(pady=20)

        self.button3 = tk.Button(
            self.root, command=lambda: threading.Thread(target=self.b3_click).start()
        )
        self.button3.configure(text="Load image", background="Grey", padx=50)
        self.button3.pack(pady=20)

        self.label2 = tk.Label(self.root, text="Image number")
        self.label2.pack(pady=20)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)

        self.button4 = tk.Button(self.root, command=self.b4_click)
        self.button4.configure(text="Reset", background="Grey", padx=50)
        self.button4.pack(pady=20)

        #
        self.imageloader = ImageLoader()

        self.img_show_thread = threading.Thread(
            target=self.update_image_label, daemon=True
        )
        self.img_show_thread.start()

    def b1_click(self):
        second = 10
        for i in range(second):
            self.label1.config(text=f"Wait {i} seconds...")
            time.sleep(1)
        self.label1.config(text=f"{second} Seconds Is Up!")
        sys.exit()

    def b2_click(self):
        self.random_label.config(text=f"Random Number: {random.randint(1, 100)}")

    def b3_click(self):
        # self.imageloader.idx = 0
        # for i in range(self.imageloader.max_idx):
        #     self.label2.config(text=f"Load {self.imageloader.idx}th image")
        #     image = self.arr2photoimg(self.imageloader.load())
        #     self.image_label.config(image=image)
        #     self.image_label.image = image
        #     self.image_label.update()
        #     time.sleep(0.2)
        # sys.exit()
        self.imageloader.increase_idx()

    def b4_click(self):
        self.imageloader = ImageLoader()

    def update_image_label(self):
        while True:
            self.label2.config(text=f"Load {self.imageloader.idx}th image")
            image = self.arr2photoimg(self.imageloader.load())
            self.image_label.config(image=image)
            self.image_label.image = image
            self.image_label.update()

    @staticmethod
    def arr2photoimg(img_arr):
        """Convert data type to show in Tkinter."""
        img_arr = cv2.resize(img_arr, (200, 200))
        return ImageTk.PhotoImage(Image.fromarray(img_arr))

    def run(self):
        self.root.mainloop()


app = GUI()
app.run()
