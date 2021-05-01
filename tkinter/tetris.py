import random

import tkinter as tk
from tkinter import ttk


class GameBoard(tk.Canvas):
    pass


class Block():

    def __init__(self, canvas, coords, color='red'):
        # creating a rectangle on the provided canvas with a specified color
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(coords, fill=color, tags=("active"))
        print(str(self.id) + " coordinates: " + str(self.canvas.coords(self.id)))


class Piece():

    LINE = [[0.0, 0.0, 15.0, 15.0],
            [15.0, 0.0, 30.0, 15.0],
            [30.0, 0.0, 45.0, 15.0],
            [45.0, 0.0, 60.0, 15.0]]

    R_L = [[]

    ]

    def __init__(self, canvas, start_point, piece_shape=None):
        self.canvas = canvas
        self.start_point = start_point
        self.matrix = []
        if piece_shape in ["line", self.LINE]:
            self.matrix = self.LINE
        # I create a list of lists, a matrix, and each inner list is a set of coordinates
        # to pass to the Block function
        for coords in self.matrix:
            Block(self.canvas, coords)


class Tetris():

    COLORS = ['black', 'red', 'green', 'blue', 'cyan', 'magenta']
    GAME_WIDTH = 350
    GAME_HEIGHT = 450
    GAME_SPEED = 500
    BLOCK_SIZE = 15

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris!")
        self.root.geometry("360x460")
        self.root.bind("<Key>", self.set_controls)

    def start_game(self):
        # will be a mainloop
        self.canvas = self.create_canvas()
        for i in range(1):
            Piece(self.canvas, 5, Piece.LINE)
        self.root.after(self.GAME_SPEED, None)
        self.root.mainloop()

    def set_controls(self, event):
        if event.char == "\0x8FB":  # Left Arrow
            id = self.canvas.find_withtag("active")
            self.canvas.move(id, -10, 0)
        if event.char == "\0x8FC":  # Up Arrow
            pass
        if event.char == "\0x8FD":  # Right Arrow
            id = self.canvas.find_withtag("active")
            self.canvas.move(id, 10, 0)

    def create_canvas(self):
        # create the canvas which will actually house the game
        self.canvas = GameBoard(self.root, width=self.GAME_WIDTH, height=self.GAME_HEIGHT,
                                bg="white")
        self.canvas.grid(row=0, rowspan=2, column=0, columnspan=2)
        return self.canvas

    def create_block(self, coords=None):
        """Creates an object of block class, returns that object"""
        if not coords:
            self.coords = self.generate_coordinates()
        color = Tetris.COLORS[random.randint(0, 5)]
        block = Block(self.canvas, coords=self.coords, color=color)
        return block

    def generate_coordinates(self):
        # left side is anything up to the width of canvas minus width of block
        x1 = random.randint(0, Tetris.GAME_WIDTH - Tetris.BLOCK_SIZE)
        # use random.choice to add element of randomness to block starting height
        y1 = random.choice([10, 20, 30])
        # size of square is 15 (14?) pixels
        x2 = x1 + Tetris.BLOCK_SIZE
        y2 = y1 + Tetris.BLOCK_SIZE
        return (x1, y1, x2, y2)


def main():
    game = Tetris()
    game.start_game()


if __name__ == "__main__":
    main()
