from __init__ import *

class Weapon:
	def __init__(self, name, damage, swing_speed, level, durability, cost):
		self.name = name
		self.damage = damage
		self.swing_speed = swing_speed
		self.level = level
		self.durability = durability
		self.cost = cost

		
	def getConfigs(self):
	  ### Iron Longsword configs
		if self.level == 1 and self.name == "Iron Longsword":
			self.durability = 100
			self.damage = 1   #Changes to buffer instead of max_damage
		if self.level == 2 and self.name == "Iron Longsword":
			self.durability = 120
			self.damage = 3
		if self.level == 3 and self.name == "Iron Longsword":
			self.max_durability = 140
			self.damage = 7
		if self.level == 4 and self.name == "Iron Longsword":
			self.durability = 160
			self.damage = 15
		if self.level == 5 and self.name == "Iron Longsword":
			self.durability = 180
			self.damage = 35



			

##### FUTURE CHANGES - MAKE ENHANCEMENTS MODIFY THE DAMAGE BUFFER AND THE SWING BUFFER
