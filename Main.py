import Assets
import easygui
from easygui import *


enginecheck = 1.5


def mainEngine():
    mainmenu = 0
    while mainmenu != "Quit":
        mainmenu = easygui.buttonbox(
            "Location: " + Assets.Object_Creation.player.location.name + ". Year: " + str(Assets.Object_Creation.game_clock.year) + ". Day: " + str(Assets.Object_Creation.game_clock.day) +
            ". Time: " + Assets.Object_Creation.game_clock.time + ". What would you like to do?",
            "The Ultimate Dungeon Crawler",
            ["Explore", "Shop", "Tavern", "Travel", "Save", "View Character", "Quit To Menu"])
        if mainmenu == "Explore":
            explorechoice = easygui.buttonbox("Where would you like to explore?", "The Ultimate Dungeon Crawler",
                              [Assets.Object_Creation.player.mainlocation.sub1.name, Assets.Object_Creation.player.mainlocation.sub2.name, Assets.Object_Creation.player.mainlocation.sub3.name])
            if explorechoice == Assets.Object_Creation.player.mainlocation.sub1.name:
                Assets.Object_Creation.player.location = Assets.Object_Creation.player.mainlocation.sub1
                Assets.Object_Creation.player.explore()
                campchoice = None
                while campchoice != "Return to Town":
                    campchoice = easygui.buttonbox("You venture your way to the " + explorechoice,
                                                   "The Ultimate Dungeon Crawler",
                                                   ["Take a closer look around", "Camp", "Return to Town"])
                    if campchoice == "Take a closer look around":
                        easygui.msgbox("You take a closer look around")
                    if campchoice == "Camp":
                        easygui.msgbox("You set up camp, and attempt to rest for a turn...")
                        Assets.Object_Creation.player.explore()
                        easygui.msgbox("You finish resting")
                    if campchoice == "Return to Town":
                        easygui.msgbox("You pack your things and set out to Town")
                    Assets.Object_Creation.game_clock.checkDate()
            if explorechoice == Assets.Object_Creation.player.mainlocation.sub2.name:
                Assets.Object_Creation.player.location = Assets.Object_Creation.player.mainlocation.sub2
                Assets.Object_Creation.player.explore()
                campchoice = None
                while campchoice != "Return to Town":
                    campchoice = easygui.buttonbox("You venture your way to the " + explorechoice,
                                                   "The Ultimate Dungeon Crawler",
                                                   ["Take a closer look around", "Camp", "Return to Town"])
                    if campchoice == "Take a closer look around":
                        easygui.msgbox("You take a closer look around")
                    if campchoice == "Camp":
                        easygui.msgbox("You set up camp, and attempt to make it through the night alive...")
                        Assets.Object_Creation.player.explore()
                        easygui.msgbox("You make it through the night alive")
                    if campchoice == "Return to Town":
                        easygui.msgbox("You pack your things and set out to Town")
                    Assets.Object_Creation.game_clock.checkDate()
            if explorechoice == Assets.Object_Creation.player.mainlocation.sub3.name:
                Assets.Object_Creation.player.location = Assets.Object_Creation.player.mainlocation.sub3
                Assets.Object_Creation.player.explore()
                campchoice = None
                while campchoice != "Return to Town":
                    campchoice = easygui.buttonbox("You venture your way to the " + explorechoice,
                                                   "The Ultimate Dungeon Crawler",
                                                   ["Take a closer look around", "Camp", "Return to Town"])
                    if campchoice == "Take a closer look around":
                        easygui.msgbox("You take a closer look around")
                    if campchoice == "Camp":
                        easygui.msgbox("You set up camp, and attempt to make it through the night alive...")
                        Assets.Object_Creation.player.explore()
                        easygui.msgbox("You make it through the night alive")
                    if campchoice == "Return to Town":
                        easygui.msgbox("You pack your things and set out to Town")
                    Assets.Object_Creation.game_clock.checkDate()



        if mainmenu == "Shop":
            Assets.Object_Creation.Start_Shop()
        if mainmenu == "View Character":
            Assets.Object_Creation.View_Character(Assets.Object_Creation.player)
        if mainmenu == "Tavern":
            easygui.msgbox("You walk into the tavern to see the hustle of many townsfolk")
        if mainmenu == "Travel":
            travelchoice = easygui.choicebox("Where would you like to travel?", "TUDC",
                              ["Crather Castle", "FellRyke Spire", "Darlek Woodlands"])
            if travelchoice == "Crather Castle":
                Assets.Object_Creation.player.mainlocation = Assets.Object_Creation.crathercastle
            if travelchoice == "FellRyke Spire":
                Assets.Object_Creation.player.mainlocation = Assets.Object_Creation.fellrykespire
            if travelchoice == "Darlek Woodlands":
                Assets.Object_Creation.player.mainlocation = Assets.Object_Creation.darlekwoodlands
            easygui.msgbox("You have arrived at " + Assets.Object_Creation.player.mainlocation.name + " !")
            Assets.Object_Creation.game_clock.checkDate()
        if mainmenu == "Save":
            easygui.msgbox("You just saved your game!")
            Assets.Object_Creation.game_clock.checkDate()
        if mainmenu == "Quit To Menu":
            break
        Assets.Object_Creation.player.location = Assets.Object_Creation.player.mainlocation

def loadGame():
    easygui.msgbox("This is where you will select a save!")
    mainEngine()


def viewCharacter():
    easygui.msgbox("Here you will select your characters!")
    charchoice = None
    while charchoice != "Back":
        option = easygui.buttonbox("Please select a character!", "v0.01",
                                   ["Character 1", "Character 2", "Character 3", "Back"])
        easygui.msgbox("You have made a selection!")
        if option == "Back":
            charchoice = "Back"


def newCharacter():
    Assets.Object_Creation.Roll_Initial_Stats(Assets.Object_Creation.player)
    Assets.Object_Creation.Create_Character(Assets.Object_Creation.player, Assets.Object_Creation.Sw_Weapon, Assets.Object_Creation.Sa_Armor)
    mainEngine()


while enginecheck != "Quit":
    choice = buttonbox("Welcome to TUDC!", "v0.01",
                       ["New Character", "Load Game", "Quit"])
    if choice == "Quit":
        break
    if choice == "Load Game":
        loadGame()
    if choice == "New Character":
        newCharacter()
