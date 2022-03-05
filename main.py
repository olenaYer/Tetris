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
        game.name = screen.field_figures.index(figure)
        # print(game.name)

        while True:
            screen.field_figures = screen.init_figures()
            screen.draw()
            game.line_reset(screen.figures)
            if game.figure_is_down:
                figure = random.choice(screen.field_figures.copy()).copy()
                game.name = screen.field_figures.index(figure)
                game.state = 1
                # print(figure)
                color_figure = random.choice(screen.colors.copy())
                screen.figures.append(figure)
                screen.color_figures.append(color_figure)

                game.bottom_border, game.left_border, game.right_border = False, False, False

                game.figure_is_down = False
            time.sleep(0.2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYUP:
                    game.move(figure, screen.figures, event.key)

            game.move(figure, screen.figures)
            game.check_collision(figure, screen.figures)


Main()
# TODO: buttons holding, score, full line reset, rotation fix with collision
