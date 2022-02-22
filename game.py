import pygame


class Game:
    def __init__(self):
        self.score = 1
        self.line = 1
        self.width = 400
        self.height = 700
        self.size_figure = self.width // 10
        self.left_border = False
        self.right_border = False
        self.bottom_border = False

        self.figure_is_down = False

    def move(self, figure, figures, event=None):
        figure_copy = figure.copy()
        max_left = figure[0].left
        max_right = figure[0].right
        max_bottom = figure[0].bottom
        for rect in figure_copy:

            if rect.left < max_left:
                max_left = rect.left
            if rect.right > max_right:
                max_right = rect.right
            if rect.bottom > max_bottom:
                max_bottom = rect.bottom

        for rect in figure_copy:
            self.check_collision(figure, figures)
            if event is None:
                if not self.bottom_border:
                    if max_bottom < self.height:
                        rect.bottom += (self.height * 0.8 - self.size_figure) // 52
                    else:
                        self.bottom_border = True
                        self.left_border = True
                        self.right_border = True
                        self.figure_is_down = True

            if event == pygame.K_LEFT:
                if not self.left_border:
                    if max_left > 0:
                        self.check_collision(figure, figures)
                        if not self.figure_is_down:
                            rect.left -= self.size_figure
                            self.right_border = False
                    else:
                        self.left_border = True
            if event == pygame.K_RIGHT:
                if not self.right_border:
                    if max_right < self.width:
                        rect.right += self.size_figure
                        self.left_border = False
                    else:
                        self.right_border = True
            if event == pygame.K_DOWN:

                if max_bottom + self.size_figure > self.height:
                    if rect.bottom == max_bottom:
                        rect.bottom = self.height
                    else:
                        if rect.bottom < max_bottom - self.size_figure:
                            if rect.bottom < max_bottom - self.size_figure * 2:
                                rect.bottom = self.height - self.size_figure * 3
                            else:
                                rect.bottom = self.height - self.size_figure * 2
                        else:
                            rect.bottom = self.height - self.size_figure

                if not self.bottom_border:
                    if max_bottom + self.size_figure <= self.height:
                        rect.bottom += self.size_figure
                        self.check_collision(figure_copy, figures)
                        if self.figure_is_down:
                            self.figure_is_down = False
                            rect.bottom -= self.size_figure

                    else:
                        self.bottom_border = True
                        self.left_border = True
                        self.right_border = True
                        self.figure_is_down = True
        figure.clear()
        for rect in figure_copy:
            figure.append(rect)

    def check_collision(self, figure, figures):
        figures_copy = figures.copy()
        figures_copy.remove(figure)

        for fig in figures_copy:
            for rect in fig:
                for r in figure:
                    if rect.top <= r.bottom < rect.bottom and r.left == rect.left:
                        self.figure_is_down = True
