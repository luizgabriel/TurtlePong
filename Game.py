import time
from turtle import *
from scenes.PongScene import PongScene

class Game:

    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.tracer(0, 0)
        self.screen.title("Pong Game")
        self.screen.setup(800, 600)
        self.scene = PongScene(self)

    def width(self):
        return self.screen.window_width()

    def height(self):
        return self.screen.window_height()

    def main_loop(self):
        start_time = time.time()
        delta = 0
        while self.running:
            self.screen.listen()
            self.scene.update(delta)
            self.screen.update()
            cur_time = time.time()
            delta = cur_time - start_time
            start_time = cur_time