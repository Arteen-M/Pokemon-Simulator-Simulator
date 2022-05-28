# IMPORTS
import pygame
import sys
import random
from GUI_Classes.images import Image
from GUI_Classes.images import Preview
from GUI_Classes.button import MoveButton
from GUI_Classes.button import Button
from GUI_Classes.text import write_text
from GUI_Classes.healthbar import DisplayHealth
from pokebutton import PokeButton
import enemy_team
import damage_checks
import all_monsters

HEIGHT = 700
WIDTH = 1000

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
DARK_GRAY = (125, 125, 150)

pygame.init()
pygame.font.init()

FPS = 60
FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pocket Monster MeetUp")
pygame.display.set_icon(pygame.image.load("../Trading Cards/Images/Icon.png"))

background_img = "../Trading Cards/Images/Arena.png"
background_pos = (WIDTH / 2, HEIGHT / 2)
background_scale = (WIDTH, HEIGHT)
bg = Image(background_img, background_pos, background_scale)


def battle_screen(three_pokemon):
    selecting = True
    choice = None

    # INIT Buttons to select your team
    pokemon_1 = PokeButton(three_pokemon[0].name, three_pokemon[0].hp, three_pokemon[0].img,
                           display, (50, 500), three_pokemon[0].atk, three_pokemon[0].defs,
                           three_pokemon[0].spc, three_pokemon[0].spe, three_pokemon[0].moveset)

    pokemon_2 = PokeButton(three_pokemon[1].name, three_pokemon[1].hp, three_pokemon[1].img,
                           display, (400, 500), three_pokemon[1].atk, three_pokemon[1].defs,
                           three_pokemon[1].spc, three_pokemon[1].spe, three_pokemon[1].moveset)

    pokemon_3 = PokeButton(three_pokemon[2].name, three_pokemon[2].hp, three_pokemon[2].img,
                           display, (750, 500), three_pokemon[2].atk, three_pokemon[2].defs,
                           three_pokemon[2].spc, three_pokemon[2].spe, three_pokemon[2].moveset)

    # Back button (For later)
    back = Button(WIDTH/2 - 50, 575, 100, 50, True, display, False)
    back_surf, back_rect = write_text("Back", WIDTH/2, 600, "calibri", 15, (0, 0, 0))

    # The Opponent is initialized (Team, preview and pokemon)
    enemy, sprite, music = enemy_team.choose_team()
    enemy_preview = Preview(enemy[0], enemy[1], enemy[2], (45, 200), (120, 40), display, False)
    enemy_image = Image(sprite, (65, 300), (100, 100))
    enemy_pokemon = enemy_team.enemy_choice(enemy)
    enemy_healthbar = DisplayHealth(enemy_pokemon.hp, enemy_pokemon.hp, 600, 25, 100, 25, display,
                                    enemy_pokemon.name)

    # Start the music
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    # Move buttons and choice
    move_buttons = [None, None, None, None]
    move_choice = None

    # Turn checking variables
    player_turn = False
    start_turn = False

    # See if you win or lose
    win = False
    lose = False

    # Switch from battling to win/loss
    loaded = False

    # Initialize the win message so I don't have to do it later
    win_message = "The opposing %s fainted! You WIN!" % enemy_pokemon.name
    win_message_surf, win_message_rect = write_text(win_message, 450, 500, "calibri", 15, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.blit(bg.surf, bg.rect)

        # Know when to switch
        if not (win or lose):
            # Win Lose checking
            if enemy_pokemon.current_hp <= 0:
                win = True
                continue
            elif choice is not None:
                if choice.current_hp <= 0:
                    lose = True
                    continue

            # Three Phases : Selecting, Battling, End Screen
            # (1) Selecting: Choosing a pokemon to battle with
            if selecting:
                # If a button is pressed (Returns True)
                if pokemon_1.update():
                    # YOUR POKEMON (choice)
                    choice = three_pokemon[0]

                    # Init Player Healthbar
                    player_healthbar = DisplayHealth(choice.hp, choice.hp, 200, 125, 100, 25, display, choice.name)

                    # Create the move buttons (for selecting moves)
                    for count, entity in enumerate(choice.moveset):
                        # If there is a moveset
                        if entity is not None:
                            move_buttons[count] = MoveButton(entity.name, entity.type, entity.power, entity.accuracy,
                                                             25 + (250 * count), 500, display)

                    # If there is no moveset, then add struggle to the moveset
                    if move_buttons == [None, None, None, None]:
                        move_buttons = [MoveButton("Struggle", "Normal", 50, 101, 25, 500, display)]
                        choice.moveset = [all_monsters.Move("Struggle", "Normal", 50, 101)]

                    # Move to the next phase
                    selecting = False
                # SAME AS THE OTHER ONE, JUST DIFFERENT BUTTON
                elif pokemon_2.update():
                    choice = three_pokemon[1]

                    player_healthbar = DisplayHealth(choice.hp, choice.hp, 200, 125, 100, 25, display, choice.name)

                    for count, entity in enumerate(choice.moveset):
                        if entity is not None:
                            move_buttons[count] = MoveButton(entity.name, entity.type, entity.power, entity.accuracy,
                                                             25 + (250 * count), 500, display)

                    if move_buttons == [None, None, None, None]:
                        move_buttons = [MoveButton("Struggle", "Normal", 50, 101, 25, 500, display)]
                        choice.moveset = [all_monsters.Move("Struggle", "Normal", 50, 101)]

                    selecting = False
                # SAME AS THE OTHER ONE< JUST DIFFERENT BUTTON
                elif pokemon_3.update():
                    choice = three_pokemon[2]

                    player_healthbar = DisplayHealth(choice.hp, choice.hp, 200, 125, 100, 25, display, choice.name)

                    for count, entity in enumerate(choice.moveset):
                        if entity is not None:
                            move_buttons[count] = MoveButton(entity.name, entity.type, entity.power, entity.accuracy,
                                                             25 + (250 * count), 500, display)

                    if move_buttons == [None, None, None, None]:
                        move_buttons = [MoveButton("Struggle", "Normal", 50, 101, 25, 500, display)]
                        choice.moveset = [all_monsters.Move("Struggle", "Normal", 50, 101)]

                    selecting = False
            # (2) Battling: Picking a move and having the turn play out
            else:
                # Display the pokemon
                display.blit(choice.image.surf, (200, 200, 100, 100))
                display.blit(enemy_pokemon.image.surf, (600, 100, 100, 100))

                # Update the healthbars
                player_healthbar.update(choice.current_hp)
                enemy_healthbar.update(enemy_pokemon.current_hp)

                # Wait for a move to be selected (start_turn will be True)
                if not start_turn:
                    for count, entity in enumerate(move_buttons):
                        if entity is not None:
                            # If button is selected
                            if entity.update():
                                # Save your move and the enemy move
                                move_choice = choice.moveset[count]
                                enemy_move = enemy_team.enemy_move_choice(enemy_pokemon, choice)
                                start_turn = True
                else:
                    # See who goes first (Based on speed) (If there is a speed tie, choose randomly)
                    if choice.spe > enemy_pokemon.spe or (enemy_pokemon.spe == choice.spe and random.randint(0, 1) == 0):
                        # Make sure the turn order proceeds as planned (and only once)
                        if not player_turn:
                            player_turn = True
                        else:
                            player_turn = False

                        # Run the damage calcs and change the HP
                        if player_turn:
                            # Player first
                            damage_checks.turn(choice, move_choice, enemy_pokemon, display, enemy_healthbar)
                        else:
                            # Then opponent
                            damage_checks.turn(enemy_pokemon, enemy_move, choice, display, player_healthbar)
                            # Move on to next turn
                            start_turn = False
                    # SAME BUT IN OPPOSITE ORDER
                    else:
                        if not player_turn:
                            player_turn = True
                        else:
                            player_turn = False

                        if player_turn:
                            damage_checks.turn(enemy_pokemon, enemy_move, choice, display, player_healthbar)
                        else:
                            damage_checks.turn(choice, move_choice, enemy_pokemon, display, enemy_healthbar)
                            start_turn = False

            # Show the enemy image and preview (above healthbar)
            display.blit(enemy_image.surf, enemy_image.rect)

            enemy_preview.update()

        else:
            # Stop the music (only once)
            if not loaded:
                pygame.mixer.music.stop()

            # Restore health to avoid glitch
            choice.restore_health()
            # Show the back button text
            display.blit(back_surf, back_rect)
            # If back is pressed
            if back.update():
                return "home"

            if win:
                # Start the music (Play only once)
                if not loaded:
                    pygame.mixer.music.load("../Trading Cards/Music/Win.mp3")
                    pygame.mixer.music.play()
                    loaded = True
                # Show message
                display.blit(win_message_surf, win_message_rect)
            # SAME AS WIN BUT DIFFERENT MESSAGE
            elif lose:
                if not loaded:
                    pygame.mixer.music.load("../Trading Cards/Music/Lose.mp3")
                    pygame.mixer.music.play()
                    # Has to init the message here instead of earlier beacuse I don't know the choice earlier
                    loss_message = "%s fainted. You lose!" % choice.name
                    loss_message_surf, loss_message_rect = write_text(loss_message, 450, 500, "calibri", 15, (0, 0, 0))

                    loaded = True
                display.blit(loss_message_surf, loss_message_rect)

        pygame.display.update()
        FramePerSec.tick(FPS)
