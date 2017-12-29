from __init__ import *
from Monster import *

class MonsterBreed:
    def __init__(self, name, attack1, attack2, attack3, attack4, attack5, enhancement):
        self.name = name
        self.attack1 = attack1 #
        self.attack2 = attack2 #
        self.attack3 = attack3 # THESE WILL BE ATTACK TYPES.
        self.attack4 = attack4 #
        self.attack5 = attack5 #
        self.enhancement = enhancement


### Changes - MonsterType will no longer have a damagebonus
# \\\\ MonsterType will now only indirectly affect the monster
# through strengths and weaknesses /////
# \\\\ NEW - MonsterType will no longer have strengths or weaknesses,
# It will have an overall enhancement that will control it's strengths
# and weaknesses ////
#\\\\MonsterType will now be known as MonsterBreed due to it's overall change
# in structure//////
#
#
#
#
###

class AttackType:
    def __init__(self, name, desc1, desc2, desc3, basedamage, damagebuffer):
        self.name = name
        self.desc1 = desc1
        self.desc2 = desc2
        self.desc3 = desc3
        self.basedamage = basedamage
        self.damagebuffer = damagebuffer

        




