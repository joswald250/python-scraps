import random

import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):

    canvas_width = 300
    canvas_height = 400

    def __init__(self, parent):
        super().__init__()

        self.colors = ['black', 'red', 'green', 'blue', 'cyan', 'magenta']

        # create a frame that is the base for everything else
        self.frame = ttk.Frame(parent, padding=(5, 5, 5, 5))
        self.frame.grid(row=0, rowspan=2, column=0, columnspan=2, sticky="nsew")

        # create the canvas which will actually house the game
        self.canvas = tk.Canvas(self.frame)
        self.canvas.configure(width=self.canvas_width, height=self.canvas_height,
                              bg="white")
        self.canvas.grid(row=0, rowspan=2, column=0, columnspan=2, sticky="nsew")

        # start the game
        self.start_game()

    def create_block(self):
        """Creates an object of block class, returns that object"""
        color = self.colors[random.randint(0, 5)]
        print(str(color))
        block = Block(self.canvas, color=color)
        return block

    def drop_block(self, block):
        # while loop drops block until its lower x coord. is less than the height of the canvas
        while block.canvas.coords(block.id)[3] < 395:
            root.after(100, block.move_down(block.id, step=10))
            root.update()
        return True

    def start_game(self):
        """Initiates the first block, drops it, then continues game"""
        for i in range(20):
            block = self.create_block()
            marker = False
            while not marker:
                marker = self.drop_block(block)
        print("done")


class Block():

    def __init__(self, canvas, color='red'):
        # creating a rectangle on the provided canvas with a specified color
        self.canvas = canvas
        self.id = self.canvas.create_rectangle((self.generate_coordinates()), fill=color, width=0)
        print(str(self.id) + " coordinates: " + str(self.canvas.coords(self.id)))
        self.generate_coordinates()

    def move_down(self, id, step=1):
        """simply grabs the provided object's object id and uses it in the canvas move method"""
        self.canvas.move(str(id), 0, step)
        print("dropped block")

    def generate_coordinates(self):
        # left side is anything up to the width of canvas minus width of block
        x1 = random.randint(0, App.canvas_width - 15)
        # use random.choice because the drop function moves in increments of ten, this needs to
        # line up with bottom (height of canvas is 395), so must end in 5
        y1 = random.choice([5, 15, 25])
        # size of square is 15 (14?) pixels
        x2 = x1 + 15
        y2 = y1 + 15
        return (x1, y1, x2, y2)


def main():
    global root
    root = tk.Tk()
    root.option_add('*tearOff', tk.FALSE)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
