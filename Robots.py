from Weapon import Weapon

class Robots:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Robo-Punch', 10, 10)
        self.power_level = 100
        self.status = 'active'
       
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.power_level -= 10

 
 
