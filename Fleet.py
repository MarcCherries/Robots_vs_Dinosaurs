from Robots import Robots
from Dinosaur import Dinosaur

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet (self):
        robot01 = Robots('Max', 'Laser Gun', 15)
        robot02 = Robots('C3P0', 'Flamethrower', 20)
        robot03 = Robots('Hal', 'Bazooka', 25)
        self.robots.append(robot01)
        self.robots.append(robot02)
        self.robots.append(robot03)

          