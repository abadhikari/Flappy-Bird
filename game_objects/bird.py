import math

from game_objects.game_object import GameObject
from misc.constants import Constants


class Bird(GameObject):
    """
    Class encompasses everything that involves the bird in Flappy Bird
    """
    def __init__(self, game):
        super().__init__(game)
        self._bird_animation = [self._sprite_sheet.bird_up,
                                self._sprite_sheet.bird_middle,
                                self._sprite_sheet.bird_down,
                                self._sprite_sheet.bird_middle]
        self._pos = self.vec(self.get_size(self._sprite_sheet.night_background)[0] // 2 -
                              self.get_size(self._bird_animation[0])[0] // 2,
                              self.get_size(self._sprite_sheet.night_background)[1] // 2 -
                              self.get_size(self._bird_animation[1])[1] // 2)
        self._curr_sprite = 0
        self._animation_speed = 15

        # gravity
        self._vel = self.vec(0, 0)
        self._acc = self.vec(0, 0)

    def update(self):
        # update the sprites position in the game screen
        if self._game.started():
            self._acc = self.vec(0, (Constants.PLAYER_GRAV // 3 * self._game.get_scale()))
            # equations of motion
            self._vel += self._acc * self._game.get_frame_elapsed_time() * .833 * self._game.get_scale()
            self._pos += (self._vel + 0.5 * self._acc) * math.sqrt(self._game.get_frame_elapsed_time())
        self._curr_sprite = (self._curr_sprite + self._animation_speed * self._game.get_frame_elapsed_time()) % len(self._bird_animation)

    def draw(self):
        # render the sprite to the game screen
        self._game.get_screen().blit(self._bird_animation[int(self._curr_sprite)], (self._pos.x, self._pos.y))

    def jump(self):
        self._vel.y = 0
        self._vel.y -= 43.33 * self._game.get_scale()

    def get_pos(self):
        return self._pos

    def get_curr_sprite(self):
        return self._bird_animation[int(self._curr_sprite)]


