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
from Engine_Parts import *

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
crathercastle = Location("Crather Castle", None, None, None, None, None)
fellrykespire = Location("FellRyke Spire", None, None, None, None, None)




###For testing purposes these initial stats will be hardcoded
player.location = cratherdungeon


