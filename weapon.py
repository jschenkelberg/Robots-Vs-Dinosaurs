class Weapon:

    def __init__(self):
        self.weapon = "Ray Gun"
        self.attack_power = 10

    def equip_weapon(self):
        self.weapon = input("Do you want to equip a weapon? Y/N")
        self.attack_power = 20
        print("Ray Gun is equipped.")
