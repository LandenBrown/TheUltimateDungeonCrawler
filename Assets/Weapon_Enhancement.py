from __init__ import *

# I decided part way though this that we will want both weapon and armor enhancement's.
class Weapon_Enhancement:
	def  __init__(self, name, damage_modifier, elemental_type, swing_speed_modifier):
		self.name = name
		self.damage_modifier = damage_modifier
		self.elemental_type = elemental_type
		self.swing_speed_modifier = swing_speed_modifier
		
		
