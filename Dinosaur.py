class Dinosaur:

    def __init__(self, name, attack_power, move):
        self.name = name
        self.attack_power = attack_power
        self.health = 100  
        self.energy = 100
        self.move = move

    def attack(self, robot):
        robot.health -= self.attack_power
        self.energy -= 10