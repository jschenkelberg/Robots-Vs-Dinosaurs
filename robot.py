from weapon import Weapon

from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 20
        self.health = 100
        self.weapon = Weapon()


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        if dinosaur.health > 0:
            print(f"{self.name} attacks {dinosaur.type}. {dinosaur.type} has {dinosaur.health} health left.")
        else:
            print(f"{self.name} has eliminated {dinosaur.type}")


