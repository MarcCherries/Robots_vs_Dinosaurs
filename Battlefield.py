import random
from Fleet import Fleet
from Herd import Herd


class Battlefield:
    def __init__(self):
       self.name = "Field of Screams"
       self.herd = Herd()
       self.fleet = Fleet()
       self.herd.create_herd()
       self.fleet.create_fleet()
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        
       
        

    def display_welcome(self):
        print('Welcome to Robots Vs Dinosaurs!  Please wait while your fighters are spawned \n')
       

    def battle(self):
        h_or_t = random.randint(0,1)
        while (self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health != 0) and (self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health != 0):  
            if h_or_t == 0:
                self.robo_turn()
            else:
                  self.dino_turn()

            if  h_or_t == 0:
                h_or_t +=1 
            else:
                h_or_t -=1

        else: 
            self.display_winners()

     
    
    def dino_turn(self):
        user_choice = int(input(f'Which Dinosaur would you like to attack with?  Type (0) for {self.herd.dinosaurs[0].name}, (1) for {self.herd.dinosaurs[1].name}, or (2) for {self.herd.dinosaurs[2].name}\n'))
        user_choice_attack = int(input(f'Which Robot would you like to attack? Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name} or (2) for {self.fleet.robots[2].name}'))
        
        self.herd.dinosaurs[user_choice].attack(self.fleet.robots[user_choice_attack])
        print (f'{self.herd.dinosaurs[user_choice].name} attacks {self.fleet.robots[user_choice_attack].name} and deals {self.herd.dinosaurs[user_choice].attack_power} worth of damage! \n')
        print(f'{self.fleet.robots[user_choice_attack].name} health is now {self.fleet.robots[user_choice_attack].health}')
       

    def robo_turn(self):
        user_choice_rob = int(input(f'Which Robot would you like to attack with?  Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name}, or (2) for {self.fleet.robots[2].name}\n'))
        rob_user_choice_attack = int(input(f'Which Dinosaur would you like to attack? Type (0) for {self.herd.dinosaurs[0].name}, (1) for {self.herd.dinosaurs[1].name} or (2) for {self.herd.dinosaurs[2].name}\n'))
        weap_sel =int(input(f'Please select your weapon: (0) Laser Gun {self.fleet.robots[0].attack_power}     (1) Flamethrower  {self.fleet.robots[1].attack_power}     (2) Bazooka {self.fleet.robots[2].attack_power}\n'))
        if weap_sel == 0:
            self.fleet.robots[user_choice_rob].weapon = 'Laser Gun'
            self.fleet.robots[user_choice_rob].attack_power = 15
        elif weap_sel == 1:
            self.fleet.robots[user_choice_rob].weapon = 'Flamethrower'
            self.fleet.robots[user_choice_rob].attack_power = 20
        elif weap_sel == 2:
            self.fleet.robots[user_choice_rob].weapon = 'Bazooka'
            self.fleet.robots[user_choice_rob].attack_power = 25
        else:
            print('Thats is not a valid selection, please try again \n') 
            
        self.fleet.robots[user_choice_rob].attack(self.herd.dinosaurs[rob_user_choice_attack])
        print(f'{self.fleet.robots[user_choice_rob].name} attacks {self.herd.dinosaurs[rob_user_choice_attack].name} with the {self.fleet.robots[user_choice_rob].weapon} dealing {self.fleet.robots[user_choice_rob].attack_power}!\n')
        print(self.herd.dinosaurs[rob_user_choice_attack].health)
       
    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        print ('Winners!')