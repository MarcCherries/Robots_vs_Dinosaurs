from Weapon import Weapon


class Robots:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Laser Gun", 15)
        
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        
