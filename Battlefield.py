
import random
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robots import Robots

class Battlefield:
    def __init__(self):
       self.name = "Field of Screams"
       self.herd = Herd()
       self.fleet = Fleet()
       self.herd.create_herd()
       self.fleet.create_fleet()
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        
       
        

    def display_welcome(self):
        print('Welcome to Robots Vs Dinosaurs!  Please wait while your fighters are spawned \n')
       

    def battle(self):
        h_or_t = random.randint(0,1)
        while self.fleet.robots[0].health  > 0 and self.herd.dinosaurs[0].health > 0:
            if h_or_t == 0:
                print('Heads! Robots go first! \n')
                self.robo_turn()
            else:
                print ('Tails! Dinosaurs go first! \n')
                self.dino_turn()
        else:
            self.display_winners()
    
    def dino_turn(self):
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])
        print(self.fleet.robots[0].health)
       

    def robo_turn(self):
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        print(self.herd.dinosaurs[0].health)
       
    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        print ('Winners!')