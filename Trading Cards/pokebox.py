import pygame
from GUI_Classes.images import Image
from GUI_Classes.button import Button
from GUI_Classes.text import write_text

WIDTH = 1000
HEIGHT = 700

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
DARK_GRAY = (125, 125, 150)
LIGHT_GRAY = (125, 125, 125)
LIGHT_BLUE = (29, 161, 242)

margin = 35


# UI ELEMENT FOR SELECTING POKEMON (Teambuilding)
class PokeBox:
    def __init__(self, name, type_1, type_2, hp, attack, defense, special, speed, disp, pos=[WIDTH/2, 305]):
        # Gets all the required variables (name, types, stats)
        self.name = name
        self.type_1 = type_1
        if isinstance(type_2, float):
            self.type_2 = None
        else:
            self.type_2 = type_2
        self.hp = hp
        self.atk = attack
        self.defe = defense
        self.spc = special
        self.spe = speed
        self.pos = pos
        self.display = disp
        self.img = "../Trading Cards/Images/Pokemon/%s.png" % self.name.upper()

        # Creates an image for the pokemon
        self.image = Image(self.img, (margin, pos[1]), (30, 30))

        # Init the surf and rect to be used later
        self.surf = pygame.Surface((WIDTH, 50))
        self.rect = self.surf.get_rect(center=self.pos)

        # Gets the images for the types
        self.type1 = Image("../Trading Cards/Images/Types/%s.png" % self.type_1.upper(), (206 + margin, self.pos[1] - 12), (68 * 0.8, 24 * 0.8))
        if self.type_2 is not None:
            self.type2 = Image("../Trading Cards/Images/Types/%s.png" % self.type_2.upper(), (206 + margin, self.pos[1] + 12), (68 * 0.8, 24 * 0.8))

        # Text for the name and stats
        self.name_surf, self.name_rect = write_text(name, 103 + margin, self.pos[1], "calibri", 15, BLACK)
        self.hp_surf, self.hp_rect = write_text(str(self.hp), 410 + margin, self.pos[1], "calibri", 15, BLACK)
        self.atk_surf, self.atk_rect = write_text(str(self.atk), 410 + 30 + margin, self.pos[1], "calibri", 15, BLACK)
        self.def_surf, self.def_rect = write_text(str(self.defe), 410 + 60 + margin, self.pos[1], "calibri", 15, BLACK)
        self.spc_surf, self.spc_rect = write_text(str(self.spc), 410 + 90 + margin, self.pos[1], "calibri", 15, BLACK)
        self.spe_surf, self.spe_rect = write_text(str(self.spe), 410 + 120 + margin, self.pos[1], "calibri", 15, BLACK)

        # Button to see if it was actually pushed
        self.button = Button(self.rect.x, self.rect.y, self.rect.w, self.rect.h, True, self.display, show=False)

    def update(self, pos_skew):
        # Skew adjusts the position of the rect
        self.pos[1] += pos_skew
        self.rect = self.surf.get_rect(center=self.pos)

        # All of them change based on skew
        self.image.rect = self.image.surf.get_rect(center=(margin, self.pos[1]))
        self.name_rect = self.name_surf.get_rect(center=(103 + margin, self.pos[1]))
        self.type1.rect = self.type1.surf.get_rect(center=(206 + margin, self.pos[1] - 12))
        if self.type_2 is not None:
            self.type2.rect = self.type2.surf.get_rect(center=(206 + margin, self.pos[1] + 12))
        self.hp_rect = self.hp_surf.get_rect(center=(410 + margin, self.pos[1]))
        self.atk_rect = self.atk_surf.get_rect(center=(410 + 30 + margin, self.pos[1]))
        self.def_rect = self.def_surf.get_rect(center=(410 + 60 + margin, self.pos[1]))
        self.spc_rect = self.spc_surf.get_rect(center=(410 + 90 + margin, self.pos[1]))
        self.spe_rect = self.spe_surf.get_rect(center=(410 + 120 + margin, self.pos[1]))

        self.button.move(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

        # Upper limit to stop drawing things
        if self.pos[1] > 304:
            pygame.draw.rect(self.display, LIGHT_GRAY, self.rect, 1)

            self.display.blit(self.image.surf, self.image.rect)
            self.display.blit(self.name_surf, self.name_rect)
            self.display.blit(self.type1.surf, self.type1.rect)
            if self.type_2 is not None:
                self.display.blit(self.type2.surf, self.type2.rect)
            self.display.blit(self.hp_surf, self.hp_rect)
            self.display.blit(self.atk_surf, self.atk_rect)
            self.display.blit(self.def_surf, self.def_rect)
            self.display.blit(self.spc_surf, self.spc_rect)
            self.display.blit(self.spe_surf, self.spe_rect)

    # Check to see if pressed
    def press(self):
        # If within limits
        if self.pos[1] > 304:
            # If pressed
            if self.button.update():
                return True
