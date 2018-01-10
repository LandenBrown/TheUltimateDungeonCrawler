import easygui
from easygui import *



class NPC:
        def __init__(self, name, intro, quest):
                self.name = name
                self.intro = intro
                self.quest = quest

        def Quest_Dialogue(self, p):
                easygui.msgbox(self.quest.d1)
                if self.quest.d2 != None:
                        easygui.msgbox(self.quest.d2)
                if self.quest.d3 != None:
                        easygui.msgbox(self.quest.d3)
                if self.quest.d4 != None:
                        easygui.msgbox(self.quest.d4)
                if self.quest.d5 != None:
                        easygui.msgbox(self.quest.d5)
                if self.quest.d6 != None:
                        easygui.msgbox(self.quest.d6)
                if self.quest.d7 != None:
                        easygui.msgbox(self.quest.d7)
                if self.quest.d8 != None:
                        easygui.msgbox(self.quest.d8)
                if self.quest.d9 != None:
                        easygui.msgbox(self.quest.d89)
                if self.quest.d10 != None:
                        easygui.msgbox(self.quest.d10)
                if self.quest.complete != True:
                        if p.quest != self.quest:
                                accept = easygui.buttonbox("Would you please help me " + self.quest.target + "?", "Quest",
                                                        ["Yes", "No"])
                                if accept == "Yes":
                                        easygui.msgbox("You have just accepted a quest to " + self.quest.target)
                                        p.quest = self.quest
                                        self.quest.d1 = "Oh, " + p.name + "! Did you " + self.quest.target + " yet?"
                                        self.quest.d2 = None
                                        self.quest.d3 = None
                                        self.quest.d4 = None
                                        self.quest.d5 = None
                                        self.quest.d6 = None
                                        self.quest.d7 = None
                                        self.quest.d8 = None
                                        self.quest.d9 = None
                                        self.quest.d10 = None
                                        p.quest.current = 0

                                if accept == "No":
                                        easygui.msgbox("You have declined the quest!")

                if p.quest != None:
                        if p.quest.current >= p.quest.goal:
                                easygui.msgbox("Ah! You have completed my quest! Thank you so much! Here is your reward!")
                                self.quest.complete = True
                                self.quest.d1 = "You have the ability to really make something of yourself someday. I will contact you if I ever need you again. Thank you."
                                p.quest = None






		


			

##### FUTURE CHANGES - MAKE ENHANCEMENTS MODIFY THE DAMAGE BUFFER AND THE SWING BUFFER
