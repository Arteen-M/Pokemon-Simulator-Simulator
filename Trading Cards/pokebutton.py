from GUI_Classes.button import Button
from GUI_Classes.images import PokeImage
from GUI_Classes.healthbar import HealthBar
from GUI_Classes.text import write_text


# Button when selecting pokemon
class PokeButton:
    def __init__(self, name, health, img, display, pos, atk, defs, spc, spe, moves):
        # Variables
        self.name = name
        self.max = health
        self.img = img
        self.display = display
        self.pos = pos

        self.atk = atk
        self.defs = defs
        self.spc = spc
        self.spe = spe
        self.moves = moves

        # Button for selecting
        self.button = Button(pos[0], pos[1], 200, 75, True, self.display)
        self.name_surf, self.name_rect = write_text(self.name, self.pos[0] + 100, self.pos[1] + 12, "calibri", 15,
                                                    (0, 0, 0))

        # Image (with hover)
        self.image = PokeImage(self.img, (self.pos[0] + 25, self.pos[1] + 25), (50, 50), self.max, self.atk, self.defs,
                               self.spc, self.spe, self.moves, (145, 65), self.display)

        # Uses the healthbar
        self.healthbar = HealthBar(self.max, self.max, self.pos[0] + 75, self.pos[1] + 25, 100, 15, self.display)
        self.health_surf, self.health_rect = write_text("%s / %s" % (self.max, self.max), self.pos[0] + 100,
                                                        self.pos[1] + 50, 'calibri', 15, (0, 0, 0))

    # Displays everything and gets when the button is pressed
    def update(self):
        self.display.blit(self.name_surf, self.name_rect)
        self.display.blit(self.health_surf, self.health_rect)

        self.image.update()
        self.healthbar.update()

        if self.button.update():
            return True
