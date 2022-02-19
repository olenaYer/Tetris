import pygame


class Game:
    def __init__(self):
        self.score = 1
        self.line = 1
        self.size_figure = 5

    def move(self, figure, event=None):
        for rect in figure:
            if event is None:
                rect.top += self.size_figure

            if event == pygame.K_LEFT:
                rect.left -= self.size_figure
            if event == pygame.K_RIGHT:
                rect.right += self.size_figure
            if event == pygame.K_DOWN:
                rect.top += self.size_figure
