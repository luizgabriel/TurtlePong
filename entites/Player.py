from turtle import Shape
from entites.Entity import Entity

class Player(Entity):

    def __init__(self, scene, n):
        super().__init__(scene)
        self.vel = 320
        self.n = n
        self.width = 100
        self.height = 20
        self.cur_y = 0
        self.up = False
        self.down = False
        self.up_keys = { 1:["W", "w"] , 2: ["Up"]}
        self.down_keys = { 1:["S", "s"] , 2: ["Down"]}
        if self.n == 1:
            self.start_x = -self.scene.game.width() / 2 + 10
        else:
            self.start_x = self.scene.game.width() / 2 - 20

    def initialize_controllers(self):
        for key in self.up_keys[self.n]:
            self.scene.game.screen.onkeypress(self.on_press_up, key)
            self.scene.game.screen.onkeyrelease(self.on_release_up, key)

        for key in self.down_keys[self.n]:
            self.scene.game.screen.onkeypress(self.on_press_down, key)
            self.scene.game.screen.onkeyrelease(self.on_release_down, key)

    def x(self):
        return self.start_x

    def y(self):
        return self.cur_y

    def on_press_up(self):
        self.up = True

    def on_release_up(self):
        self.up = False

    def on_press_down(self):
        self.down = True

    def on_release_down(self):
        self.down = False

    def start(self):
        self.turtle.color("white")
        self.turtle.shape(self.init_shape())
        self.initialize_controllers()

    def init_shape(self):
        shape = "player" + str(self.n)
        p0 = (self.width/2, -self.height/2)
        p1 = (self.width/2, self.height/2)
        p2 = (-self.width/2, self.height/2)
        p3 = (-self.width/2, -self.height/2)
        self.scene.game.screen.register_shape("player" + str(self.n), (p0, p1, p2, p3))
        return shape

    def update(self, delta):
        if self.up: self.move_up(delta)
        if self.down: self.move_down(delta)

        self.turtle.goto(self.start_x, self.cur_y)

    def move_up(self, delta):
        if self.cur_y + self.width//2 + 2 <= self.scene.game.height()//2:
            self.cur_y += self.vel * delta

    def move_down(self, delta):
        if self.cur_y - self.width//2 - 2 > -self.scene.game.height()//2:
            self.cur_y -= self.vel * delta
