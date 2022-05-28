import pygame
import sys

from pygame.locals import *

from GUI_Classes.images import Image
from GUI_Classes.button import Button, BackButton
from GUI_Classes.textbox import text_box
from GUI_Classes.text import write_text
import all_monsters
from pokebox import PokeBox

# Get all the pokemon for pokeboxes
all_pokemon = all_monsters.get_all_pokemon()

HEIGHT = 700
WIDTH = 1000

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
DARK_GRAY = (125, 125, 150)
LIGHT_GRAY = (125, 125, 125)
LIGHT_BLUE = (29, 161, 242)

# USED FOR THE TEXTBOXES
input_list = [K_EXCLAIM, K_QUOTEDBL, K_HASH, K_DOLLAR, K_AMPERSAND, K_QUOTE, K_LEFTPAREN,
              K_RIGHTPAREN, K_ASTERISK, K_PLUS, K_COMMA, K_MINUS, K_PERIOD, K_SLASH,
              K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_COLON, K_SEMICOLON, K_LESS, K_EQUALS, K_GREATER,
              K_QUESTION, K_AT, K_LEFTBRACKET, K_BACKSLASH, K_RIGHTBRACKET, K_CARET, K_UNDERSCORE, K_BACKQUOTE,
              K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u,
              K_v, K_w, K_x, K_y, K_z, K_KP0, K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9,
              K_KP_PERIOD, K_KP_DIVIDE, K_KP_MULTIPLY, K_KP_MINUS, K_KP_PLUS, K_KP_EQUALS]

number_list = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]

shift_check_list = [(K_0, K_RIGHTPAREN), (K_1, K_EXCLAIM), (K_2, K_AT), (K_3, K_HASH), (K_4, K_DOLLAR),
                    (K_5, K_PERCENT), (K_6, K_CARET), (K_7, K_AMPERSAND), (K_8, K_ASTERISK), (K_9, K_LEFTPAREN),
                    (K_MINUS, K_UNDERSCORE), (K_EQUALS, K_PLUS), (K_SEMICOLON, K_COLON), (K_QUOTE, K_QUOTEDBL),
                    (K_COMMA, K_LESS), (K_PERIOD, K_GREATER), (K_SLASH, K_QUESTION)]

pygame.init()
pygame.font.init()

# FPS CLOCK
FPS = 60
FramePerSec = pygame.time.Clock()
# WINDOW
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pocket Monster MeetUp")
pygame.display.set_icon(pygame.image.load("Images/Icon.png"))

# BACKGROUND
background_img = "../Trading Cards/Images/Pokemon_Select.png"
background_pos = (WIDTH / 2, HEIGHT / 2)
background_scale = (WIDTH, HEIGHT)
bg = Image(background_img, background_pos, background_scale)

# BACK BUTTON
back_img = "../Trading Cards/Images/back_button.png"
back_scale = (92, 31)
back_pos = (10 + back_scale[0] / 2, 10 + back_scale[1] / 2)
back = Image(back_img, back_pos, back_scale)

plus_button = "../Trading Cards/Images/plus_button.png"
plus_scale = (89, 45)

plus_pos_1 = (200, 23)
plus_pos_2 = (290, 23)
plus_pos_3 = (380, 23)

# Boxes for adding pokemon to the team
plus_1 = Image(plus_button, plus_pos_1, plus_scale)
plus_2 = Image(plus_button, plus_pos_2, plus_scale)
plus_3 = Image(plus_button, plus_pos_3, plus_scale)

# CATEGORY BARS
hp = write_text('Hp', 445, 225, "calibri", 15, BLACK)
atk = write_text('Atk', 475, 225, "calibri", 15, BLACK)
defe = write_text('Def', 505, 225, "calibri", 15, BLACK)
spc = write_text('Spc', 535, 225, "calibri", 15, BLACK)
spe = write_text('Spe', 565, 225, "calibri", 15, BLACK)

name = write_text('Name', 134, 225, "calibri", 15, BLACK)
types = write_text('Types', 240, 225, "calibri", 15, BLACK)

note = write_text('* Combination of PWR and ACC cannot be greater than 180', 240, 90, "calibri", 10, BLACK)
submit = write_text('Hit Enter to submit moveset', 540, 90, "calibri", 10, BLACK)

# ALL POKEMON IN THIS LIST
pokeboxes = [PokeBox(x.name, x.types[0], x.types[1], x.health, x.attack, x.defense, x.special, x.speed, display,
                     [WIDTH / 2, 305 + (50 * y)]) for y, x in enumerate(all_pokemon)]

three_pokemon_choices = []


def pokemon_screen():
    # BACK BUTTON
    back_btn = BackButton('home', display)

    # PLUS BUTTONS
    pokemon_1 = Button(155, 1, 89, 44, True, display)
    pokemon_2 = Button(245, 1, 89, 44, True, display)
    pokemon_3 = Button(335, 1, 89, 44, True, display)

    num_shift_check = 0

    # NAME SEARCH TEXTBOXES
    poke_pressed = False
    poke_message = ""

    # MOVESET TEXTBOXES
    move_1_pressed = False
    move_1_message = ""
    type_1_pressed = False
    type_1_message = ""
    pwr_1_pressed = False
    pwr_1_message = ""
    acc_1_pressed = False
    acc_1_message = ""

    move_2_pressed = False
    move_2_message = ""
    type_2_pressed = False
    type_2_message = ""
    pwr_2_pressed = False
    pwr_2_message = ""
    acc_2_pressed = False
    acc_2_message = ""

    move_3_pressed = False
    move_3_message = ""
    type_3_pressed = False
    type_3_message = ""
    pwr_3_pressed = False
    pwr_3_message = ""
    acc_3_pressed = False
    acc_3_message = ""

    move_4_pressed = False
    move_4_message = ""
    type_4_pressed = False
    type_4_message = ""
    pwr_4_pressed = False
    pwr_4_message = ""
    acc_4_pressed = False
    acc_4_message = ""

    # MOUSE SKEW
    skew = 0
    # TEAM
    three_pokemon_choices = [None, None, None]
    # TEAM SLOT (SELECTING)
    selected = 0

    while True:
        shift_check = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # MOUSEWHEEL FOR SCROLLING PAST BUTTONS
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    skew = 30
                elif event.button == 5:
                    skew = -30

            # FOR TEXTBOXES
            if event.type == pygame.KEYDOWN:
                for x in range(len(input_list)):
                    # IF PRESSING A VALID KEY
                    if event.key == input_list[x]:
                        # IF TEXTBOX IS SELECTED
                        if poke_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                # CHECK FOR VALID SHIFT INPUTS
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        poke_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                # IF NO SPECIAL CHARACTERS, DISPLAY CAPITAL LETTER
                                if num_shift_check == len(shift_check_list):
                                    poke_message += str(pygame.key.name(input_list[x])).upper()
                            # PRINT NORMAL LETTER
                            else:
                                poke_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE NAME (1)
                        if move_1_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        move_1_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    move_1_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                move_1_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE TYPE (1)
                        if type_1_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        type_1_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    type_1_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                type_1_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE NAME (2)
                        if move_2_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        move_2_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    move_2_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                move_2_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE TYPE (2)
                        if type_2_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        type_2_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    type_2_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                type_2_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE NAME (3)
                        if move_3_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        move_3_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    move_3_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                move_3_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE TYPE (3)
                        if type_3_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        type_3_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    type_3_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                type_3_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE NAME (4)
                        if move_4_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        move_4_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    move_4_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                move_4_message += str(pygame.key.name(input_list[x])).lower()

                        # SAME AS PREVIOUS, BUT FOR MOVE NAME (4)
                        if type_4_pressed:
                            if shift_check[K_LSHIFT] or shift_check[K_RSHIFT]:
                                for i in range(len(shift_check_list)):
                                    if input_list[x] == shift_check_list[i][0]:
                                        type_4_message += str(pygame.key.name(shift_check_list[i][1]))
                                    else:
                                        num_shift_check += 1
                                if num_shift_check == len(shift_check_list):
                                    type_4_message += str(pygame.key.name(input_list[x])).upper()
                            else:
                                type_4_message += str(pygame.key.name(input_list[x])).lower()

                # VERY SIMILAR TO ABOVE, BUT FOR ONLY NUMBERS (NO SHIFTS OR LETTERS)
                for x in range(len(number_list)):
                    if event.key == number_list[x]:
                        # FOR POWER AND ACC (1)
                        if pwr_1_pressed:
                            pwr_1_message += str(pygame.key.name(number_list[x])).lower()
                        if acc_1_pressed:
                            acc_1_message += str(pygame.key.name(number_list[x])).lower()

                        # FOR POWER AND ACC (2)
                        if pwr_2_pressed:
                            pwr_2_message += str(pygame.key.name(number_list[x])).lower()
                        if acc_2_pressed:
                            acc_2_message += str(pygame.key.name(number_list[x])).lower()

                        # FOR POWER AND ACC (3)
                        if pwr_3_pressed:
                            pwr_3_message += str(pygame.key.name(number_list[x])).lower()
                        if acc_3_pressed:
                            acc_3_message += str(pygame.key.name(number_list[x])).lower()

                        # FOR POWER AND ACC (4)
                        if pwr_4_pressed:
                            pwr_4_message += str(pygame.key.name(number_list[x])).lower()
                        if acc_4_pressed:
                            acc_4_message += str(pygame.key.name(number_list[x])).lower()

                # FOR SPACEBAR (SPECIAL CHARACTER)
                if event.key == K_SPACE:
                    if poke_pressed:
                        poke_message += " "
                    if move_1_pressed:
                        move_1_message += " "
                    if type_1_pressed:
                        type_1_message += " "

                    if move_2_pressed:
                        move_2_message += " "
                    if type_2_pressed:
                        type_2_message += " "

                    if move_3_pressed:
                        move_3_message += " "
                    if type_3_pressed:
                        type_3_message += " "

                    if move_4_pressed:
                        move_4_message += " "
                    if type_4_pressed:
                        type_4_message += " "

                # FOR BACKSPACE (DELETE ONLY ONCE PER PRESS)
                if event.key == K_BACKSPACE:
                    if poke_pressed:
                        if len(poke_message) > 0:
                            poke_message = poke_message[:-1]
                    if move_1_pressed:
                        if len(move_1_message) > 0:
                            move_1_message = move_1_message[:-1]
                    if type_1_pressed:
                        if len(type_1_message) > 0:
                            type_1_message = type_1_message[:-1]
                    if pwr_1_pressed:
                        if len(pwr_1_message) > 0:
                            pwr_1_message = pwr_1_message[:-1]
                    if acc_1_pressed:
                        if len(acc_1_message) > 0:
                            acc_1_message = acc_1_message[:-1]

                    if move_2_pressed:
                        if len(move_2_message) > 0:
                            move_2_message = move_2_message[:-1]
                    if type_2_pressed:
                        if len(type_2_message) > 0:
                            type_2_message = type_2_message[:-1]
                    if pwr_2_pressed:
                        if len(pwr_2_message) > 0:
                            pwr_2_message = pwr_2_message[:-1]
                    if acc_2_pressed:
                        if len(acc_2_message) > 0:
                            acc_2_message = acc_2_message[:-1]

                    if move_3_pressed:
                        if len(move_3_message) > 0:
                            move_3_message = move_3_message[:-1]
                    if type_3_pressed:
                        if len(type_3_message) > 0:
                            type_3_message = type_3_message[:-1]
                    if pwr_3_pressed:
                        if len(pwr_3_message) > 0:
                            pwr_3_message = pwr_3_message[:-1]
                    if acc_3_pressed:
                        if len(acc_3_message) > 0:
                            acc_3_message = acc_3_message[:-1]

                    if move_4_pressed:
                        if len(move_4_message) > 0:
                            move_4_message = move_4_message[:-1]
                    if type_4_pressed:
                        if len(type_4_message) > 0:
                            type_4_message = type_4_message[:-1]
                    if pwr_4_pressed:
                        if len(pwr_4_message) > 0:
                            pwr_4_message = pwr_4_message[:-1]
                    if acc_4_pressed:
                        if len(acc_4_message) > 0:
                            acc_4_message = acc_4_message[:-1]

                # IF ENTER IS PRESSED
                if event.key == K_RETURN:
                    # IF THERE IS A VALID POKEMON PRESENT
                    if three_pokemon_choices[selected] is not None:
                        set = []
                        # ERROR AVOIDING
                        if pwr_1_message != "" and acc_1_message != "":
                            # CONDITION (AS DETAILED ON THE PAGE)
                            if int(pwr_1_message) + int(acc_1_message) <= 180:
                                # CREATE A MOVE AND ADD IT TO THE LIST
                                set.append(all_monsters.Move(move_1_message, type_1_message, int(pwr_1_message), int(acc_1_message)))
                        # SAME AS ABOVE
                        if pwr_2_message != "" and acc_2_message != "":
                            if int(pwr_2_message) + int(acc_2_message) <= 180:
                                set.append(all_monsters.Move(move_2_message, type_2_message, int(pwr_2_message), int(acc_2_message)))
                        if pwr_3_message != "" and acc_3_message != "":
                            if int(pwr_3_message) + int(acc_3_message) <= 180:
                                set.append(all_monsters.Move(move_3_message, type_3_message, int(pwr_3_message), int(acc_3_message)))
                        if pwr_4_message != "" and acc_4_message != "":
                            if int(pwr_4_message) + int(acc_4_message) <= 180:
                                set.append(all_monsters.Move(move_4_message, type_4_message, int(pwr_4_message), int(acc_4_message)))

                        # SET THE CURRENT MOVESET AS THE SET CREATED ABOVE
                        three_pokemon_choices[selected].moveset = set

        # DISPLAY EVERYTHING THAT IS CONSTANT
        display.blit(bg.surf, bg.rect)
        display.blit(back.surf, back.rect)

        display.blit(plus_1.surf, plus_1.rect)
        display.blit(plus_2.surf, plus_2.rect)
        display.blit(plus_3.surf, plus_3.rect)

        display.blit(hp[0], hp[1])
        display.blit(atk[0], atk[1])
        display.blit(defe[0], defe[1])
        display.blit(spc[0], spc[1])
        display.blit(spe[0], spe[1])

        display.blit(name[0], name[1])
        display.blit(types[0], types[1])
        display.blit(note[0], note[1])
        display.blit(submit[0], submit[1])

        # ALL THE POKEBOXES (POKEMON THAT ARE DISPLAYED AND SELECTABLE)
        for count, entity in enumerate(pokeboxes):
            entity.update(skew)
            # IF PRESSED OR YOU SEARCHED FOR IT (AND ITS NOT MEW BECAUSE HES UNDER THE TRUCK)
            if entity.press() or (poke_message.lower() == entity.name.lower() and poke_message.lower() != 'mew'):
                poke_message = ""
                three_pokemon_choices[selected] = all_pokemon[count]

        # RESET SKEW SO ITS NOT SCROLLING DOWN FOREVER
        skew = 0

        # BACK TO HOME
        if back_btn.update() is not None:
            return back_btn.value, three_pokemon_choices

        # CHANGE WHICH POKEMON YOU'RE EDITING
        if pokemon_1.update():
            selected = 0
        elif pokemon_2.update():
            selected = 1
        elif pokemon_3.update():
            selected = 2

        # DISPLAY THE SELECTED POKEMON
        if three_pokemon_choices[selected] is not None:
            display.blit(three_pokemon_choices[selected].image.surf, (120, 100, 30, 30))
        # OTHERWISE, DISPLAY A QUESTION MARK
        else:
            display.blit(pygame.image.load("../Trading Cards/Images/Question.png"), (120, 100, 30, 30))
        # DISPLAY THE POKEMON ON TOP OF THE PLUS BUTTON
        for count, entity in enumerate(three_pokemon_choices):
            if entity is not None:
                display.blit(pokeboxes[all_pokemon.index(entity)].image.surf, (184 + (count * 90), 8, 30, 30))

        num_shift_check = 0

        # DISPLAY ALL THE TEXTBOXES
        poke_pressed = text_box("Pokémon", 10, 185, 100, 25, LIGHT_GRAY, LIGHT_BLUE, poke_pressed, 15,
                                poke_message, display)

        move_1_pressed = text_box("Move 1", 250, 100, 110, 25, LIGHT_GRAY, LIGHT_BLUE, move_1_pressed, 15,
                                  move_1_message, display)

        type_1_pressed = text_box("Type", 365, 100, 75, 25, LIGHT_GRAY, LIGHT_BLUE, type_1_pressed, 15,
                                  type_1_message, display)

        pwr_1_pressed = text_box("PWR", 445, 100, 75, 25, LIGHT_GRAY, LIGHT_BLUE, pwr_1_pressed, 15,
                                  pwr_1_message, display)

        acc_1_pressed = text_box("ACC", 525, 100, 75, 25, LIGHT_GRAY, LIGHT_BLUE, acc_1_pressed, 15,
                                  acc_1_message, display)

        move_2_pressed = text_box("Move 2", 250, 126, 110, 25, LIGHT_GRAY, LIGHT_BLUE, move_2_pressed, 15,
                                  move_2_message, display)

        type_2_pressed = text_box("Type", 365, 126, 75, 25, LIGHT_GRAY, LIGHT_BLUE, type_2_pressed, 15,
                                  type_2_message, display)

        pwr_2_pressed = text_box("PWR", 445, 126, 75, 25, LIGHT_GRAY, LIGHT_BLUE, pwr_2_pressed, 15,
                                 pwr_2_message, display)

        acc_2_pressed = text_box("ACC", 525, 126, 75, 25, LIGHT_GRAY, LIGHT_BLUE, acc_2_pressed, 15,
                                 acc_2_message, display)

        move_3_pressed = text_box("Move 3", 250, 152, 110, 25, LIGHT_GRAY, LIGHT_BLUE, move_3_pressed, 15,
                                  move_3_message, display)

        type_3_pressed = text_box("Type", 365, 152, 75, 25, LIGHT_GRAY, LIGHT_BLUE, type_3_pressed, 15,
                                  type_3_message, display)

        pwr_3_pressed = text_box("PWR", 445, 152, 75, 25, LIGHT_GRAY, LIGHT_BLUE, pwr_3_pressed, 15,
                                 pwr_3_message, display)

        acc_3_pressed = text_box("ACC", 525, 152, 75, 25, LIGHT_GRAY, LIGHT_BLUE, acc_3_pressed, 15,
                                 acc_3_message, display)

        move_4_pressed = text_box("Move 4", 250, 178, 110, 25, LIGHT_GRAY, LIGHT_BLUE, move_4_pressed, 15,
                                  move_4_message, display)

        type_4_pressed = text_box("Type", 365, 178, 75, 25, LIGHT_GRAY, LIGHT_BLUE, type_4_pressed, 15,
                                  type_4_message, display)

        pwr_4_pressed = text_box("PWR", 445, 178, 75, 25, LIGHT_GRAY, LIGHT_BLUE, pwr_4_pressed, 15,
                                 pwr_4_message, display)

        acc_4_pressed = text_box("ACC", 525, 178, 75, 25, LIGHT_GRAY, LIGHT_BLUE, acc_4_pressed, 15,
                                 acc_4_message, display)

        pygame.display.update()
        FramePerSec.tick(FPS)
