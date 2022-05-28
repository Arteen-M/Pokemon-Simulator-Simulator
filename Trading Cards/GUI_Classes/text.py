import pygame


# Functions to create text


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)  # Renders the font with the colour (usually black)
    return textSurface, textSurface.get_rect()


def write_text(msg, x, y, font, size, colour=(0, 0, 0)):
    text = pygame.font.SysFont(font, size)  # Initializes the font
    textSurf, textRect = text_objects(msg, text, colour)  # Creates (renders) the text
    textRect.center = (x, y)  # Sets the center of the text
    return textSurf, textRect

