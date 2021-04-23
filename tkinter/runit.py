import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog


class MainWindow():

    def __init__(self, window):
        self.window = window
        self.system = str(window.tk.call("tk", "windowingsystem"))

        # Create a menu at the top
        self.menubar = ClassicMenu(self.window)
        self.window['menu'] = self.menubar

        # create a frame on top
        self.content = ContentFrame(self.window)
        self.content.grid(column=0, columnspan=2, row=0, sticky="nsew")

        # Create a seperator between the two frames
        self.seperator = ttk.Separator(self.window, orient=tk.HORIZONTAL)
        self.seperator.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Create a frame on bottom with the nav buttons
        self.bottomframe = NavFrame(self.window)
        self.bottomframe.grid(column=0, columnspan=2, row=2, sticky="nsew")

        # Configure rows/columns to shrink/grow
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)


class ContentFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__()
        self.configure(padding=(12, 3, 3, 3))
        # Create a canvas widget inside frame widget for scrollability
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.canvas.grid(row=0, rowspan=1000, column=0, columnspan=1000, sticky="nsew")
        self.columnconfigure(0, weight=1)

        # Create additional frame inside canvas to place actual stuff on
        self.frame = ttk.Frame(self)
        # Need to bind the configure event to a function that will reset the canvas scrollregion
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # create a window within the canvas to hold the frame
        self.canvas.create_window(0, 0, window=self.frame, anchor="nw",
                                  tags="self.frame")

        # Scrollbar
        self.s = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.s.grid(row=0, rowspan=1000, column=100, sticky="ns")
        self.canvas.configure(yscrollcommand=self.s.set)

    # This function resets the canvas scroll region whenever we add something
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class NavFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        # Need a super call to initiate Frame attributes
        super().__init__(*args, **kwargs)

        self.configure(padding=(10, 3, 10, 3))
        # Back, space, next buttons
        self.back_btn = ttk.Button(self, text="Back")
        self.middle = tk.Canvas(self, height=30)
        self.next_btn = ttk.Button(self, text="Next", )
        # Grid the three objects above
        self.back_btn.grid(row=1, column=1, sticky="ew")
        self.middle.grid(row=1, column=2, sticky="nsew")
        self.next_btn.grid(row=1, column=5, sticky="ew")
        # Configure the three above
        self.columnconfigure(2, weight=1)


class ClassicMenu(tk.Menu):

    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create Menu widgets to place in menubar
        self.fileMenu = tk.Menu(self)
        self.editMenu = tk.Menu(self)
        self.helpMenu = tk.Menu(self)
        self.viewMenu = tk.Menu(self)

        # Create cascades for each of the menu widgets
        self.add_cascade(menu=self.fileMenu, label='File')
        self.add_cascade(menu=self.editMenu, label='Edit')
        self.add_cascade(menu=self.viewMenu, label="View")
        self.add_cascade(menu=self.helpMenu, label="Help")

        # File menu commands
        self.fileMenu.add_command(label='New', command=self.newFile)
        self.fileMenu.add_command(label='Open...', command=self.openFile)
        self.fileMenu.add_command(label='Close', command=self.closeFile)
        self.fileMenu.add_command(label="Save As", command=self.saveAsFile)

        # Edit menu commands
        self.editMenu.add_command(label='Clear',
                                  command=lambda: window.focus_get().event_generate("<<Clear>>"))
        self.editMenu.add_command(label='Cut', accelerator='Ctrl + X',
                                  command=lambda: window.focus_get().event_generate("<<Cut>>"))
        self.editMenu.add_command(label='Copy', accelerator="Ctrl + C",
                                  command=lambda: window.focus_get().event_generate("<<Copy>>"))
        self.editMenu.add_command(label='Paste', accelerator="Ctrl + V",
                                  command=lambda: window.focus_get().event_generate("<<Paste>>"))
        self.editMenu.add_command(label='Undo', accelerator="Ctrl + Z",
                                  command=lambda: window.event_generate("<<Undo>>"))
        self.editMenu.add_command(label='Redo', accelerator="Ctrl + Y",
                                  command=lambda: window.event_generate("<<Redo>>"))

    def newFile(self):
        pass

    def openFile(self, multiple=False):
        filedialog.askopenfile(title='Open File', parent=self)

    def closeFile(self):
        pass

    def saveAsFile(self):
        filedialog.asksaveasfile(title="Save As", parent=self)


# Defines what the next button does in the nav menu
def nextButton(on_click: tk.Tk, close: tk.Tk):
    on_click
    close


# How to stop root when it is withdrawn
def onClose():
    if messagebox.askokcancel("Quit", "Would you like to close the entire application?"):
        root.destroy()


# Actually running the script
def main():
    global root
    root = tk.Tk()
    # tearOff prevents menus from being "torn off" into their own windows
    root.option_add('*tearOff', tk.FALSE)
    # root.withdraw()
    base = MainWindow(root)

    """window = tk.Toplevel()
    window.protocol("WM_DELETE_WINDOW", onClose)
    base = MainWindow(window)"""
    # Custom self.content for Index
    base.window.title("Index")
    welcome = ttk.Label(base.content, text="Welcome! Please enter your name below:")
    name = tk.StringVar()
    username = ttk.Entry(base.content, textvariable=name, width=10)

    for i in range(100):
        button = ttk.Button(base.content, text=i)
        button.grid(row=i+3, column=0)

    # Grid the above
    welcome.grid(row=1, column=1, sticky="nsew")
    username.grid(row=2, column=0, columnspan=3, sticky="nsew")

    # Start the mainloop
    root.mainloop()


if __name__ == '__main__':
    main()
