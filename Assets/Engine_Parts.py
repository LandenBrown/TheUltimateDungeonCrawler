class Game_Time:
        def __init__(self, day, year):
                self.day = day
                self.year = year
	def checkDate(self):
		if self.day >= 60:
			self.year = self.year + 1
			self.day = 1
			if year == 351:
				print "Welcome to the year of the Scorpion."
				#A significant "Attention Grabber" designed to interest the player 
				#Will bring new merchants to the world, earthquakes will open new dungeons
				#A new element will envelope the world, causing imbalance in combat until contained (new quests)
				#A Seeker will enter the world, often entering towns and offering legendary spells for high gold prices
			if year == 352:
				print "Welcome to the year of the Centaur"
				#A great centuar will visit the town, look beautiful, but bring curses
				#Must investigate and determine what is causing the dark magic (new quests)
			if year == 353:
				print "Welcome to the year of the Void Kraken"
				#The Void Kraken will consume the FellRyke Spire, Must Climb the spire and kill each stage of him  
				#Defeat it to visit this town again and help rebuild (New quests)
			if year == 354:
				print "Welcome to the year of the Ghoul"
				#Ghouls will be twice as powerful this year
				#An Army of Ghouls (level 3) will invade Crather Castle. You can run/fight
				#Ghouls will grow in numbers if not dealt with, could potentially take over the world and all zones
				#Ghouls will disapear upon the new year when the Searing Cornerstone turns them to ash
				#Will force you to camp in the wilderness and not visit towns.
			if year == 355:
				print "Welcome to the decade of the Searing CornerStone"
				#Sears all Ghouls from the year of the ghoul to ash
				#Special event happens on day 25 
				#Significant world changes
                
game_clock = Game_Time(1, 350)
####
def Generate_Monster(cnfg):
    monster1 = Monster(cnfg[0], cnfg[1], cnfg[2], cnfg[3], cnfg[4], cnfg[5], cnfg[6], cnfg[7], cnfg[8], cnfg[9]) #Monster is created based on location configs // in our real game it would be like player.location.sublocation.monsterconfig or something
    monster1.getConfigs() #We load the monster drop configurations
    return monster1 #This creates a location for this data outside of the scope and into a public memory status to be called-by-reference - which is essential

####
def Generate_Weapon(m):
    weapon1 = Weapon(m.wdropconfig[0], m.wdropconfig[1], m.wdropconfig[2], m.wdropconfig[3], m.wdropconfig[4], m.wdropconfig[5]) #What kind of weapon are we dropping is developed on the monsters config stats
    weapon1.getConfigs() #Load the weapon stats
    print "The " + m.name +" dropped you a level " + str(weapon1.level) + " " + weapon1.name + "!"
    print "This weapon does " + str(weapon1.damage) + " damage!"
    return weapon1
####
def Generate_Armor(m):
    armor1 = armor(m.adropconfig)
    return armor1
####
def Start_Fight():
  player.checkLevel()
  myMonster = Generate_Monster(player.location.monster[0])
  print "You have encountered a level " + str(myMonster.level) + " " + myMonster.name + "!"
  while myMonster.health != "Dead": 
    print "press anything to hit the monster!"
    raw_input()
    player.Hit(myMonster)
    if myMonster.health <= 0:
      print "You have killed the " + myMonster.name
      Generate_Weapon(myMonster)
      break
    myMonster.Hit(player)
    if player.health <= 0:
      print "You have died!"
      break
    print myMonster.name + " health: " + str(myMonster.health) + " +|+ Player health: " + str(player.health) + "/" + str(player.maxhealth)
####
		
def Engine_Start_Init():
        ############################################################################
        ################################---DEFINING LOCATION VALUES----####################
        ############################################################################
        #####CRATHER CASTLE####
        crathercastle.tavern = crathertavern
        crathercastle.shop = crathershop
        crathercastle.sub1 = cratherdungeon
        crathercastle.sub2 = cratherplains
        crathercastle.sub3 = cratherruins
        ############################################################################
        ################################---DEFINING MONSTER VALUES---####################
        ############################################################################
        
        ############################################################################
        ################################---DEFINING WEAPON VALUES---####################
        ############################################################################
        
        
        ############################################################################
        ################################----DEFINING ARMOR VALUES---####################
        ############################################################################

