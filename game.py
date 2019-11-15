import time

import pygame

from game_objects.background import Background
from game_objects.bird import Bird
from game_objects.ground import Ground
from game_objects.pipe import Pipe
from misc.center_gui import center_screen
from misc.collision_detection import CollisionDetection
from misc.constants import Constants
from misc.game_over_menu import GameOverMenu
from misc.score_tracker import ScoreTracker
from sprite_sheet.sprite_sheet import SpriteSheet


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((1, 1))
        self._sprite_sheet_scale = Constants.SPRITE_SCALE
        self._sprite_sheet = SpriteSheet()
        self._sprite_sheet.init(self._sprite_sheet_scale)

        # screen
        self._width = self._sprite_sheet.get_size(self._sprite_sheet.day_background)[0]
        self._height = self._sprite_sheet.get_size(self._sprite_sheet.day_background)[1]
        center_screen((self._width, self._height))
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Flappy Bird")

        # class instances
        self._bird = Bird(self)
        self._pipe = Pipe(self)
        self._ground = Ground(self)
        self._background = Background(self)

        # game variables
        self._running = True
        self._start = False
        self._mouse_pos = None
        self._score_tracker = ScoreTracker(self)

        # collision detection
        self._collision_detection = CollisionDetection(self)

        # fps variables
        self._fps = 60
        self._prev_time = time.time()
        self._curr_time = 0
        self._delta = 0
        self._fps_counter = 0
        self._time_per_frame = 1 / self._fps
        self._elapsed_time = 0
        self._lag = 0

        # game over variables
        self._game_over = False
        self._game_over_menu = GameOverMenu(self)

    def _update(self):
        # update the sprite positions in the game screen
        instances = (self._ground, self._bird) if not self._start else (self._background, self._pipe, self._ground, self._bird, self._score_tracker)
        for instance in instances:
            if not self._game_over:
                instance.update()

        if self._collision_detection.check_collision():
            self._game_over = True

    def _draw(self):
        # render the sprites to the game screen
        instances = (self._background, self._pipe, self._ground, self._bird, self._score_tracker)
        for instance in instances:
            instance.draw()
        if self._game_over:
            self._game_over_menu.draw()
            self._score_tracker.draw()
        pygame.display.flip()

    def _events(self):
        # checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                self._score_tracker.high_score_to_json()
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self._game_over:
                        self.new_game()
                    else:
                        self._bird.jump()
                        self._start = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                if self._game_over and self._game_over_menu.get_restart_button().mouse_is_over(self.mouse_pos):
                    self.new_game()

    def _run(self):
        # run an instance of Flappy Bird
        self._running = True
        while self._running:
            self._curr_time = time.time()
            self._elapsed_time = self._curr_time - self._prev_time
            self._prev_time = self._curr_time
            self._delta += self._elapsed_time
            self._lag += self._elapsed_time

            self._events()

            while self._lag > self._time_per_frame:
                self._update()
                self._fps_counter += 1
                self._lag -= self._time_per_frame

            self._draw()

            # fps counter
            if self._delta > 1:
                print(self._fps_counter)
                self._fps_counter = 0
                self._delta = 0

    def new_game(self):
        # reset all the game variables
        self._running = False
        self._game_over = False
        self._start = False
        self._bird = Bird(self)
        self._pipe = Pipe(self)
        self._ground = Ground(self)
        self._background = Background(self)

        # reset score
        self._score_tracker.reset()

        # run the game once again
        self._run()

    def get_screen(self):
        return self._screen

    def get_pipe(self):
        return self._pipe

    def get_ground(self):
        return self._ground

    def get_bird(self):
        return self._bird

    def get_background(self):
        return self._background

    def get_sprite_sheet(self):
        return self._sprite_sheet

    def get_frame_elapsed_time(self):
        return self._time_per_frame

    def get_fps(self):
        return self._fps

    def get_fps_counter(self):
        return self._fps_counter

    def get_collision_detection(self):
        return self._collision_detection

    def is_over(self):
        return self._game_over

    def get_score(self):
        return self._score_tracker.get_score()

    def get_scale(self):
        return self._sprite_sheet_scale

    def started(self):
        return self._start
if __name__ == "__main__":
    Game().new_game()
