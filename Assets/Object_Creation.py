
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
from NPC_Class import *
from Quest_Class import *
import random
import easygui
from easygui import *




class Game_Time:
        def __init__(self, day, year, time, turn):
            self.day = day
            self.year = year
            self.time = time
            self.turn = turn
        def checkDate(self):
            self.turn += 1
            if self.turn >= 6:
                self.day += 1
                self.turn = 0
                print "You have advanced a day!"
            if self.turn <= 2:
                self.time = "Morning"
            if self.turn == 3:
                self.time = "Afternoon"
            if self.turn > 3:
                self.time = "Evening"
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
                
game_clock = Game_Time(1, 350, "Morning", 0)
#### Strength, Dexterity, Wisdom, Charisma, Constitution


def Talk_To_NPC(p):
    #Decide what NPC we are talking to
    npc = 0
    while npc != "Leave Tavern":
        npc = easygui.buttonbox(p.mainlocation.tavern.description+"Who would you like to talk to?", "Tavern",
                                [p.mainlocation.tavern.owner.name, p.mainlocation.tavern.npc1.name, "Leave Tavern"])
        if npc == p.mainlocation.tavern.npc1.name:
            if p.mainlocation.tavern.npc1.quest != None:
                p.mainlocation.tavern.npc1.Quest_Dialogue(player)
            else:
                easygui.msgbox(p.mainlocation.tavern.npc1.intro)
        if npc == p.mainlocation.tavern.owner.name:
            if p.mainlocation.tavern.owner.quest != None:
                p.mainlocation.tavern.owner.Quest_Dialogue(player)
            else:
                easygui.msgbox(p.mainlocation.tavern.owner.intro)



def View_Character(p):
    y = 0
    while y != "Quit":
        y = easygui.buttonbox("Here you can view your equipment and spend skill points. What would you like to do?", "TUDC",
                          ["Spend Skill Points", "View Equipment", "Quit"])
        if y == "Spend Skill Points":
            x = 0
            while x != "Quit":
                if p.statpoints != 0:
                    x = easygui.buttonbox("You have " + str(p.statpoints) + " Stat point(s) to spend!" +
                                          " -- Strength: " + str(p.strength) + ". Dexterity: " + str(p.dexterity) + ". Constitution: " + str(p.constitution) +
                                          ". Charisma: " + str(p.charisma) + ". Wisdom: " + str(p.wisdom), "TUDC",
                                          ["Strength", "Dexterity", "Constitution", "Charisma", "Wisdom"])
                    if x == "Strength":
                        p.strength += 1
                        p.statpoints -= 1
                        easygui.msgbox("You have increased your Strength to: " +str(p.strength))
                    if x == "Dexterity":
                        p.dexterity += 1
                        p.statpoints -= 1
                        easygui.msgbox("You have increased your Dexterity to: " +str(p.dexterity))
                    if x == "Constitution":
                        p.constitution += 1
                        p.statpoints -= 1
                        easygui.msgbox("You have increased your Constitution to: " +str(p.constitution))
                    if x == "Charisma":
                        p.charisma += 1
                        p.statpoints -= 1
                        easygui.msgbox("You have increased your Charisma to: " +str(p.charisma))
                    if x == "Wisdom":
                        p.wisdom += 1
                        p.statpoints -= 1
                        easygui.msgbox("You have increased your Wisdom to: " +str(p.wisdom))
                else:
                    easygui.msgbox("You are out of skill points!")
                    break
        if y == "View Equipment":
            b = 0
            while b != "Back":
                b = easygui.buttonbox("What equipment would you like to examine?", "TUDC",
                                      ["Armor", "Weapon", "Inventory", "Back"])
                if b == "Armor":
                    easygui.msgbox("You are currently wearing " + p.armor.name + ", which gives you an HP Bonus of: " + str(p.armor.hpbonus) + "!")
                if b == "Weapon":
                    easygui.msgbox("You are currently wielding a level " + str(p.mainweapon.level) + " " + p.mainweapon.name + ". It does " + str(p.mainweapon.damage) + " damage on its own, and can sell for " + str(p.mainweapon.cost))
                else:
                    break
def Roll_Initial_Stats(p):
    easygui.msgbox("You are going to roll your stats!")
    rolls = 5
    yesno = 0
    while rolls > 0 or yesno != "Accept":
        if yesno == "Accept":
            easygui.msgbox("You have accepted the stats!")
            break
        rolls -= 1
        stren = random.randint(1, 20)
        dex = random.randint(1, 20)
        wis = random.randint(1, 20)
        con = random.randint(1, 20)
        char = random.randint(1, 20)
        easygui.msgbox("Strength: " + str(stren) + ". Dexterity: " +str(dex) + ". Wisdom: " + str(wis) + ". Constitution: " + str(con) + ". Charisma: " + str(char) + ".")
        if rolls <= 0:
            easygui.msgbox("You ran out of rolls! Click OK to see your final stats!")
            break
        yesno = easygui.buttonbox(
            "Click Roll to attempt to roll your stats! Click Accept when you are satisfied with your randomized stats! Rolls Left: " + str(
                rolls), "Roll Stats",
            ["Roll", "Accept"])
    easygui.msgbox("Your final stats are- Strength: " + str(stren) + ". Dexterity: " +str(dex) + ". Wisdom: " + str(wis) + ". Constitution: " + str(con) + ". Charisma: " + str(char) + ".")
    p.strength = stren
    p.dexterity = dex
    p.wisdom = wis
    p.constitution = con
    p.charisma = char


def Give_Weapon(cnfg):
    w1 = Weapon(cnfg[0], cnfg[1], cnfg[2], cnfg[3], cnfg[4], cnfg[5])
    w1.getConfigs()
    easygui.msgbox("You've been given a " + w1.name + "! It does " + str(w1.damage) + " damage!")
    return w1
def Give_Armor(cnfg):
    a1 = Armor(cnfg[0], cnfg[1], cnfg[2], cnfg[3])
    easygui.msgbox("You've been given " + a1.name + "! It gives " + str(a1.hpbonus) + " bonus HP!")
    return a1


def Create_Character(p, c, cc):
    p.mainlocation = crathercastle
    p.location = crathercastle
    easygui.msgbox("You wake up slowly to the smell of a lemprus weed pipe being gently blown in your face... The sweet aftertaste in the back of your throat sooths the pain that is " +
                   "becoming more and more prevalent as you become more concious.. You open your eyes wearily and turn to see an old man sitting over you..." +
                   "He is clearly not here to hurt you, as the small medical supplies around him suggest he may have been helping you... 'But where am i... WHO am i?' You think to yourself.")
    p.name = easygui.enterbox("'Say, What is your name adventurer?' The old man says. You don't remember your name at all... or anything of who you previously were, but you refuse to keep him waiting...")
    p.age = easygui.integerbox("'Ahh, " + p.name + "... I'm sorry friend, my eyesight is very poor, what is your age?' The old man utters as he squints fervently trying to make a personal account himself.")
    if p.age >= 35:
        easygui.msgbox("'Ah, the pains of age begin to grow on you...' He chuckled. '...but the peace of wisdom is growing...")
    else:
        easygui.msgbox("'A young lad we have here! Off for some excitement I presume?' The old man says as he laughs, pointing to his own head, clearly mocking your injury.")
    racechoice = easygui.buttonbox("'Well " + p.name + ", Of what birth do you originate? Your life presence seems too complex to guess...' He says. Is he some kind of wizard? Life sense? How can he feel my life sense?", "TUDC",
                      ["Human", "Elf", "Dwarf", "Lyzard"])
    if racechoice == "Human":
        p.race = human
        easygui.msgbox("You get a health bonus of " + str(human.hpbonus))
    if racechoice == "Elf":
        p.race = elf
        easygui.msgbox("You get a health bonus of " + str(elf.hpbonus))
    if racechoice == "Dwarf":
        p.race = dwarf
        easygui.msgbox("You get a health bonus of " + str(dwarf.hpbonus))
    if racechoice == "Lyzard":
        p.race = lyzard
        easygui.msgbox("You get a health bonus of " + str(lyzard.hpbonus))
    easygui.msgbox("'Oh is that so? " + p.name + " The " + p.race.name + ", you are known as?' The man chuckled. 'Well, That sounds like a name to be remembered...'")
    lifechoice = easygui.buttonbox("The man softly draws back, and gently asks me, 'What do you seek to accomplish here in the land of Ramera?'. I had no idea, about anything. I better decide fast. 'I'll trust my gut' you think to yourself.", "TUDC",
                      ["Adventure", "Conquer", "Merchant"])
    if lifechoice == "Adventure":
        easygui.msgbox("A very stable fellow you seem to be, " + p.name + "...")
        easygui.msgbox("You've gained +1 to every life stature!")
        p.strength += 1
        p.dexterity += 1
        p.constitution += 1
        p.charisma += 1
        p.wisdom += 1
    if lifechoice == "Conquer":
        easygui.msgbox("A passion for power brings fame and many riches, be careful, as many will test your worth!")
        easygui.msgbox("You've gained +2 to Strength and Consitution, and +1 to Dexterity")
        p.strength += 2
        p.constitution += 2
        p.dexterity += 1
    if lifechoice == "Merchant":
        easygui.msgbox("A simple life's satisfaction and glory is often one overlooked...")
        easygui.msgbox("You've gained +3 to Charisma, and +2 to Wisdom!")
        p.charisma += 3
        p.wisdom += 2
    easygui.msgbox("Well friend, I found you washed ashore the crather castle beach with a minor wound to the head, give yourself some time. You reside in " + p.mainlocation.tavern.name + ". Here take this for safe journey...")
    p.mainweapon = Give_Weapon(c)
    p.armor = Give_Armor(cc)
    player.checkStats()






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
    armor1 = Armor(m.adropconfig[0], m.adropconfig[1], m.adropconfig[2], m.adropconfig[3])
    return armor1
    easygui.msgbox("You have equipped new armor!")
####
def Start_Fight():
    myMonster = Generate_Monster(player.location.monster[0])
    easygui.msgbox("You have encountered a level " + str(myMonster.level) + " " + myMonster.name + "!")
    while myMonster.health != "Dead":
        easygui.msgbox("You hit the monster!")
        player.Hit(myMonster)
        if myMonster.health <= 0:
            easygui.msgbox("You have killed the " + myMonster.name)
            player.mainweapon = Generate_Weapon(myMonster)
            if myMonster.name == "Void Lord":
                achoice = easygui.buttonbox("The " + myMonster.name + " dropped legendary armor: " + myMonster.adropconfig[0] + ". Would you like to equip it now?", "Rare Loot",
                                            ["Yes", "No"])
                if achoice == "Yes":
                    player.armor = Generate_Armor(myMonster)
                else:
                    easygui.msgbox("You have chosen to give up the legendary item!")

            player.xp += myMonster.xpdrop
            player.checkStats()
            player.checkQuest(myMonster)
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
    def __init__(self, name, race, profession, level, gold, health, maxhealth, inventory, mainweapon, mainlocation, location, age, strength, dexterity, wisdom, constituion, charisma, xp, max_xp, statpoints, armor, quest):
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
        self.location = location
        self.age = age
        self.strength = strength
        self.dexterity = dexterity
        self. wisdom = wisdom
        self. constitution = constituion
        self.charisma = charisma
        self.xp = xp
        self.max_xp = max_xp
        self.statpoints = statpoints
        self.armor = armor
        self.quest = quest

    def checkStats(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.max_xp = self.max_xp*1.5
            self.statpoints += 1
            self.xp = 0
            self.max_xp = int(self.max_xp)
            easygui.msgbox("You have leveled up! You are now level " + str(self.level) +", and have also gained a stat point to spend!")
            easygui.msgbox("You only have " + str((self.max_xp - self.xp)) + " Experience points to go before you level up!")
        else:
            easygui.msgbox("You only have " + str((self.max_xp-self.xp)) + " Experience points to go before you level up!")
        self.maxhealth = self.race.hpbonus + (self.constitution*10)
        self.health = self.maxhealth
    def checkQuest(self, m):
        if self.quest.target_objective == (m.name):
            self.quest.current += 1
            print "added to quest obective - TESTING" #Bug testing
            print self.quest.current
            print "needed: " + str(self.quest.goal)
            if self.quest.current >= self.quest.goal:
                easygui.msgbox("You have completed your quest! You should return and receive your rewards!")


    def Hit(self, m):
        #here we are going to make the function to hit the monster, so we can call it during game
        m.health = m.health - (self.mainweapon.damage+self.strength)
        easygui.msgbox("You swing at the monster and deal " + str(self.mainweapon.damage+self.strength) + " damage!")
        ##if player.damagedealt < 0: #making sure that we never do negative damage    ############## I COMMENTED THIS OUT BECAUSE NOW DAMAGE SHOULD NEVER BE NEGATIVE DUE TO THE NEW DAMAGE_BUFFER CALCULATIONS - SCORE!                                                                     
        ##  damagedealt = 0                                                                                                                             
    
    def explore(self):
      encounterChance = random.randint(1, 10)
      if encounterChance <= player.location.monster_rating:
        Start_Fight()
        
player = Humanoid(None, None, None, 1, 0, 0, 0, [], None, None, None, None, 1, 1, 1, 1, 1, 1, 10, 5, None, None)


#######Creation of Objects#######



##########################---ELEMENTAL TYPES---########################
fire_element = Elemental_Type("Fire", 1)
water_element = Elemental_Type("Water", 1)
darkness_element = Elemental_Type("Darkness", 1)
Brightness_element = Elemental_Type("Brightness", 1)




##########################---ENHANCEMENTS---###########################
####MONSTER ENHANCEMENTS
flesh = Monster_Enhancement("Flesh", 0, water_element, fire_element )


##############---PROFESSIONS---######################

##############--- QUESTS ---############################
quest_kill10skeletons = Quest("Clearing the boneyard", "Well, as you may have heard, skeletons are ammassing in the Crather Dungeon...", "They have been relentlessly slaughtering villagers, or any livestock that dares near the area",
                              "Unfortunately I do not have the skill or the aptitude to take care of this myself...", None, None, None, None, None, None, None, "Kill 3 Creaking Skeletons", "Creaking Skeleton", 3, 0, False)
quest_killvoidlord = Quest("The Void Lord", "Oh heavens, what are we going to do?", "There is a dark Lord that is summoning demons across the land! He resides in the Msnor!", "He must be stopped! The entire world of Ramera is resting in his hands!",
                           None, None, None, None, None, None, None, "Kill the Void Lord", "Void Lord", 1, 0, False)
quest_killwildabeast = Quest("Hunt or be Hunted", "Traveler! Would ya like to main some coin?", "There is a wildabeast about. You can find him in the -", "He is quite the challenge. Bring me his head and 500 gold will be yours",
                             None, None, None, None, None, None, None, "Hunt and kill the Wildabeast", "Wildabeast", 1, 0, False)
##########################----WEAPONS----###############################

##Object rules ----


##########################---ATTACK TYPES---########################### (Name, desc1, desc2, desc3, dmg, dmgbuffer)
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
voidlord_breed = MonsterBreed("Void Lord", demonize, stress_mind, manipulate, void_ball, blood_curdle, darkness_element) #Boss
wildabeast_breed = MonsterBreed("Wildabeast", claw, bite, trip, claw_bite, trip, fire_element) #Boss




#########################----LOCATION ASSETS----#########################

      #######SHOPS#######
crathershop = Shop("Crather Castle Market", ["Iron Longsword", 3, 3, 1, 30, 5], ["Iron Spear", 3, 3, 1, 30, 5])
fellrykeshop = Shop("FellRyke Spire Market", ["Iron Spear", 3, 3, 1, 30, 5], ["Iron Hammer", 3, 3, 1, 30, 5])
darlekshop = Shop("Darlek Black Market", ["Iron Spear", 3, 3, 1, 30, 5], ["Iron Hammer", 3, 3, 1, 30, 5])


####### NPCs


####CRATHER TAVERN
greji_stormbeard = NPC("Greji Stormbeard", "Greetings Adventurer! You seem new to Remera! Sit down and enjoy a drink!", None)
reyla_crosser = NPC("Reyla Crosser", "Mmm, Hello there friend... I've had quite a bit to drink, do you mind taking care of something for me?", quest_kill10skeletons)
####FELLRYKE TAVERN
mystic_grear = NPC("Mystic Grear", "'Hello...' the mystic says as he stares blankly into your eyes...", None)
jarvek_hurf = NPC("Jarvek Hurf", "Interesting, my mind affecting magic seems to be warded against you... come hither, breahting life-source...", quest_killvoidlord)
####DARLEK TAVERN
samuel_farwell = NPC("Samuel Farmwell", "Move along... You have no business speaking to me.", None)
harold_campen = NPC("Harold Campen", "Aha! You look like somebody that could use some work... Come... Sit with me...", quest_killwildabeast)


      #######TAVERNS#####
crathertavern = Tavern("Crather Castle Tavern", greji_stormbeard, reyla_crosser, "Towns folk dance and sing, farmers smoke lempus, and guards rejoice in the King's glory. Happiness exudes from the enviroment...")
fellryketavern = Tavern("FellRyke Spire Tavern", mystic_grear, jarvek_hurf, "A dark, mysterious aura exudes from everyone here... Not many people talking, and there is no bard to make music... The silence is not calming...")
darlektavern = Tavern("Darlek Crowded Tavern", samuel_farwell, harold_campen, "Theives, murderers, and bandits crowd together in the tavern, many looking your way is if you're prey... Best stick to myself here...")



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
voidlord_conifg = ["Void Lord", 1, 1, 1, 1, 1, voidlord_breed, 1, None, None, None]
wildabeast_conifg = ["Wildabeast", 1, 1, 1, 1, 1, wildabeast_breed, 1, None, None, None]


###CRATHER CASTLE

#########################----SUB LOCATIONS----##########################
cratherdungeon = SubLocation("Crather Castle Dungeon", None, 3, [cratherruins_skeleton_config])
cratherplains = SubLocation("Crather Plains", None, 3, [cratherplains_goblin_config])
cratherruins = SubLocation("Crather Ruins", None, 5, [cratherruins_skeleton_config])
fellrykemanor = SubLocation("FellRyke Manor", None, 5, [fellrykemanor_bloodwizard_config])
fellrykemagetower = SubLocation("FellRyke Mage Tower", None, 5, [voidlord_conifg])
fellrykegraveyard = SubLocation("FellRyke Grave Yard", None, 5, [fellrykegraveyard_necromancer_config])
darlekhideout = SubLocation("Darlek Rogue Hideout", None, 5, [fellrykegraveyard_necromancer_config])
darlekcave = SubLocation("Darlek Cave", None, 5, [fellrykegraveyard_necromancer_config])
darlekdeepwoods = SubLocation("Darlek Deep Woods", None, 5, [wildabeast_conifg])


#########################----LOCATIONS----##############################
crathercastle = Location("Crather Castle", crathertavern, crathershop, cratherdungeon, cratherplains, cratherruins)
fellrykespire = Location("FellRyke Spire", fellryketavern, fellrykeshop, fellrykemanor, fellrykemagetower, fellrykegraveyard)
darlekwoodlands = Location("Darlek Woodlands", darlektavern, darlekshop, darlekhideout, darlekcave, darlekdeepwoods)

Sw_Weapon = ["Rusty Dagger", 1, 1, 1, 100, 1]
Sa_Armor = ["Torn Leather Armor", 10, 1, flesh]


###For testing purposes these initial stats will be hardcoded // This is just to give our player a weapon to test combat with 





