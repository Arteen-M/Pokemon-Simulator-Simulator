# -------------------------------------------------------------------------
# Program: Pokemon Simulator Simulator
# Author: Arteen Mirzaei
# Date: 2022-05-10
#
# Description: This is a simulator (or rough recreation) of the pokemon simulator "Pokemon Showdown".
# You go to build a team in the teambuilder, and once you have a team, you can fighting a preset
# team (Either Red, Lance, GameFreak or Youngster Joey) and their respective pokemons.
#
# Input: Mouse buttons, scroll wheel and keyboard inputs
# Output: No distinct output
# -------------------------------------------------------------------------

from start import start_screen
from pokemons import pokemon_screen
from battle import battle_screen

nex = 'home'  # Variable that tells you which page to go to
team = [None, None, None]  # The chosen team

while True:
    # Home Screen
    if nex == 'home':
        nex = start_screen(team)
    # Teambuilder
    if nex == 'new team':
        nex, team = pokemon_screen()
    # Battle
    if nex == 'battle':
        if team[0] is not None and team[1] is not None and team[2] is not None:
            nex = battle_screen(team)
        else:
            nex = 'home'
