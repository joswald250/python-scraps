import random

import tkinter as tk


class GameBoard(tk.Canvas):
    pass


class Block():

    COLORS = ['red', 'green', 'blue', 'cyan', 'magenta']

    def __init__(self, canvas, coords, color, start_point=[1, 1]):
        # creating a rectangle on the provided canvas with a specified color
        self.canvas = canvas
        self.color = color
        self.start_point = start_point
        self.coords = coords
        self.offset_coords = self.add_offset(self.coords, self.start_point)
        # Once coordinates are obtained, draw the block on screen with tags
        self.id = self.canvas.create_rectangle(self.offset_coords, fill=self.color,
                                               tags=("active", "block"))
        # print(str(self.id) + " coordinates: " + str(self.canvas.coords(self.id)))

    def add_offset(self, coords, start_point):
        # Convert the start point to offset coordinates
        x_off = start_point[0]
        y_off = start_point[1]
        # take the coordinates passed from piece matrix and add offset
        x_left = (coords[0] + x_off)
        y_top = (coords[1] + y_off)
        x_right = (coords[2] + x_off)
        y_bottom = (coords[3] + y_off)
        # Error validation - make sure piece is on screen
        if x_left < 0 or x_right > Tetris.GAME_WIDTH or y_top < 0 or y_bottom > 60:
            return (1, 1, 16, 16)
        else:
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

    def deactivate_all(self):  # Removes active tag from everything
        self.canvas.dtag("active", "active")

    def choose_color(self):
        return random.choice(Block.COLORS)

    def choose_matrix(self, piece_shape):  # Series of if statements chooses which shape to return
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
    GAME_WIDTH = 360
    GAME_HEIGHT = 480
    GAME_SPEED = 500
    BLOCK_SIZE = 15

    # Series of matrices that represent shapes in Tetris
    s = BLOCK_SIZE

    LINE = [[0, 0, s, s],
            [s, 0, (2 * s), s],
            [(2 * s), 0, (3 * s), s],
            [(3 * s), 0, (4 * s), s]]

    RIGHT_L = [[0, 0, s, s],
               [0, s, s, (2 * s)],
               [0, (2 * s), s, (3 * s)],
               [s, (2 * s), (2 * s), (3 * s)]]

    LEFT_L = [[s, 0, (2 * s), s],
              [s, s, (2 * s), (2 * s)],
              [s, (2 * s), (2 * s), (3 * s)],
              [0, (2 * s), s, (3 * s)]]

    T_SHAPE = [[0, 0, s, s],
               [s, 0, (2 * s), s],
               [(2 * s), 0, (3 * s), s],
               [s, s, (2 * s), (2 * s)]]

    S_SHAPE = [[0, s, s, (2 * s)],
               [s, 0, (2 * s), s],
               [s, s, (2 * s), (2 * s)],
               [(2 * s), 0, (3 * s), s]]

    Z_SHAPE = [[0, 0, s, s],
               [s, 0, (2 * s), s],
               [s, s, (2 * s), (2 * s)],
               [(2 * s), s, (3 * s), (2 * s)]]

    SQUARE = [[0, 0, s, s],
              [s, 0, (2 * s), s],
              [0, s, s, (2 * s)],
              [s, s, (2 * s), (2 * s)]]

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("360x490")
        self.root.bind("<Key>", self.set_controls)  # Anytime a key is pressed, runs this function

    def start_game(self):
        self.canvas = self.create_canvas()
        self.drop()
        self.root.mainloop()

    def set_controls(self, event):
        if event.keysym == "Left":  # Left Arrow
            # Returns True/False depending upon ability to move
            ok_to_move = self.check_move([-self.BLOCK_SIZE, 0])
            if ok_to_move:
                active_piece = self.canvas.find_withtag("active")
                # Finds all objects with "active" tag, then for each block, moves them
                for block_id in active_piece:
                    self.canvas.move(block_id, -self.BLOCK_SIZE, 0)

        if event.keysym == "Up":  # Up Arrow
            pass
        if event.keysym == "Down":
            active_piece = self.canvas.find_withtag("active")
            if self.check_below([0, self.BLOCK_SIZE]):
                # Finds all objects with "active" tag, then for each block, moves them
                for block_id in active_piece:
                    self.canvas.move(block_id, 0, self.BLOCK_SIZE)
        if event.keysym == "Right":  # Right Arrow
            ok_to_move = self.check_move([self.BLOCK_SIZE, 0])
            if ok_to_move:
                active_piece = self.canvas.find_withtag("active")
                for block_id in active_piece:
                    self.canvas.move(block_id, self.BLOCK_SIZE, 0)

    def create_canvas(self):  # create the canvas which will actually house the game
        self.canvas = GameBoard(self.root, width=self.GAME_WIDTH, height=self.GAME_HEIGHT,
                                bg="white")
        self.canvas.grid(row=0, rowspan=2, column=0, columnspan=2, padx=3, pady=3)
        return self.canvas

    def choose_piece(self):
        return random.choice([self.LINE, self.RIGHT_L, self.LEFT_L, self.SQUARE,
                              self.S_SHAPE, self.Z_SHAPE, self.T_SHAPE])

    def check_move(self, coords_change=[]):  # returns False if the piece will contact a boundary
        active_piece = self.canvas.find_withtag("active")  # Find piece
        can_move = False
        for block_id in active_piece:
            # For each block, get its coordinates
            block_coords = self.canvas.coords(block_id)
            x_left = block_coords[0]
            y_top = block_coords[1]
            x_right = block_coords[2]
            y_bottom = block_coords[3]
            # All coordinates with the coordinate change factored in
            x_left_new = x_left + coords_change[0]
            y_top_new = y_top + coords_change[1]
            x_right_new = x_right + coords_change[0]
            y_bottom_new = y_bottom + coords_change[1]
            # If new coords are out of bounds, return false
            if x_left_new < 0 or y_bottom_new >= self.GAME_HEIGHT or x_right_new > self.GAME_WIDTH:
                can_move = False
                return False
            # Going to create a box with coordinate change factored in to
            # check if that box is tangent to any other piece
            # Subtract 1 b/c canvas automatically adds 1 to box size when it makes it
            overlapping = self.canvas.find_overlapping(
                                        x_left_new + 1,
                                        y_top_new,
                                        x_right_new - 1,
                                        y_bottom_new - 1)
        # Add the expected coordinate changes to mins/maxes and check
        # If any blocks have a non-active overlapping piece, return False
            for i in range(len(overlapping)):
                if overlapping[i] not in active_piece:
                    return False
                else:
                    can_move = True
                    # Can't return true, or else loop will terminate before all options
        return can_move

    def check_below(self, coords_change=[]):  # Will return True if another piece is below
        active_piece = self.canvas.find_withtag("active")  # Find piece
        can_move = False
        for block_id in active_piece:
            # For each block, get its coordinates
            block_coords = self.canvas.coords(block_id)
            x_left = block_coords[0]
            y_top = block_coords[1]
            x_right = block_coords[2]
            y_bottom = block_coords[3]
            if y_bottom >= self.GAME_HEIGHT:
                for block_id in active_piece:
                    self.canvas.dtag(block_id, "active")
                return False
            # All coordinates with the coordinate change factored in
            x_left_new = x_left + coords_change[0]
            y_top_new = y_top + coords_change[1]
            x_right_new = x_right + coords_change[0]
            y_bottom_new = y_bottom + coords_change[1]
            # Going to find if any pieces are tangent to bottom coordinates
            overlapping = self.canvas.find_overlapping(
                                        x_left_new + 1,
                                        y_top_new,
                                        x_right_new - 1,
                                        y_bottom_new - 1)
            for i in range(len(overlapping)):
                if overlapping[i] not in active_piece:
                    # deactivates the piece
                    for block_id in active_piece:
                        self.canvas.dtag(block_id, "active")
                    return False
                else:
                    can_move = True
        return can_move

    def game_over(self):  # Returns true for game over
        active_piece = self.canvas.find_withtag("active")  # Find piece
        tops = []
        # Going to grab each block's top coordinate
        for block_id in active_piece:
            block_coords = self.canvas.coords(block_id)
            tops.append(block_coords[1])
        # loss conditions = piece can't move down, is at top
        if (0 in tops or 1 in tops) and not self.check_below([0, self.BLOCK_SIZE]):
            return True
        else:
            return False

    def end_game(self):
        print("game over!")

    def drop(self):
        active_piece = self.canvas.find_withtag("active")  # Find piece
        if not active_piece:
            Piece(self.canvas, piece_shape=self.LINE)
            # Piece(self.canvas, piece_shape=self.choose_piece())
        if not self.game_over():
            if self.check_below([0, self.BLOCK_SIZE]):
                # Finds all objects with "active" tag, then for each block, moves them
                for block_id in active_piece:
                    self.canvas.move(block_id, 0, self.BLOCK_SIZE)
        else:
            return
        self.root.after(50, self.drop)


def main():
    game = Tetris()
    game.start_game()


if __name__ == "__main__":
    main()
