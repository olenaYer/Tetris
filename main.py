import random

import pygame
from screen import Screen
from game import Game
import time


class Main:
    def __init__(self):
        game = Game()
        screen = Screen(game.score, game.line)
        figure = screen.figures[0]

        while True:
            if game.figure_is_down:
                figure = random.choice(screen.field_figures)
                color_figure = random.choice(screen.colors)
                screen.figures.append(figure)
                screen.color_figures.append(color_figure)

                game.bottom_border, game.left_border, game.right_border = False, False, False

                game.figure_is_down = False
            screen.draw()
            time.sleep(0.2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYUP:
                    game.move(figure, event.key)

            game.move(figure)


Main()
# TODO: buttons holding, score, full line reset, collision
