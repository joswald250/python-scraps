import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk
# ttk is a submodule of tkinter, any widget you pull from it needs to be
# prefixed with ttk


class FeetToMeters:
    # Create a class to hold everything, which are defined as methods
    def __init__(self, root):
        root.title("Feet to Meters")  # Gives the main window a name

        """ The code below creates a context widget (ttk.Frame) that will hold
        all the contents of the user interface.
        After creating the frame, we use the .grid method to place the frame
        in the main window. The columnconfigure
        and rowconfigure tell tk that the frame should expand to fill any
        extra space if the window is resized."""

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        """ Here we create a ttk.Entry widget and place it in its "parent"
        frame, mainframe. This makes it a "child" of the mainframe widget.
        The "parent" widget is passed as the first parameter when
        instantiating any widget. When we create a widget, we can give
        it configuration options (width and textvariable, here). When
        widgets are created, they need to be placed on screen, otherwise
        they won't appear, this is the ".grid" method used.
        The "sticky" option tells tkinter to attach the widget to a side
        (indicated by cardinal directions) of its container cell, multiple
        attachments will spread the widget out. """

        self.feet = tk.StringVar()
        # must be a stringvar for the textvariable method to work
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        # textvariable automatically updates the widget whenever feet changes
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        """ Do the same as above for multiple widgets, notice the command for
        the button widget - links to a function
        object (not the function itself, thus the lack of parentheses). """

        self.meters = tk.StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2,
                                                            row=2,
                                                            sticky=(W, E))

        ttk.Button(mainframe, text="Calculate",
                   command=self.calculate).grid(column=3, row=3, sticky=W)
        # The command option here is given a "callback" -
        # a function object to execute

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2,
                                                           sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        """ The below puts some padding on every child widget in the content
        frame widget. We then start the cursor in the entry field, and "bind"
        the return (enter) key to the calculate function
        (not the button widget, though the effect is the same). """

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        # Included this function first simply because we reference it
        # throughout the program
        try:
            value = float(self.feet.get())
            # Use the get or set variable on a StringVar() object to read/write
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


root = tk.Tk()  # Sets up the main application window
FeetToMeters(root)  # Instantiates class
root.mainloop()  # Event loop starts, puts everything on screen
