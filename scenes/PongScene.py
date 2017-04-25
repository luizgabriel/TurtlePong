from entites.Ball import Ball
from entites.Field import Field
from entites.Player import Player
from scenes.Scene import Scene


class PongScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game.screen.bgcolor(0, 0, 0)
        self.balls_count = 1
        self.balls = []

        for b in range(self.balls_count):
            self.createBall(b)

        self.createField()
        self.createPlayer1()
        self.createPlayer2()

    def update(self, delta):
        for ball in self.balls:

            # player 1
            if ball.x() < self.player1.x() + self.player1.height / 2:
                if self.player1.y() + self.player1.width // 2 > ball.y() > self.player1.y() - self.player1.width // 2:
                    ball.hit(self.player1)

            # player 2
            if ball.x() > self.player2.x() - self.player2.height / 2:
                if self.player2.y() + self.player2.width // 2 > ball.y() > self.player2.y() - self.player2.width // 2:
                    ball.hit(self.player2)

        super().update(delta)

    def createBall(self, n):
        ball = Ball(self, n, self.balls_count)
        self.balls.append(ball)
        self.add_entity(ball)

    def createPlayer1(self):
        self.player1 = Player(self, 1)
        self.add_entity(self.player1)

    def createPlayer2(self):
        self.player2 = Player(self, 2)
        self.add_entity(self.player2)

    def createField(self):
        field = Field(self)
        self.add_entity(field)
