import pygame


class Screen:

    def __init__(self):
        self.width = 300
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = (18, 18, 19)
        self.border_color = (237, 235, 252)
        self.colors = [(240, 62, 70), (0, 128, 128), (255, 119, 119), (150, 137, 127)]
        self.field_figures = list()

    def draw(self):
        self.draw_background()
        self.draw_field()

    def draw_background(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.screen.fill(self.bg)

    #def draw_score(self):


    def draw_field(self):

        rect = pygame.Rect(0, self.height * 0.3, self.width, self.height * 0.7)
        pygame.draw.rect(self.screen, self.border_color, rect, 2)
        pygame.display.flip()
