import Robot


class Dinosaur:

    def __init__(self):
        self.type = ""
        self.energy = 100
        self.attack_power = 30
        self.health = 100

    def set_dinosaur_type(self):
        self.type = input("What type of dinosaur?")
        print("Dinosaur Type: ", self.type)

    def attack_robot(self, robot):
        dinosaur_attack = robot.health - dinosaur.attack_power
        if robot.health > 0:
            print({dinosaur.type}, "attacks", {robot.name}, ".", {robot.name}, "has", {robot.health}, "left.")
        else:
            print({dinosaur.type}, "has eliminated", {robot.name})

