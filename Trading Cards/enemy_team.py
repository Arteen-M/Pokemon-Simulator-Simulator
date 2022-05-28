import random
from all_monsters import *
import damage_checks


def choose_team():
    # PICK FROM PRE-GENERATED TEAMS
    pokemon1 = Monster("Mewtwo", "Mewdos", "Psychic", None, 106, 110, 90, 154, 130)
    pokemon1.moveset = [
        Move("Psystrike", "Psychic", 80, 100),
        Move("Flamethrower", "Fire", 80, 100),
        Move("Bug Buzz", "Bug", 80, 100),
        Move("Thunderbolt", "Electric", 80, 100)
    ]

    pokemon2 = Monster("MissingNo", None, "Bird", "Normal", 33, 136, 1, 6, 29)
    pokemon2.moveset = [
        Move("?", "Normal", 90, 90),
        Move("??", "Ground", 100, 80),
        Move("???", "Bug", 110, 70),
        Move("????", "Normal", 179, 1),
    ]

    pokemon3 = Monster("Mew", None, "Psychic", None, 95, 100, 100, 100, 100)
    pokemon3.moveset = [
        Move("Psychic", "Psychic", 90, 90),
        Move("Flamethrower", "Fire", 90, 90),
        Move("Surf", "Water", 90, 90),
        Move("Ice Beam", "Ice", 90, 90)
    ]

    team_1 = [pokemon1, pokemon2, pokemon3]

    pokemon4 = Monster("Dragonite", None, "Dragon", "Flying", 91, 134, 95, 100, 80)
    pokemon4.moveset = [
        Move("Outrage", "Dragon", 80, 100),
        Move("Hyper Beam", "Normal", 110, 70),
        Move("Fire Blast", "Fire", 90, 90),
        Move("Blizzard", "Ice", 100, 80)
    ]

    team_2 = [pokemon4, pokemon4, pokemon4]

    pokemon5 = Monster("Rattata", None, "Normal", None, 120, 120, 120, 120, 120)
    pokemon5.moveset = [
        Move("Judgement", "Normal", 110, 70),
        Move("Magnitude (10)", "Ground", 80, 100),
        Move("Shadow Claw", "Ghost", 80, 100),
        Move("Thunderbolt", "Electric", 80, 100),
    ]

    team_3 = [pokemon5, pokemon5, pokemon5]

    pokemon6 = Monster("Charizard", None, "Fire", "Flying", 78, 84, 78, 85, 100)
    pokemon6.moveset = [
        Move("Fire Blast", "Fire", 110, 70),
        Move("Earthquake", "Ground", 80, 100),
        Move("Body Slam", "Normal", 80, 100),
        Move("Fly", "Flying", 80, 100),
    ]

    team_4 = [pokemon6, pokemon6, pokemon6]

    # PICK RANDOMLY AND GIVE ALL THE ASSOCIATED INFO (team, image and music)
    choice = random.randint(1, 4)
    if choice == 1:
        return team_1, "../Trading Cards/Images/Trainers/red.png", "../Trading Cards/Music/Reds Theme.mp3"
    elif choice == 2:
        return team_2, "../Trading Cards/Images/Trainers/Lance.png", "../Trading Cards/Music/Reds Theme.mp3"
    elif choice == 3:
        return team_3, "../Trading Cards/Images/Trainers/Joey.png", "../Trading Cards/Music/Joey Theme.mp3"
    elif choice == 4:
        return team_4, "../Trading Cards/Images/Trainers/GameFreak.png", "../Trading Cards/Music/GameFreak Theme.mp3"


def enemy_choice(team):
    # Choose a pokemon
    choice = random.randint(0, 2)
    return team[choice]


def enemy_move_choice(player, enemy):
    # Pick based on max damage
    max_damage = [0, 0]
    for count, entity in enumerate(player.moveset):
        damage = damage_checks.damage_output(player, enemy, entity)
        if damage > max_damage[0]:
            # Save the damage output and the position to help with comparison and selecting
            max_damage[0] = damage
            max_damage[1] = count

    # Returns the move itself
    return player.moveset[max_damage[1]]
