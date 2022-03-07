import random
from Fleet import Fleet
from Herd import Herd
from Weapon import Weapon

class Battlefield:
    def __init__(self):
       self.name = "Field of Screams"
       self.herd = Herd()
       self.fleet = Fleet()
       self.herd.create_herd()
       self.fleet.create_fleet()
       self.fleet.create_armory()
       self.herd.create_repertoire()
       
    def run_game(self):
        self.display_welcome()
        self.battle()
        
    def display_welcome(self):
        print(f'Welcome to the {self.name}!  You are about to witness the battle of the century (or eon?), Robots vs. Dinosaurs!\n')
        print('Here are the rules: THERE ARE NO RULES!!!!  But seriously, pay attention because there are several very important rules.\n')
        print('*****A coin flip will determine which side goes first.  Once the battle begins, each side will have one chance to attack the other side with fighters of your choosing\n')
        print('*****The two sides will alternate attacks until one side is out of players either because they are deceased or can not attack because of low power/energy\n')
        print('*****Each attack removes health from the attacked player in the amount of that fighter\'s weapon or attack strength\n')
        print('*****Along with removing health from your opponent, each attack attempt reduces your fighters own energy or power level by 10!\n')
        print('*****Robots have access to stronger weapons, but unlike the dinosaurs, their hits are not guaranteed to land.  If they miss, no damage will be done to the dinosaur and 10 power-level is still lost by the robot!\n')
        print('*****As any intelligent being knows, all dinosaurs are trained in the art of Tae Kwan Dino, and you will be able to select from a repertoire of moves, all of which are delivered at 100 percent accuracy\n')
        print('*****Robots, on the other hand, are reliant on technology created by inferior humans. While these weapons expertly do what humans do best -- destroy things --  the accuracy of the weapons varies, so choose wisely!\n')
        input('Well, before our prehistoric friends go extinct (again!) let\'s move along!  A herd of dinosaurs and a fleet of robots are being assembled as we speak.  Press any key and then (enter) to continue:\n')

    def battle(self):
        print('Why dont we get started by arming the robots. Our armory is fully stocked so you can choose the same weapon for more than one robot.  All robots, by default, have a Robo-Punch attack (10 damage, 100 percent accuracy). To keep this default weapon, type (3), but feel free to choose a new weapon! Remember, this weapon will be assigned to that robot for the entire battle!\n')
        while True:
            try:
                johnny_weapon_choice = int(input(f'Please select a weapon for {self.fleet.robots[0].name}      (0) for the Laser Gun (20 damage, 90% accuracy)     (1) for the Flamethrower  (25 damage, 80% accuracy)     (2) for the Bazooka  (30 damage, 70% accuracy)\n' ))
            except:
                ValueError
                print('Does Not Compute. Try again silly human!\n')
                continue

            if johnny_weapon_choice > 3 or johnny_weapon_choice < 0:
                print ('Sorry, only numbers 0, 1, 2, or 3 please!\n')
                continue

            elif johnny_weapon_choice == 3:
                 break
            
            else:
                self.fleet.robots[0].weapon = self.fleet.armory[johnny_weapon_choice]
                break
        while True:
            try:
                C3PO_weapon_choice = int(input(f'Please select a weapon for {self.fleet.robots[1].name}      (0) for the Laser Gun (20 damage, 90% accuracy)     (1) for the Flamethrower  (25 damage, 80% accuracy)     (2) for the Bazooka  (30 damage, 70% accuracy)\n' ))
            except:
                ValueError
                print('Does Not Compute. Try again silly human!\n')
                continue

            if C3PO_weapon_choice > 3 or C3PO_weapon_choice < 0:
                print ('Sorry, only numbers 0, 1, 2, or 3 please!\n')
                continue

            elif C3PO_weapon_choice == 3:
                 break

            else:
                self.fleet.robots[1].weapon = self.fleet.armory[C3PO_weapon_choice]
                break
        while True:
            try:
                HAL_weapon_choice = int(input(f'Please select a weapon for {self.fleet.robots[2].name}      (0) for the Laser Gun (20 damage, 90% accuracy)     (1) for the Flamethrower  (25 damage, 80% accuracy)     (2) for the Bazooka  (30 damage, 70% accuracy)\n'))
            except:
                ValueError
                print('Does Not Compute. Try again silly human!\n')
                continue

            if HAL_weapon_choice > 3 or HAL_weapon_choice < 0:
                print ('Sorry, only numbers 0, 1, 2, or 3 please!\n')
                continue

            elif HAL_weapon_choice == 3:
                break
           
            else:
                self.fleet.robots[2].weapon = self.fleet.armory[HAL_weapon_choice]
                break
        input('Okay, now that our robots are armed and our dinosaurs are, umm, legged, let\'s flip a coin to see which side goes first!  Please press any key and then (enter) to flip the coin\n')
        for i in range (10):
            print ('                ******************************************************                        \n')
        heads_or_tails = random.randint(0,1)
        
        if heads_or_tails == 0:
            print ('It\'s heads! Robots, start your processors.\n')
       
        else:
            print('It\'s tails! Dinosaurs are roaring to go! ')
        
        while (self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health > 0) and (self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health > 0):  
            if (self.fleet.robots[0].power_level < 11 or self.fleet.robots[0].health <= 0) and (self.fleet.robots[1].health <=0 or self.fleet.robots[1].power_level < 11 ) and (self.fleet.robots[2].health <= 0 or self.fleet.robots[2].power_level < 11):
                print('No players left to use! Robots forfeit!\n')
                self.display_winners()
                break
                
            elif (self.herd.dinosaurs[0].energy < 11 or self.herd.dinosaurs[0].health <= 0) and (self.herd.dinosaurs[1].health <= 0 or self.herd.dinosaurs[1].energy < 11 ) and (self.herd.dinosaurs[2].health <= 0 or self.herd.dinosaurs[2].energy < 11):
                print ('No players left to use! Dinosaurs forfeit!\n')
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
        print('Dinosaurs\' Turn!')
        self.show_dino_opponent_options('fighters')
        self.show_robo_opponent_options('opponents')
        while True:
            try:
                user_choice_fighter = int(input(f'Which Dinosaur would you like to attack with? {self.herd.dinosaurs[0]. name} type (0), for {self.herd.dinosaurs[1]. name} type (1) or for {self.herd.dinosaurs[2].name} type (2) \n'))
            except ValueError:
                print('Does Not Compute. Try again silly human!\n')   
                continue

            if user_choice_fighter > 2 or user_choice_fighter < 0:
                print ('Sorry, only numbers 0, 1 or 2 please\n')
                continue
                
            elif 'extinct' in self.herd.dinosaurs[user_choice_fighter].status:
                print (f'{self.herd.dinosaurs[user_choice_fighter].name} is extinct! please select again \n')
                continue
                
            elif  'low' in self.herd.dinosaurs[user_choice_fighter].status:
                print (f'{self.herd.dinosaurs[user_choice_fighter].name} is low on energy! please select again \n')
                continue
                
            else: 
                break
                
        while True:
            try:
                user_choice_attack = int(input(f'Which Robot would you like to attack? Type (0) for {self.fleet.robots[0].name}, (1) for {self.fleet.robots[1].name} or (2) for {self.fleet.robots[2].name}\n'))
            except ValueError:
                print('Does Not Compute. Try again silly human!\n')
                continue
        
            if   user_choice_attack > 2 or user_choice_attack < 0:
                   print('Sorry, only numbers 0, 1 or 2 please\n')
                   continue
            
            elif   'off' in self.fleet.robots[user_choice_attack].status:
                    print(f'{self.fleet.robots[user_choice_attack].name} is powered off! Have mercy! Please select again\n')
                    continue  
            
            else:
                break
        while True:
            try:
                move_sel = int(input(f'Which special attack-move would you like to use?  All deal 15 damge with 100 percent accuracy:  Type (0) for {self.herd.move[0].name}  , type (1) for  {self.herd.move[1].name}  type (2) for  {self.herd.move[2].name} type (3) to stay with the Dino Bite\n') ) 
            except ValueError:
                print('Does Not Compute. Try again silly human!\n')
                continue
            
            if move_sel  > 3 or move_sel < 0:
                print ('Sorry, only numbers 0, 1, 2 or 3 please\n')
                continue
            
            elif move_sel == 3:
                break
            
            else:
               self.herd.dinosaurs[user_choice_fighter].move = self.herd.move[move_sel]
               break

        self.herd.dinosaurs[user_choice_fighter].attack(self.fleet.robots[user_choice_attack])
        print (f'{self.herd.dinosaurs[user_choice_fighter].name} attacks {self.fleet.robots[user_choice_attack].name} with the {self.herd.dinosaurs[user_choice_fighter].move.name} and deals {self.herd.dinosaurs[user_choice_fighter].move.attack_power} worth of damage! \n')
        print(f'{self.fleet.robots[user_choice_attack].name} health is now {self.fleet.robots[user_choice_attack].health}')
        print(f'{self.herd.dinosaurs[user_choice_fighter].name} energy is now {self.herd.dinosaurs[user_choice_fighter].energy}')
#this needs to be at the end so the main game over loop can do an accurate check BEFORE the next round begins, a negative value could cause a false game over
        if self.fleet.robots[user_choice_attack].health <= 0:
           self.fleet.robots[user_choice_attack].health =  0
           self.fleet.robots[user_choice_attack].status = (f'{self.fleet.robots[user_choice_attack].name} is powered off!') 

        if self.herd.dinosaurs[user_choice_fighter].energy <= 10:
           self.herd.dinosaurs[user_choice_fighter].status = (f'{self.herd.dinosaurs[user_choice_fighter].name} is low on energy and can not attack!')

    def robo_turn(self):
        print('Robots\' Turn!')
        self.show_robo_opponent_options('fighters')
        self.show_dino_opponent_options('opponents')
        while True:
            try:
                user_choice_fighter = int(input(f'Which Robot would you like to attack with? for {self.fleet.robots[0].name} type (0), for {self.fleet.robots[1].name} type (1) or for {self.fleet.robots[2].name} type (2) \n'))
            except ValueError:
                print ('Does Not Compute. Try again silly human!\n')
                continue
            
            if user_choice_fighter > 2 or user_choice_fighter < 0:
                 print('Sorry, only numbers 0, 1 or 2 please \n')
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
                print ('Does Not Compute. Try again silly human!\n')
                continue
          
            if user_choice_attack > 2 or user_choice_attack < 0:
                print('Sorry, only numbers 0, 1, or 2 please.\n')
                continue
            
            elif 'extinct' in self.herd.dinosaurs[user_choice_attack].status:
                print(f'Sorry, {self.herd.dinosaurs[user_choice_attack].name} is extinct! Do not beat a dead dinosaur! Please select again.\n')
                continue

            else:
                break
             
        if self.fleet.robots[user_choice_fighter].weapon.accuracy == 9:
            chances = random.randint(0,9)
            if chances <= 8:
                self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
                print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
               
            else:
                print('Oh no! A miss! No damage done and 10 power lost!\n')
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
                print('Oh no! A miss! No damage done and 10 power lost!\n')
                self.fleet.robots[user_choice_fighter].power_level -= 10
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
                print (f'{self.herd.dinosaurs[user_choice_attack].name} health remains at {self.herd.dinosaurs[user_choice_attack].health}\n')
      
        elif self.fleet.robots[user_choice_fighter].weapon.accuracy == 7:
            chances = random.randint(0,9)
            if chances <= 6:
                self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
                print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
                print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}\n')
            else:
                print('Oh no! A miss! No damage done and 10 power lost!')
                self.fleet.robots[user_choice_fighter].power_level -= 10
                print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}')
                print (f'{self.herd.dinosaurs[user_choice_attack].name} health remains at {self.herd.dinosaurs[user_choice_attack].health}\n')

        else:
            self.fleet.robots[user_choice_fighter].attack(self.herd.dinosaurs[user_choice_attack])
            print(f'{self.fleet.robots[user_choice_fighter].name} attacks {self.herd.dinosaurs[user_choice_attack].name} with the {self.fleet.robots[user_choice_fighter].weapon.name} dealing {self.fleet.robots[user_choice_fighter].weapon.attack_power} damage!\n')
            print(f'{self.herd.dinosaurs[user_choice_attack].name} health is now {self.herd.dinosaurs[user_choice_attack].health}')
            print(f'{self.fleet.robots[user_choice_fighter].name} power level is now {self.fleet.robots[user_choice_fighter].power_level}\n')

        if self.herd.dinosaurs[user_choice_attack].health <= 0:
           self.herd.dinosaurs[user_choice_attack].health = 0
           self.herd.dinosaurs[user_choice_attack].status = (f'{self.herd.dinosaurs[user_choice_attack].name} is extinct!')
         
        if self.fleet.robots[user_choice_fighter].power_level < 11:
           self.fleet.robots[2].status = (f'{self.fleet.robots[2].name} is low on power and cannot attack!')
        
    def show_dino_opponent_options(self, type):
        print( f'Here are the current statuses of your {type}')
        print(f' (0) {self.herd.dinosaurs[0].name}    {self.herd.dinosaurs[0].health}(health)      {self.herd.dinosaurs[0].energy}(energy)   {self.herd.dinosaurs[0].status}') 
        print(f' (1) {self.herd.dinosaurs[1].name}       {self.herd.dinosaurs[1].health}(health)      {self.herd.dinosaurs[1].energy}(energy)   {self.herd.dinosaurs[1].status}') 
        print(f' (2) {self.herd.dinosaurs[2].name}     {self.herd.dinosaurs[2].health}(health)      {self.herd.dinosaurs[2].energy}(energy)   {self.herd.dinosaurs[2].status}') 

    def show_robo_opponent_options(self, type):
        print(f'Here are the current statuses of your {type}')
        print(f' (0) {self.fleet.robots[0].name}   {self.fleet.robots[0].health}(health)      {self.fleet.robots[0].power_level}(power level)   {self.fleet.robots[0].status}     {self.fleet.robots[0].weapon.name}') 
        print(f' (1) {self.fleet.robots[1].name}        {self.fleet.robots[1].health}(health)      {self.fleet.robots[1].power_level}(power level)   {self.fleet.robots[1].status}     {self.fleet.robots[1].weapon.name}') 
        print(f' (2) {self.fleet.robots[2].name}         {self.fleet.robots[2].health}(health)      {self.fleet.robots[2].power_level}(power level)   {self.fleet.robots[2].status}     {self.fleet.robots[2].weapon.name}') 

    def display_winners(self):
        if self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health <= 0 or (self.fleet.robots[0].power_level < 11 or self.fleet.robots[0].health <= 0) and (self.fleet.robots[1].health <=0 or self.fleet.robots[1].power_level < 11 ) and (self.fleet.robots[2].health <= 0 or self.fleet.robots[2].power_level < 11):
            for i in range (100) :
                print('Dinosaurs rule the Earth once again! Dinosaurs rule the Earth once again! Dinosaurs rule the Earth once again!  ')
            for i in range (10):
                print(' roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!  roooooooooooaaaaaaaaaaaaaaaarrrrrrrrr!!!!!!')
            print('*******Powered by Radon Technologies (c) 2022  NO Dinosaurs and MANY Robots were harmed in the making of this game.  Powered by Radon Technologies (c)********')

        
        else:
            for i in range (100):
                print('Robots are the victors! Resistance is futile! Robots are the victors! Resistance is futile! Robots are the victors! Resistance is futile! ')
            for i in range (10):
                 print ('100101001101001001110101001010010010010100101101010!!!!100101010010100101010010001001001!!!10000100010001000100101001001!!!!!01001001000100110100100010010010001!!!!')
            print('*******Powered by Radon Technologies (c) 2022  NO Dinosaurs and MANY Robots were harmed in the making of this game.  Powered by Radon Technologies (c)*********')
