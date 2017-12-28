import time, math, os, easygui
from easygui import *
from Assets import *
enginecheck = 1.5

def mainEngine():
    easygui.msgbox("You have started the main engine!")
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
    easygui.msgbox("Here you will be able to create a new character!");
        

while enginecheck != "Quit":
    choice = buttonbox("Welcome to TUDC!", "v0.01",
                       ["Play Game", "Load Game", "View Character", "New Character", "Quit"])
    if choice == "Quit":
        enginecheck = "Quit"
    if choice == "Play Game":
        mainEngine()
    if choice == "Load Game":
        loadGame()
    if choice == "View Character":
        viewCharacter()
    if choice == "New Character":
        newCharacter()


                    
