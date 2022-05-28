import pygame


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def write_text(msg, x, y, font, size, colour):
    text = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(msg, text, colour)
    textRect.center = (x, y)
    return textSurf, textRect


# For displaying images, inherited from the pygame sprite class
class Image(pygame.sprite.Sprite):
    def __init__(self, image, center, scale):
        pygame.sprite.Sprite.__init__(self)
        # Try to find the file, if it's not found, use the default (?) image
        try:
            self._surf = pygame.transform.scale(pygame.image.load(image), scale).convert_alpha()
        except FileNotFoundError:
            self._surf = pygame.transform.scale(pygame.image.load("../Trading Cards/Images/Question.png"),
                                                scale).convert_alpha()
        self._rect = self._surf.get_rect(center=center)

    @property
    def surf(self):
        return self._surf

    @surf.setter
    def surf(self, new_surf, new_scale):
        self._surf = pygame.transform.scale(pygame.image.load(new_surf), new_scale).convert_alpha()

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, new_rect):
        self._rect = new_rect


# Custom image class, for displaying pokemon info when hovered over
class PokeImage(Image):
    def __init__(self, image, center, scale, hp, atk, defs, spc, spe, moves, adjustment, display, show=True):
        Image.__init__(self, image, center, scale)
        # Gets all the stats to display
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.spc = spc
        self.spe = spe

        self.moves = moves

        self.display = display

        self.show = show

        # Initializes text for stats and moves
        self.stats_surf, self.stats_rect = write_text("%s/%s/%s/%s/%s" %
                                                      (self.hp, self.atk, self.defs, self.spc, self.spe),
                                                      self.rect.x + adjustment[0], self.rect.y + adjustment[1],
                                                      'calibri', 15, (0, 0, 0))

        self.moves_surfs = [write_text("%s/%s/%s/%s" % (self.moves[x].name, self.moves[x].type, self.moves[x].power,
                                                        self.moves[x].accuracy), self.rect.x + adjustment[0], self.rect.y + adjustment[1] + 20 +
                                       (20 * x), 'calibri', 15, (0, 0, 0)) for x in range(len(self.moves))
                            if self.moves[x] is not None]

    def update(self):
        self.display.blit(self.surf, self.rect)

        mouse = pygame.mouse.get_pos()
        # If the mouse is hovering over the image
        if self.rect.x + self.rect.w > mouse[0] > self.rect.x and self.rect.y + self.rect.h > mouse[1] > self.rect.y:
            # Display all the stats
            pygame.draw.rect(self.display, (255, 255, 255),
                             (self.rect.x + self.rect.w, self.rect.y + self.rect.h, 220, 120))
            pygame.draw.rect(self.display, (0, 0, 0),
                             (self.rect.x + self.rect.w, self.rect.y + self.rect.h, 220, 120), 1)

            self.display.blit(self.stats_surf, self.stats_rect)

            # If the pokemon belongs to the player, then show the moves
            if self.show:
                for entity in self.moves_surfs:
                    self.display.blit(entity[0], entity[1])


# Creates a team preview for both sides
class Preview:
    def __init__(self, pokemon1, pokemon2, pokemon3, pos, adjustment, display, show=True):
        # Gets all variables required
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pos = pos
        self.adjustment = adjustment
        self.display = display

        # Initializes each team (Consists of three)
        self.image_1 = PokeImage(self.pokemon1.img, (self.pos[0], self.pos[1]), (30, 30), self.pokemon1.hp,
                                 self.pokemon1.atk, self.pokemon1.defs, self.pokemon1.spc, self.pokemon1.spe,
                                 self.pokemon1.moveset, self.adjustment, self.display, show)

        self.image_2 = PokeImage(self.pokemon2.img, (self.pos[0] + 30, self.pos[1]), (30, 30), self.pokemon2.hp,
                                 self.pokemon2.atk, self.pokemon2.defs, self.pokemon2.spc, self.pokemon2.spe,
                                 self.pokemon2.moveset, self.adjustment, self.display, show)

        self.image_3 = PokeImage(self.pokemon3.img, (self.pos[0] + 60, self.pos[1]), (30, 30), self.pokemon3.hp,
                                 self.pokemon3.atk, self.pokemon3.defs, self.pokemon3.spc, self.pokemon3.spe,
                                 self.pokemon3.moveset, self.adjustment, self.display, show)

    # Updates all of them
    def update(self):
        self.image_1.update()
        self.image_2.update()
        self.image_3.update()

