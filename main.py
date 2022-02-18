import pygame
from screen import Screen
from game import Game


class Main:
    def __init__(self):
        game = Game()
        screen = Screen(game.score, game.line)


        while True:
            screen.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

Main()
