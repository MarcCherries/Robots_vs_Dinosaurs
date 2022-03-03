from Robots import Robots
from Dinosaur import Dinosaur

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet (self):
        robot01 = Robots('Max')
        robot02 = Robots('C3P0')
        robot03 = Robots('Hal')
        self.robots.append(robot01)
        self.robots.append(robot02)
        self.robots.append(robot03)

          