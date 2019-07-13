import pygame


class SpriteSheetLoader:
    """ Class used to grab images out of a sprite sheet. """
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        self._sprite_sheet = self.load_image(file_name)

    def crop(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        image = pygame.Surface([width, height]).convert()  # Create a new blank image
        image.blit(self._sprite_sheet, (0, 0), (x, y, width, height)) # Copy the sprite from the large sheet onto the smaller image
        image.set_colorkey((0, 0, 0))  # Assuming black works as the transparent color
        return image

    @staticmethod
    def load_image(string):
        return pygame.image.load(string).convert_alpha()