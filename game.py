import pygame


class Game:
    def __init__(self):
        self.score = 1
        self.line = 1
        self.size_figure = 30

    def move(self, figure, event=None):
        for rect in figure:
            rect.top += self.size_figure

            if event == pygame.K_LEFT:
                rect.left -= self.size_figure
            if event == pygame.K_RIGHT:
                rect.right += self.size_figure

