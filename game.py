import pygame

import ground
import pipe
import player
from misc import button


class game():

    def __init__(self, width=500, height=580):
        pygame.init()

        # screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Flappy Bird")

        # game variables
        self.clock = pygame.time.Clock()
        self.start_game = False
        self.gameOver = False
        self.running = False
        self.timer = 0
        self.high_score = 0
        self.score = 0

        # game elements
        self.background = self.load_image("res/background.png")
        self.player = player.player(self)
        self.pipe = pipe.pipe(self)
        self.ground = ground.ground(self)

        #button
        self.restart_button = button.button(self.load_image("res/restart.png"), self.width // 2 - 68, self.height // 2 - 28, 132, 45)
        self.game_over_button = button.button(self.player.spritesheet.get_image(390, 60, 105, 25), self.width // 2 - 78, self.height // 2 - 110, 163, 38)
        self.mouse_pos = None

    def update(self):
        self.player.update()
        if not self.gameOver and self.start_game:
            self.pipe.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.pipe.draw()
        self.ground.draw()
        self.player.draw()

        # render the score and high score
        my_font = pygame.font.SysFont("monospace", 16)
        high_score_text = my_font.render("HighScore: {0}".format(self.high_score), 1, (0, 0, 0))
        score_text = my_font.render("Score: {0}".format(self.score), 1, (0, 0, 0))

        # score on the top lefthand side if the game isn't over, else, place it in the middle of the screen
        score_x,score_y = (5,10) if not self.gameOver else (self.width//2-55,self.height//2-75)

        self.screen.blit(high_score_text, (score_x, score_y))
        self.screen.blit(score_text, (score_x + 13, score_y + 20))

        if self.gameOver:
            self.game_over_button.draw(self.screen)
            self.restart_button.draw(self.screen)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.gameOver:
                        self.player.jump()
                    if not self.start_game:
                        self.start_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                if self.restart_button.isOver(self.mouse_pos):
                    self.new()

    def load_image(self, string):
        return pygame.image.load(string).convert_alpha()

    def new(self):
        # re-initailize game variables
        self.gameOver = False
        self.start_game = False
        self.running = False
        self.clock = pygame.time.Clock()
        self.player = player.player(self)
        self.score = 0
        self.pipe.reset_pipes()

        self.run()

    def run(self):
        self.running = True
        while self.running:
            self.update()
            # check for events
            self.events()

            #check score
            if self.score > self.high_score:
                self.high_score = self.score

            #check for collisions
            if not self.gameOver and self.pipe.checkCollision():
                self.gameOver = True

            self.draw()
            self.timer += 1
            self.clock.tick(60)

