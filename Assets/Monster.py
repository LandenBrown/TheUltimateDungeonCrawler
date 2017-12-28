from __init__ import *
from MonsterType import *

class Monster:
    def __init__(self, name, health, maxhealth, damage, golddrop, xpdrop, monstertype):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage
        self.golddrop = golddrop
        self.xpdrop = xpdrop
        self.monstertype = monstertype


    def monsterHit():
        self.monstertype.attack() #has not been created yet

wolf = Monster("Wolf", 20, 20, 3, 10, 1, None)


