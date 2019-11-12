from game_object import GameObject
import time


class Background(GameObject):
    """
    Class encompasses everything that involves the background in Flappy Bird
    """
    def __init__(self, game):
        super().__init__(game)
        self._background = self.curr_background()

    def draw(self):
        # render sprites to the game screen
        self._game.get_screen().blit(self._background, (0, 0))

    def update(self):
        # update the background sprite position in the game screen
        self._background = self.curr_background()

    def curr_background(self):
        # chooses the respective background based on if the sun has set yet
        month = time.localtime().tm_mon
        day = time.localtime().tm_mday
        hour = time.localtime().tm_hour
        if hour >= self._sunset_hour(month, day) or hour < self._sunrise_hour(month,day):
            return self._sprite_sheet.night_background
        else:
            return self._sprite_sheet.day_background

    def _sunset_hour(self, month, day):
        # approximates the hour of sunset based on the day in the year
        total_day = month * 30 + day
        return int((3 * total_day / 178) + 17) if total_day < 178 else int((-3 * (total_day - 178) / 178) + 20)

    def _sunrise_hour(self, month, day):
        # approximates the hour of sunrise based on the day in the year
        total_day = month * 30 + day
        return int((-4 * total_day / 178) + 8) if total_day < 178 else int((4 * (total_day - 178) / 178) + 4)

