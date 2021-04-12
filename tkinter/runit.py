import os
import tkinter as tk
from tkinter import ttk


class Index:

    def __init__(self, root):
        root.title("Index")

        # create a frame on top
        content = ContentFrame(root)
        content.grid(column=0, row=0, sticky="nsew")
        # Create a frame on bottom with the nav buttons
        bottomframe = NavFrame(root)
        bottomframe.grid(column=0, row=1, sticky="nsew")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)


class ContentFrame(ttk.Frame):

    def __init__(self, frame):
        super(ContentFrame, self).__init__()

        self.configure(padding=(10, 3, 10, 3))

        welcome = ttk.Label(self, text="Welcome!")
        welcome.grid(row=1, column=3, sticky="nsew")


class NavFrame(ttk.Frame):

    def __init__(self, frame):
        super(NavFrame, self).__init__()

        self.configure(padding=(10, 3, 10, 3))

        back_btn = tk.Button(self, text="Back")
        middle = tk.Canvas(self, height=50)
        next_btn = tk.Button(self, text="Next")

        back_btn.grid(row=1, column=1, sticky="ew")
        middle.grid(row=1, column=2, sticky="nsew")
        next_btn.grid(row=1, column=5, sticky="ew")


def main():
    root = tk.Tk()
    Index(root)
    root.mainloop()


if __name__ == '__main__':
    main()
