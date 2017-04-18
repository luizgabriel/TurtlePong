import time
from random import Random
from Timer import Timer
from entites.Entity import Entity

class Ball(Entity):

    def __init__(self, scene, n, total):
        super().__init__(scene)
        self.vel = 230
        self.n = n
        self.total = total
        self.stopTimer = Timer(2)

    def start(self):
        self.turtle.color("white")
        self.turtle.shape("circle")
        self.reset()

    def reset(self):
        self.stopTimer.start()
        self.turtle.goto(0, (self.n * 20) - ((self.total * 20) / 2))
        self.launch()

    def launch(self):
        random = Random(time.time())
        right = random.randint(0, 200) > 100 == 0

        if right:
            self.turtle.right(random.randint(-45, 45))
        else:
            self.turtle.left(180 + random.randint(-45, 45))

    def x(self):
        return self.turtle.xcor()

    def y(self):
        return self.turtle.ycor()

    def hit(self, player):
        a = self.turtle.heading()
        self.vel += self.vel * 0.01
        r = Random(self.vel)
        self.turtle.setheading((180 - a) + r.randint(0, 10))

    def update(self, delta):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        w = self.scene.game.width()
        h = self.scene.game.height()
        a = self.turtle.heading()

        self.stopTimer.update(delta)

        if x > w/2 or x < -w/2:
            self.reset()

        if y >= h/2:
            self.turtle.setheading(-a)

        if y <= -h/2:
            self.turtle.setheading(360 - a)

        if self.stopTimer.is_off():
            self.turtle.forward(self.vel * delta)


