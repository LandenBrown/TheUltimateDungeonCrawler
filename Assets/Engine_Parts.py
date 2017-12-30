from __init__ import *

		
def Engine_Start_Init():
        ###Defining location values
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
