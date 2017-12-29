from __init__ import *

class Weapon:
	def __init__(self, name, damage, swing_speed, level, durability, max_durability, max_damage_buffer, swing_buffer, cost):
		self.name = name
		self.damage = damage
		self.swing_speed = swing_speed
		self.level = level
		self.durability = durability
		self.max_durability = max_durability
		self.max_damage_buffer = max_damage_buffer
		self.swing_buffer = swing_buffer ####Changes from maxswing to  swing_buffer
		self.cost = cost

		
	def checklevel(self):
		if self.level == 1:
			self.max_durability = 100
			self.max_damage_buffer = 10   #Changes to buffer instead of max_damage
			self.swing_buffer = 5
		if self.level == 2:
			self.max_durability = 120
			self.max_damage_buffer = 15
			self.swing_buffer = 6
		if self.level == 3:
			self.max_durability = 140
			self.max_damage_buffer = 20
			self.swing_buffer = 7
		if self.level == 4:
			self.max_durability = 160
			self.max_damage_buffer = 25
			self.swing_buffer = 8
		if self.level == 5:
			self.max_durability = 180
			self.max_damage_buffer = 30
			self.swing_buffer = 9



			

##### FUTURE CHANGES - MAKE ENHANCEMENTS MODIFY THE DAMAGE BUFFER AND THE SWING BUFFER
