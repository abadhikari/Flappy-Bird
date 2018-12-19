import pygame

from misc import spritesheet

vec = pygame.math.Vector2

PLAYER_GRAV = 0.6
PLAYER_ACC = 0.5

class player():
    def __init__(self,game):
        self.game = game

        # spritesheet
        self.spritesheet = spritesheet.SpriteSheet("res/bird.png")
        self.bird_animations = []
        self._fill_bird_animations()
        self.curr_bird = pygame.transform.scale(self.bird_animations[0],(80,80))
        self.curr_index = 0

        #resize the bird images
        for f in range(len(self.bird_animations)):
            self.bird_animations[f] = pygame.transform.scale(self.bird_animations[f], (80, 80))

        # player postition variables
        self.pos = vec(100, 200)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def draw(self):
        size_diff = self.curr_bird.get_rect().size[0] - 80
        xPos = self.game.player.pos.x - (size_diff / 2)
        yPos = self.game.player.pos.y - (size_diff / 2)
        self.game.screen.blit(self.curr_bird, (xPos, yPos))

    def jump(self):
        self.vel.y = 0
        self.vel.y -= 11.5

    def update(self):
        if self.game.start_game:
            self.acc = vec(0, PLAYER_GRAV)
            # equations of motion
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc

        # keeps the bird on the screen when it touches the ground
        if self.pos.y >= 450:
            self.pos.y = 450

        if not self.game.gameOver:
            #flapping animation
            if self.game.timer % 6 == 0:
                self.curr_bird = self.bird_animations[self.curr_index]
                self.curr_index += 1
                if self.curr_index > 3:
                    self.curr_index = 0

            # rotation animation
            if self.game.timer % 6 == 0:
                self.rotation()

    def rotation(self):
        # controls how the bird rotates while it is in the air depending on the velocity
        curr_y_vec = self.game.player.vel.y
        angle = (-(6 * min(curr_y_vec,15)) if curr_y_vec >= 0 else 30)
        self.curr_bird = pygame.transform.rotate(self.curr_bird, angle)

    def _fill_bird_animations(self):
        # fills the list with the possible bird flapping positions
        sprite_size = self.spritesheet.sprite_sheet.get_rect().size
        length = 28
        for f in range(3):
            self.bird_animations.append(self.spritesheet.get_image(f * length, sprite_size[1] - length, length, length))
        self.bird_animations.append(self.spritesheet.get_image(length, sprite_size[1] - length, length, length))
