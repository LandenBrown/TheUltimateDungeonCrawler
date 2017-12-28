from __init__ import *
from Monster import *

class MonsterType:
    def __init__(self, name, damagebonus, weakness, strength):
        self.name = name
        self.damagebonus = damagebonus
        self.weakness = weakness
        self.strength = strength
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.attack5 = attack5
        

earthen = MonsterType("Earthen", 0, None, None)
void = MonsterType("Void Realm", 5, None, None)
chaotic = MonsterType("Chaotic", 7, None, None)




