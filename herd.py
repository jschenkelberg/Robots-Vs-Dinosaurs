from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.herd = []

    def create_herd(self, dinosaur):
        self.herd.append(dinosaur())
        pass