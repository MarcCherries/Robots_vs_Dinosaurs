from Weapon import Weapon


class Robots:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon()
        
    def attack(self, dinosaur):
        pass