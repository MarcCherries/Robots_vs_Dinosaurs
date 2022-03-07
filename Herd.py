from Dinosaur import Dinosaur
from Weapon import Weapon

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.move = ()
        
        

    def create_herd(self):
            dino01 = Dinosaur('Barney')
            dino02 = Dinosaur('Rex')
            dino03 = Dinosaur('Ptera')
            self.dinosaurs.append(dino01)
            self.dinosaurs.append(dino02)
            self.dinosaurs.append(dino03)

    def create_repertoire(self):
        move_01 = Weapon('Bull Rush', 20, 10)
        move_02 = Weapon('Chomp Stomp', 20, 10)
        move_03 = Weapon('Pteradactyl Swoop', 20, 10)
        self.move = (move_01, move_02, move_03)
       



       