import pygame


class Button:
    def __init__(self, img, x, y, width, height, text=''):
        self._img = pygame.transform.scale(img, (width, height))
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._text = text

    def draw(self, win):
        # Call this method to draw the button onto the screen
        win.blit(self._img, (self._x, self._y))

    def mouse_is_over(self, pos):
        # pos is the mouse position, which is a tuple of (x,y) coordinates
        if (pos[0] > self._x) and (pos[0] < (self._x + self._width)) and (pos[1] > self._y) and (pos[1] < self._y + self._height):
                return True
        return False
