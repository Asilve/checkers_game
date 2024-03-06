import pygame
import menu
import board

# Variable to set frames per second of the program
fps = 60


def main():
    # Gameplay Loop
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        # Start main menu
        menu.start_screen()
        # Get mouse position and call hover over function
        mouse = pygame.mouse.get_pos()
        menu.one_player_button.hover_over(mouse)
        menu.two_player_button.hover_over(mouse)
        menu.quit_button.hover_over(mouse)

        # Check main menu events
        for event in pygame.event.get():
            # Check for Quitting Options
            if event.type == pygame.QUIT:
                run = False
            elif menu.quit_button.hover:
                if menu.quit_button.clicked:
                    run = False

            # Check if user wants to play a one player game against a computer
            elif menu.one_player_button.hover:
                if menu.one_player_button.clicked:
                    print("Not yet implemented")

            # Check if user wants to play a two player game against another human.
            elif menu.two_player_button.hover:
                if menu.two_player_button.clicked:
                    board.play_2player()
    # Outside loop, Exits the game
    pygame.quit()


# Calling Main function
main()
