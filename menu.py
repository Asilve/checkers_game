import buttons
import pygame

# initialise
pygame.init()

# Game Screen parameters
screen_height = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Checkers")
icon_image = pygame.image.load("Icon.jpg").convert_alpha()
pygame.display.set_icon(icon_image)

# Main Menu Background
background_image = pygame.image.load('Background.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (600, 600))

# Creation of three buttons for the main menu
one_player_button = buttons.Button(180, 230, screen)
two_player_button = buttons.Button(180, 330, screen)
quit_button = buttons.Button(180, 430, screen)

# Text (Keeping button text outside of button class, due to positioning difficulties)
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 40)
title_font.set_underline(True)
title = title_font.render("Checkers", True, "Black")
button_one_text = button_font.render("One Player", True, "Black")
button_two_text = button_font.render("Two Player", True, "Black")
button_three_text = button_font.render("Quit", True, "Black")


# Function that displays the main menu to the user
def start_screen():
    # Background and Title Display
    screen.blit(background_image, (0, 0))
    screen.blit(title, (172, 100))
    # Button Display
    one_player_button.draw()
    two_player_button.draw()
    quit_button.draw()
    screen.blit(button_one_text, (226, 244))
    screen.blit(button_two_text, (227, 344))
    screen.blit(button_three_text, (271, 444))

    pygame.display.update()
