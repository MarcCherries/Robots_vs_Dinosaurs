from Weapon import Weapon

class Robots:
    
    def __init__(self, name, weapon, attack_power):
        self.name = name
        self.health = 100
        self.weapon = weapon
        self.attack_power = attack_power
        self.power_level = 100
    
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        self.power_level -= 20

