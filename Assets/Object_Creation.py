from __init__ import *
from Humanoid import *
from Monster import *
from MonsterType import *
from Weapon import *


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

#########################----SUB LOCATIONS----##########################
