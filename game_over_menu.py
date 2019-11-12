from misc.button import Button
from game_object import GameObject


class GameOverMenu(GameObject):
    """
    Creates and renders the game over menu when game over
    """
    def __init__(self, game):
        super().__init__(game)
        self._game = game
        self._restart_button = None
        self._score_box_pos = None
        self._restart_button_size = None
        self._background_size = self.get_size(self._game.get_background().curr_background())
        self._score_box_size = self.get_size(self._sprite_sheet.score_box)
        self._game_over_size = self.get_size(self._sprite_sheet.game_over)
        self._init()

    def _init(self):
        # initialize the various aspects in the gameover menu
        score_box_x = self._background_size[0] // 2 - self._score_box_size[0] // 2
        score_box_y = self._background_size[1] // 2 - self._score_box_size[1] // 2
        self._score_box_pos = self.vec(score_box_x, score_box_y)

        self._restart_button_size = self.get_size(self._sprite_sheet.restart)
        restart_button_x = (self._background_size[0] // 2 - self._restart_button_size[0] // 2 * .85)
        restart_button_y = (score_box_y + self._score_box_size[1]) - self._restart_button_size[1] * 1.2
        self._restart_button = Button(self._sprite_sheet.restart, restart_button_x, restart_button_y)

    def draw(self):
        # render game over menu sprites to the game screen
        self._game.get_screen().blit(self._sprite_sheet.score_box, (self._score_box_pos.x, self._score_box_pos.y))
        self._game.get_screen().blit(self._sprite_sheet.game_over, self._get_game_over_pos())
        self._restart_button.draw(self._game.get_screen())
        self._game.get_screen().blit(self._determine_medal(), self._get_medal_pos())

    def _determine_medal(self):
        # chooses a medal sprite out of bronze, silver, and gold depending on the score of the player
        score = self._game.get_score()
        medal = self._sprite_sheet.bronze_medal
        if score >= 50:
            medal = self._sprite_sheet.silver_medal
        if score >= 100:
            medal = self._sprite_sheet.gold_medal
        return medal

    def _get_game_over_pos(self):
        # determines the location of the game over sprite
        pos_x = self._background_size[0] // 2 - self._game_over_size[0] // 2
        pos_y = self._background_size[1] // 4 - self._game_over_size[1] // 2
        return pos_x, pos_y

    def _get_medal_pos(self):
        # determines the location of the medal sprite
        pos_x = self._background_size[0] // 2 - self._score_box_size[0] // 2 + self._background_size[0] / 9.1915
        pos_y = self._background_size[1] // 2 - self._score_box_size[1] // 2 + self._background_size[1] / 10.8857
        return pos_x, pos_y

    def update(self):
        # as game is over, no need to update anything
        pass

    def get_restart_button(self):
        return self._restart_button

