"""CLASS GUI EXAMPLE"""
# =============================================================================
# from tkinter import *
# import random
# 
# class GUIDie(Canvas):
#     '''6-sided Die class for GUI'''
# 
#     def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
#         '''GUIDie(master,[valueList,colorList]) -> GUIDie
#         creates a GUI 6-sided die
#           valueList is the list of values (1,2,3,4,5,6 by default)
#           colorList is the list of colors (all black by default)'''
#         # create a 60x60 white canvas with a 5-pixel grooved border
#         Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
#         # store the valuelist and colorlist
#         self.valueList = valueList
#         self.colorList = colorList
#         # initialize the top value
#         self.top = 1
# 
#     def get_top(self):
#         '''GUIDie.get_top() -> int
#         returns the value on the die'''
#         return self.valueList[self.top - 1]
# 
#     def roll(self):
#         '''GUIDie.roll()
#         rolls the die'''
#         self.top = random.randrange(1, 7)
#         self.draw()
# 
#     def draw(self):
#         """GUIDie.draw()
#         draws the pips on the die"""
#         # clear old pips first
#         self.erase()
#         # location of which pips should be drawn
#         pipList = [
#             [(1, 1)],
#             [(0, 0), (2, 2)],
#             [(0, 0), (1, 1), (2, 2)],
#             [(0, 0), (0, 2), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
#         ]
#         for location in pipList[self.top - 1]:
#             self.draw_pip(location, self.colorList[self.top - 1])
# 
#     def draw_pip(self, location, color):
#         '''GUIDie.draw_pip(location,color)
#         draws a pip at (row,col) given by location, with given color'''
#         (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
#         self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)
# 
#     def erase(self):
#         '''GUIDie.erase()
#         erases all the pips'''
#         pipList = self.find_all()
#         for pip in pipList:
#             self.delete(pip)
# 
# class Decath400MFrame(Frame):
#     '''frame for a game of 400 Meters'''
# 
#     def __init__(self, master, name):
#         '''Decath400MFrame(master,name) -> Decath400MFrame
#         creates a new 400 Meters frame
#         name is the name of the player'''
#         # set up Frame object
#         Frame.__init__(self, master)
#         self.grid()
#         # label for player's name
#         Label(self, text=name, font=('Arial', 18)).grid(columnspan=3, sticky=W)
#         # set up score and rerolls
#         self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 18))
#         self.scoreLabel.grid(row=0, column=3, columnspan=2)
#         self.rerollLabel = Label(self, text='Rerolls: 5', font=('Arial', 18))
#         self.rerollLabel.grid(row=0, column=5, columnspan=3, sticky=E)
#         # initialize game data
#         self.score = 0
#         self.rerolls = 5
#         self.gameround = 0
#         # set up dice
#         self.dice = []
#         for n in range(8):
#             self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, -6], ['black'] * 5 + ['red']))
#             self.dice[n].grid(row=1, column=n)
#         # set up buttons
#         self.rollButton = Button(self, text='Roll', command=self.roll)
#         self.rollButton.grid(row=2, columnspan=2)
#         self.keepButton = Button(self, text='Keep', state=DISABLED, command=self.keep)
#         self.keepButton.grid(row=3, columnspan=2)
# 
#     def roll(self):
#         '''Decath400MFrame.roll()
#         handler method for the roll button click'''
#         # roll both dice
#         self.dice[2 * self.gameround].roll()
#         self.dice[2 * self.gameround + 1].roll()
#         # if this was the first roll of the round, turn on the keep button
#         if self.keepButton['state'] == DISABLED:
#             self.keepButton['state'] = ACTIVE
#         else:  # otherwise we just spent a reroll
#             self.rerolls -= 1
#             self.rerollLabel['text'] = 'Rerolls: {}'.format(self.rerolls)
#         if self.rerolls == 0:  # no rerolls left, so turn off roll button
#             self.rollButton['state'] = DISABLED
# 
#     def keep(self):
#         '''Decath400MFrame.keep()
#         handler method for the keep button click'''
#         # add dice to score and update the scoreboard
#         self.score += self.dice[2 * self.gameround].get_top() + \
#                       self.dice[2 * self.gameround + 1].get_top()
#         self.scoreLabel['text'] = 'Score: {}'.format(self.score)
#         self.gameround += 1  # go to next round
#         if self.gameround < 4:  # move buttons to next pair of dice
#             self.rollButton.grid(row=2, column=2 * self.gameround, columnspan=2)
#             self.keepButton.grid(row=3, column=2 * self.gameround, columnspan=2)
#             self.rollButton['state'] = ACTIVE
#             self.keepButton['state'] = DISABLED
#         else:  # game over
#             self.keepButton.grid_remove()
#             self.rollButton.grid_remove()
#             self.rerollLabel['text'] = 'Game over'
# 
# # play the game
# name = input("Enter your name: ")
# root = Tk()
# root.title('400 Meters')
# game = Decath400MFrame(root, name)
# game.mainloop()
# =============================================================================
"""PROBLEMS"""
# =============================================================================
# from tkinter import *
# import random
# 
# class GUIDie(Canvas):
#     '''6-sided Die class for GUI'''
# 
#     def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
#         '''GUIDie(master,[valueList,colorList]) -> GUIDie
#         creates a GUI 6-sided die
#           valueList is the list of values (1,2,3,4,5,6 by default)
#           colorList is the list of colors (all black by default)'''
#         # create a 60x60 white canvas with a 5-pixel grooved border
#         Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
#         # store the valuelist and colorlist
#         self.valueList = valueList
#         self.colorList = colorList
#         # initialize the top value
#         self.top = 1
# 
#     def get_top(self):
#         '''GUIDie.get_top() -> int
#         returns the value on the die'''
#         return self.valueList[self.top - 1]
# 
#     def roll(self):
#         '''GUIDie.roll()
#         rolls the die'''
#         self.top = random.randrange(1, 7)
#         self.draw()
# 
#     def draw(self):
#         """GUIDie.draw()
#         draws the pips on the die"""
#         # clear old pips first
#         self.erase()
#         # location of which pips should be drawn
#         pipList = [
#             [(1, 1)],
#             [(0, 0), (2, 2)],
#             [(0, 0), (1, 1), (2, 2)],
#             [(0, 0), (0, 2), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
#         ]
#         for location in pipList[self.top - 1]:
#             self.draw_pip(location, self.colorList[self.top - 1])
# 
#     def draw_pip(self, location, color):
#         '''GUIDie.draw_pip(location,color)
#         draws a pip at (row,col) given by location, with given color'''
#         (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
#         self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)
# 
#     def erase(self):
#         '''GUIDie.erase()
#         erases all the pips'''
#         pipList = self.find_all()
#         for pip in pipList:
#             self.delete(pip)
# 
# class Decath100MFrame(Frame):
#     '''frame for a game of 100 Meters'''
# 
#     def __init__(self, master, name):
#         '''Decath100MFrame(master,name) -> Decath400MFrame
#         creates a new 400 Meters frame
#         name is the name of the player'''
#         # set up Frame object
#         Frame.__init__(self, master)
#         self.grid()
#         # label for player's name
#         Label(self, text=name, font=('Arial', 18)).grid(columnspan=3, sticky=W)
#         # set up score and rerolls
#         self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 18))
#         self.scoreLabel.grid(row=0, column=3, columnspan=2)
#         self.rerollLabel = Label(self, text='Rerolls: 5', font=('Arial', 18))
#         self.rerollLabel.grid(row=0, column=5, columnspan=3, sticky=E)
#         # initialize game data
#         self.score = 0
#         self.rerolls = 5
#         self.gameround = 0
#         # set up dice
#         self.dice = []
#         for n in range(8):
#             self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, -6], ['black'] * 5 + ['red']))
#             self.dice[n].grid(row=1, column=n)
#         # set up buttons
#         self.rollButton = Button(self, text='Roll', command=self.roll)
#         self.rollButton.grid(row=2, columnspan=2)
#         self.keepButton = Button(self, text='Keep', state=DISABLED, command=self.keep)
#         self.keepButton.grid(row=3, columnspan=2)
# 
#     def roll(self):
#         '''Decath100MFrame.roll()
#         handler method for the roll button click'''
#         # roll both dice
#         self.dice[2 * self.gameround].roll()
#         self.dice[2 * self.gameround + 1].roll()
#         # if this was the first roll of the round, turn on the keep button
#         if self.keepButton['state'] == DISABLED:
#             self.keepButton['state'] = ACTIVE
#         else:  # otherwise we just spent a reroll
#             self.rerolls -= 1
#             self.rerollLabel['text'] = 'Rerolls: {}'.format(self.rerolls)
#         if self.rerolls == 0:  # no rerolls left, so turn off roll button
#             self.rollButton['state'] = DISABLED
# 
#     def keep(self):
#         '''Decath100MFrame.keep()
#         handler method for the keep button click'''
#         # add dice to score and update the scoreboard
#         self.score += self.dice[2 * self.gameround].get_top() + \
#                       self.dice[2 * self.gameround + 1].get_top()
#         self.scoreLabel['text'] = 'Score: {}'.format(self.score)
#         self.gameround += 1  # go to next round
#         if self.gameround < 2:  # move buttons to next pair of dice
#             self.rollButton.grid(row=2, column=2 * self.gameround, columnspan=2)
#             self.keepButton.grid(row=3, column=2 * self.gameround, columnspan=2)
#             self.rollButton['state'] = ACTIVE
#             self.keepButton['state'] = DISABLED
#         else:  # game over
#             self.keepButton.grid_remove()
#             self.rollButton.grid_remove()
#             self.rerollLabel['text'] = 'Game over'
# 
# # play the game
# name = input("Enter your name: ")
# root = Tk()
# root.title('100 Meters')
# game = Decath100MFrame(root, name)
# game.mainloop()
# 
# =============================================================================
# =============================================================================
# from tkinter import *
# import random
# 
# class GUIDie(Canvas):
#     '''6-sided Die class for GUI'''
# 
#     def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
#         '''GUIDie(master,[valueList,colorList]) -> GUIDie
#         creates a GUI 6-sided die
#           valueList is the list of values (1,2,3,4,5,6 by default)
#           colorList is the list of colors (all black by default)'''
#         # create a 60x60 white canvas with a 5-pixel grooved border
#         Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
#         # store the valuelist and colorlist
#         self.valueList = valueList
#         self.colorList = colorList
#         # initialize the top value
#         self.top = 1
# 
#     def get_top(self):
#         '''GUIDie.get_top() -> int
#         returns the value on the die'''
#         return self.valueList[self.top - 1]
# 
#     def roll(self):
#         '''GUIDie.roll()
#         rolls the die'''
#         self.top = random.randrange(1, 7)
#         self.draw()
# 
#     def draw(self):
#         """GUIDie.draw()
#         draws the pips on the die"""
#         # clear old pips first
#         self.erase()
#         # location of which pips should be drawn
#         pipList = [
#             [(1, 1)],
#             [(0, 0), (2, 2)],
#             [(0, 0), (1, 1), (2, 2)],
#             [(0, 0), (0, 2), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
#         ]
#         for location in pipList[self.top - 1]:
#             self.draw_pip(location, self.colorList[self.top - 1])
# 
#     def draw_pip(self, location, color):
#         '''GUIDie.draw_pip(location,color)
#         draws a pip at (row,col) given by location, with given color'''
#         (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
#         self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)
# 
#     def erase(self):
#         '''GUIDie.erase()
#         erases all the pips'''
#         pipList = self.find_all()
#         for pip in pipList:
#             self.delete(pip)
# 
# class Decath1500MFrame(Frame):
#     '''frame for a game of 1500 Meters'''
# 
#     def __init__(self, master, name):
#         '''Decath1500MFrame(master,name) -> Decath1500MFrame
#         creates a new 1500 Meters frame
#         name is the name of the player'''
#         # set up Frame object
#         Frame.__init__(self, master)
#         self.grid()
#         # label for player's name
#         Label(self, text=name, font=('Arial', 18)).grid(columnspan=3, sticky=W)
#         # set up score and rerolls
#         self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 18))
#         self.scoreLabel.grid(row=0, column=3, columnspan=2)
#         self.rerollLabel = Label(self, text='Rerolls: 5', font=('Arial', 18))
#         self.rerollLabel.grid(row=0, column=5, columnspan=3, sticky=E)
#         # initialize game data
#         self.score = 0
#         self.rerolls = 5
#         self.gameround = 0
#         # set up dice
#         self.dice = []
#         for n in range(8):
#             self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, -6], ['black'] * 5 + ['red']))
#             self.dice[n].grid(row=1, column=n)
#         # set up buttons
#         self.rollButton = Button(self, text='Roll', command=self.roll)
#         self.rollButton.grid(row=2, columnspan=2)
#         self.keepButton = Button(self, text='Keep', state=DISABLED, command=self.keep)
#         self.keepButton.grid(row=3, columnspan=2)
# 
#     def roll(self):
#         '''Decath1500MFrame.roll()
#         handler method for the roll button click'''
#         # roll both dice
#         self.dice[self.gameround].roll()
#         # if this was the first roll of the round, turn on the keep button
#         if self.keepButton['state'] == DISABLED:
#             self.keepButton['state'] = ACTIVE
#         else:  # otherwise we just spent a reroll
#             self.rerolls -= 1
#             self.rerollLabel['text'] = 'Rerolls: {}'.format(self.rerolls)
#         if self.rerolls == 0:  # no rerolls left, so turn off roll button
#             self.rollButton['state'] = DISABLED
# 
#     def keep(self):
#         '''Decath1500MFrame.keep()
#         handler method for the keep button click'''
#         # add dice to score and update the scoreboard
#         self.score += self.dice[self.gameround].get_top()
#         self.scoreLabel['text'] = 'Score: {}'.format(self.score)
#         self.gameround += 1  # go to next round
#         if self.gameround < 8:  # move buttons to next pair of dice
#             self.rollButton.grid(row=2, column=self.gameround, columnspan=2)
#             self.keepButton.grid(row=3, column=self.gameround, columnspan=2)
#             self.rollButton['state'] = ACTIVE
#             self.keepButton['state'] = DISABLED
#         else:  # game over
#             self.keepButton.grid_remove()
#             self.rollButton.grid_remove()
#             self.rerollLabel['text'] = 'Game over'
# 
# # play the game
# name = input("Enter your name: ")
# root = Tk()
# root.title('1500 Meters')
# game = Decath1500MFrame(root, name)
# game.mainloop()
# =============================================================================
from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top - 1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1, 7)
        self.draw()

    def draw(self):
        """GUIDie.draw()
        draws the pips on the die"""
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [
            [(1, 1)],
            [(0, 0), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 0), (0, 2), (2, 0), (2, 2)],
            [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
            [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
        ]
        for location in pipList[self.top - 1]:
            self.draw_pip(location, self.colorList[self.top - 1])

    def draw_pip(self, location, color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
        self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class ShotPut(Frame):
    """represents a game of ShotPut"""
    
    def __init__(self, master, name):
        """ShotPut(master, name) -> ShotPut
        initializes a ShotPut game with master and player name"""
        Frame.__init__(self, master)
        self.grid()
        
        self.score = 0
        self.attempt = 1
        self.highScore = 0
        self.rollNumber = 0
        
        Label(self, text = name, font = ("Arial", 18)).grid(row = 0, columnspan = 2, sticky = W)
        self.scoreLabel = Label(self, text = f"Attempt #{self.attempt} Score: {self.score}", font = ("Arial", 18))
        self.scoreLabel.grid(row = 0, column = 2, columnspan = 4)
        self.highScoreLabel = Label(self, text = f"High Score: {self.highScore}", font = ("Arial", 18))
        self.highScoreLabel.grid(row = 0, column = 6, columnspan = 2, sticky = E)
        
        self.rollButton = Button(self, text = "Roll", command = self.roll)
        self.rollButton.grid(row = 2)
        self.stopButton = Button(self, text = "Stop", command = self.stop, state= DISABLED)
        self.stopButton.grid(row = 3)
        
        self.dice = []
        for i in range(8):
            self.dice.append(GUIDie(self, [1,2,3,4,5,6], ['red'] + ['black']*5))
            self.dice[i].grid(row = 1, column = i)
    
    def roll(self):
        """ShotPut.roll() -> None
        rolls a GUIDie"""
        self.dice[self.rollNumber].roll()
        self.stopButton['state'] = ACTIVE
        self.rollNumber += 1
        if (self.dice[self.rollNumber-1].get_top() ==1): #foul roll, reset score
            self.rollButton['state'] = DISABLED 
            self.stopButton['text'] = "FOUL"
            self.score = 0
            self.scoreLabel['text'] = "FOUL ATTEMPT"
        else: #valid roll, update score
            self.score += self.dice[self.rollNumber-1].get_top()
            self.scoreLabel['text'] = f"Attempt #{self.attempt} Score: {self.score}"
            
            if (self.rollNumber <8): #if more dice are left, move buttons
                self.rollButton.grid(row = 2, column = self.rollNumber)
                self.stopButton.grid(row=3, column = self.rollNumber)
            else: #no more rolls
                self.rollButton['state'] = DISABLED
        
    def stop(self):
        """ShotPut.stop() -> None
        stops an attempt"""
        self.attempt += 1
        self.highScore = max(self.highScore, self.score)
        self.highScoreLabel['text'] = f"High Score: {self.highScore}"
        if (self.attempt >3): 
            self.scoreLabel['text'] = "Game Over"
            self.stopButton.destroy()
            self.rollButton.destroy()
            return
        #Reset buttons and dice
        self.score = 0
        self.rollNumber = 0
        self.stopButton['text'] = "Stop"
        self.scoreLabel['text'] = f"Attempt #{self.attempt} Score: {self.score}"
        self.rollButton.grid(row = 2, column = 0)
        self.stopButton.grid(row = 3, column = 0)
        self.rollButton['state'] = ACTIVE
        self.stopButton['state'] = DISABLED
        for die in self.dice:
            die.erase()
        
        
root = Tk()
root.title("Shot Put")
name = input("Enter your name: ")
shot = ShotPut(root, name)
shot.mainloop()
        

# =============================================================================
# from tkinter import *
# import random
# 
# class GUIDie(Canvas):
#     '''6-sided Die class for GUI'''
# 
#     def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
#         '''GUIDie(master,[valueList,colorList]) -> GUIDie
#         creates a GUI 6-sided die
#           valueList is the list of values (1,2,3,4,5,6 by default)
#           colorList is the list of colors (all black by default)'''
#         # create a 60x60 white canvas with a 5-pixel grooved border
#         Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
#         # store the valuelist and colorlist
#         self.valueList = valueList
#         self.colorList = colorList
#         # initialize the top value
#         self.top = 1
# 
#     def get_top(self):
#         '''GUIDie.get_top() -> int
#         returns the value on the die'''
#         return self.valueList[self.top - 1]
# 
#     def roll(self):
#         '''GUIDie.roll()
#         rolls the die'''
#         self.top = random.randrange(1, 7)
#         self.draw()
# 
#     def draw(self):
#         """GUIDie.draw()
#         draws the pips on the die"""
#         # clear old pips first
#         self.erase()
#         # location of which pips should be drawn
#         pipList = [
#             [(1, 1)],
#             [(0, 0), (2, 2)],
#             [(0, 0), (1, 1), (2, 2)],
#             [(0, 0), (0, 2), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
#             [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
#         ]
#         for location in pipList[self.top - 1]:
#             self.draw_pip(location, self.colorList[self.top - 1])
# 
#     def draw_pip(self, location, color):
#         '''GUIDie.draw_pip(location,color)
#         draws a pip at (row,col) given by location, with given color'''
#         (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
#         self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)
# 
#     def erase(self):
#         '''GUIDie.erase()
#         erases all the pips'''
#         pipList = self.find_all()
#         for pip in pipList:
#             self.delete(pip)
# 
# class GUIFreezeableDie(GUIDie):
#     '''a GUIDie that can be "frozen" so that it can't be rolled'''
# 
#     def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
#         '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
#         creates a GUI 6-sided freeze-able die
#           valueList is the list of values (1,2,3,4,5,6 by default)
#           colorList is the list of colors (all black by default)'''
#         GUIDie.__init__(self, master, valueList, colorList)
#         self.isFrozen = False
# 
#     def is_frozen(self):
#         '''GUIFreezeableDie.is_frozen() -> bool
#         returns True if the die is frozen, False otherwise'''
#         return self.isFrozen
#     
#     def toggle_freeze(self):
#         '''GUIFreezeableDie.toggle_freeze()
#         toggles the frozen status'''
#         if (self.isFrozen):
#             self.isFrozen = False
#             self['bg'] = 'white'
#         else:
#             self.isFrozen = True
#             self['bg'] = 'grey'
# 
#     def roll(self):
#         '''GuiFreezeableDie.roll()
#         overloads GUIDie.roll() to not allow a roll if frozen'''
#         if (self.isFrozen):
#             return
#         GUIDie.roll(self)
# 
# class Discus(Frame):
#     """represents a game of Discus"""
#     
#     def __init__(self, master, name):
#         """Discus(master, name) -> Discus
#         initializes a game of Discus for player name"""
#         Frame.__init__(self, master)
#         self.grid()
#         
#         self.attempt = 1
#         self.score = 0
#         self.highScore = 0
#         self.firstRoll = True
#         self.frozenStates = [True]*5
#         
#         #Label args: master, text = , font = 
#         #grid args: row = , column = , columnspan = , sticky = 
#         #Button __Init__ args: master, text = , command = , state = DISABLED/ACTIVE
#         Label(self, text = f"{name}", font = ("Arial", 18)).grid(row =0, columnspan=2,sticky = W)
#         self.scoreLabel = Label(self, text = f"Attempt #{self.attempt} Score: {self.score}", font = ("Arial", 18))
#         self.scoreLabel.grid(row =0, column =2, columnspan=3)
#         self.highScoreLabel = Label(self, text = f"High Score: {self.highScore}", font = ("Arial", 18))
#         self.highScoreLabel.grid(row =0, column = 5, columnspan=2, sticky=E)
#         
#         self.dice = []
#         self.freezeButtons = []
#         for i in range(5):
#             self.dice.append(GUIFreezeableDie(self, valueList = [0,2,0,4,0,6], colorList = ['red', 'black']*3))
#             self.dice[i].grid(row=1, column=i)
#             self.freezeButtons.append(Button(self, text = "Freeze", command = self.dice[i].toggle_freeze, state = DISABLED))
#             self.freezeButtons[i].grid(row=2, column = i)
#         
#         self.rollButton = Button(self, text = "Roll", command = self.roll)
#         self.rollButton.grid(row = 1, column = 5, columnspan=2)
#         self.stopButton = Button(self, text = "Stop", command = self.stop, state = DISABLED)
#         self.stopButton.grid(row=2, column=5, columnspan=2)
#         self.descriptionLabel = Label(self, text = "Click Roll Button to start", font = ("Arial", 18))
#         self.descriptionLabel.grid(row=3, column = 1, columnspan=3)
#         
#     def stop(self):
#         """Discus.stop() -> None
#         stops the attempt and resets the widgets"""
#         self.attempt += 1
#         self.highScore = max(self.highScore, self.score)
#         self.highScoreLabel['text'] = f"High Score: {self.highScore}"
#         for but in self.freezeButtons:
#             but['state'] = DISABLED
#         
#         if (self.attempt >3):
#             self.scoreLabel['text'] = "Game over"
#             self.rollButton.destroy()
#             self.stopButton.destroy()
#             self.descriptionLabel.destroy()
#             return
#         #Reset for new attempt
#         for die in self.dice:
#             die.erase() 
#             if (die.is_frozen()):
#                 die.toggle_freeze()
#         self.score = 0
#         self.descriptionLabel['text'] = "Click Roll Button to start"
#         self.stopButton['state'] = DISABLED
#         self.stopButton['text'] = "Stop"
#         self.firstRoll = True
#         self.scoreLabel['text'] = f"Attempt #{self.attempt} Score: {self.score}"
#         self.rollButton['state'] = ACTIVE
#         
#         
#     def roll(self):
#         """Discus.roll() -> None
#         rolls dice in the game and update widgets"""
#         if (self.firstRoll): #first roll
#             self.firstRoll = False
#             for but in self.freezeButtons:
#                 but['state'] = ACTIVE
#             self.stopButton['state'] = ACTIVE
#         elif (self.frozenStates == [self.dice[i].is_frozen() for i in range(5)]): #need to freeze before rolling
#             self.descriptionLabel['text'] = "You need freeze a die before rerolling"
#             return
#         
#         for die in self.dice: #reroll
#             die.roll()
#             
#         if (self.check_foul()):
#             self.stopButton['text']= "Foul"
#             self.scoreLabel['text'] = "FOULED ATTEMPT"
#             self.descriptionLabel['text'] = "Click the Foul button to continue"
#             self.score = 0
#             for but in self.freezeButtons:
#                 but['state'] = DISABLED
#             self.rollButton['state'] = DISABLED
#         else: #no foul, update scores and widgets
#             self.descriptionLabel['text'] = "Click stop button to keep"
#             self.update_frozen_states()
#             self.update_button_states() #disable some buttons
#             self.update_score() #recalculate scores
#             self.scoreLabel['text'] = f"Attempt #{self.attempt} Score: {self.score}"
#             
#                 
#     def check_foul(self):
#         """Discus.check_foul() -> bool
#         returns True if in foul position, False otherwise"""
#         for die in self.dice:
#             if (not die.is_frozen() and die.get_top() != 0):
#                 return False
#         return True
#         
#     def update_frozen_states(self):
#         """Discus.update_frozen_states() -> None
#         updates self.frozenStates"""
#         for i in range(5):
#             if (self.dice[i].is_frozen()):
#                 self.frozenStates[i] = True
#             else:
#                 self.frozenStates[i] = False
#                 
#     def update_button_states(self):
#         """Discus.update_button_states() -> None
#         update states of self.freezeButtons"""
#         for i in range(5):
#             if (self.dice[i].is_frozen() or self.dice[i].get_top() == 0):
#                 self.freezeButtons[i]['state'] = DISABLED
#             else:
#                 self.freezeButtons[i]['state'] = ACTIVE
#     
#     def update_score(self):
#         """Discus.update_score() -> None
#         updates self.score"""
#         self.score = 0
#         for die in self.dice:
#             self.score+= die.get_top()
#         
# 
# # test application
# root = Tk()
# test = Discus(root, "Ray")
# root.mainloop()
#     
# =============================================================================
