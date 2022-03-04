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
        print(f'Welcome to the {self.name}!  You are about to witness the battle of the century (or eon?), Robots vs. Dinosaurs!\n')
        print('Here are the rules: there are no rules!  No, but seriously, there are several rules.')
        print('Well, before our prehistoric friends go extinct (again!) lets get started!  A herd of dinosaurs and a fleet of robots are being assembled as we speak.')
        input('While were waiting on the robots to charge up, why dont we settle who goes first?  Press (enter) to flip a coin.  Heads for robots and, of course, tails for dinosaurs! \n')
       

    def battle(self):
        h_or_t = random.randint(0,1)
        if h_or_t == 0:
            print ('It is heads! Robots, start your engines. ')
        else:
            print('It is tails! Dinosaurs are roaring to go! ')
        while (self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health > 0) and (self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health > 0):  
            
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
        if self.herd.dinosaurs[0].health <= 0:
           self.herd.dinosaurs[0].health = 0
        elif self.herd.dinosaurs[1].health <= 0:
            self.herd.dinosaurs[1].health = 0
        elif self.herd.dinosaurs[2].health <= 0:
            self.herd.dinosaurs[2].health = 0


        user_choice = int(input(f'Which Dinosaur would you like to attack with?  Type (0) for {self.herd.dinosaurs[0].name}, (1) for {self.herd.dinosaurs[1].name}, or (2) for {self.herd.dinosaurs[2].name}\n'))
        user_choice_attack = int(input(f'Which Robot would you like to attack? Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name} or (2) for {self.fleet.robots[2].name}'))
        
        self.herd.dinosaurs[user_choice].attack(self.fleet.robots[user_choice_attack])
        print (f'{self.herd.dinosaurs[user_choice].name} attacks {self.fleet.robots[user_choice_attack].name} and deals {self.herd.dinosaurs[user_choice].attack_power} worth of damage! \n')
        print(f'{self.fleet.robots[user_choice_attack].name} health is now {self.fleet.robots[user_choice_attack].health}')
        print(f'{self.herd.dinosaurs[user_choice].name} energy is now {self.herd.dinosaurs[user_choice].energy}')

    def robo_turn(self):
#doing this so that if a robot is attacked with more than their health they wont go negative which affects the overall bool checking for gameover might need to move it down
        if self.fleet.robots[0].health <= 0:
           self.fleet.robots[0].health = 0
        elif self.fleet.robots[1].health <= 0:
            self.fleet.robots[1].health = 0
        elif self.fleet.robots[2].health <= 0:
            self.fleet.robots[2].health = 0
        
        user_choice_rob = int(input(f'Which Robot would you like to attack with?  Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name}, or (2) for {self.fleet.robots[2].name}\n'))
        rob_user_choice_attack = int(input(f'Which Dinosaur would you like to attack? Type (0) for {self.herd.dinosaurs[0].name}, (1) for {self.herd.dinosaurs[1].name} or (2) for {self.herd.dinosaurs[2].name}\n'))
        weap_sel =int(input(f'Please select your weapon: (0) Laser Gun {self.fleet.robots[0].attack_power}(damage) 9 (accuracy)     (1) Flamethrower  {self.fleet.robots[1].attack_power}(damage) 8 (accuracy)     (2) Bazooka {self.fleet.robots[2].attack_power}(damage) 7 (accuracy)\n'))
        while True:
            if weap_sel == 0:
                self.fleet.robots[user_choice_rob].weapon = 'Laser Gun'
                self.fleet.robots[user_choice_rob].attack_power = 15
                self.fleet.robots[user_choice_rob].accuracy = 9
                break
            elif weap_sel == 1:
                self.fleet.robots[user_choice_rob].weapon = 'Flamethrower'
                self.fleet.robots[user_choice_rob].attack_power = 20
                self.fleet.robots[user_choice_rob].accuracy = 8
                break
            elif weap_sel == 2:
                self.fleet.robots[user_choice_rob].weapon = 'Bazooka'
                self.fleet.robots[user_choice_rob].attack_power = 25
                self.fleet.robots[user_choice_rob].accuracy = 7
                break
            else:
                print('Thats is not a valid selection, please try again \n')
                weap_sel =int(input(f'Please select your weapon: (0) Laser Gun {self.fleet.robots[0].attack_power}     (1) Flamethrower  {self.fleet.robots[1].attack_power}     (2) Bazooka {self.fleet.robots[2].attack_power}\n'))
 
                continue

        if self.fleet.robots[user_choice_rob].accuracy == 9:
            chances = random.randint(0,9)
            if chances <= 8:
                self.fleet.robots[user_choice_rob].attack(self.herd.dinosaurs[rob_user_choice_attack])
                print(f'{self.fleet.robots[user_choice_rob].name} attacks {self.herd.dinosaurs[rob_user_choice_attack].name} with the {self.fleet.robots[user_choice_rob].weapon} dealing {self.fleet.robots[user_choice_rob].attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[rob_user_choice_attack].name} health is now {self.herd.dinosaurs[rob_user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_rob].name} power level is now {self.fleet.robots[user_choice_rob].power_level}')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_rob].power_level -= 10
        elif self.fleet.robots[user_choice_rob].accuracy == 8:
            chances = random.randint(0,9)
            if chances <= 7:
                self.fleet.robots[user_choice_rob].attack(self.herd.dinosaurs[rob_user_choice_attack])
                print(f'{self.fleet.robots[user_choice_rob].name} attacks {self.herd.dinosaurs[rob_user_choice_attack].name} with the {self.fleet.robots[user_choice_rob].weapon} dealing {self.fleet.robots[user_choice_rob].attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[rob_user_choice_attack].name} health is now {self.herd.dinosaurs[rob_user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_rob].name} power level is now {self.fleet.robots[user_choice_rob].power_level}')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_rob].power_level -= 10
        elif self.fleet.robots[user_choice_rob].accuracy == 7:
            chances = random.randint(0,9)
            if chances <= 6:
                self.fleet.robots[user_choice_rob].attack(self.herd.dinosaurs[rob_user_choice_attack])
                print(f'{self.fleet.robots[user_choice_rob].name} attacks {self.herd.dinosaurs[rob_user_choice_attack].name} with the {self.fleet.robots[user_choice_rob].weapon} dealing {self.fleet.robots[user_choice_rob].attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[rob_user_choice_attack].name} health is now {self.herd.dinosaurs[rob_user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_rob].name} power level is now {self.fleet.robots[user_choice_rob].power_level}')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_rob].power_level -= 10




    
    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        if self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health <= 0:
           print('Dinosaurs rule the Earth once again!')
           print(' roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!')
           print(' roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!')
 
        else:
            print('Robots are the victors! Resistance is futile! ')
            print ('100101001101001001110101001010010010010100101101010!!!!100101010010100101010010001001001!!!10000100010001000100101001001!!!!!01001001000100110100100010010010001!!!!! 100101001101001001110101001010010010010100101101010!!!!')
            print ('100101001101001001110101001010010010010100101101010!!!!100101010010100101010010001001001!!!10000100010001000100101001001!!!!!01001001000100110100100010010010001!!!!! 100101001101001001110101001010010010010100101101010!!!!')
