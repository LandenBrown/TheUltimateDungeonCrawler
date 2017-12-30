from __init__ import *
from Weapon import *
from Object_Creation import *
import random


class Humanoid:
    def __init__(self, name, race, profession, level, gold, health, maxhealth, inventory, mainweapon, damagedealt):
        self.name = name
        self.race = race
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
        self.damagedealt = random.randint(self.mainweapon.damage, self.mainweapon.damage + self.mainweapon.max_damage_buffer)
        ##if player.damagedealt < 0: #making sure that we never do negative damage    ############## I COMMENTED THIS OUT BECAUSE NOW DAMAGE SHOULD NEVER BE NEGATIVE DUE TO THE NEW DAMAGE_BUFFER CALCULATIONS - SCORE!                                                                     
        ##  damagedealt = 0                                                                                                                             
        print self.damagedealt
        


player = Humanoid(None, None, None, 1, 0, 0, 0, [], iron_knife, None)


        
        


###LAST CHANGE - CREATED "RACE" Attribute 12/29/17
### Changed the HIT function to calculate from the base weapon damage as its primary, and a random number between the main weapon damage plus whatever the weapons damagebuffer is.
#############################   CONT. The damage buffer is calculated every interaction on the weapon based on enhancements etc. See Weapon class for this
