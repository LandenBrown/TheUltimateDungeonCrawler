import Assets
import easygui
from easygui import *


enginecheck = 1.5


def mainEngine():
    mainmenu = 0
    while mainmenu != "Quit":
        mainmenu = easygui.buttonbox(
            "Location: " + Assets.Object_Creation.player.location.name + ". What would you like to do?",
            "The Ultimate Dungeon Crawler",
            ["Explore", "Shop", "Tavern", "Save", "Quit To Menu"])
        if mainmenu == "Explore":
            easygui.buttonbox("Where would you like to explore?", "The Ultimate Dungeon Crawler",
                              ["empty"])
        if mainmenu == "Shop":
            easygui.msgbox("What would you like to buy?")
        if mainmenu == "Tavern":
            easygui.msgbox("You walk into the tavern to see the hustle of many townfolk")
        if mainmenu == "Save":
            easygui.msgbox("You just saved your game!")
        if mainmenu == "Quit To Menu":
            break


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
    easygui.msgbox("Here you will be able to create a new character!")


while enginecheck != "Quit":
    choice = buttonbox("Welcome to TUDC!", "v0.01",
                       ["Play Game", "Load Game", "View Character", "New Character", "Quit"])
    if choice == "Quit":
        break
    if choice == "Play Game":
        mainEngine()
    if choice == "Load Game":
        loadGame()
    if choice == "View Character":
        viewCharacter()
    if choice == "New Character":
        newCharacter()
