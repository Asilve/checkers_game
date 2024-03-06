import pygame
import sys
from menu import screen
from pieces import Piece

# Board size values
rows, cols = 8, 8
square_size = 70

# Colour values
dark_brown_square = (175, 130, 45)
light_brown_square = (240, 210, 150)
teal = (115, 225, 225)


class Board:
    # Creates a background for the board. The lighter squares will be added on top of this background.
    board_window = pygame.Surface((560, 560))
    board_fill = board_window.fill(dark_brown_square)

    def __init__(self):
        self.board = []
        self.black_pieces = 12
        self.black_kings = 0
        self.white_pieces = 12
        self.white_kings = 0
        self.selected_piece = None
        self.create_board()

    def draw_grid(self, window):
        # Fill whole screen
        window.fill("Black")
        # Add the dark brown square to the screen
        window.blit(self.board_window, (20, 20))
        # Add the light squares on top of the dark square to create a checkerboard pattern
        for r in range(rows):
            for c in range(r % 2, rows, 2):
                pygame.draw.rect(window, light_brown_square, (20 + r*square_size, 20 + c*square_size, square_size, square_size))

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, "Black"))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, "White"))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_grid(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


# Create instance of a board
board = Board()


# 2 player game loop
def play_2player():
    playing = True

    while playing:
        # Display the board
        board.draw(screen)
        pygame.display.update()

        # Get event
        for event in pygame.event.get():
            # If Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
