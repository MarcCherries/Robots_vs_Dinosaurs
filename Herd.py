from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
            dino01 = Dinosaur('Barney', 10)
            dino02 = Dinosaur('Rex', 15)
            dino03 = Dinosaur('Ptera', 20)
            self.dinosaurs.append(dino01)
            self.dinosaurs.append(dino02)
            self.dinosaurs.append(dino03)

       