import time
from random import Random
from entites.Entity import Entity

class Ball(Entity):

    def __init__(self, scene):
        super().__init__(scene)
        self.vel = 0.08
        self.stopTime = 2500
        self.stopTimer = -1

    def start(self):
        self.turtle.color("white")
        self.turtle.shape("circle")

        self.launch()

    def launch(self):
        random = Random(time.time())
        right = random.randint(0, 200) > 100 == 0

        if right:
            self.turtle.right(random.randint(-45, 45))
        else:
            self.turtle.left(180 + random.randint(-45, 45))

    def update(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        w = self.scene.game.width()
        h = self.scene.game.height()
        a = self.turtle.heading()

        if x > w or x < -w:
            self.launch()
            self.turtle.goto(0, 0)
            self.stopTimer = 0


        if self.stopTimer != -1:
            if self.stopTimer >= self.stopTime:
                self.stopTimer = -1
            else:
                self.stopTimer += 1

        if y >= h/2:
            self.turtle.setheading(-a)

        if y <= -h/2:
            self.turtle.setheading(360 - a)

        if self.stopTimer == -1:
            self.turtle.forward(self.vel)


