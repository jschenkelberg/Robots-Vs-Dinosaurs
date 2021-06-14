from robot import Robot


class Dinosaur:

    def __init__(self, type):
        self.type = type
        self.energy = 100
        self.attack_power = 30
        self.health = 100

    def attack_robot(self, robot):
        dinosaur_attack = Robot.health - Dinosaur.attack_power
        if Robot.health > 0:
            print({Dinosaur.type}, "attacks", {Robot.name}, ".", {Robot.name}, "has", {Robot.health}, "left.")
        else:
            print({Dinosaur.type}, "has eliminated", {Robot.name})
        pass
