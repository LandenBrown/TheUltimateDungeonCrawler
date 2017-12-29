from __init__ import *
from MonsterType import *
import random

class Monster:
    def __init__(self, name, health, maxhealth, damage, golddrop, xpdrop, monsterbreed, swingspeed):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage
        self.golddrop = golddrop
        self.xpdrop = xpdrop
        self.monsterbreed = monsterbreed
        self.swingspeed = swingspeed


    def monsterHit(self, p):
        pickanattack = random.randit(1, 5)
        if pickanattack == 1:
            self.damage = self.monsterbreed.attack1.basedamage + self.monsterbreed.attack1.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc3 + "!")
            easygui.msgbox("you take " + self.damage + " points of damage!")
            p.health = p.health - self.damage
        if pickanattack == 2:
            self.damage = self.monsterbreed.attack2.basedamage + self.monsterbreed.attack2.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack2.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack2.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack2.desc3 + "!")
            easygui.msgbox("you take " + self.damage + " points of damage!")
            p.health = p.health - self.damage
        if pickanattack == 3:
            self.damage = self.monsterbreed.attack3.basedamage + self.monsterbreed.attack3.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack3.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack3.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack3.desc3 + "!")
            easygui.msgbox("you take " + self.damage + " points of damage!")
            p.health = p.health - self.damage
        if pickanattack == 4:
            self.damage = self.monsterbreed.attack4.basedamage + self.monsterbreed.attack4.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack4.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack4.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack4.desc3 + "!")
            easygui.msgbox("you take " + self.damage + " points of damage!")
            p.health = p.health - self.damage
        if pickanattack == 5:
            self.damage = self.monsterbreed.attack5.basedamage + self.monsterbreed.attack5.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack5.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack5.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack5.desc3 + "!")
            easygui.msgbox("you take " + self.damage + " points of damage!")
            p.health = p.health - self.damage



##CHANGES - MonsterType is now MonsterBreed
# Added the first, initial monster-combat-hit-calculator 
# Will be called like "Wolf.monsterHit(player)" - Simple.
#
#
#
#
#
#
#
##


