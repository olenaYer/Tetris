import pygame
from screen import Screen
from game import Game
import time


class Main:
    def __init__(self):
        game = Game()
        screen = Screen(game.score, game.line)

        while True:
            screen.draw()
            time.sleep(0.2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYUP:
                    game.move(screen.figure, event.key)

            game.move(screen.figure)


Main()
