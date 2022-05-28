import random
import math
import type_chart
import pygame
from GUI_Classes.text import write_text


def damage_calc(power, atk, defs, poke_type1, poke_type2, move_type, enemy_types):
    # Damage formula (without outside factors)
    damage = (((42 * power * atk / defs) / 50) + 2) * (
            random.randint(85, 100) / 100)

    # STAB BOOST
    if poke_type1.upper() == move_type.upper() or poke_type2.upper() == move_type.upper():
        damage *= 1.5
    # TYPE MULTIPLIER
    damage *= type_chart.type_effectiveness(move_type, enemy_types[0], enemy_types[1])

    return damage


def damage_output(player_poke, enemy_poke, player_move):
    physical_list = ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "GHOST", "???"]
    # special_list = ["FIRE", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "DRAGON", "ICE"]

    # AVOID ERRORS (any blank types will be interpreted as NaN, which is a float)
    if isinstance(player_poke.types[1], float) or player_poke.types[1] is None:
        type_2 = ""
    else:
        type_2 = player_poke.types[1]

    # Physical/Special Split (Chosen by move type)
    if player_move.type.upper() in physical_list:
        damage = damage_calc(player_move.power, player_poke.atk, enemy_poke.defs, player_poke.types[0],
                             type_2, player_move.type, enemy_poke.types)
    else:
        damage = damage_calc(player_move.power, player_poke.spc, enemy_poke.spc, player_poke.types[0],
                             type_2, player_move.type, enemy_poke.types)

    return damage


def accuracy_check(accuracy):
    # Accuracy check (includes the 1/256 glitch for faithfulness to the original game)
    if math.floor(255 * (accuracy / 100)) > random.randint(0, 255):
        return True
    else:
        return False


# How a turn would go
def turn(pokemon, move, enemy, display, enemy_healthbar):
    # Check accuracy
    hit = accuracy_check(move.accuracy)
    if hit:
        # Display text based on effectiveness
        if type_chart.type_effectiveness(move.type, enemy.types[0],
                                         enemy.types[1]) > 1:
            message = "%s used %s! It was super effective!" % (pokemon.name, move.name)
        elif type_chart.type_effectiveness(move.type, enemy.types[0],
                                           enemy.types[1]) < 1:
            message = "%s used %s! It was not very effective!" % (pokemon.name, move.name)
        else:
            message = "%s used %s!" % (pokemon.name, move.name)
    else:
        # Miss message
        message = "%s used %s! The attack missed!" % (pokemon.name, move.name)

    message_surf, message_rect = write_text(message, 450, 500, "calibri", 15, (0, 0, 0))
    # Display the message
    display.blit(message_surf, message_rect)
    # Update the window
    pygame.display.update()

    # Delay so the player actually has time to read the text
    pygame.time.delay(1000)

    if hit:
        # Change HP
        enemy.current_hp -= damage_output(pokemon, enemy, move)

    # UPDATE THE HEALTH
    enemy_healthbar.update(enemy.current_hp)
    # UPDATE AGAIN
    pygame.display.update()

    # WAIT AGAIN
    pygame.time.delay(1000)
