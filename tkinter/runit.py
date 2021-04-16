import tkinter as tk
from tkinter import ttk


class Index:

    def __init__(self, root):
        root.title("Index")
        system = str(root.tk.call("tk", "windowingsystem"))

        # Create a menu at the top
        menubar = ClassicMenu(root)
        root['menu'] = menubar
        # create a frame on top
        content = ContentFrame(root)
        content.grid(column=0, columnspan=2, row=0, sticky="nsew")
        # Create a frame on bottom with the nav buttons
        bottomframe = NavFrame(root)
        bottomframe.grid(column=0, columnspan=2, row=1, sticky="nsew")

        # Configure rows/columns to shrink/grow
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        # Custom content for Index
        welcome = ttk.Label(content, text="Welcome!")
        system_text = ttk.Label(content, text=system)
        name = tk.StringVar()
        username = ttk.Entry(content, textvariable=name)

        welcome.grid(row=1, column=2, sticky="nsew")
        system_text.grid(row=2, column=2, sticky="nsew")
        username.grid(row=3, column=2, sticky="nsew")


class ContentFrame(ttk.Frame):

    def __init__(self, frame):
        super(ContentFrame, self).__init__()

        self.configure(padding=(10, 3, 10, 3))

        # Create a canvas widget inside frame widget for scrollability
        canvas = tk.Canvas(self)
        canvas.grid(row=0, rowspan=100, column=0, columnspan=100, sticky="nsew")
        self.columnconfigure(0, weight=1)

        # Scrollbar
        s = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=s.set)
        s.grid(row=0, rowspan=100, column=1000)


class NavFrame(ttk.Frame):

    def __init__(self, frame):
        # Need a super call to initiate Frame attributes
        super(NavFrame, self).__init__()

        self.configure(padding=(10, 3, 10, 3))
        # Back, space, next buttons
        back_btn = ttk.Button(self, text="Back")
        middle = tk.Canvas(self, height=50)
        next_btn = ttk.Button(self, text="Next")
        # Grid the three objects above
        back_btn.grid(row=1, column=1, sticky="ew")
        middle.grid(row=1, column=2, sticky="nsew")
        next_btn.grid(row=1, column=5, sticky="ew")
        # Configure the three above
        self.columnconfigure(2, weight=1)


class ClassicMenu(tk.Menu):

    def __init__(self, root):
        super(ClassicMenu, self).__init__()

        # Create Menu widgets to place in menubar
        fileMenu = tk.Menu(self)
        editMenu = tk.Menu(self)
        helpMenu = tk.Menu(self)
        viewMenu = tk.Menu(self)

        # Create cascades for each of the menu widgets
        self.add_cascade(menu=fileMenu, label='File')
        self.add_cascade(menu=editMenu, label='Edit')
        self.add_cascade(menu=viewMenu, label="View")
        self.add_cascade(menu=helpMenu, label="Help")

        # File menu commands
        fileMenu.add_command(label='New', command=self.newFile)
        fileMenu.add_command(label='Open...', command=self.openFile)
        fileMenu.add_command(label='Close', command=self.closeFile)

        # Edit menu commands
        editMenu.add_command(label='Clear',
                             command=lambda: root.focus_get().event_generate("<<Clear>>"))
        editMenu.add_command(label='Cut', accelerator='Ctrl + X',
                             command=lambda: root.focus_get().event_generate("<<Cut>>"))
        editMenu.add_command(label='Copy', accelerator="Ctrl + C",
                             command=lambda: root.focus_get().event_generate("<<Copy>>"))
        editMenu.add_command(label='Paste', accelerator="Ctrl + V",
                             command=lambda: root.focus_get().event_generate("<<Paste>>"))
        editMenu.add_command(label='Undo', accelerator="Ctrl + Z",
                             command=lambda: root.event_generate("<<Undo>>"))
        editMenu.add_command(label='Redo', accelerator="Ctrl + Y",
                             command=lambda: root.event_generate("<<Redo>>"))

    def newFile(self):
        pass

    def openFile(self):
        tk.ask_filedialog

    def closeFile(self):
        pass


# Actually running the script
def main():
    root = tk.Tk()
    root.option_add('*tearOff', tk.FALSE)
    Index(root)
    root.mainloop()


if __name__ == '__main__':
    main()
