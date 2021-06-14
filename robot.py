from weapon import Weapon


# from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 10
        self.health = 100
        self.weapon = Weapon


    def attack_dinosaur(self, dinosaur):
        robot_attack = robot.attack_power - dinosaur.health
        if dinosaur.health > 0:
            print({robot.name}, "attacks", {dinosaur.name}, ".", {dinosaur.name},"has",{dinosuar.health},"left.")
        else:
            print({robot.name}, "has eliminated",{dinosaur.name})
        pass