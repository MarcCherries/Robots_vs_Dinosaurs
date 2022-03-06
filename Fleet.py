from Robots import Robots
from Dinosaur import Dinosaur
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    
           
    
    def create_fleet(self):
        robot01 = Robots('Max (the Robot)')
        robot02 = Robots('C3P0')
        robot03 = Robots('HAL')
        self.robots.append(robot01)
        self.robots.append(robot02)
        self.robots.append(robot03)

        
          