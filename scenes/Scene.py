class Scene:

    def __init__(self, game):
        self.entities = []
        self.game = game

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.start()

    def update(self):
        for s in self.entities:
            s.update()