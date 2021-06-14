from weapon import Weapon
from dinosaur import Dinosaur

class Robot:

    def __init__(self):
        self.name = ""
        self.power_level = 10
        self.health = 100
        self.weapon = bool

    def set_robot_name(self):
        self.name = input("Enter Robot Name:")
        print("Robot name: ", self.name)

    def attack_dinosaur(self, dinosaur):
        robot_attack = robot.attack_power - dinosaur.health
        if dinosaur.health > 0:
            print({robot.name}, "attacks", {dinosaur.name}, ".", {dinosaur.name},"has",{dinosuar.health},"left.")
        else:
            print({robot.name}, "has eliminated",{dinosaur.name})