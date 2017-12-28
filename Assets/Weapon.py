from __init__ import *

class Weapon:
	def __init__(self, name, damage, swing_speed, level, durability, max_durability, max_damage, max_swing_speed):
		self.name = name
		self.damage = damage
		self.swing_speed = swing_speed
		self.level = level
		self.durability = durability
		self.max_durability = max_durability
		self.max_damage = max_damage
		self.max_swing_speed = max_swing_speed
		
	def checklevel(self):
		if self.level == 1:
			self.max_durability = 100
			self.max_damage = 10
			self.max_swing_speed = 5
		if self.level == 2:
			self.max_durability = 120
			self.max_damage = 15
			self.max_swing_speed = 6
		if self.level == 3:
			self.max_durability = 140
			self.max_damage = 20
			self.max_swing_speed = 7
		if self.level == 4:
			self.max_durability = 160
			self.max_damage = 25
			self.max_swing_speed = 8
		if self.level == 5:
			self.max_durability = 180
			self.max_damage = 30
			self.max_swing_speed =9
			