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
        # dinosaur_selection_result = self.dinosaur_fighter_selection()
        # robot_selection_result = self.robot_fighter_selection()
        # self.dinosaur_turn(dinosaur_selection_result)
        # self.robot_turn(robot_selection_result)
        # self.fight()
        # Pick a Robot
        # Pick dinosaur to attack
        #



        # Display Winners
        pass


    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        battle_start = input("Are your ready to start? (y/n)")
        if battle_start.lower() == "y":
            # print(f"{self.fleet.robots[0].name} attacks {self.herd.dinosaurs[0].type}")
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            print(f"{self.herd.dinosaurs[0].type} makes a counter attack!")
            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            attack_again = input("Would you like the robot to attack again? (y/n)")
            if self.herd.dinosaurs[0].health > 0:
                print(attack_again)
            if attack_again.lower() == "y":
                self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            elif attack_again.lower() == "n":
                print(f"{self.fleet.robots[0].name} has decided not to fight {self.herd.dinosaurs[0].type}. Robots have retreated. Game Over.")
            print(f"Next Fight! {self.fleet.robots[1].name} vs. {self.herd.dinosaurs[1].type}")
            self.fleet.robots[1].attack(self.herd.dinosaurs[1])
            print(f"{self.herd.dinosaurs[1].type}'s turn")
            self.herd.dinosaurs[1].attack(self.fleet.robots[1])
            attack_again = input("Would you like to attack again? (y/n)")
            if self.herd.dinosaurs[1].health > 0:
                print(attack_again)
            if attack_again.lower() == "y":
                self.fleet.robots[1].attack(self.herd.dinosaurs[0])
            elif attack_again.lower() == "n":
                print(f"{self.fleet.robots[1].name} has decided not to fight {self.herd.dinosaurs[1].type}. Robots have retreated. Game Over.")
            print(f"Next Fight! {self.fleet.robots[2].name} vs. {self.herd.dinosaurs[2].type}")
            self.fleet.robots[2].attack(self.herd.dinosaurs[2])
            print(f"{self.herd.dinosaurs[2].type}'s turn")
            self.herd.dinosaurs[2].attack(self.fleet.robots[2])
            attack_again = input("Would you like to attack again? (y/n)")
            if self.herd.dinosaurs[2].health > 0:
                print(attack_again)
            if attack_again.lower() == "y":
                self.fleet.robots[2].attack(self.herd.dinosaurs[2])
            elif attack_again.lower() == "n":
                print(f"{self.fleet.robots[2].name} has decided not to fight {self.herd.dinosaurs[2].type}. Robots have retreated! Game Over.")
            print ("Robots emerge victorious again!!!")
        elif battle_start.lower() == "n":
            print("Come back when you are ready.")


    # def dinosaur_fighter_selection(self):
    #     battle_start = input("Are your ready to pick your fighters? (y/n)")
    #     dinosaur_selection = input("Pick a dinosaur. \n 1-T-Rex \n 2-Velociraptor \n 3-Allosaurus \n")
    #     if battle_start.lower() == "y":
    #         if dinosaur_selection.lower() == "1":
    #             dinosaur_selection_answer = self.herd.dinosaurs[0].type
    #             print(f"You have chosen {dinosaur_selection_answer}")
    #             return dinosaur_selection_answer
    #         elif dinosaur_selection.lower() == "2":
    #             dinosaur_selection_answer = self.herd.dinosaurs[1].type
    #             print(f"You have chosen {dinosaur_selection_answer}")
    #             return dinosaur_selection_answer
    #         elif dinosaur_selection.lower() == "3":
    #             dinosaur_selection_answer = self.herd.dinosaurs[2].type
    #             print(f"You have chosen {dinosaur_selection_answer}")
    #             return dinosaur_selection_answer
    #         else:
    #             print("That is not a valid selection. Please restart the program.")
    #     elif battle_start.lower() == "n":
    #         print("Come back when you are ready.")
    #
    # def robot_fighter_selection(self):
    #     robot_selection = input("Pick a robot. \n 1-Optimus Prime \n 2-Megatron \n 3-Ultron \n")
    #     if robot_selection.lower() == "1":
    #         robot_selection_answer = self.fleet.robots[0].name
    #         print(f"You have chosen {robot_selection_answer}")
    #         return robot_selection_answer
    #     elif robot_selection.lower() == "2":
    #         robot_selection_answer = self.fleet.robots[1].name
    #         print(f"You have chosen {robot_selection_answer}")
    #         return robot_selection_answer
    #     elif robot_selection.lower() == "3":
    #         robot_selection_answer = self.fleet.robots[2].name
    #         print(f"You have chosen {robot_selection_answer}")
    #         return robot_selection_answer()
    #     else:
    #         # print("That is not a valid selection. Please restart the program.")
    #     #
        #
        # battle_start = input("Are your ready to start? (y/n)")
        # if battle_start.lower() == "y":
        #     print(f"{self.fleet.robots[0].name} attacks {self.herd.dinosaurs[0].type}")
        #     self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        #     attack_again = input("Would you like to attack again? (y/n)")
        #     if self.herd.dinosaurs[0].health > 0:
        #         print(attack_again)
        #         if attack_again.lower() == "y":
        #             self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        #         elif attack_again.lower() == "n":
        #             print(f"{self.fleet.robots[0].name} has decided not to fight {self.herd.dinosaurs[0].type}. Game Over.")
        # elif battle_start.lower() == "n":
        #     print("Come back when you are ready.")


        # print(herd.dinosaurs[0].health)
        # print(fleet.robots[0].name)

    # def dinosaur_turn(dinosaur, selection):
    #     print(f"Let the battle begin! Dinosaur Combatant: {selection}.")

        #     self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        #     attack_again = input("Would you like to attack again? (y/n)")
        #     if self.herd.dinosaurs[0].health > 0:
        #         print(attack_again)
        #         if attack_again.lower() == "y":
        #             self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        #         elif attack_again.lower() == "n":
        #             print(f"{self.fleet.robots[0].name} has decided not to fight {self.herd.dinosaurs[0].type}. Game Over.")
        # elif battle_start.lower() == "n":
        #     print("Come back when you are ready.")


    # def robot_turn(robot, selection):
    #     print(f"Let the battle begin! Dinosaur Combatant: {selection}.")


    # def fight(self):
    #     self.dinosaur_turn.attack(self.robot_turn())
    #     attack_again = input("Would you like to attack again? (y/n)")
    #     if self.dinosaur_fighter_selection.health > 0:
    #         print(attack_again)
    #     if attack_again.lower() == "y":
    #         self.fleet.robots[0].attack(self.herd.dinosaurs[0])
    #     elif attack_again.lower() == "n":
    #         print(f"{self.dinosaur_fighter_selection()} has decided not to fight {self.robot_fighter_selection()} Game Over.")


    def show_dinosaur_opponent_options(self):
        pass


    def show_robot_opponent_options(self):
        pass


    def display_winners(self):
        pass
