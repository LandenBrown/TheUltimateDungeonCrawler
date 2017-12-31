
from Monster_Class import *
from MonsterType import *
from Weapon import *
from Object_Creation import *
from Race import *
from Location import *
from Weapon_Enhancement import *
from Armor_Enhancement import *
from Armor import *
from Resource import *
from Monster_Enhancement import *
from Elemental_Type import *
import random, time


class Game_Time:
        def __init__(self, day, year):
                self.day = day
                self.year = year
        def checkDate(self):
                if self.day >= 60:
                        self.year = self.year + 1
                        self.day = 1
                        if self.year == 351:
                                print "Welcome to the year of the Scorpion."
				                #A significant "Attention Grabber" designed to interest the player
				                #Will bring new merchants to the world, earthquakes will open new dungeons
				                #A new element will envelope the world, causing imbalance in combat until contained (new quests)
				                #A Seeker will enter the world, often entering towns and offering legendary spells for high gold prices
                        if self.year == 352:
                                print "Welcome to the year of the Centaur"
				                #A great centuar will visit the town, look beautiful, but bring curses
				                #Must investigate and determine what is causing the dark magic (new quests)
                        if self.year == 353:
                                print "Welcome to the year of the Void Kraken"
				                #The Void Kraken will consume the FellRyke Spire, Must Climb the spire and kill each stage of him
				                #Defeat it to visit this town again and help rebuild (New quests)
                        if self.year == 354:
                                print "Welcome to the year of the Ghoul"
				                #Ghouls will be twice as powerful this year
				                #An Army of Ghouls (level 3) will invade Crather Castle. You can run/fight
				                #Ghouls will grow in numbers if not dealt with, could potentially take over the world and all zones
				                #Ghouls will disapear upon the new year when the Searing Cornerstone turns them to ash
				                #Will force you to camp in the wilderness and not visit towns.
                        if self.year == 355:
                                print "Welcome to the decade of the Searing CornerStone"
				#Sears all Ghouls from the year of the ghoul to ash
				#Special event happens on day 25 
				#Significant world changes
                
game_clock = Game_Time(1, 350)
####
def Generate_Monster(cnfg):
    monster1 = Monster(cnfg[0], cnfg[1], cnfg[2], cnfg[3], cnfg[4], cnfg[5], cnfg[6], cnfg[7], cnfg[8], cnfg[9]) #Monster is created based on location configs // in our real game it would be like player.location.sublocation.monsterconfig or something
    monster1.getConfigs() #We load the monster drop configurations
    return monster1 #This creates a location for this data outside of the scope and into a public memory status to be called-by-reference - which is essential

####
def Generate_Weapon(m):
    weapon1 = Weapon(m.wdropconfig[0], m.wdropconfig[1], m.wdropconfig[2], m.wdropconfig[3], m.wdropconfig[4], m.wdropconfig[5]) #What kind of weapon are we dropping is developed on the monsters config stats
    weapon1.getConfigs() #Load the weapon stats
    print "The " + m.name +" dropped you a level " + str(weapon1.level) + " " + weapon1.name + "!"
    print "This weapon does " + str(weapon1.damage) + " damage!"
    return weapon1
####
def Generate_Armor(m):
    armor1 = Armor(m.adropconfig)
    return armor1
####
def Start_Fight():
  player.checkLevel()
  myMonster = Generate_Monster(player.location.monster[0])
  print "You have encountered a level " + str(myMonster.level) + " " + myMonster.name + "!"
  while myMonster.health != "Dead": 
    print "press anything to hit the monster!"
    raw_input()
    player.Hit(myMonster)
    if myMonster.health <= 0:
      print "You have killed the " + myMonster.name
      Generate_Weapon(myMonster)
      break
    myMonster.Hit(player)
    if player.health <= 0:
      print "You have died!"
      break
    print myMonster.name + " health: " + str(myMonster.health) + " +|+ Player health: " + str(player.health) + "/" + str(player.maxhealth)
####

class Humanoid:
    def __init__(self, name, race, profession, level, gold, health, maxhealth, inventory, mainweapon, mainlocation):
        self.name = name
        self.race = race
        self.profession = profession
        self.level = level
        self.gold = gold
        self.health = health
        self.maxhealth = maxhealth
        self.inventory = inventory
        self.mainweapon = mainweapon
        self.mainlocation = mainlocation

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

    def Hit(self, m):
        #here we are going to make the function to hit the monster, so we can call it during game
        m.health = m.health - self.mainweapon.damage
        print "You swing at the monster and deal " + str(self.mainweapon.damage) + " damage!"
        ##if player.damagedealt < 0: #making sure that we never do negative damage    ############## I COMMENTED THIS OUT BECAUSE NOW DAMAGE SHOULD NEVER BE NEGATIVE DUE TO THE NEW DAMAGE_BUFFER CALCULATIONS - SCORE!                                                                     
        ##  damagedealt = 0                                                                                                                             
    
    def explore(self):
      encounterChance = random.randint(1, 10)
      if encounterChance <= player.location.monster_rating:
        Start_Fight()
        
player = Humanoid(None, None, None, 1, 0, 0, 0, [], None, None)


#######Creation of Objects#######



##########################---ELEMENTAL TYPES---########################
fire_element = Elemental_Type("Fire", 1)
water_element = Elemental_Type("Water", 1)
darkness_element = Elemental_Type("Darkness", 1)
Brightness_element = Elemental_Type("Brightness", 1)




##########################---ENHANCEMENTS---###########################
####MONSTER ENHANCEMENTS
flesh = Monster_Enhancement("Flesh", 0, water_element, fire_element )


##########################----WEAPONS----###############################

##Object rules ----


##########################---ATTACK TYPES---###########################
#####WOLF-LIKE MONSTER ATTACK TYPES #############
claw = AttackType("Claw", "lunges at you and swipes his claws against your body!",
                  "dashes at your legs while viciously penetrating its claws into your lower extremeties",
                  "swipes his claws and lacerates your body",
                       2, 2)
bite = AttackType("Bite", "makes a rapid pounce and bites into your ankle",
                  "quickly extends his body and sinks its teeth into your obliques",
                  "sidesteps out of your reach and quickly lunges to sink his teeth into the flesh of your thighs",
                       1, 3)
trip = AttackType("Trip", "rushes at your leg and relentlessly thrashes its body until you trip",
                  "swiftly slashes your hamstring with his razor sharp claws, causing you to stumble and fall",
                  "unpredictably jukes your movements, causing you to fall as he slashes his claws at your face",
                       1, 2)
howl = AttackType("Howl", "braces its body with power and lets out a blood curdling howl",
                  "lets out a howl that causes your blood to bubble",
                  "birskly moves back while letting out a howl with such intensity, your ears start to bleed",
                       1, 1)
claw_bite = AttackType("Claw and Bite", "lunges at you, swipes his claws against your chest, and sinks his teeth into your forearms",
                       "bites your lower leg with a great force as it sinks its claws into your thigh",
                       "violently pounces at your chest, sinking its teeth into your neck and mangles your forearms with its claws",
                       2, 4)

##########################---MONSTER BREEDS---##########################
wolf_breed = MonsterBreed("Wolf", claw, bite, trip, howl, claw_bite, fire_element)
goblin_breed = MonsterBreed("Goblin", claw, bite, trip, howl, claw_bite, fire_element)
skeleton_breed = MonsterBreed("Skeleton", claw, bite, trip, howl, claw_bite, fire_element)


#########################----LOCATION ASSETS----#########################

      #######SHOPS#######
crathershop = Shop("Crather Castle Market", [])
fellrykeshop = Shop("FellRyke Spire Market", [])


      #######TAVERNS#####
crathertavern = Tavern("Crather Castle Tavern", None, None)
fellryketavern = Tavern("FellRyke Spire Tavern", None, None)



####################----RACES----################################
dwarf = Race("Dwarf", 40, 0)
elf = Race("Elf", 15, 3)
human = Race("Human", 25, 2)
lyzard = Race("Lyzard", 35, 1)

####################----RESOURCE TYPES----#############################
ore = Resource_Type("Ore")
wood = Resource_Type("Wood")
plant = Resource_Type("Plant")
####################----RESOURCES----#################################

iron = Resource("Iron", ore, 3)
copper = Resource("Copper", ore, 1)
#
birch = Resource("Birch", wood, 1)
oak = Resource("Oak", wood, 2)
#
marigold = Resource("Marigold", plant, 8)
aloe = Resource("Aloe", plant, 15)


###MONSTER CONIFGS
cratherdungeon_wolf_config = ["Wolf", 1, 1, 1, 1, 1, wolf_breed, 1, None, None]
cratherplains_goblin_config = ["Goblin", 1, 1, 1, 1, 1, goblin_breed, 1, None, None]
cratherruins_skeleton_config =  ["skeleton", 1, 1, 1, 1, 1, skeleton_breed, 1, None, None]


###CRATHER CASTLE

#########################----SUB LOCATIONS----##########################
cratherdungeon = SubLocation("Crather Castle Dungeon", None, 3, [cratherdungeon_wolf_config])
cratherplains = SubLocation("Crather Plains", None, 3, [cratherplains_goblin_config])
cratherruins = SubLocation("Crather Ruins", None, 5, [cratherruins_skeleton_config])



#########################----LOCATIONS----##############################
crathercastle = Location("Crather Castle", crathertavern, crathershop, cratherdungeon, cratherplains, cratherruins)
fellrykespire = Location("FellRyke Spire", None, None, None, None, None)




###For testing purposes these initial stats will be hardcoded // This is just to give our player a weapon to test combat with 
myMonster = None
player.mainlocation = crathercastle
player.location = cratherdungeon
myMonster = Generate_Monster(player.location.monster[0])

player.mainweapon = Generate_Weapon(myMonster)




