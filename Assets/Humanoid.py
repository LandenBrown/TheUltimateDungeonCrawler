from __init__ import *
from Weapon import *
from Object_Creation import *
import random
class Humanoid:
    def __init__(self, name, profession, level, gold, health, maxhealth, inventory, mainweapon, damagedealt):
        self.name = name
        self.profession = profession
        self.level = level
        self.gold = gold
        self.health = health
        self.maxhealth = maxhealth
        self.inventory = inventory
        self.mainweapon = mainweapon
        self.damagedealt = damagedealt

    def checkLevel(self):
        if self.level == 1:
            self.maxhealth = 100
        if self.level == 2:
            self.maxhealth = 120
        if self.level == 3:
            self.maxhealth = 144
        if self.level == 4:
            self.maxhealth = 172
        if self.level == 5:
            self.maxhealth = 206

        self.health = self.maxhealth

    def Hit(self):
        #here we are going to make the function to hit the monster, so we can call it during game
        self.damagedealt = random.randint(self.mainweapon.damage - self.mainweapon.damagebuffer, self.mainweapon.damage + self.mainweapon.damagebuffer)  # so if we take the stats from the current weapon the player has equipped
        if player.damagedealt < 0: #making sure that we never do negative damage                                                                         this would be damagedealt = random.randint(1 - 3, 1+3) 
            damagedealt = 0                                                                                                                             # So basically any number from (-2, 4)
        print self.damagedealt
        

player = Humanoid(None, None, 1, 0, 0, 0, [], ironKnife, None)
        
        


