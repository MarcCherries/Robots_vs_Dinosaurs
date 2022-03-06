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
        print('Here are the rules: THERE ARE NO RULES!!!!  But seriously, pay attention because there are several very important rules.')
        print('Well, before our prehistoric friends go extinct (again!) lets get started!  A herd of dinosaurs and a fleet of robots are being assembled as we speak.')
        input('While we are waiting on the robots to charge up, why dont we settle who goes first?  Press (enter) to flip a coin.  Heads for robots and, of course, tails for dinosaurs! \n')
       
    def battle(self):
        heads_or_tails = random.randint(0,1)
        if heads_or_tails == 0:
            print ('It is heads! Robots, start your processors. ')
        else:
            print('It is tails! Dinosaurs are roaring to go! ')
        while (self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health > 0) and (self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health > 0):  
            if (self.fleet.robots[0].power_level < 11 or self.fleet.robots[0].health <= 0) and (self.fleet.robots[1].health <=0 or self.fleet.robots[1].power_level < 11 ) and (self.fleet.robots[2].health <= 0 or self.fleet.robots[2].power_level < 11):
                print('No players left to use! Robots forfeit!')
                self.display_winners()
                break
                
            elif (self.herd.dinosaurs[0].energy < 11 or self.herd.dinosaurs[0].health <= 0) and (self.herd.dinosaurs[1].health <= 0 or self.herd.dinosaurs[1].energy < 11 ) and (self.herd.dinosaurs[2].health <= 0 or self.herd.dinosaurs[2].energy < 11):
                print ('No players left to use! Dinosaurs forfeit!')
                self.display_winners()
                break

            if heads_or_tails == 0:
               heads_or_tails +=1  
               self.robo_turn()
            else:
                heads_or_tails -=1
                self.dino_turn()

        else: 
            self.display_winners()
    
    def dino_turn(self):
        print('Dinosaurs Turn!')
        self.show_dino_opponent_options('fighters')
        self.show_robo_opponent_options('enemies')
        while True:
            try:
                user_choice_fighter = int(input(f'Which Dinosaur would you like to attack with? {self.herd.dinosaurs[0]. name} type (0), for {self.herd.dinosaurs[1]. name} type (1) or for {self.herd.dinosaurs[2].name} type (2) \n'))
            except ValueError:
                print('invalid input')   
                continue

            if user_choice_fighter > 2 or user_choice_fighter < 0:
                print ('Sorry, only numbers 0, 1 or 2 please')
                continue
                
            elif 'dead' in self.herd.dinosaurs[user_choice_fighter].status:
                print (f'{self.herd.dinosaurs[user_choice_fighter].name} is dead! please select again \n')
                continue
                
            elif  'low' in self.herd.dinosaurs[user_choice_fighter].status:
                print (f'{self.herd.dinosaurs[user_choice_fighter].name} is low on energy! please select again \n')
                continue
                
           

            else: 
                break
                
        while True:
            try:
                user_choice_attack = int(input(f'Which Robot would you like to attack? Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name} or (2) for {self.fleet.robots[2].name}'))
            except ValueError:
                print('Does Not Compute. Try again silly human!')
                continue
        
            if   user_choice_attack > 2 or user_choice_attack < 0:
                   print('Sorry, only numbers 0, 1 or 2 please')
                   continue
            
            elif   'off' in self.fleet.robots[user_choice_attack].status:
                    print(f'{self.fleet.robots[user_choice_attack].name} is powered off! Have mercy! Please select again')
                    continue  
            
            else:
                break

        while True:
            try:
                move_sel = int(input(f'Which special attack move would you like to use?  Type (0) for {self.herd.dinosaurs[0].move} {self.herd.dinosaurs[0].attack_power} (damage)   90% accuracy, type (1) for  {self.herd.dinosaurs[1].move} {self.herd.dinosaurs[1].attack_power} (damage)   80%  (accuracy), or type (2) for  {self.herd.dinosaurs[2].move} {self.herd.dinosaurs[2].attack_power} (damage)   70%  (accuracy)   ') ) 
            except ValueError:
                print('Does Not Compute. Try again silly human!')
                continue
            
            if move_sel == 0:
                self.herd.dinosaurs[user_choice_fighter].move = 'Bull Rush'
                self.herd.dinosaurs[user_choice_fighter].attack_power = 15
                self.herd.dinosaurs[user_choice_fighter].accuracy = 9
                break
            elif move_sel == 1:
                self.herd.dinosaurs[user_choice_fighter].move = 'Chomp Stomp'
                self.herd.dinosaurs[user_choice_fighter].attack_power = 20
                self.herd.dinosaurs[user_choice_fighter].accuracy = 8
                break
            elif move_sel == 2:
                self.herd.dinosaurs[user_choice_fighter].move = 'Pteradactyl Swoop'
                self.herd.dinosaurs[user_choice_fighter].attack_power = 25
                self.herd.dinosaurs[user_choice_fighter].accuracy = 7
                break
            elif move_sel  > 2 or move_sel < 0:
                print ('Sorry, only numbers 0, 1 or 2 please')
                continue

        self.herd.dinosaurs[user_choice_fighter].attack(self.fleet.robots[user_choice_attack])
        print (f'{self.herd.dinosaurs[user_choice_fighter].name} attacks {self.fleet.robots[user_choice_attack].name} with the {self.herd.dinosaurs[user_choice_fighter].move} and deals {self.herd.dinosaurs[user_choice_fighter].attack_power} worth of damage! \n')
        print(f'{self.fleet.robots[user_choice_attack].name} health is now {self.fleet.robots[user_choice_attack].health}')
        print(f'{self.herd.dinosaurs[user_choice_fighter].name} energy is now {self.herd.dinosaurs[user_choice_fighter].energy}')
#this needs to be at the end so the main game over loop can do an accurate check before the next round begins, a negative value could cause a false game over
        if self.fleet.robots[user_choice_attack].health <= 0:
           self.fleet.robots[user_choice_attack].health =  0
           self.fleet.robots[user_choice_attack].status = (f'{self.fleet.robots[user_choice_attack].name} is powered off!') 

        if self.fleet.robots[user_choice_fighter].power_level <= 0:
           self.herd.dinosaurs[user_choice_fighter].status = (f'{self.herd.dinosaurs[user_choice_fighter].name} is low on energy and can not attack!')

    def robo_turn(self):
        print('Robots Turn!')
        self.show_robo_opponent_options('fighters')
        self.show_dino_opponent_options('enemies')
        while True:
            try:
                user_choice_fighter = int(input(f'Which Robot would you like to attack with? for {self.fleet.robots[0].name} type (0), for {self.fleet.robots[1].name} type (1) or for {self.fleet.robots[2].name} type (2) \n'))
            except ValueError:
                print ('Does Not Compute. Try again silly human!')
                continue
            
            if user_choice_fighter > 2 or user_choice_fighter < 0:
                 print('Sorry, only number 0, 1 or 2 please \n')
                 continue
            
            elif 'off' in self.fleet.robots[user_choice_fighter].status:
                print (f'{self.fleet.robots[user_choice_fighter].name} is powered off! please select again \n')
                continue
            
            elif 'low' in self.fleet.robots[user_choice_fighter].status:
                  print (f'{self.fleet.robots[user_choice_fighter].name} is low on power and can not attack! please select again \n')
                  continue   
        
          
            
            else: 
                break
                
        while True:
            try:
                user_choice_attack = int(input(f'Which Dinosaur would you like to attack? Type (0) for {self.herd.dinosaurs[0].name}, (1) for {self.herd.dinosaurs[1].name} or (2) for {self.herd.dinosaurs[2].name}\n'))
            except ValueError:
                print ('Does Not Compute. Try again silly human!')
                continue
          
            
            if user_choice_attack > 2 or user_choice_attack < 0:
                print('Sorry, only numbers 0, 1, or 2 please. \n')
                continue
            
            elif 'dead' in self.herd.dinosaurs[user_choice_attack].status:
                print(f'Sorry, {self.herd.dinosaurs[user_choice_attack].name} is dead! Do not beat a dead dinosaur! Please select again. \n')
                continue

                
            else:
                break
             
        while True:
            try:
                weapon_selection =int(input(f'Please select your weapon: (0) Laser Gun {self.fleet.robots[0].weapon.attack_power} (damage)   9 (accuracy)     (1) Flamethrower  {self.fleet.robots[1].weapon.attack_power} (damage)   8 (accuracy)     (2) Bazooka {self.fleet.robots[2].weapon.attack_power} (damage)   7 (accuracy)\n'))
            except ValueError:
                print ('Does Not Compute. Try again silly human!')
                continue
            
            if weapon_selection == 0:
                self.fleet.robots[user_choice_fighter].weapon.name = 'Laser Gun'
                self.fleet.robots[user_choice_fighter].weapon.attack_power = 15
                self.fleet.robots[user_choice_fighter].weapon.accuracy = 9
                break
            elif weapon_selection == 1:
                self.fleet.robots[user_choice_fighter].weapon.name = 'Flamethrower'
                self.fleet.robots[user_choice_fighter].weapon.attack_power = 20
                self.fleet.robots[user_choice_fighter].weapon.accuracy = 8
                break
            elif weapon_selection == 2:
                self.fleet.robots[user_choice_fighter].weapon.mame = 'Bazooka'
                self.fleet.robots[user_choice_fighter].weapon.attack_power = 25
                self.fleet.robots[user_choice_fighter].weapon.accuracy = 7
                break
            elif weapon_selection > 2 or weapon_selection < 0:
                print ('Sorry, only numbers 0, 1 or 2 please')
                continue            
            
        if self.fleet.robots[user_choice_fighter].weapon.accuracy == 9:
            chances = random.randint(0,9)
            if chances <= 8:
                self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
                print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
               
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_fighter].power_level -= 10
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
                print (f'{self.herd.dinosaurs[user_choice_attack].name} health remains at {self.herd.dinosaurs[user_choice_attack].health}')
        
        elif self.fleet.robots[user_choice_fighter].weapon.accuracy == 8:
            chances = random.randint(0,9)
            if chances <= 7:
                self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
                print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_fighter].power_level -= 10
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
                print (f'{self.herd.dinosaurs[user_choice_attack].name} health remains at {self.herd.dinosaurs[user_choice_attack].health}')
      
        elif self.fleet.robots[user_choice_fighter].weapon.accuracy == 7:
            chances = random.randint(0,9)
            if chances <= 6:
                self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
                print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_fighter].power_level -= 10
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
                print (f'{self.herd.dinosaurs[user_choice_attack].name} health remains at {self.herd.dinosaurs[user_choice_attack].health}')
      
        if self.herd.dinosaurs[user_choice_attack].health <= 0:
           self.herd.dinosaurs[user_choice_attack].health = 0
           self.herd.dinosaurs[user_choice_attack].status = (f'{self.herd.dinosaurs[user_choice_attack].name} is dead!')
         
        if self.fleet.robots[user_choice_fighter].power_level < 11:
           self.fleet.robots[2].status = (f'{self.fleet.robots[2].name} is low on power and cannot attack!')
        
    def show_dino_opponent_options(self, type):
        print( f'Here are the current statuses of your {type}')
        print(f' (0) {self.herd.dinosaurs[0].name}    {self.herd.dinosaurs[0].health}(health)      {self.herd.dinosaurs[0].energy}(energy)   {self.herd.dinosaurs[0].status}') 
        print(f' (1) {self.herd.dinosaurs[1].name}       {self.herd.dinosaurs[1].health}(health)      {self.herd.dinosaurs[1].energy}(energy)   {self.herd.dinosaurs[1].status}') 
        print(f' (2) {self.herd.dinosaurs[2].name}    {self.herd.dinosaurs[2].health}(health)      {self.herd.dinosaurs[2].energy}(energy)   {self.herd.dinosaurs[2].status}') 

    def show_robo_opponent_options(self, type):
        print(f'Here are the current statuses of your {type}')
        print(f' (0) {self.fleet.robots[0].name}   {self.fleet.robots[0].health}(health)      {self.fleet.robots[0].power_level}(power level)   {self.fleet.robots[0].status}') 
        print(f' (1) {self.fleet.robots[1].name}       {self.fleet.robots[1].health}(health)      {self.fleet.robots[1].power_level}(power level)   {self.fleet.robots[1].status}') 
        print(f' (2) {self.fleet.robots[2].name}    {self.fleet.robots[2].health}(health)      {self.fleet.robots[2].power_level}(power level)   {self.fleet.robots[2].status}') 

    def display_winners(self):
        if self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health <= 0 or (self.fleet.robots[0].power_level < 11 or self.fleet.robots[0].health <= 0) and (self.fleet.robots[1].health <=0 or self.fleet.robots[1].power_level < 11 ) and (self.fleet.robots[2].health <= 0 or self.fleet.robots[2].power_level < 11):
           print('Dinosaurs rule the Earth once again!')
           print(' roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!')
           print(' roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!')

        else:
            print('Robots are the victors! Resistance is futile! ')
            print ('100101001101001001110101001010010010010100101101010!!!!100101010010100101010010001001001!!!10000100010001000100101001001!!!!!01001001000100110100100010010010001!!!!! 100101001101001001110101001010010010010100101101010!!!!')
            print ('100101001101001001110101001010010010010100101101010!!!!100101010010100101010010001001001!!!10000100010001000100101001001!!!!!01001001000100110100100010010010001!!!!! 100101001101001001110101001010010010010100101101010!!!!')
