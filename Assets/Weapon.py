from __init__ import *

class Weapon:

	def __init__(self, name, damage, swing_speed, level, durability, max_durability, damagebuffer, swingbuffer):
		self.name = name
		self.damage = damage
		self.swing_speed = swing_speed
		self.level = level
		self.durability = durability
		self.max_durability = max_durability
		self.damagebuffer = damagebuffer
		self.swingbuffer = swingbuffer ####Changes from maxswing to buffer

		
	def checklevel(self):
		if self.level == 1:
			self.max_durability = 100
			self.damagebuffer = 10   #Changes to buffer instead of max_damage
			self.swingbuffer = 5
		if self.level == 2:
			self.max_durability = 120
			self.damagebuffer = 15
			self.swingbuffer = 6
		if self.level == 3:
			self.max_durability = 140
			self.damagebuffer = 20
			self.swingbuffer = 7
		if self.level == 4:
			self.max_durability = 160
			self.damagebuffer = 25
			self.swingbuffer = 8
		if self.level == 5:
			self.max_durability = 180
			self.damagebuffer = 30
			self.swingbuffer = 9



			

