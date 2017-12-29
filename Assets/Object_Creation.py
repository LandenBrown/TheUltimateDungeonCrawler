from __init__ import *
from Character import *
from Monster import *
from MonsterType import *
from Weapon import *
from Location import *


#######Creation of Objects#######




##########################----WEAPONS----###############################

##Object rules ----
#
# Swing_speed can be a max of 5 and a minimum of 1 (5 is faster, 1 is slower)
#
#
##

##Small Weapons
ironKnife = Weapon("Iron Knife", 1, 5, 1, 30, 30, 1, 1, 3)
cratherdagger = Weapon("Crather Dagger", 2, 5, 1, 50, 50, 1, 1, 200)
fellrykedagger = Weapon("FellRyke Dagger", 1, 5, 1, 30, 30, 3, 1, 200)


##Medium Weapons
ironlongsword = Weapon("Iron Longsword", 3, 3, 1, 30, 30, 2, 3, 5)
cratherlongsword = Weapon("Crather Longsword", 6, 3, 1, 50, 50, 3, 3, 500) #Drop from monster only
fellrykerapier = Weapon("FellRyke Rapier", 3, 4, 1, 60, 60, 5, 3, 500) 


##Large Weapons
irongreatsword = Weapon("Iron Great Sword", 5, 1, 1, 30, 30, 2, 3, 15)
cratherpike = Weapon("Crather Pike", 8, 1, 1, 20, 30, 1, 3, 750)
fellrykespear = Weapon("FellRyke Spear", 4, 2, 1, 40, 40, 10, 3, 750)

##########################----MONSTERS----##############################
wolf = Monster("Wolf", 20, 20, 3, 10, 1, None, None)
bandit = Monster("Bandit", 20, 20, 3, 10, 1, None, None)





##########################----MONSTER TYPES----#########################
earthen = MonsterBreed("Earthen", None, None, None, None, None, None)
void = MonsterBreed("Void Realm", None, None, None, None, None, None)
chaotic = MonsterBreed("Chaotic", None, None, None, None, None, None)

#########################----LOCATIONS----##############################
crathercastle = Location("Crather Castle", None, None, None, None, None)
fellrykespire = Location("FellRyke Spire", None, None, None, None, None)


#########################----SUB LOCATIONS----##########################
cratherdungeon = SubLocation("Crather Castle Dungeon", None, None, None)
cratherplains = SubLocation("Crather Plains", None, None, None)
cratherruins = SubLocation("Crather Ruins", None, None, None)



#########################----LOCATION ASSETS----#########################

      #######SHOPS#######
crathershop = Shop("Crather Castle Market", [])
fellrykeshop = Shop("FellRyke Spire Market", [])


      #######TAVERNS#####
crathertavern = Tavern("Crather Castle Tavern", None, None)
fellryketavern = Tavern("FellRyke Spire Tavern", None, None)





#####################    PLAYER ASSET   #####################

