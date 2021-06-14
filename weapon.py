import robot


class Weapon:

    def __init__(self):
        self.weapon = "Ray Gun"
        self.attack_power = 10

    def equip_weapon(self):
        self.weapon = input("Do you want to equip a weapon? Y/N")
        if self.weapon: 'Y'
        equipped_weapon = self.attack_power + robot.power_level
        print("Ray Gun is equipped.")
        return equipped_weapon


