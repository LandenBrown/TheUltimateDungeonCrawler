from __init__ import *

class Weapon:
	def __init__(self, name, damage, swing_speed, level, durability, max_durability, damagebuffer , max_swing_speed):
		self.name = name
		self.damage = damage
		self.swing_speed = swing_speed
		self.level = level
		self.durability = durability
		self.max_durability = max_durability
		self.damagebuffer = damagebuffer
		self.max_swing_speed = max_swing_speed
		
	def checklevel(self):
		if self.level == 1:
			self.max_durability = 100
			self.damagebuffer = 10
			self.max_swing_speed = 5
		if self.level == 2:
			self.max_durability = 120
			self.damagebuffer = 15
			self.max_swing_speed = 6
		if self.level == 3:
			self.max_durability = 140
			self.damagebuffer = 20
			self.max_swing_speed = 7
		if self.level == 4:
			self.max_durability = 160
			self.damagebuffer = 25
			self.max_swing_speed = 8
		if self.level == 5:
			self.max_durability = 180
			self.damagebuffer = 30
			self.max_swing_speed =9
			
	def Hit(hitdamage)
		hitdamage = randit(damage - damagebuffer, damage + damagebuffer)