from Robots import Robots
from Dinosaur import Dinosaur
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.armory = []

    
           
    
    def create_fleet(self):
        robot01 = Robots('Johnny #5')
        robot02 = Robots('C3PO')
        robot03 = Robots('HAL')
        self.robots.append(robot01)
        self.robots.append(robot02)
        self.robots.append(robot03)

    def create_armory(self):
        weapon_01 = Weapon('Laser Gun', 20, 9)
        weapon_02 = Weapon('Flamethrower', 25, 8)
        weapon_03 = Weapon('Bazooka', 30, 7)
        self.armory.append(weapon_01)
        self.armory.append(weapon_02)
        self.armory.append(weapon_03)
        
          