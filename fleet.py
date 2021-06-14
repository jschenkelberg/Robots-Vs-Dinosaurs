from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot("Optimus Prime")
        robot_2 = Robot("Megatron")
        robot_3 = Robot("Ultron")
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)

