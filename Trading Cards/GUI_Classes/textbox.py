import pygame
pygame.font.init()


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def write_text(msg, x, y, font, size, colour):
    text = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(msg, text, colour)
    textRect.center = (x, y)
    return textSurf, textRect


def text_box(msg, x, y, w, h, bp, ap, pressed, msg_size, box_msg, display_screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Display the text over the box
    additional_message = write_text(box_msg, x + 10, y + h / 2, "calibri", msg_size, (0, 0, 0))
    additional_message[1].center = (x + 10 + additional_message[0].get_width() / 2, y + h / 2)
    display_screen.blit(additional_message[0], additional_message[1])

    # If clicked on it
    if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
        pygame.draw.rect(display_screen, ap, (x, y, w, h), 1)
        return True
    # If not clicked on
    elif (not (x + w > mouse[0] > x and y + h > mouse[1] > y) and click[0] == 1) or not pressed:
        pygame.draw.rect(display_screen, bp, (x, y, w, h), 1)
        message = write_text(msg, x + 20, y + h / 2, "calibri", msg_size, bp)
        message[1].center = (x + 20 + message[0].get_width() / 2, y + h / 2)
        if len(box_msg) == 0:
            display_screen.blit(message[0], message[1])
        return False
    # If already clicked on
    elif pressed:
        pygame.draw.rect(display_screen, ap, (x, y, w, h), 1)
        return True
