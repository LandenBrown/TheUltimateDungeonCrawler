# #### lists or arrays
#
#
#
#
#
#
# class Monster:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#
#
#
# myMonster_conifg = ["Wolf", 10, 10]
#
#
# newMonster = "There is nothing assigned to me!"
#
# def Generate_Monster():
#     m = Monster(myMonster_conifg[0], myMonster_conifg[1], myMonster_conifg[2])
#     return m
#
#
# print newMonster
#
# newMonster = Generate_Monster()
#
# print "It should have values now... Let's check"
#
#
# print newMonster.name
#



class player:
    def __init__(self, weapon):
        self.weapon = weapon


    def Hit(self):
        print self.weapon.damage



class weapon:
    def __init__(self, damage):
        self.damage = damage


# ###scopes
#
# x = 1
# y = 2
#
# def addThem():
#     x = x + y