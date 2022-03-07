from Weapon import Weapon


class Dinosaur:

    def __init__(self, name, ):
        self.name = name
        self.health = 100  
        self.energy = 100
        self.move = Weapon('Dino Bite', 10, 10)
        self.status = 'active'

    def attack(self, robot):
        robot.health -= self.move.attack_power
        self.energy -= 10