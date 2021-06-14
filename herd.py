from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_1 = Dinosaur("T-Rex")
        dinosaur_2 = Dinosaur('Velociraptor')
        dinosaur_3 = Dinosaur("Allosaurus")
        self.dinosaurs.append(dinosaur_1)
        self.dinosaurs.append(dinosaur_2)
        self.dinosaurs.append(dinosaur_3)
