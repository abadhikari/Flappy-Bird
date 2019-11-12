class CollisionDetection:
    """
    Accounts for the collision detection in FlappyBird
    """
    def __init__(self, game):
        self._game = game
        self._bird_hit_box = None
        self._bird_hit_box_pos = None
        self._init_bird_hit_box()

    def check_pipe_collision(self):
        # need to add accurate box on bird
        self._init_bird_hit_box()
        pipe_width, pipe_height = self._game.get_pipe().get_size(self._game.get_pipe().get_up_pipe())
        for pos_list in self._game.get_pipe().get_pos_lists():
            for pos in pos_list:
                # check to see if any of the four vertices of the hitbox are within a pipe
                if (self._bird_hit_box_pos.x > pos.x and self._bird_hit_box_pos.x < pos.x + pipe_width and
                        self._bird_hit_box_pos.y > pos.y and self._bird_hit_box_pos.y < pos.y + pipe_height):
                    return True
                if (self._bird_hit_box_pos.x + self._bird_hit_box[0] > pos.x and self._bird_hit_box_pos.x + self._bird_hit_box[0] < pos.x + pipe_width and
                        self._bird_hit_box_pos.y > pos.y and self._bird_hit_box_pos.y < pos.y + pipe_height):
                    return True
                if (self._bird_hit_box_pos.x > pos.x and self._bird_hit_box_pos.x < pos.x + pipe_width and
                        self._bird_hit_box_pos.y + self._bird_hit_box[1] > pos.y and self._bird_hit_box_pos.y + self._bird_hit_box[1] < pos.y + pipe_height):
                    return True
                if (self._bird_hit_box_pos.x + self._bird_hit_box[0] > pos.x and self._bird_hit_box_pos.x + self._bird_hit_box[0] < pos.x + pipe_width and
                        self._bird_hit_box_pos.y + self._bird_hit_box[1] > pos.y and self._bird_hit_box_pos.y + self._bird_hit_box[1] < pos.y + pipe_height):
                    return True
        return False

    def _init_bird_hit_box(self):
        # initializes the hit box of the bird in flappy bird
        bird_dim = self.get_size(self._game.get_bird().get_curr_sprite())
        self._bird_hit_box = (bird_dim[0] * .389, bird_dim[1] * .32)
        bird_pos = self._game.get_bird().get_pos()
        self._bird_hit_box_pos = self._game.get_bird().vec(bird_pos.x + bird_dim[0] * .214, bird_pos.y + bird_dim[1] * .309)

    def check_ground_collision(self):
        ground_y = self._game.get_ground().get_pos_list()[0].y
        if self._bird_hit_box[1] + self._bird_hit_box_pos.y >= ground_y:
            return True
        return False

    def check_collision(self):
        return self.check_pipe_collision() or self.check_ground_collision()

    def get_bird_hit_box_pos(self):
        return self._bird_hit_box_pos

    def get_size(self, img):
        return self._game.get_bird().get_size(img)