from game_objects.game_object import GameObject


class Ground(GameObject):
    """
    Class encompasses everything that involves the ground in Flappy Bird
    """
    def __init__(self, game):
        super().__init__(game)
        self._ground = self._sprite_sheet.ground
        self._speed = 58.33 * self._game.get_scale()
        self._pos_list = []
        self._init_pos_list()

    def update(self):
        # update the sprite position in the game screen
        for pos in self._pos_list:
            pos.x = pos.x - self._speed * self._game.get_frame_elapsed_time()
            if pos.x < -self.get_size(self._sprite_sheet.night_background)[0]:
                pos.x = self.get_size(self._sprite_sheet.night_background)[0]

    def draw(self):
        # render sprites to the game screen
        for pos in self._pos_list:
            self._game.get_screen().blit(self._ground, (int(pos.x), pos.y))

    def _init_pos_list(self):
        # initialize the position of the ground sprites
        self._pos_list = [self.vec(0, self.get_size(self._sprite_sheet.night_background)[1]
                                    - self.get_size(self._ground)[1] + 10 * self._game.get_scale()),
                          self.vec(self.get_size(self._sprite_sheet.night_background)[0], self.get_size(self._sprite_sheet.night_background)[1]
                                    - self.get_size(self._ground)[1] + 10 * self._game.get_scale())]

    def get_pos_list(self):
        return self._pos_list


