from abc import ABC, abstractmethod
import pygame


class GameObject(ABC):
    """
    Abstract class for all game objects
    """
    def __init__(self, game):
        super().__init__()
        self._game = game
        self._sprite_sheet = game.get_sprite_sheet()
        self._speed = 30

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    def get_size(self, img):
        return self._sprite_sheet.get_size(img)

    def vec(self, x, y):
        return pygame.math.Vector2(x, y)

    def resize_img(self, img, scale):
        img_size = self.get_size(img)
        return pygame.transform.scale(img, (int(img_size[0] * scale), int(img_size[1] * scale)))

