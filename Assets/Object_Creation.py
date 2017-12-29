from __init__ import *
from Character import *
from Monster import *
from MonsterType import *
from Weapon import *
from Location import *


#######Creation of Objects#######




##########################----WEAPONS----###############################
ironKnife = Weapon("Iron Knife", 1, 1, 1, 5, 5, 3, 3)


##########################----MONSTERS----##############################
wolf = Monster("Wolf", 20, 20, 3, 10, 1, None, None)






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

