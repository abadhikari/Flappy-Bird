import pygame


class Button:
    def __init__(self, img, x, y, width=None, height=None, text=''):
        self._width = img.get_size()[0] if not width else width
        self._height = img.get_size()[1] if not height else height
        self._button_img = pygame.transform.scale(img, (self._width, self._height))
        self._x = x
        self._y = y
        self._text = text

    def draw(self, win):
        """
        Call this method to draw the button onto the screen
        """
        win.blit(self._button_img, (self._x, self._y))

    def mouse_is_over(self, pos):
        """
        Determines if pos is the mouse position, which is a tuple of (x,y) coordinates
        """
        if (pos[0] > self._x) and (pos[0] < (self._x + self._width)) and (pos[1] > self._y) and (pos[1] < self._y + self._height):
                return True
        return False
