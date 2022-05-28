import pygame
import sys

from GUI_Classes.images import Image
from GUI_Classes.button import Button

HEIGHT = 700
WIDTH = 1000

pygame.init()
pygame.font.init()


FPS = 60
FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pocket Monster MeetUp")
pygame.display.set_icon(pygame.image.load("Images/Icon.png"))

background_img = "../Trading Cards/Images/Background.png"
background_pos = (WIDTH/2, HEIGHT/2)
background_scale = (WIDTH, HEIGHT)
bg = Image(background_img, background_pos, background_scale)


def start_screen(team):
    # DISPLAYING THE POKEMON ON THE START SCREEN
    if team[0] is not None:
        team_1_img = "../Trading Cards/Images/Pokemon/%s.png" % team[0].name
    else:
        team_1_img = "../Trading Cards/Images/Question.png"

    team_1_pos = (100, 165)
    team_1_scale = (30, 30)

    team_1 = Image(team_1_img, team_1_pos, team_1_scale)

    if team[1] is not None:
        team_2_img = "../Trading Cards/Images/Pokemon/%s.png" % team[1].name
    else:
        team_2_img = "../Trading Cards/Images/Question.png"

    team_2_pos = (160, 165)
    team_2_scale = (30, 30)

    team_2 = Image(team_2_img, team_2_pos, team_2_scale)

    if team[2] is not None:
        team_3_img = "../Trading Cards/Images/Pokemon/%s.png" % team[2].name
    else:
        team_3_img = "../Trading Cards/Images/Question.png"

    team_3_pos = (220, 165)
    team_3_scale = (30, 30)

    team_3 = Image(team_3_img, team_3_pos, team_3_scale)

    # BUTTONS FOR SELECTING WHERE TO GO
    teambuilder = Button(55, 392, 225, 40, 'new team', display)
    battle = Button(42, 248, 250, 70, 'battle', display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # DISPLAY THE POKEMON AND BG
        display.blit(bg.surf, bg.rect)

        display.blit(team_1.surf, team_1.rect)
        display.blit(team_2.surf, team_2.rect)
        display.blit(team_3.surf, team_3.rect)

        # UPDATE THE BUTTONS
        if teambuilder.update():
            return teambuilder.value

        if battle.update():
            return battle.value

        pygame.display.update()
        FramePerSec.tick(FPS)
