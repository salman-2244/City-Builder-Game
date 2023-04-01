import pygame, sys, colorsys


class GUI:  # firstly creating of the grid
    pygame.init()
    # create a screen:
    HEIGHT = 600
    WIDTH = 800

    BLOCKS = 5
    BLOCK_H = round(HEIGHT / BLOCKS)
    BLOCK_W = round(WIDTH / BLOCKS)

    TITLE = "City Builder"

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    done = False

    # (red,green,blue)
    c = (0, 150, 255)

    # drawing the grid
    for i in range(BLOCKS):
        h = round(i * HEIGHT)
        w = round(i * WIDTH)
        # horizontal lines 
        pygame.draw.line(screen, c, (0, h), (WIDTH, h))  # -- fill in the grid
        # vertical lines
        pygame.draw.line(screen, c, (w, 0), (w, HEIGHT))  # -- fill in the grid


def main():
    GUI()
