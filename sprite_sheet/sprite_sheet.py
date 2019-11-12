import pygame

from sprite_sheet.sprite_sheet_loader import SpriteSheetLoader


class SpriteSheet:
    """
    Creates all the sprites needed for flappy bird.
    Requires the init function to be called.
    """

    # game sprites
    sprite_sheet = None
    ground = None
    up_pipe = None
    down_pipe = None
    day_background = None
    night_background = None
    bird_up = None
    bird_down = None
    bird_middle = None

    # menu sprites
    score_box = None
    bronze_medal = None
    silver_medal = None
    gold_medal = None
    game_over = None
    restart = None

    # score sprites
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    seven = None
    eight = None
    nine = None


    @staticmethod
    def init(scale):
        # initializes all the sprites using the SpriteSheetLoader class
        sprite_sheet_loader = SpriteSheetLoader('res/flappy_bird_sprite.png', scale)
        SpriteSheet.sprite_sheet = sprite_sheet_loader.get_sheet()

        # game sprites
        SpriteSheet.ground = SpriteSheetLoader.crop(292 * scale, 0, 169 * scale, 55 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.up_pipe = SpriteSheetLoader.crop(84 * scale, 323 * scale, 26 * scale, 160 * scale,
                                                     SpriteSheet.sprite_sheet)
        SpriteSheet.down_pipe = pygame.transform.flip(SpriteSheet.up_pipe, False, True)
        SpriteSheet.day_background = SpriteSheetLoader.crop(0, 0, 144 * scale, 254 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.night_background = SpriteSheetLoader.crop(146 * scale, 0, 144 * scale, 254 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.bird_up = SpriteSheetLoader.crop(0 * 28 * scale,
                                                     SpriteSheet.get_size(SpriteSheet.sprite_sheet)[1] - 28 * scale,
                                                     28 * scale, 28 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.bird_down = SpriteSheetLoader.crop(2 * 28 * scale,
                                                       SpriteSheet.get_size(SpriteSheet.sprite_sheet)[1] - 28 * scale,
                                                       28 * scale, 28 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.bird_middle = SpriteSheetLoader.crop(1 * 28 * scale,
                                                         SpriteSheet.get_size(SpriteSheet.sprite_sheet)[1] - 28 * scale,
                                                         28 * scale, 28 * scale, SpriteSheet.sprite_sheet)

        # menu sprites
        SpriteSheet.score_box = SpriteSheetLoader.crop(0, 257 * scale, 116 * scale, 60 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.silver_medal = SpriteSheetLoader.crop(112 * scale, 453 * scale, 22 * scale, 22 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.bronze_medal = SpriteSheetLoader.crop(112 * scale, 477 * scale, 22 * scale, 22 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.gold_medal = SpriteSheetLoader.crop(121 * scale, 282 * scale, 22 * scale, 22 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.game_over = SpriteSheetLoader.crop(392 * scale, 56 * scale, 99 * scale, 25 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.restart = SpriteSheetLoader.load_image('res/restart.PNG', scale / 4)

        # score sprites
        SpriteSheet.zero = SpriteSheetLoader.crop(494 * scale, 58 * scale, 14 * scale, 26 * scale,SpriteSheet.sprite_sheet)
        SpriteSheet.one = SpriteSheetLoader.crop(134 * scale, 453 * scale, 10 * scale, 25 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.two = SpriteSheetLoader.crop((290 + 14 * 0) * scale, (158 + 26 * 0) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.three = SpriteSheetLoader.crop((290 + 14 * 1) * scale, (158 + 26 * 0) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.four = SpriteSheetLoader.crop((290 + 14 * 2) * scale, (158 + 26 * 0) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.five = SpriteSheetLoader.crop((290 + 14 * 3) * scale, (158 + 26 * 0) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.six = SpriteSheetLoader.crop((290 + 14 * 0) * scale, (156 + 26 * 1) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.seven = SpriteSheetLoader.crop((290 + 14 * 1) * scale, (156 + 26 * 1) * scale, 14 * scale, 25 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.eight = SpriteSheetLoader.crop((290 + 14 * 2) * scale, (156 + 26 * 1) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)
        SpriteSheet.nine = SpriteSheetLoader.crop((290 + 14 * 3) * scale, (156 + 26 * 1) * scale, 14 * scale, 26 * scale, SpriteSheet.sprite_sheet)



    @staticmethod
    def get_size(img):
        return img.get_rect().size
