class Ground:
    def __init__(self, game):
        self._game = game
        self._ground_sprite = self._game.player._spritesheet.load_image("res/ground.png")
        self._ground_x = 0

    def draw(self):
        for f in range(3):
            self._game.screen.blit(self._ground_sprite, (self._ground_x + (480 * f), 500))
        if not self._game.gameOver:
            self._ground_x -= 3.5
            if self._ground_x < -500:
                self._ground_x = 0

