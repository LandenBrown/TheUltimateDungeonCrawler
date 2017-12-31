





class Game_Time:
        def __init__(self, day, year):
                self.day = day
                self.year = year
                
game_clock = Game_Time(1, 350)
		
def Engine_Start_Init():
        ############################################################################
        ################################---DEFINING LOCATION VALUES----####################
        ############################################################################
        #####CRATHER CASTLE####
        crathercastle.tavern = crathertavern
        crathercastle.shop = crathershop
        ######CRATHER SHOP
        crathershop.items = [iron_knife, iron_longsword, iron_greatsword]
        crathercastle.sub1 = cratherdungeon
        ######CRATHER DUNGEON
        cratherdungeon.resource = iron
        cratherdungeon.monster_rating = 1
        crathercastle.sub2 = cratherplains
        #####CRATHER PLAINS
        cratherplains.resource = marigold
        cratherplains.monster_rating = 2
        crathercastle.sub3 = cratherruins
        #####CRATHER RUINS
        cratherruins.resource = copper
        cratherruins.monster_rating = 4
        ############################################################################
        ################################---DEFINING MONSTER VALUES---####################
        ############################################################################
        
        ############################################################################
        ################################---DEFINING WEAPON VALUES---####################
        ############################################################################
        
        
        ############################################################################
        ################################----DEFINING ARMOR VALUES---####################
        ############################################################################


##class Sword:
##        def __init__(self, damage, cost):
##                self.damage = damage
##                self.cost = cost
##
##
##def Get_Drop_Config(m):
##        print "placeholder"
##        
##        
##
######MIND FUCKING BLOWNNNNNNN
##def Generate_Weapon(d, c):
##        neweapon = Sword(d, c)
##        return neweapon

###BRAIN STORMING
###player.weapon = Generate_Weapon(d, c)

##arrayof array // this Type of monster drops these
# monster loot drop [[], [], []]  
