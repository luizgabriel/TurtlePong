from entites.Ball import Ball
from entites.Player import Player
from scenes.Scene import Scene

class PongScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.game.screen.bgcolor(0, 0, 0)

        self.createBall()
        self.createPlayer1()

    def createBall(self):
        self.ball = Ball(self)
        self.add_entity(self.ball)

    def createPlayer1(self):
        self.player1 = Player(self, 1)
        self.add_entity(self.player1)