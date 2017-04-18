from entites.Entity import Entity


class Field(Entity):

    def start(self):
        self.turtle.hideturtle()
        self.turtle.pencolor("white")
        self.turtle.pensize(2)
        self.draw()

    def update(self, delta):
        pass

    def draw(self):
        h = self.scene.game.height()
        self.turtle.pendown()
        self.turtle.goto(0, -h/2)
        self.turtle.left(90)
        self.turtle.forward(h)
        self.turtle.penup()