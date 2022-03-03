
from imaplib import ParseFlags
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robots import Robots

class Battlefield:
    def __init__(self):
       self.name = "Field of Screams"
       self.herd = Herd()
       self.fleet = Fleet()
        

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle(self)
        Battlefield.dino_turn(self)
       
        

    def display_welcome(self):
        print('Welcome to Robots Vs Dinosaurs!  Please wait while your fighters are spawned \n')
       

    def battle(self):
        pass
        

    
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass