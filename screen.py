import pygame
import random


class Screen:

    def __init__(self, score, line):
        self.width = 500
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = (18, 18, 19)
        self.border_color = (237, 235, 252)
        self.colors = [(240, 62, 70), (0, 128, 128), (255, 119, 119), (150, 137, 127)]
        self.score = score
        self.line = line
        self.size_figure = self.width // 10
        self.field_figures = self.init_figures()
        self.figure = random.choice(self.field_figures)
        self.color_figure = random.choice(self.colors)

    def draw(self):
        self.draw_background()
        self.draw_field()
        self.draw_score(self.score, self.line)
        self.draw_figure()
        pygame.display.flip()

    def draw_background(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.screen.fill(self.bg)

    def draw_score(self, score, line):
        rect_score = pygame.Rect(0, 0, self.width, self.height * 0.1)
        rect_line = pygame.Rect(0, self.height * 0.1, self.width, self.height * 0.1)
        pygame.draw.rect(self.screen, self.border_color, rect_score, 1)
        pygame.draw.rect(self.screen, self.border_color, rect_line, 1)

        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render(f'SCORE: {score}', True, (255, 255, 255), self.bg)
        score_rect = score.get_rect()
        score_rect.center = (self.width // 4, (self.height * 0.1) // 2)

        line = font.render(f'LINE: {line}', True, (255, 255, 255), self.bg)
        line_rect = score.get_rect()
        line_rect.center = (self.width // 4, self.height * 0.3 // 2)

        self.screen.blit(score, score_rect)
        self.screen.blit(line, line_rect)

    def draw_figure(self):
        for rect in self.figure:
            pygame.draw.rect(self.screen, self.color_figure, rect)

    def draw_field(self):
        rect = pygame.Rect(0, self.height * 0.2, self.width, self.height * 0.8)
        pygame.draw.rect(self.screen, self.border_color, rect, 1)

    def init_figures(self):
        figures = []
        s_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2 - self.size_figure, self.height * 0.2 + self.size_figure,
                               self.size_figure, self.size_figure)]
        z_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2 - self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2 + self.size_figure,
                               self.size_figure, self.size_figure)]
        l_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2 + 2 * self.size_figure, self.height * 0.2,
                               self.size_figure, self.size_figure)]
        j_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2 - self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2 - 2 * self.size_figure, self.height * 0.2,
                               self.size_figure, self.size_figure)]
        t_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2 - self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure)]

        i_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure * 2, self.size_figure,
                               self.size_figure),
                   pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure * 3, self.size_figure,
                               self.size_figure)]

        sq_block = [pygame.Rect(self.width // 2, self.height * 0.2, self.size_figure, self.size_figure),
                    pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2, self.size_figure,
                                self.size_figure),
                    pygame.Rect(self.width // 2, self.height * 0.2 + self.size_figure, self.size_figure,
                                self.size_figure),
                    pygame.Rect(self.width // 2 + self.size_figure, self.height * 0.2 + self.size_figure,
                                self.size_figure,
                                self.size_figure)]
        figures.append(s_block)
        figures.append(z_block)
        figures.append(l_block)
        figures.append(j_block)
        figures.append(t_block)
        figures.append(i_block)
        figures.append(sq_block)

        return figures
