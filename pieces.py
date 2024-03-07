import pygame.draw
import board


class Piece:
    # Class variables to be used in the draw function.
    padding = 10
    outline = 2

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        # if piece is white, we will go up the board
        if self.colour == "White":
            self.direction = -1
        # Otherwise, we will go down the board (as black)
        else:
            self.direction = 1
        self.xpos = 0
        self.ypos = 0
        self.calculate_pos()

    def __repr__(self):
        return str(self.colour)

    # Calculates the position of the piece
    def calculate_pos(self):
        self.xpos = board.square_size * self.col + 20 + board.square_size // 2
        self.ypos = board.square_size * self.row + 20 + board.square_size // 2

    # Turns the piece into a king piece
    def make_king(self):
        self.king = True

    # Draws the piece onto the board
    def draw(self, window):
        radius = board.square_size // 2 - self.padding
        # Grey outline
        pygame.draw.circle(window, "Gray", (self.xpos, self.ypos), radius + self.outline)
        # Piece colour on top of the outline to create a shadow effect
        pygame.draw.circle(window, self.colour, (self.xpos, self.ypos), radius)

