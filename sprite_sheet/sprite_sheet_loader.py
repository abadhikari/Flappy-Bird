import pygame


class SpriteSheetLoader:
    """
    Loads the Flappy Bird spritesheet for use
    """
    def __init__(self, sprite_path, scale):
        self._sprite_sheet = SpriteSheetLoader.load_image(sprite_path, scale)

    @staticmethod
    def load_image(strng, scale):
        img = pygame.image.load(strng).convert_alpha()
        size = img.get_rect().size
        return pygame.transform.scale(img, (int(size[0] * scale), int(size[1] * scale)))

    @staticmethod
    def crop(x, y, width, height, img):
        image = pygame.Surface([width, height]).convert()  # Create a new blank image
        image.blit(img, (0, 0),
                   (x, y, width, height))  # Copy the sprite from the large sheet onto the smaller image
        image.set_colorkey((0, 0, 0))  # Assuming black works as the transparent color
        return image

    def get_sheet(self):
        return self._sprite_sheet

