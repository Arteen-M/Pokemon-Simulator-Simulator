import pygame
import time


# These two functions are for writing text to the screen. For some reason, I couldn't import my text module
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def write_text(msg, x, y, font, size, colour):
    text = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(msg, text, colour)
    textRect.center = (x, y)
    return textSurf, textRect
# -------------------------------------------------------


# For buttons
class Button:
    def __init__(self, x, y, w, h, val, disp, show=False):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self._value = val
        self.window = disp
        self.show = show

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # The paramaters of the button must be met
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            # If the mouse is clicked AND the mouse is within its borders
            if click[0] == 1:
                # Slight delay, before returning True
                time.sleep(0.1)
                return True

        # Show the outline (For testing purposes)
        if self.show:
            pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)

        # Returns none otherwise
        return None

    # Move the button if necessary
    def move(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val


# Inherited class from the button, since all Back Buttons share attributes
class BackButton(Button):
    def __init__(self, val, disp, show=False):
        Button.__init__(self, 10, 10, 92, 31, val, disp, show)

    def update(self):
        return Button.update(self)


# Inherited class from the button, this one is specific because it shows the moves of each pokemon
class MoveButton(Button):
    def __init__(self, name, type, power, acc, x, y, display):
        Button.__init__(self, x, y, 200, 50, True, display, False)

        self.name = name
        self.type = type
        self.power = power
        self.accuracy = acc
        self.display = display

        self.name_surf, self.name_rect = write_text(self.name, self.x + 50, self.y + 15, "calibri", 15, (0, 0, 0))
        self.type_surf, self.type_rect = write_text(self.type, self.x + self.width - 50, self.y + 15, "calibri", 15, (0, 0, 0))
        self.stat_surf, self.stat_rect = write_text("%s/%s" % (str(self.power), str(self.accuracy)), self.x + 50, self.y + 35, "calibri", 15, (0, 0, 0))

    def update(self):
        # Displays an outline and all text
        pygame.draw.rect(self.display, (0, 0, 0), (self.x, self.y, self.width, self.height), 1)
        self.display.blit(self.name_surf, self.name_rect)
        self.display.blit(self.type_surf, self.type_rect)
        self.display.blit(self.stat_surf, self.stat_rect)

        return Button.update(self)
