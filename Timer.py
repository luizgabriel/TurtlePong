class Timer:

    def __init__(self, stopTime):
        self.totalTime = stopTime
        self.timer = -1

    def update(self, delta):
        if self.is_on():
            if self.has_finished():
                self.stop()
            else:
                self.icr_timer(delta)

    def is_off(self):
        return self.timer == -1

    def is_on(self):
        return self.timer != -1

    def has_finished(self):
        return self.timer >= self.totalTime

    def icr_timer(self, delta):
        self.timer += delta

    def start(self):
        self.timer = 0

    def stop(self):
        self.timer = -1