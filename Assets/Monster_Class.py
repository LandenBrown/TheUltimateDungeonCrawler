import random
import easygui
from easygui import *
class Monster:
    def __init__(self, name, level, health, damage, golddrop, xpdrop, monsterbreed, swingspeed, wdropconfig, adropconfig):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.golddrop = golddrop
        self.xpdrop = xpdrop
        self.monsterbreed = monsterbreed
        self.swingspeed = swingspeed
        self.wdropconfig = wdropconfig
        self.adropconfig = adropconfig
    def getConfigs(self): #We will create the configs for every monster in the game in this here little config generator, NO MORE GLOBAL OBJECTS!!! WE CAN ADD MONSTERS TO THE GAME BY ADDING THEM HERE AND TO THE LOCATION CONFIGS!
        ### Wolf
        if self.level == 1 and self.name == "Wolf":
            self.wdropconfig = ["Iron Longsword", 3, 3, 2, 30, 5]
            self.health = 10
            self.xpdrop = 1
            self.golddrop = 1
        if self.level == 2 and self.name == "Wolf":
            self.wdropconfig = ["Iron Longsword", 3, 3, 2, 30, 5]
            self.health = 25
            self.xpdrop = 2
            self.golddrop = 4
        if self.level == 3 and self.name == "Wolf":
            self.wdropconfig = ["Iron Longsword", 3, 3, 3, 30, 5]
            self.health = 35
            self.xpdrop = 7
            self.golddrop = 9
        ### Golbin
        if self.level == 1 and self.name == "Goblin":
            self.wdropconfig = ["Iron Spear", 3, 3, 1, 30, 5]
            self.health = 15
            self.xpdrop = 1
            self.golddrop = 2
        if self.level == 2 and self.name == "Goblin":
            self.wdropconfig = ["Iron Spear", 3, 3, 2, 30, 5]
            self.health = 30
            self.xpdrop = 3
            self.golddrop = 15
        if self.level == 3 and self.name == "Goblin":
            self.wdropconfig = ["Iron Spear", 3, 3, 3, 30, 5]
            self.health = 50
            self.xpdrop = 6
            self.golddrop = 30
        ### Skeleton
        if self.level == 1 and self.name == "Skeleton":
            self.wdropconfig = ["Iron Hammer", 3, 3, 3, 30, 5]
            self.health = 5
            self.xpdrop = 1
            self.golddrop = 1
        if self.level == 2 and self.name == "Skeleton":
            self.wdropconfig = ["Iron Hammer", 3, 3, 2, 30, 5]
            self.health = 20
            self.xpdrop = 2
            self.golddrop = 3
        if self.level == 3 and self.name == "Skeleton":
            self.wdropconfig = ["Iron Hammer", 3, 3, 3, 30, 5]
            self.health = 35
            self.xpdrop = 2
            self.golddrop = 3
            
    def Hit(self, p):
        pickanattack = random.randint(1, 5)
        if pickanattack == 1:
            self.damage = self.monsterbreed.attack1.basedamage + self.monsterbreed.attack1.damagebuffer
            description = random.randint(1, 3)
            if description == 1:
               easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc1 + "!")
            if description == 2:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc2 + "!")
            if description == 3:
                easygui.msgbox("The " + self.name + " " + self.monsterbreed.attack1.desc3 + "!")
            easygui.msgbox("you take " + str(self.damage) + " points of damage!")
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
            easygui.msgbox("you take " + str(self.damage) + " points of damage!")
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
            easygui.msgbox("you take " + str(self.damage) + " points of damage!")
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
            easygui.msgbox("you take " + str(self.damage) + " points of damage!")
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
            easygui.msgbox("you take " + str(self.damage) + " points of damage!")
            p.health = p.health - self.damage
      
 

