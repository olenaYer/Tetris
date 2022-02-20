import pygame


class Game:
    def __init__(self):
        self.score = 1
        self.line = 1
        self.width = 500
        self.height = 900
        self.size_figure = self.width // 10
        self.left_border = False
        self.right_border = False
        self.bottom_border = False

    def move(self, figure, event=None):
        max_left = figure[0].left
        max_right = figure[0].right
        max_bottom = figure[0].bottom
        dif_height = 0
        for rect in figure:

            if rect.left < max_left:
                max_left = rect.left
            if rect.right > max_right:
                max_right = rect.right
            if rect.bottom > max_bottom:
                max_bottom = rect.bottom

        for rect in figure:
            if event is None:
                if not self.bottom_border:
                    if max_bottom < self.height:
                        rect.bottom += (self.height * 0.8 - self.size_figure) // 67
                    else:
                        self.bottom_border = True
                        self.left_border = True
                        self.right_border = True

            if event == pygame.K_LEFT:
                if not self.left_border:
                    if max_left > 0:
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
                if max_bottom > self.height:
                    if rect.bottom == max_bottom:
                        rect.bottom = self.height
                    else:
                        rect.bottom = self.height - self.size_figure

                if not self.bottom_border:
                    if max_bottom < self.height:
                        rect.bottom += self.size_figure
                    else:
                        self.bottom_border = True
                        self.left_border = True
                        self.right_border = True
                print(max_bottom)


        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     rect.left -= self.size_figure
        # if keys[pygame.K_RIGHT]:
        #     rect.right += self.size_figure
        # if keys[pygame.K_DOWN]:
        #     rect.top += self.size_figure
