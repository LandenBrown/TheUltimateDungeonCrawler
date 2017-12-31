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

