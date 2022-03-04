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

        self.state = 1

        self.name = ''

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
        elif event == pygame.K_UP:
            self.rotate(figure_copy)
            self.check_collision(figure_copy, figures)
            self.get_max_cords(figure_copy)
            if self.figure_is_down or self.max_bottom > self.height or self.max_left < 0 or self.max_right > self.width:
                for i in range(3):
                    self.rotate(figure_copy)
                self.figure_is_down = False
                self.left_border = False
                self.right_border = False
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

    def rotate(self, figure):
        self.left_border = False
        self.right_border = False
        if self.state == 5:
            self.state = 1
        print(self.state)

        if self.state == 1 or self.state == 3:
            # print(self.name)
            if self.name == 0:
                figure[0].left += self.size_figure
                figure[1].top += self.size_figure
                figure[2].top -= self.size_figure
                figure[3].top -= self.size_figure * 2
                figure[3].left += self.size_figure
            elif self.name == 1:
                figure[0].left += self.size_figure
                figure[1].left += self.size_figure * 2
                figure[1].top -= self.size_figure
                figure[2].top -= self.size_figure
                figure[3].left -= self.size_figure
            elif self.name == 2:
                if self.state == 1:
                    figure[0].left += self.size_figure * 2
                    figure[0].top -= self.size_figure
                    figure[1].left += self.size_figure
                    figure[2].left += self.size_figure
                    figure[2].top -= self.size_figure * 2
                    figure[3].top += self.size_figure
                else:
                    figure[0].top += self.size_figure
                    figure[0].left -= self.size_figure * 2
                    figure[1].left -= self.size_figure
                    figure[2].left -= self.size_figure
                    figure[2].top += self.size_figure * 2
                    figure[3].top -= self.size_figure
            elif self.name == 3:
                if self.state == 1:
                    figure[0].top += self.size_figure * 2
                    figure[1].top += self.size_figure
                    figure[2].top += self.size_figure
                    figure[1].left += self.size_figure
                    figure[2].left -= self.size_figure
                    figure[3].left += self.size_figure * 2
                else:
                    figure[0].top -= self.size_figure * 2
                    figure[1].left -= self.size_figure
                    figure[1].top -= self.size_figure
                    figure[2].top -= self.size_figure
                    figure[2].left += self.size_figure
                    figure[3].left -= self.size_figure * 2

            elif self.name == 4:
                if self.state == 1:
                    figure[0].left += self.size_figure
                    figure[1].left += self.size_figure * 2
                    figure[1].top -= self.size_figure
                    figure[2].top += self.size_figure
                    figure[3].top -= self.size_figure
                else:
                    figure[0].left -= self.size_figure
                    figure[0].top -= self.size_figure
                    figure[1].left -= self.size_figure * 2
                    figure[2].top -= self.size_figure * 2
            elif self.name == 5:
                for rect in figure:
                    rect.top = figure[1].top
                figure[0].left -= self.size_figure
                figure[2].left += self.size_figure
                figure[3].left += self.size_figure * 2

        elif self.state == 2 or self.state == 4:
            if self.name == 0:
                figure[0].left -= self.size_figure
                figure[1].top -= self.size_figure
                figure[2].top += self.size_figure
                figure[3].top += self.size_figure * 2
                figure[3].left -= self.size_figure
            elif self.name == 1:
                figure[0].left -= self.size_figure
                figure[1].left -= self.size_figure * 2
                figure[1].top += self.size_figure
                figure[2].top += self.size_figure
                figure[3].left += self.size_figure
            elif self.name == 2:
                if self.state == 2:
                    figure[0].top += self.size_figure
                    figure[1].left -= self.size_figure
                    figure[2].left += self.size_figure
                    figure[3].left -= self.size_figure * 2
                    figure[3].top -= self.size_figure
                else:
                    figure[0].top -= self.size_figure
                    figure[1].left += self.size_figure
                    figure[2].left -= self.size_figure
                    figure[3].left += self.size_figure * 2
                    figure[3].top += self.size_figure
            elif self.name == 3:
                if self.state == 2:
                    figure[0].left -= self.size_figure
                    figure[1].top += self.size_figure
                    figure[2].top -= self.size_figure
                    figure[3].top += self.size_figure * 2
                    figure[3].left += self.size_figure
                else:
                    figure[0].left += self.size_figure
                    figure[1].top -= self.size_figure
                    figure[2].top += self.size_figure
                    figure[3].top -= self.size_figure * 2
                    figure[3].left -= self.size_figure
            elif self.name == 4:
                if self.state == 2:
                    figure[0].left -= self.size_figure
                    figure[0].top += self.size_figure
                    figure[1].top += self.size_figure * 2
                    figure[2].left -= self.size_figure * 2
                else:
                    figure[0].left += self.size_figure
                    figure[0].top -= self.size_figure
                    figure[1].top -= self.size_figure * 2
                    figure[2].left += self.size_figure * 2
            elif self.name == 5:
                for rect in figure:
                    rect.left = figure[1].left
                figure[0].top -= self.size_figure
                figure[2].top += self.size_figure
                figure[3].top += self.size_figure * 2

        self.state += 1

    def line_reset(self, figures):
        x, y = 0, self.height
        for figure in figures:
            for rect in figure:
                if rect.left == x and rect.bottom == y:
                    x += self.size_figure
        if x == self.width:
            x = 0
            print('ready')
            y -= self.size_figure
            for i in range(len(figures)):
                for j in range(len(figures[i])):
                    rect = figures[i][j]
                    if rect.left == x and rect.bottom == y:
                        print(rect)
