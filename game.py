import pygame


class Game:
    def __init__(self):
        self.score = 1
        self.line = 1
        self.size_figure = 30
        self.width = 350
        self.height = 750

    def move(self, figure, event=None):
        if self.check_borders(figure):
            for rect in figure:
                if event is None:
                    rect.top += self.size_figure / 3

                if event == pygame.K_LEFT:
                    rect.left -= self.size_figure
                if event == pygame.K_RIGHT:
                    rect.right += self.size_figure
                if event == pygame.K_DOWN:
                    rect.top += self.size_figure

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_LEFT]:
            #     rect.left -= self.size_figure
            # if keys[pygame.K_RIGHT]:
            #     rect.right += self.size_figure
            # if keys[pygame.K_DOWN]:
            #     rect.top += self.size_figure

    def check_borders(self, figure):
        for rect in figure:
            if rect.left < 0:
                return False
            if rect.right > self.width:
                return False
            if rect.bottom > self.height:
                return False
        return True
