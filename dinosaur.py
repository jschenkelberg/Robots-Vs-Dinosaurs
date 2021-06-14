

class Dinosaur:

    def __init__(self, type):
        self.type = type
        self.energy = 100
        self.attack_power = 30
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power
        if robot.health > 0:
            print(f"{self.type} attacks {robot.name}. {robot.name} has {robot.health} left.")
        else:
            print(f"{self.type} has eliminated {robot.name}.")

