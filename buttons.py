import pygame

# initialise
pygame.init()
pygame.mixer.init()


# Button class for the main menu
class Button:

    def __init__(self, x, y, display):
        # Display options
        self.back_size = pygame.Surface((240, 55))
        self.top_size = pygame.Surface((234, 49))
        self.back_fill = self.back_size.fill((100, 85, 10))
        self.top_fill = self.top_size.fill((190, 145, 50))
        self.coord_one = (x, y)
        self.coord_two = (x + 3, y + 3)
        self.display = display
        # Button behaviour
        self.rect = pygame.Rect(x, y, 240, 55)
        self.hover = False
        self.clicked = False
        # Button sound effect
        self.sound = pygame.mixer.Sound('button-hover.mp3')

    # Function that lets us display the buttons.
    def draw(self):
        self.display.blit(self.back_size, self.coord_one)
        self.display.blit(self.top_size, self.coord_two)

    # Function that alters the states of the button and to play a sound every time we hover over it.
    def hover_over(self, mouse):
        # Check if mouse is over the button location
        if self.rect.collidepoint(mouse):
            # Check if it's the first occurrence of us hovering over, if so play a sound and change hover state
            if not self.hover:
                self.hover = True
                self.sound.play()
            # Check if we click the button while we hover over, if so change clicked state of the button
            elif pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        # Otherwise, if not hovering over, reset the button states to default
        else:
            self.hover = False
            self.clicked = False
