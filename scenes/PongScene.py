from entites.Ball import Ball
from entites.Field import Field
from entites.Player import Player
from scenes.Scene import Scene

class PongScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.game.screen.bgcolor(0, 0, 0)

        self.createField()
        self.createBall()
        self.createPlayer1()
        self.createPlayer2()

    def update(self, delta):
        #player 1
        if self.ball.x() < self.player1.x() + self.player1.height / 2:
            if self.ball.y() <  self.player1.y() + self.player1.width/2 and self.ball.y() > self.player1.y() - self.player1.width/2:
                self.ball.hit(self.player1)

        #player 2
        if self.ball.x() > self.player2.x() - self.player2.height / 2:
            if self.ball.y() <  self.player2.y() + self.player2.width/2 and self.ball.y() > self.player2.y() - self.player2.width/2:
                self.ball.hit(self.player2)

        super().update(delta)

    def createBall(self):
        self.ball = Ball(self)
        self.add_entity(self.ball)

    def createPlayer1(self):
        self.player1 = Player(self, 1)
        self.add_entity(self.player1)

    def createPlayer2(self):
        self.player2 = Player(self, 2)
        self.add_entity(self.player2)

    def createField(self):
        field = Field(self)
        self.add_entity(field)