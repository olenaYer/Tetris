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

        self.max_left = 0
        self.max_right = 0
        self.max_bottom = 0

    def move(self, figure, figures, event=None):
        figure_copy = figure.copy()
        self.get_max_cords(figure_copy)

        if event is None:
            if not self.bottom_border:
                if self.max_bottom < self.height:
                    for rect in figure_copy:
                        rect.bottom += (self.height * 0.8 - self.size_figure) // 52
                else:
                    self.bottom_border = True
                    self.left_border = True
                    self.right_border = True
                    self.figure_is_down = True

        elif event == pygame.K_LEFT:
            if not self.left_border and not self.bottom_border:
                if self.max_left > 0:
                    for rect in figure_copy:
                        rect.left -= self.size_figure
                        self.right_border = False
                    self.check_collision(figure_copy, figures)
                    if self.figure_is_down:
                        for rect in figure_copy:
                            rect.left += self.size_figure
                        self.figure_is_down = False
                else:
                    self.left_border = True

        elif event == pygame.K_RIGHT:
            if not self.right_border and not self.bottom_border:
                if self.max_right < self.width:
                    for rect in figure_copy:
                        rect.left += self.size_figure
                        self.left_border = False
                    self.check_collision(figure_copy, figures)
                    if self.figure_is_down:
                        for rect in figure_copy:
                            rect.left -= self.size_figure
                        self.figure_is_down = False
                else:
                    self.right_border = True

        elif event == pygame.K_DOWN:
            if not self.bottom_border:
                if self.max_bottom < self.height:
                    for rect in figure_copy:
                        rect.bottom += self.size_figure
                        self.get_max_cords(figure_copy)

                    self.check_collision(figure_copy, figures)
                    if self.figure_is_down or self.max_bottom > self.height:
                        for rect in figure_copy:
                            rect.bottom -= self.size_figure
                        self.figure_is_down = False
        figure.clear()
        for rect in figure_copy:
            figure.append(rect)

    def check_collision(self, figure, figures):
        figures_copy = figures.copy()
        figures_copy.remove(figure)

        for fig in figures_copy:
            for rect in fig:
                for r in figure:
                    if rect.top <= r.bottom <= rect.bottom and r.left == rect.left:
                        self.figure_is_down = True

    def get_max_cords(self, figure):
        self.max_bottom = self.height // 2
        self.max_left = self.width // 2
        self.max_right = self.width // 2

        for rect in figure:
            if rect.left < self.max_left:
                self.max_left = rect.left
            if rect.right > self.max_right:
                self.max_right = rect.right
            if rect.bottom > self.max_bottom:
                self.max_bottom = rect.bottom
