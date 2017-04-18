from turtle import Shape
from entites.Entity import Entity

class Player(Entity):

    def __init__(self, scene, n):
        super().__init__(scene)
        self.vel = 0.1
        self.n = n
        self.width = 100
        self.height = 20
        self.cur_y = 0
        if self.n == 1:
            self.start_x = -self.scene.game.width()/2 + 5
        else:
            self.start_x = self.scene.game.width() / 2 - 5

    def start(self):
        self.turtle.color("white")
        self.turtle.shape(self.init_shape())

    def init_shape(self):
        shape = "player" + str(self.n)
        p0 = (self.width/2, -self.height/2)
        p1 = (self.width/2, self.height/2)
        p2 = (-self.width/2, self.height/2)
        p3 = (-self.width/2, -self.height/2)
        self.scene.game.screen.register_shape("player" + str(self.n), (p0, p1, p2, p3))
        return shape

    def pos_left(self):
        self.turtle.goto(-self.scene.game.width()/2 + 5, -20)

    def pos_right(self):
        self.turtle.goto(self.scene.game.width() / 2 - 5, -20)

    def update(self):
        if self.n == 1:
            self.pos_left()
        else:
            self.pos_right()
        self.turtle.goto(self.start_x, self.cur_y)

    def move_up(self):
        if self.cur_y + self.width//2 + 2 <= self.scene.game.height()//2:
            self.cur_y += self.vel

    def move_down(self):
        if self.cur_y - self.width//2 - 2 > -self.scene.game.height()//2:
            self.cur_y -= self.vel
