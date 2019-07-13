from misc import spritesheetloader
import pygame

vec = pygame.math.Vector2
PLAYER_GRAV = 0.6
PLAYER_ACC = 0.5


class Player:
    def __init__(self,game):
        self._game = game

        # bird sprites
        self._spritesheet = spritesheetloader.SpriteSheetLoader("res/bird.png")
        self._bird_animations = []
        self._fill_bird_animations()
        self._curr_bird = pygame.transform.scale(self._bird_animations[0], (80, 80))
        self._curr_index = 0

        # resize the bird images
        for f in range(len(self._bird_animations)):
            self._bird_animations[f] = pygame.transform.scale(self._bird_animations[f], (80, 80))

        # player position variables
        self._pos = vec(100, 200)
        self._vel = vec(0, 0)
        self._acc = vec(0, 0)

    def draw(self):
        size_diff = self._curr_bird.get_rect().size[0] - 80
        x_pos = self._game.player._pos.x - (size_diff / 2)
        y_pos = self._game.player._pos.y - (size_diff / 2)
        self._game.screen.blit(self._curr_bird, (x_pos, y_pos))

    def jump(self):
        self._vel.y = 0
        self._vel.y -= 11.5

    def update(self):
        if self._game.start_game:
            self._acc = vec(0, PLAYER_GRAV)
            # equations of motion
            self._vel += self._acc
            self._pos += self._vel + 0.5 * self._acc

        # keeps the bird on the screen when it touches the ground
        if self._pos.y >= 450:
            self._pos.y = 450

        if not self._game.gameOver:
            # flapping animation
            if self._game.timer % 6 == 0:
                self._curr_bird = self._bird_animations[self._curr_index]
                self._curr_index += 1
                if self._curr_index > 3:
                    self._curr_index = 0

            # rotation animation
            if self._game.timer % 6 == 0:
                self._rotation()

    def _rotation(self):
        # controls how the bird rotates while it is in the air depending on the velocity
        curr_y_vec = self._game.player._vel.y
        angle = (-(6 * min(curr_y_vec,15)) if curr_y_vec >= 0 else 30)
        self._curr_bird = pygame.transform.rotate(self._curr_bird, angle)

    def _fill_bird_animations(self):
        # fills the list with the possible bird flapping positions
        sprite_size = self._spritesheet._sprite_sheet.get_rect().size
        length = 28
        for f in range(3):
            self._bird_animations.append(self._spritesheet.crop(f * length, sprite_size[1] - length, length, length))
        self._bird_animations.append(self._spritesheet.crop(length, sprite_size[1] - length, length, length))
