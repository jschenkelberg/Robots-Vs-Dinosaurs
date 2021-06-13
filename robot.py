from weapon import Weapon


class Robot:

    def __init__(self):
        self.name = ""
        self.power_level = 10
        self.health = 100
        self.weapon = bool

    def set_robot_name(self):
        self.name = input("Enter Robot Name:")
        print("Robot name: ", self.name)



