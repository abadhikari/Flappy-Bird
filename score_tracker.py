from game_object import GameObject
import json
import os


class ScoreTracker(GameObject):
    """
    Keeps track of score and everything score-related
    """
    def __init__(self, game):
        super().__init__(game)
        self._high_score = 0
        # if file doesn't exist, create and then initialize
        if not os.path.exists('high_score.json'):
            self.high_score_to_json()
        self._json_to_high_score()   # get high score from json file
        self._score = 0
        self._game_over_scale = .7

    def draw(self):
        # renders the score and the high score (if game over) onto the screen
        num_size = self.get_size(self._sprite_sheet.two)
        one_size = self.get_size(self._sprite_sheet.one)
        score_pos, high_score_pos = self._draw_pos(one_size, num_size)

        for j, strng in enumerate([str(self._score), str(self._high_score)]):
            pos = score_pos if j == 0 else high_score_pos
            for i, char in enumerate(strng):
                size = num_size[0] if char is not '1' else one_size[0]
                score_img = self.num_strng_to_num_sprite(char)

                if self._game.is_over():
                    size *= self._game_over_scale
                    score_img = self.resize_img(score_img, self._game_over_scale)
                self._game.get_screen().blit(score_img, (pos.x, pos.y))
                pos.x += size

    def _draw_pos(self, one_size, num_size):
        # determines the appropriate location of high score and score
        background_size = self.get_size(self._sprite_sheet.day_background)
        score_box_size = self.get_size(self._sprite_sheet.score_box)
        score_pos = self.vec(background_size[0] // 2 -
                             ((num_size[0] * (len(str(self._score)) - str(self._score).count('1')) +
                               (one_size[0] * str(self._score).count('1'))) // 2), background_size[1] // 8)
        high_score_pos = self.vec(-100, -100)

        # determines the high score location on the screen only if game over
        if self._game.is_over():
            score_pos.x = background_size[0] // 2 + score_box_size[0] // 2.7 - \
                          ((num_size[0] * (len(str(self._score)) - str(self._score).count('1')) +
                            (one_size[0] * str(self._score).count('1'))) // 2)
            score_pos.y = background_size[1] // 2 - score_box_size[1] // 4.2
            high_score_pos = self.vec(background_size[0] // 2 + score_box_size[0] // 2.7 -
                                      ((num_size[0] * (len(str(self._score)) - str(self._score).count('1')) +
                                        (one_size[0] * str(self._score).count('1'))) // 2),background_size[1] // 2 + score_box_size[1] // 7)
        return score_pos, high_score_pos

    def update(self):
        # checks if the bird has fully entered either of the rendered pipes and if so, score increases by one for each pipe
        bird_hit_box_x = self._game.get_collision_detection().get_bird_hit_box_pos().x
        pipe1_x = self._game.get_pipe().get_pos_lists()[0][0].x
        pipe2_x = self._game.get_pipe().get_pos_lists()[0][1].x
        if (bird_hit_box_x > pipe1_x and bird_hit_box_x < pipe1_x + 3) or (bird_hit_box_x > pipe2_x and bird_hit_box_x < pipe2_x + 3):
            self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score

    def reset(self):
        self._score = 0

    def num_strng_to_num_sprite(self, num_strng):
        # use a dict to act like a switch statement to select the number sprite that corresponds to a number string
        switcher = {
            '0': self._sprite_sheet.zero,
            '1': self._sprite_sheet.one,
            '2': self._sprite_sheet.two,
            '3': self._sprite_sheet.three,
            '4': self._sprite_sheet.four,
            '5': self._sprite_sheet.five,
            '6': self._sprite_sheet.six,
            '7': self._sprite_sheet.seven,
            '8': self._sprite_sheet.eight,
            '9': self._sprite_sheet.nine
        }
        return switcher[num_strng]

    def high_score_to_json(self):
        with open('high_score.json', 'w') as write_file:
            json.dump(self._high_score, write_file)

    def _json_to_high_score(self):
        with open('high_score.json', 'r') as read_file:
            self._high_score = json.load(read_file)

    def get_score(self):
        return self._score