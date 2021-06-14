import herd
from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()


    def run_game(self):
        # """Main method where game happens line by line"""
        # Display welcome
        self.display_welcome()
        # Start Battle
        self.battle()
        # Pick a Robot
        # Pick dinosaur to attack
        #



        # Display Winners
        pass


    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs")


    def battle(self):
        battle_start = input("Are your ready to start? (y/n)")
        if battle_start.lower() == "y":
            print(f"{self.fleet.robots[0].name} attacks {self.herd.dinosaurs[0].type}")
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            attack_again = input("Would you like to attack again? (y/n)")
            if self.herd.dinosaurs[0].health > 0:
                print(attack_again)
                if attack_again.lower() == "y":
                    self.fleet.robots[0].attack(self.herd.dinosaurs[0])
                elif attack_again.lower() == "n":
                    print(f"{self.fleet.robots[0].name} has decided not to fight {self.herd.dinosaurs[0].type}. Game Over.")
        elif battle_start.lower() == "n":
            print("Come back when you are ready.")


        # print(herd.dinosaurs[0].health)
        # print(fleet.robots[0].name)



    def dinosaur_turn(dinosaur):
        pass


    def robot_turn(robot):
        pass


    def show_dinosaur_opponent_options(self):
        pass


    def show_robot_opponent_options(self):
        pass


    def display_winners(self):
        pass
