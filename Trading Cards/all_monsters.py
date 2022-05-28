import pandas as pd
import pygame
from GUI_Classes.images import Image
import math

pygame.init()
pygame.font.init()

FPS = 60
FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Pocket Monster MeetUp")
pygame.display.set_icon(pygame.image.load("../Trading Cards/Images/Icon.png"))

types = ["BUG", "DRAGON", "ELECTRIC", "FIGHTING", "FIRE", "FLYING", "GHOST", "GRASS", "GROUND", "ICE", "NORMAL",
         "POISON", "PSYCHIC", "QUESTION", "ROCK", "WATER"]


# Class for each pokemon
class Monster:
    def __init__(self, name, nickname, type_1, type_2, hp, attack, defense, special, speed):
        # Name of pokemon (Official)
        self.name = name
        # Nickname of pokemon (Unofficial) (Unused)
        self._nickname = nickname
        # Types list
        self.types = [type_1, type_2]

        # Base stats
        self.health = hp
        self.attack = attack
        self.defense = defense
        self.special = special
        self.speed = speed

        # Actual stats
        self.hp = stat_calc(self.health, True)
        self._current_hp = self.hp
        self.atk = stat_calc(self.attack)
        self.defs = stat_calc(self.defense)
        self.spc = stat_calc(self.special)
        self.spe = stat_calc(self.speed)

        # Moveset (Not always four moves)
        self._moveset = [None, None, None, None]

        # Pokemon Images
        self.img = "../Trading Cards/Images/Pokemon/%s.png" % self.name
        self.image = Image(self.img, (0, 0), (100, 100))

    # Used to get and set the moveset of a pokemon
    @property
    def moveset(self):
        return self._moveset

    @moveset.setter
    def moveset(self, sets):
        self._moveset = sets

    # Used to get and set the HP of a pokemon during a battle
    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, health):
        self._current_hp = health

    # Sets the HP back to full health after the game to avoid a glitch
    def restore_health(self):
        self._current_hp = self.hp


# Class for each individual move
class Move:
    def __init__(self, name, type, power, accuracy):
        # Variables like names power, accuracy and type
        self.name = name
        if type.upper() in types:
            self.type = type
        else:
            self.type = "???"
        self.power = power
        self.accuracy = accuracy


# Extract a list of all pokemon, formatted into the proper class
def get_all_pokemon():
    pokemon_list = pd.read_csv('Pokemon.csv')
    # Drops useless columns like BST, Sp. Def, Gen and Legendary status
    pokemon_list = pokemon_list.drop(columns=['Total', 'Sp. Def', 'Generation', 'Legendary'])

    pokemon = []

    for x in range(len(pokemon_list)):
        # Adds the pokemon to a list to be used later
        pokemon.append(Monster(pokemon_list['Name'][x], None, pokemon_list['Type 1'][x], pokemon_list['Type 2'][x],
                               pokemon_list['HP'][x], pokemon_list['Attack'][x], pokemon_list['Defense'][x],
                               pokemon_list['Sp. Atk'][x], pokemon_list['Speed'][x]))

    return pokemon


# Used to calculate stats
def stat_calc(base, ishp=False):
    # Stat formula
    stat = math.floor((base + 15) * 2) + 100 + 5
    # HP gets an extra 5
    if ishp:
        stat += 5

    return stat
