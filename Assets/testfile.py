###Test file for instances
import random

### - Engine Configs - ###
myMonster = None


def Generate_Monster(cnfg):
    monster1 = monster(cnfg[0], cnfg[1], cnfg[2], cnfg[3], cnfg[4], cnfg[5]) #Monster is created based on location configs // in our real game it would be like player.location.sublocation.monsterconfig or something
    monster1.getConfigs() #We load the monster drop configurations
    return monster1 #This creates a location for this data outside of the scope and into a public memory status to be called-by-reference - which is essential
        
def Generate_Weapon(m):
    weapon1 = weapon(m.wdropconfig[0], m.wdropconfig[1], m.wdropconfig[2]) #What kind of weapon are we dropping is developed on the monsters config stats
    weapon1.getConfigs() #Load the weapon stats
    return weapon1
####
def Generate_Armor(m):
    armor1 = armor(m.adropconfig)
    return armor1


    
c1 = ["Wolf", 2, None, None, None, None] #This is the monster configuration of say, the crather ruins

class weapon:
    def __init__(self, name, tier, damage):
        self.name = name
        self.tier = tier
        self.damage = damage
    def getConfigs(self):
        if self.tier == 1:
            self.damage = self.damage + 0
        if self.tier == 2:
            self.damage = self.damage + 2
        if self.tier == 3:
            self.damage = self.damage + 4

    
class armor:
    def __init__(self, name, tier, defense):
        self.name = name
        self.tier = tier
        self.defense = defense
        
class humanoid:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

player = humanoid("Player", None)

class monster:
    def __init__(self, name, level, hp, loot, wdropconfig, adropconfig):
        self.name = name
        self.level = level
        self.hp = hp
        self.loot = loot
        self.wdropconfig = wdropconfig
        self.adropconfig = adropconfig

    def getConfigs(self): #We will create the configs for every monster in the game in this here little config generator, NO MORE GLOBAL OBJECTS!!! WE CAN ADD MONSTERS TO THE GAME BY ADDING THEM HERE AND TO THE LOCATION CONFIGS!
        if self.level == 1 and self.name == "Wolf":
            self.wdropconfig = ["Iron Sword", 1, 1]
            self.adropconfig = ["Iron Armor", 1, 1]
                            #Name, Tiermodifier
            self.hp = 10   #If self.monsterbreed = wolf // hp = 7
        if self.level == 2 and self.name == "Wolf":
            self.wdropconfig = ["Iron Sword", 2, 1]
            self.adropconfig = ["Iron Armor", 2, 1]
            self.hp = 25
        if self.level == 3 and self.name == "Wolf":
            self.wdropconfig = ["Iron Sword", 1, 1]
            self.adropconfig = ["Iron Armor", 1, 1]
            self.hp = 35
 

        
