from game_object import GameObject
import random


class Pipe(GameObject):
    """
    Class encompasses everything that involves the pipes in Flappy Bird
    """
    def __init__(self, game):
        super().__init__(game)
        self._up_pipe = self._sprite_sheet.up_pipe
        self._down_pipe = self._sprite_sheet.down_pipe
        self._speed = 58.33 * self._game.get_scale()

        self._up_pipe_pos_list = []
        self._down_pipe_pos_list = []
        self._init_pos_lists()

    def update(self):
        # update the sprite position in the game screen
        up_pipe_pos, down_pipe_pos = None, None
        for i, pos_list in enumerate([self._down_pipe_pos_list, self._up_pipe_pos_list]):
            for j, pos in enumerate(pos_list):
                pos.x = pos.x - self._speed * self._game.get_frame_elapsed_time()
                if pos.x < -self.get_size(self._up_pipe)[0]:
                    if i == 0:
                        up_pipe_pos, down_pipe_pos = self._make_pipe_pair()
                        pos_list[j] = self.vec(down_pipe_pos[0], down_pipe_pos[1])
                    else:
                        pos_list[j] = self.vec(up_pipe_pos[0], up_pipe_pos[1])
                    pos.x = pos_list[j - 1].x + 83.33 * self._game.get_scale()

    def draw(self):
        # render sprites to the game screen
        pipe_sprites = [self._down_pipe, self._up_pipe]
        for i, pos_list in enumerate([self._down_pipe_pos_list, self._up_pipe_pos_list]):
            for pos in pos_list:
                self._game.get_screen().blit(pipe_sprites[i], (pos.x, pos.y))

    def _init_pos_lists(self):
        # initialize the position of the pipe sprites
        for i in range(2):
            up_pipe_pos, down_pipe_pos = self._make_pipe_pair()
            self._up_pipe_pos_list.append(self.vec(up_pipe_pos[0] + 83.33 * self._game.get_scale() * i, up_pipe_pos[1]))
            self._down_pipe_pos_list.append(self.vec(down_pipe_pos[0] + 83.33 * self._game.get_scale() * i, down_pipe_pos[1]))

    def _make_pipe_pair(self):
        # returns a valid pair of positions that correspond to a pair of a top and bottom pipe
        space_between_pipes = 46.67 * self._game.get_scale()
        background_size = self.get_size(self._sprite_sheet.night_background)
        random_number = random.randrange(int(33.33 * self._game.get_scale()), int(100 * self._game.get_scale()))
        up_pipe_pos = [background_size[0], random_number + space_between_pipes]
        down_pipe_pos = [background_size[0], random_number - self.get_size(self._up_pipe)[1]]
        return up_pipe_pos, down_pipe_pos

    def get_pos_lists(self):
        return self._down_pipe_pos_list, self._up_pipe_pos_list

    def get_up_pipe(self):
        return self._up_pipe


