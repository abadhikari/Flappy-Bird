from misc.deque import Deque
import random
import pygame


class Pipe:
    def __init__(self, game):
        self._game = game
        self._pipe = pygame.transform.scale(self._game.player._spritesheet.crop(84, 320, 28, 160), (80, 450))
        self._flipped_pipe = pygame.transform.flip(self._pipe, False, True)

        # pipe variables
        self.b_pipes = Deque()
        self.t_pipes = Deque()
        self.b_pipes_pos = Deque()
        self.t_pipes_pos = Deque()

        # fill pipes
        for i in range(3):
            self.make_pipe()

    def update(self):
        # only move the pipes if the game is still going on
        if self._game.start_game:
            # pipes
            b_head, t_head, b_pos_head, t_pos_head = self.b_pipes._head, self.t_pipes._head, self.b_pipes_pos._head, self.t_pipes_pos._head
            for i in range(len(self.b_pipes)):
                if b_pos_head.data[0] < -80:
                    self.make_pipe()
                    self.remove_first_pipes()

                if b_pos_head.data[0] - 15 in [self._game.player._pos.x - y for y in range(7)]:
                    self._game.score += 1

                b_pos_head.data[0] -= 3.5
                t_pos_head.data[0] -= 3.5

                b_head, t_head, b_pos_head, t_pos_head = b_head.link, t_head.link, b_pos_head.link, t_pos_head.link

    def draw(self):
        b_head, t_head, b_pos_head, t_pos_head = self.b_pipes._head, self.t_pipes._head, self.b_pipes_pos._head, self.t_pipes_pos._head
        for i in range(len(self.b_pipes)):
            self._game.screen.blit(b_head.data, b_pos_head.data)
            self._game.screen.blit(t_head.data, t_pos_head.data)
            b_head, t_head, b_pos_head, t_pos_head = b_head.link, t_head.link, b_pos_head.link,t_pos_head.link

    def remove_first_pipes(self):
        self.b_pipes.remove_first()
        self.t_pipes.remove_first()
        self.b_pipes_pos.remove_first()
        self.t_pipes_pos.remove_first()

    def reset_pipes(self):
        self.__init__(self._game)

    def checkCollision(self):
        # only used rectangles for collision detection so had to hard code several values
        player_rect = pygame.Rect(self._game.player._pos.x + 22, self._game.player._pos.y + 25, 27, 25)
        t_pipe_rect = pygame.Rect(self.t_pipes.peek_first().get_rect())
        t_pipe_rect.left, t_pipe_rect.top = self.t_pipes_pos.peek_first()[0], self.t_pipes_pos.peek_first()[1] - 8
        b_pipe_rect = pygame.Rect(self.b_pipes.peek_first().get_rect())
        b_pipe_rect.left, b_pipe_rect.top = self.b_pipes_pos.peek_first()[0], self.b_pipes_pos.peek_first()[1] + 8

        # if bird collides with a pipe
        if player_rect.colliderect(t_pipe_rect) or player_rect.colliderect(b_pipe_rect):
            return True

        # if bird hits the ground or goes too far above the screen
        if self._game.player._pos.y >= 450 or self._game.player._pos.y < -100:
            return True

        return False

    def make_pipe(self):
        space_between_pipes = 140
        pipe_size = self._pipe.get_rect().size
        top_pos = [250]

        if len(self.b_pipes) != 0:
            top_pos = self.t_pipes_pos.peek_last()

        random_number = random.randrange(100, 260)
        top_pipe_pos = [top_pos[0] + 250, random_number - pipe_size[1]]
        bottom_pipe_pos = [top_pos[0] + 250, random_number + space_between_pipes]

        self.b_pipes.add_last(self._pipe)
        self.t_pipes.add_last(self._flipped_pipe)
        self.b_pipes_pos.add_last(bottom_pipe_pos)
        self.t_pipes_pos.add_last(top_pipe_pos)



