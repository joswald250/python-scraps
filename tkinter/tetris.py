#! usr/bin/python3

import random

import tkinter as tk


class GameBoard(tk.Canvas):
    pass


class Block():

    COLORS = ['black', 'red', 'green', 'blue', 'cyan', 'magenta']

    def __init__(self, canvas, coords, color, start_point=[1, 1]):
        # creating a rectangle on the provided canvas with a specified color
        self.canvas = canvas
        self.color = color
        self.start_point = start_point
        self.coords = coords
        self.offset_coords = self.add_offset(self.coords, self.start_point)
        self.id = self.canvas.create_rectangle(self.offset_coords, fill=self.color,
                                               tags=("active", "block"))
        print(str(self.id) + " coordinates: " + str(self.canvas.coords(self.id)))

    def add_offset(self, coords, start_point):
        # Convert the start point to offset coordinates
        x_off = start_point[0]
        y_off = start_point[1]
        # take the coordinates passed from piece matrix and add offset
        x_left = (coords[0] + x_off)
        y_top = (coords[1] + y_off)
        x_right = (coords[2] + x_off)
        y_bottom = (coords[3] + y_off)
        return (x_left, y_top, x_right, y_bottom)


class Piece():

    def __init__(self, canvas, start_point=[1, 1], piece_shape=None):
        self.canvas = canvas
        self.deactivate_all()  # Need to make this new piece the only active one
        self.start_point = start_point
        self.color = self.choose_color()
        self.matrix = self.choose_matrix(piece_shape)
        for coords in self.matrix:
            # Actually builds the shape by constructing block objects at each set of coords
            Block(self.canvas, coords, color=self.color,
                  start_point=self.start_point)

    def deactivate_all(self):
        self.canvas.dtag("active", "active")

    def choose_color(self):
        return random.choice(Block.COLORS)

    def choose_matrix(self, piece_shape):
        # Series of if statements chooses which shape to return
        if piece_shape in ["line", Tetris.LINE]:
            self.matrix = Tetris.LINE
            return self.matrix
        elif piece_shape in ["RIGHT_L", Tetris.RIGHT_L, "right L"]:
            self.matrix = Tetris.RIGHT_L
            return self.matrix
        elif piece_shape in ["LEFT_L", Tetris.LEFT_L, "left L"]:
            self.matrix = Tetris.LEFT_L
            return self.matrix
        elif piece_shape in ["T", "t shape", "T Shape", Tetris.T_SHAPE]:
            self.matrix = Tetris.T_SHAPE
            return self.matrix
        elif piece_shape in ["S", "s shape", "S Shape", Tetris.S_SHAPE]:
            self.matrix = Tetris.S_SHAPE
            return self.matrix
        elif piece_shape in ["Z", "z shape", "Z Shape", Tetris.Z_SHAPE]:
            self.matrix = Tetris.Z_SHAPE
            return self.matrix
        elif piece_shape in ["SQUARE", "square", Tetris.SQUARE]:
            self.matrix = Tetris.SQUARE
            return self.matrix
        else:
            self.matrix = Tetris.LINE
            return self.matrix


class Tetris():

    # Game-wide variables
    GAME_WIDTH = 350
    GAME_HEIGHT = 450
    GAME_SPEED = 500
    BLOCK_SIZE = 15

    # Series of matrices that represent shapes in Tetris
    s = BLOCK_SIZE

    LINE = [[0, 0, s, s],
            [s, 0, (2 * s), s],
            [(2 * s), 0, (3 * s), s],
            [(3 * s), 0, (4 * s), s]]

    RIGHT_L = [[0, s, s, (2 * s)],
               [0, (2 * s), s, (s)],
               [0, (s), s, (4 * s)],
               [s, (s), (2 * s), (4 * s)]]

    LEFT_L = [[s, s, (2 * s), (2 * s)],
              [s, (2 * s), (2 * s), (s)],
              [s, (s), (2 * s), (4 * s)],
              [0, (s), s, (4 * s)]]

    T_SHAPE = [[0, 0, s, s],
               [s, 0, (2 * s), s],
               [(2 * s), 0, (s), s],
               [s, s, (2 * s), (2 * s)]]

    S_SHAPE = [[0, s, s, (2 * s)],
               [s, 0, (2 * s), s],
               [(2 * s), 0, (s), s],
               [s, s, (2 * s), (2 * s)]]

    Z_SHAPE = [[0, 0, s, s],
               [s, 0, (2 * s), s],
               [s, s, (2 * s), (2 * s)],
               [(2 * s), s, (s), (2 * s)]]

    SQUARE = [[0, 0, s, s],
              [s, 0, (2 * s), s],
              [0, s, s, (2 * s)],
              [s, s, (2 * s), (2 * s)]]

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("360x460")
        self.root.bind("<Key>", self.set_controls)  # Anytime a key is pressed, runs this function

    def start_game(self):
        # will be a mainloop
        self.canvas = self.create_canvas()
        Piece(self.canvas, [20, 30], self.SQUARE)
        Piece(self.canvas, piece_shape=self.LINE)
        self.root.after(self.GAME_SPEED, None)
        self.root.mainloop()

    def set_controls(self, event):
        if event.keysym == "Left":  # Left Arrow
            # Returns True/False depending upon ability to move
            ok_to_move = self.check_move([-10, 0])
            if ok_to_move:
                active_piece = self.canvas.find_withtag("active")
                # Finds all objects with "active" tag, then for each block, moves them
                for block_id in active_piece:
                    self.canvas.move(block_id, -10, 0)
        if event.keysym == "Up":  # Up Arrow
            pass
        if event.keysym == "Down":
            pass
        if event.keysym == "Right":  # Right Arrow
            ok_to_move = self.check_move([10, 0])
            if ok_to_move:
                active_piece = self.canvas.find_withtag("active")
                for block_id in active_piece:
                    self.canvas.move(block_id, 10, 0)

    def create_canvas(self):
        # create the canvas which will actually house the game
        self.canvas = GameBoard(self.root, width=self.GAME_WIDTH, height=self.GAME_HEIGHT,
                                bg="white")
        self.canvas.grid(row=0, rowspan=2, column=0, columnspan=2, padx=3, pady=3)
        return self.canvas

    def check_move(self, coords_change=[]):
        # Will return False if the move brings the piece in contact with a boundary
        active_piece = self.canvas.find_withtag("active")  # Find piece
        # Sets variables that will be checked
        x_min = self.GAME_WIDTH
        x_max = 0
        y_max = self.GAME_HEIGHT  # Y value increases as piece goes down
        piece_ids = []  # Going to be used to compare with overlapping blocks
        for block_id in active_piece:
            piece_ids.append(block_id)
            # For each block, get its coordinates
            block_coords = self.canvas.coords(block_id)
            x_left = block_coords[0]
            y_top = block_coords[1]
            x_right = block_coords[2]
            y_bottom = block_coords[3]
            # Then check if that coordinate is a min/max
            if x_left < x_min:
                x_min = x_left
            if y_bottom < y_max:
                y_max = y_bottom
            if x_right > x_max:
                x_max = x_right
        # All coordinates with the coordinate change factored in
        x_left_new = x_min + coords_change[0]
        y_top_new = y_top + coords_change[1]
        x_right_new = x_max + coords_change[0]
        y_bottom_new = y_max + coords_change[1]
        # Going to create a box with coordinate change factored in to
        # check if that box is tangent to any other piece
        overlapping = self.canvas.find_overlapping(
                                    x_left_new,
                                    y_top_new,
                                    x_right_new,
                                    y_bottom_new)
        # Add the expected coordinate changes to mins/maxes and check
        if x_left_new < 0 or \
            y_bottom_new >= self.GAME_HEIGHT or \
                x_right_new > self.GAME_WIDTH or \
                any(overlapping) not in piece_ids:  # box automatically includes pieces in it
            print(x_left_new)
            print(y_bottom_new)
            print(x_right_new)
            print(False)
            return False
        else:
            return True


def main():
    game = Tetris()
    game.start_game()


if __name__ == "__main__":
    main()
