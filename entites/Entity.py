from turtle import Turtle

class Entity:

    def __init__(self, scene):
        self.scene = scene
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.speed(0)

