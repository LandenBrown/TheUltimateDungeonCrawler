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

                        if accept == "No":
                                easygui.msgbox("You have declined the quest!")





		


			

##### FUTURE CHANGES - MAKE ENHANCEMENTS MODIFY THE DAMAGE BUFFER AND THE SWING BUFFER
