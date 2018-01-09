
from Monster_Class import *
from MonsterType import *
from Weapon import *
from Object_Creation import *
from Race import *
from Location import *
from Weapon_Enhancement import *
from Armor_Enhancement import *
from Armor import *
from Resource import *
from Monster_Enhancement import *
from Elemental_Type import *
import random
import easygui
from easygui import *




class Game_Time:
        def __init__(self, day, year):
                self.day = day
                self.year = year
        def checkDate(self):
                if self.day >= 60:
                        self.year = self.year + 1
                        self.day = 1
                        if self.year == 351:
                                print "Welcome to the year of the Scorpion."
				                #A significant "Attention Grabber" designed to interest the player
				                #Will bring new merchants to the world, earthquakes will open new dungeons
				                #A new element will envelope the world, causing imbalance in combat until contained (new quests)
				                #A Seeker will enter the world, often entering towns and offering legendary spells for high gold prices
                        if self.year == 352:
                                print "Welcome to the year of the Centaur"
				                #A great centuar will visit the town, look beautiful, but bring curses
				                #Must investigate and determine what is causing the dark magic (new quests)
                        if self.year == 353:
                                print "Welcome to the year of the Void Kraken"
				                #The Void Kraken will consume the FellRyke Spire, Must Climb the spire and kill each stage of him
				                #Defeat it to visit this town again and help rebuild (New quests)
                        if self.year == 354:
                                print "Welcome to the year of the Ghoul"
				                #Ghouls will be twice as powerful this year
				                #An Army of Ghouls (level 3) will invade Crather Castle. You can run/fight
				                #Ghouls will grow in numbers if not dealt with, could potentially take over the world and all zones
				                #Ghouls will disapear upon the new year when the Searing Cornerstone turns them to ash
				                #Will force you to camp in the wilderness and not visit towns.
                        if self.year == 355:
                                print "Welcome to the decade of the Searing CornerStone"
				#Sears all Ghouls from the year of the ghoul to ash
				#Special event happens on day 25 
				#Significant world changes
                
game_clock = Game_Time(1, 350)
####
def Generate_Monster(cnfg):
    monster1 = Monster(cnfg[0], cnfg[1], cnfg[2], cnfg[3], cnfg[4], cnfg[5], cnfg[6], cnfg[7], cnfg[8], cnfg[9], cnfg[10]) #Monster is created based on location configs // in our real game it would be like player.location.sublocation.monsterconfig or something
    monster1.getConfigs() #We load the monster drop configurations
    return monster1 #This creates a location for this data outside of the scope and into a public memory status to be called-by-reference - which is essential

####
def Generate_Weapon(m):
    weapon1 = Weapon(m.wdropconfig[0], m.wdropconfig[1], m.wdropconfig[2], m.wdropconfig[3], m.wdropconfig[4],
                     m.wdropconfig[5])
    #What kind of weapon are we dropping is developed on the monsters config stats
    weapon1.getConfigs() #Load the weapon stats
    easygui.msgbox("The " + m.name +" dropped you a level " + str(weapon1.level) + " " + weapon1.name + "!")
    easygui.msgbox("This weapon does " + str(weapon1.damage) + " damage!")
    return weapon1
def Buy_Weapon(s):
    shopweapon = Weapon(s.wconfig[0], s.wconfig[1], s.wconfig[2], s.wconfig[3], s.wconfig[4], s.wconfig[5])
    buy = easygui.buttonbox("Are you sure you want to buy and equip this weapon?", "Shop",
                            ("Yes", "No"))
    if buy == "Yes":
        return shopweapon
def Generate_Armor(m):
    armor1 = Armor(m.adropconfig)
    return armor1
####
def Start_Fight():
    player.checkLevel()
    myMonster = Generate_Monster(player.location.monster[0])
    easygui.msgbox("You have encountered a level " + str(myMonster.level) + " " + myMonster.name + "!")
    while myMonster.health != "Dead":
        easygui.msgbox("You hit the monster!")
        player.Hit(myMonster)
        if myMonster.health <= 0:
            easygui.msgbox("You have killed the " + myMonster.name)
            player.mainweapon = Generate_Weapon(myMonster)
            break
        myMonster.Hit(player)
        if player.health <= 0:
            easygui.msgbox("You have died!")
            break
        easygui.msgbox(myMonster.name + " health: " + str(myMonster.health) + " +|+ Player health: " + str(player.health) + "/" + str(player.maxhealth))
###
def Start_Shop():
    shopchoice = easygui.choicebox("Please select an item", "Shop",
                                   [player.mainlocation.shop.wconfig[0], player.mainlocation.shop.aconfig[0]])
    if shopchoice == player.mainlocation.shop.wconfig[0]:
        player.mainweapon = Buy_Weapon(player.mainlocation.shop)
    if shopchoice == player.mainlocation.shop.aconfig[0]:
        player.mainweapon = Buy_Weapon(player.mainlocation.shop)


class Humanoid:
    def __init__(self, name, race, profession, level, gold, health, maxhealth, inventory, mainweapon, mainlocation):
        self.name = name
        self.race = race
        self.profession = profession
        self.level = level
        self.gold = gold
        self.health = health
        self.maxhealth = maxhealth
        self.inventory = inventory
        self.mainweapon = mainweapon
        self.mainlocation = mainlocation

    def checkLevel(self):
        if self.level == 1:
            self.maxhealth = 100
        if self.level == 2:
            self.maxhealth = 120
        if self.level == 3:
            self.maxhealth = 144
        if self.level == 4:
            self.maxhealth = 172
        if self.level == 5:
            self.maxhealth = 206

        self.health = self.maxhealth

    def Hit(self, m):
        #here we are going to make the function to hit the monster, so we can call it during game
        m.health = m.health - self.mainweapon.damage
        easygui.msgbox("You swing at the monster and deal " + str(self.mainweapon.damage) + " damage!")
        ##if player.damagedealt < 0: #making sure that we never do negative damage    ############## I COMMENTED THIS OUT BECAUSE NOW DAMAGE SHOULD NEVER BE NEGATIVE DUE TO THE NEW DAMAGE_BUFFER CALCULATIONS - SCORE!                                                                     
        ##  damagedealt = 0                                                                                                                             
    
    def explore(self):
      encounterChance = random.randint(1, 10)
      if encounterChance <= player.location.monster_rating:
        Start_Fight()
        
player = Humanoid(None, None, None, 1, 0, 0, 0, [], None, None)


#######Creation of Objects#######



##########################---ELEMENTAL TYPES---########################
fire_element = Elemental_Type("Fire", 1)
water_element = Elemental_Type("Water", 1)
darkness_element = Elemental_Type("Darkness", 1)
Brightness_element = Elemental_Type("Brightness", 1)




##########################---ENHANCEMENTS---###########################
####MONSTER ENHANCEMENTS
flesh = Monster_Enhancement("Flesh", 0, water_element, fire_element )


##########################----WEAPONS----###############################

##Object rules ----


##########################---ATTACK TYPES---########################### (Name, desc1, desc2, desc3, dmg, maxdmg)
#####WOLF-LIKE MONSTER ATTACK TYPES #############
claw = AttackType("Claw", "lunges at you and swipes his claws against your body!",
                  "dashes at your legs while viciously penetrating its claws into your lower extremeties",
                  "swipes his claws and lacerates your body",
                       2, 2)
bite = AttackType("Bite", "makes a rapid pounce and bites into your ankle",
                  "quickly extends his body and sinks its teeth into your obliques",
                  "sidesteps out of your reach and quickly lunges to sink his teeth into the flesh of your thighs",
                       1, 3)
trip = AttackType("Trip", "rushes at your leg and relentlessly thrashes its body until you trip",
                  "swiftly slashes your hamstring with his razor sharp claws, causing you to stumble and fall",
                  "unpredictably jukes your movements, causing you to fall as he slashes his claws at your face",
                       1, 2)
howl = AttackType("Howl", "braces its body with power and lets out a blood curdling howl",
                  "lets out a howl that causes your blood to bubble",
                  "birskly moves back while letting out a howl with such intensity, your ears start to bleed",
                       1, 1)
claw_bite = AttackType("Claw and Bite", "lunges at you, swipes his claws against your chest, and sinks his teeth into your forearms",
                       "bites your lower leg with a great force as it sinks its claws into your thigh",
                       "violently pounces at your chest, sinking its teeth into your neck and mangles your forearms with its claws",
                       2, 4)
#####GOBLIN-LIKE MONSTER ATTACK TYPES ###########
scratch = AttackType("Fingernail Scratch", "screams and hurdles on top of you, tearing at your flesh with its nails",
                       "spins and scratches you with its fingeranils",
                       "furiously charges you and begins thrashing at your skin with its sharp nails",
                       1, 4)
screech = AttackType("Screech", "screeches a war cry, deafening you",
                       "puffs its chest and screeches, causing you to have major disorientation",
                       "raises its arms to the sky and screeches to its god, giving it strength and making your ears bleed",
                       1, 1)
punch = AttackType("Punch", "throws a jab at you, clipping your jaw",
                       "unexpectedly strikes you in the neck with a jab",
                       "quickly throws a hook, landing on the lower part of your jaws, disorienting you",
                       2, 2)
swing = AttackType("Swing", "swings its war club at you, colliding with your armor, causing the wind to violently exit your lungs",
                       "with great strength, swings his club against your weapon, easily out-weighing it, causing you to lose grip of your weapon",
                       "swings his weapon at your legs, completely knocking you off your feet",
                       2, 3)
throw = AttackType("Trhow", "uses all its strength to hurdle its war club at you, colliding with your head, leaving you disoriented",
                       "picks up the nearest rock and throws it in your direction, colliding with your forehead causing major bleeding",
                       "throws its shoe at you, distracting you as rock collides with your ribs with great force",
                       1, 3)
#####SKELETON-LIKE MONSTER ATTACK TYPES #########
sword_swing = AttackType("Sword Swing", "flies its sword in the air and down onto your armor, ripping the metal apart like butter",
                       "swings its sword into the armor protecting your ribcage, causing trauma to your cartilage",
                       "swings its sword against your forearms, leaving a massive gash, pouring blood",
                       3, 5)
shield_bash = AttackType("Shield Bash", "lunges towards you, shoving its shield into your sternum and shoving violently",
                       "swings the edge of its shield into your head armor, disorienting you and causing confusion",
                       "quickly spins and throws its shield into your platearmor, hitting with such force that it dents your armor",
                       2, 4)
sword_slap = AttackType("Sword Slap", "turns its sword on its side, and slaps your helmet, causing disorientation and ringing",
                       "slaps the flat of its sword against the side of your thigh, causing you to collapse to the floor in pain",
                       "slaps your hands with the side of its sword, immediately causing severe bruising and swellingalong your fingers",
                       3, 3)
sword_throw = AttackType("Sword_Throw", "winds up and throws it sword directly into your chest, causing you to pull out 3 inches of the blade from your body",
                       "throws its sword like an axe at your legs, lacerating your shin open, exposing the bone",
                       "wildly throws its sword at you, perfectly landing in an open spot in your armor, viciously lacerating your flesh",
                       6, 6)
demonize = AttackType("Demonize", "stares directly into your soul, dazing you and sucking the life force from your body",
                       "reaches both hands towards you and sucks your blood from your capillaries",
                       "raises both hands in the air, as you suddenly feel a great force pull you to your knees and begin pulling the life force from your chest",
                       5, 7)
####WIZARD-LIKE MONSTER ATTACK TYPES ##################
##DEMONIZE
stress_mind = AttackType("Stress Mind", "holds a sinlge hand out and clenches his fist, as you feel a great pressure consume your mind",
                       "reaches a hand to the sky, as your mind becomes unclear and you feel the blood vessels popping in your eyes",
                       "points a finger at you as you suddenly begin to get light headed and can hear the blood in your head thicken",
                       5, 7)
manipulate = AttackType("Demonize", "manipulates your body to dislocate and put in place your shoulder joints",
                       "manipulates your weapon to slice your wrists",
                       "forces your hips to become unpostured, ripping them out of the joints",
                       5, 7)
void_ball = AttackType("Demonize", "suddenly summons a mysterious blue and purple ball, and hurdles it at you, throwing you 20 feet backward",
                       "throws a ball of pure hatred and void in your direction exploding against your armor and burning your skin",
                       "channels a ball of void energy into your armor, heating the armor to smoldering temperatures",
                       5, 7)
blood_curdle = AttackType("Demonize", "gazes into your soul, as you feel your blood start to thicken and curdle throughout your body",
                       "points his staff at you, forcing your blood to ooze out of your eyes and nose",
                       "draws a blood magic circle at your feet ripping the viens out of the bottom of your feet and through your armor",
                       5, 7)


##########################---MONSTER BREEDS---##########################
wolf_breed = MonsterBreed("Wolf", claw, bite, trip, howl, claw_bite, fire_element)
goblin_breed = MonsterBreed("Goblin", scratch, screech, punch, swing, throw, fire_element)
skeleton_breed = MonsterBreed("Skeleton", sword_swing, shield_bash, sword_slap, sword_throw, demonize, fire_element)
bloodwizard_breed = MonsterBreed("Blood Wizard", demonize, stress_mind, manipulate, void_ball, blood_curdle, darkness_element)
necromancer_breed = MonsterBreed("Necromancer", demonize, stress_mind, manipulate, void_ball, blood_curdle, darkness_element)
voidchancellor_breed = MonsterBreed("Void Chancellor", demonize, stress_mind, manipulate, void_ball, blood_curdle, darkness_element)



#########################----LOCATION ASSETS----#########################

      #######SHOPS#######
crathershop = Shop("Crather Castle Market", ["Iron Longsword", 3, 3, 1, 30, 5], ["Iron Spear", 3, 3, 1, 30, 5])
fellrykeshop = Shop("FellRyke Spire Market", ["Iron Spear", 3, 3, 1, 30, 5], ["Iron Hammer", 3, 3, 1, 30, 5])
darlekshop = Shop("Darlek Black Market", ["Iron Spear", 3, 3, 1, 30, 5], ["Iron Hammer", 3, 3, 1, 30, 5])


      #######TAVERNS#####
crathertavern = Tavern("Crather Castle Tavern", None, None)
fellryketavern = Tavern("FellRyke Spire Tavern", None, None)
darlektavern = Tavern("Darlek Crowded Tavern", None, None)



####################----RACES----################################
dwarf = Race("Dwarf", 40, 0)
elf = Race("Elf", 15, 3)
human = Race("Human", 25, 2)
lyzard = Race("Lyzard", 35, 1)

####################----RESOURCE TYPES----#############################
ore = Resource_Type("Ore")
wood = Resource_Type("Wood")
plant = Resource_Type("Plant")
####################----RESOURCES----#################################

iron = Resource("Iron", ore, 3)
copper = Resource("Copper", ore, 1)
#
birch = Resource("Birch", wood, 1)
oak = Resource("Oak", wood, 2)
#
marigold = Resource("Marigold", plant, 8)
aloe = Resource("Aloe", plant, 15)


###MONSTER CONIFGS
cratherdungeon_wolf_config = ["Wolf", 1, 1, 1, 1, 1, wolf_breed, 1, None, None, None]
cratherplains_goblin_config = ["Goblin", 1, 1, 1, 1, 1, goblin_breed, 1, None, None, None]
cratherruins_skeleton_config = ["Skeleton", 1, 1, 1, 1, 1, skeleton_breed, 1, None, None, None]
fellrykemanor_bloodwizard_config = ["Blood Wizard", 1, 1, 1, 1, 1, bloodwizard_breed, 1, None, None, None]
fellrykemagetower_voidchancellor_config = ["Void Chancellor", 1, 1, 1, 1, 1, voidchancellor_breed, 1, None, None, None]
fellrykegraveyard_necromancer_config = ["Necromancer", 1, 1, 1, 1, 1, necromancer_breed, 1, None, None, None]


###CRATHER CASTLE

#########################----SUB LOCATIONS----##########################
cratherdungeon = SubLocation("Crather Castle Dungeon", None, 3, [cratherdungeon_wolf_config])
cratherplains = SubLocation("Crather Plains", None, 3, [cratherplains_goblin_config])
cratherruins = SubLocation("Crather Ruins", None, 5, [cratherruins_skeleton_config])
fellrykemanor = SubLocation("FellRyke Manor", None, 5, [fellrykemanor_bloodwizard_config])
fellrykemagetower = SubLocation("FellRyke Mage Tower", None, 5, [fellrykemagetower_voidchancellor_config])
fellrykegraveyard = SubLocation("FellRyke Grave Yard", None, 5, [fellrykegraveyard_necromancer_config])
darlekhideout = SubLocation("Darlek Rogue Hideout", None, 5, [fellrykegraveyard_necromancer_config])
darlekcave = SubLocation("Darlek Cave", None, 5, [fellrykegraveyard_necromancer_config])
darlekdeepwoods = SubLocation("Darlek Deep Woods", None, 5, [fellrykegraveyard_necromancer_config])


#########################----LOCATIONS----##############################
crathercastle = Location("Crather Castle", crathertavern, crathershop, cratherdungeon, cratherplains, cratherruins)
fellrykespire = Location("FellRyke Spire", fellryketavern, fellrykeshop, fellrykemanor, fellrykemagetower, fellrykegraveyard)
darlekwoodlands = Location("Darlek Woodlands", darlektavern, darlekshop, darlekhideout, darlekcave, darlekdeepwoods)




###For testing purposes these initial stats will be hardcoded // This is just to give our player a weapon to test combat with 
myMonster = None
player.mainlocation = crathercastle
player.location = crathercastle
myMonster = Generate_Monster(player.location.sub1.monster[0])
player.mainweapon = Generate_Weapon(myMonster)




