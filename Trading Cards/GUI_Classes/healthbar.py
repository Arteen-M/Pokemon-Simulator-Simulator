import pygame

# Same as Button Class
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def write_text(msg, x, y, font, size, colour):
    text = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(msg, text, colour)
    textRect.center = (x, y)
    return textSurf, textRect


class HealthBar:
    # Initializes the required variables
    def __init__(self, total, current, x, y, w, h, display, thickness=1):
        self.total = total
        self.current = current
        self.rect = (x, y, w, h)
        self.display = display
        self.thickness = thickness

    # Draws the healtbar
    def update(self):
        pygame.draw.rect(self.display, (0, 255, 0), (self.rect[0], self.rect[1], self.rect[2] * (self.current/self.total), self.rect[3]))
        pygame.draw.rect(self.display, (0, 0, 0), self.rect, self.thickness)


# Inherited class, the only difference is that it shows a name with the healthbar, and can change values
class DisplayHealth(HealthBar):
    # Initializes the required variables
    def __init__(self, total, current, x, y, w, h, display, name):
        HealthBar.__init__(self, total, current, x, y, w, h, display, 1)
        self.name = name
        self.name_surf, self.name_rect = write_text(self.name, x+(w/2), y-(h/2), "calibri", 15, (0, 0, 0))

    # Displays the new health with the updated healthbar (and the name)
    def update(self, new_health):
        self.current = new_health
        HealthBar.update(self)
        self.display.blit(self.name_surf, self.name_rect)





