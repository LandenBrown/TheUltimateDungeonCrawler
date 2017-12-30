from __init__ import *
from Character import *
from Monster import *
from MonsterType import *
from Weapon import *
from Location import *
from Race import *
from Resource import *
from Monster_Enhancement import *
from Elemental_Type import *

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
#
# Swing_speed can be a max of 5 and a minimum of 1 (5 is faster, 1 is slower)
#
#
##

##Small Weapons
iron_knife = Weapon("Iron Knife", 1, 5, 1, 30, 30, 1, 1, 3)
crather_dagger = Weapon("Crather Dagger", 2, 5, 1, 50, 50, 1, 1, 200)
fellryke_dagger = Weapon("FellRyke Dagger", 1, 5, 1, 30, 30, 3, 1, 200)
spiders_fang = Weapon("Spidersfang", 2, 5, 1, 50, 50, 4, 1, 300) #small chance for drop on queen spider, 100% on Shelob


##Medium Weapons
iron_longsword = Weapon("Iron Longsword", 3, 3, 1, 30, 30, 2, 3, 5)
crather_longsword = Weapon("Crather Longsword", 6, 3, 1, 50, 50, 3, 3, 500) #Drop from monster only
fellryke_rapier = Weapon("FellRyke Rapier", 3, 4, 1, 60, 60, 5, 3, 500) 


##Large Weapons
iron_greatsword = Weapon("Iron Great Sword", 5, 1, 1, 30, 30, 2, 3, 15)
crather_pike = Weapon("Crather Pike", 8, 1, 1, 20, 30, 1, 3, 750)
fellryke_spear = Weapon("FellRyke Spear", 4, 2, 1, 40, 40, 10, 3, 750)


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
earthen = MonsterBreed("Earthen", claw, bite, trip, howl, claw_bite, flesh)

##########################----MONSTERS----##############################
wolf = Monster("Wolf", 20, 20, 3, 10, 1, earthen, 1)
#wolf_alpha = Monster("Alpha Wolf", 50, 50,5, 20, 3, None, 1)
#bandit = Monster("Bandit", 20, 20, 3, 10, 1, None, 1)
#bandit_journeyman = Monster("Journeyman Bandit", 30, 30, 5, 20, 3, None, 1)
#bandit_chieftain = Monster("Chieftain Bandit", 60, 60, 7, 30, 6, None, 1)
#bandit_warlord = Monster("Bandit Warlord", 100, 100, 15, 80, 20, None, 1)
#cthulhu = Monster("Cthulhu: Reaper of all Worlds", 1000, 1000, 50, 1000, 1000, None, 1) #unique
#spiderling = Monster("Spiderling", 5, 5, 2, 1, 1, None, 1)
#spider_adult = Monster("Adult Spider", 10, 10, 3, 5, 3, None, 1)
#spider_queen = Monster("Queen Spider", 30, 30, 6, 20, 10, None, 1)
#shelob = Monster("Her Ladyship, Shelob", 100, 100, 10, 100, 100, None, 1)#Unique spider



#########################----LOCATION ASSETS----#########################

      #######SHOPS#######
crathershop = Shop("Crather Castle Market", [])
fellrykeshop = Shop("FellRyke Spire Market", [])


      #######TAVERNS#####
crathertavern = Tavern("Crather Castle Tavern", None, None)
fellryketavern = Tavern("FellRyke Spire Tavern", None, None)


#########################----SUB LOCATIONS----##########################
cratherdungeon = SubLocation("Crather Castle Dungeon", None, None, [])
cratherplains = SubLocation("Crather Plains", None, None, [])
cratherruins = SubLocation("Crather Ruins", None, None, [])



#########################----LOCATIONS----##############################
crathercastle = Location("Crather Castle", None, None, None, None, None)
fellrykespire = Location("FellRyke Spire", None, None, None, None, None)





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





