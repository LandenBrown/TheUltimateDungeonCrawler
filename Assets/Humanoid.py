from __init__ import *

class Humanoid:
    def __init__(self, name, profession, level, gold, health, maxhealth, inventory):
        self.name = name
        self.profession = profession
        self.level = level
        self.gold = gold
        self.health = health
        self.maxhealth = maxhealth
        self.inventory = inventory

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


player = Humanoid(None, None, 1, 0, 0, 0, [])
