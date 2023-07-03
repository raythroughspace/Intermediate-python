"""Inheritance, can initialize self.attr outside of __init__, Deck.__str__(self), 
cloning for iterating while removing, order of methods don't matter"""
# =============================================================================
# 
# class Card:
#     suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
#              "8", "9", "10", "Jack", "Queen", "King"]
# 
#     def __init__(self, suit=0, rank=0):
#         self.suit = suit
#         self.rank = rank
# 
#     def __str__(self):
#         return (self.ranks[self.rank] + " of " + self.suits[self.suit])
# 
#     def cmp(self, other):
#         # Check the suits
#         if self.suit > other.suit:
#             return 1
#         if self.suit < other.suit:
#             return -1
#         # Suits are the same... check ranks
#         if self.rank > other.rank:
#             return 1
#         if self.rank < other.rank:
#             return -1
#         # Ranks are the same... it's a tie
#         return 0
# 
#     def __eq__(self, other):
#         return self.cmp(other) == 0
# 
#     def __le__(self, other):
#         return self.cmp(other) <= 0
# 
#     def __ge__(self, other):
#         return self.cmp(other) >= 0
# 
#     def __gt__(self, other):
#         return self.cmp(other) > 0
# 
#     def __lt__(self, other):
#         return self.cmp(other) < 0
# 
#     def __ne__(self, other):
#         return self.cmp(other) != 0
# 
# class Deck:
# 
#     def __init__(self):
#         self.cards = []
#         for suit in range(4):
#             for rank in range(1, 14):
#                 self.cards.append(Card(suit, rank))
# 
#     def __str__(self):
#         s = ""
#         for card in self.cards:
#             s += str(card) + '\n'
#         return s
# 
#     def shuffle(self):
#         import random
#         random.shuffle(self.cards)
# 
#     def remove(self, card):
#         if card in self.cards:
#             self.cards.remove(card)
#             return True
#         else:
#             return False
# 
#     def pop(self):
#         return self.cards.pop()
# 
#     def is_empty(self):
#         return self.cards == []
#     
#     def deal(self, hands, numCards = 999):
#         j=0
#         for i in range(numCards):
#             if (self.is_empty()):
#                 break
#             hands[j].add(self.pop())
#             j  = (j+1)%len(hands)
#         
# class Hand(Deck):
#     
#     def __init__(self, name = ""):
#         self.name = name
#         self.cards = []
#         
#     def __str__(self):
#         s = self.name + " 's hand "
#         if (self.is_empty()):
#             s += "is empty."
#         else:
#             s += "contains " + Deck.__str__(self)
#         return s
#     
#     def add(self, card):
#         self.cards.append(card)
#     
# class CardGame:
#     
#     def __init__(self):
#         self.deck = Deck()
#         self.deck.shuffle()
# 
# class OldMaidHand(Hand):
#     
#     def __init__(self, name):
#         Hand.__init__(self, name)
#     
#     def remove_matches(self):
#         count = 0
#         copyHand = self.cards[:]
#         ncards = len(copyHand)
#         for card in copyHand:
#             match = Card(3- card.suit, card.rank)
#             if (match in self.cards and card in self.cards):
#                 Deck.remove(self, match)
#                 Deck.remove(self, card)
#                 print("Hand " + self.name + ":", end = ' ')
#                 print(str(card) + " matches " + str(match))
#                 count += 1
#         return count
# 
# class OldMaidGame(CardGame):
#     
#     def play(self, names):
#         self.deck.remove(Card(0,12))
#         
#         self.hands = []
#         for name in names:
#             self.hands.append(OldMaidHand(name))
#         
#         self.deck.deal(self.hands)
#         print("Cards have been dealt!")
#         self.print_hands()
# 
#         matches = self.remove_all_matches()
#         
#         turn = 0
#         numHands = len(self.hands)
#         while (matches <25):
#             matches += self.play_one_turn(turn)
#             turn = (turn + 1) % numHands
#         
#         print("Game is over")
#         self.print_hands()
#         
#     def print_hands(self):
#         for hand in self.hands:
#             print(hand)
#     
#     def remove_all_matches(self):
#         matches = 0
#         for hand in self.hands:
#             matches += hand.remove_matches()
#         return matches
#     
#     def play_one_turn(self, i):
#         if self.hands[i].is_empty():
#             return 0
#         neighbor = self.find_neighbor(i)
#         pickedCard = self.hands[neighbor].pop()
#         self.hands[i].add(pickedCard)
#         print("Hand", self.hands[i].name, "picked", pickedCard)
#         count = self.hands[i].remove_matches()
#         self.hands[i].shuffle()
#         return count
# 
#     def find_neighbor(self, i):
#         numHands = len(self.hands)
#         for countToTheLeft in range(1,numHands):
#             neighbor = (i + countToTheLeft) % numHands
#             if not self.hands[neighbor].is_empty():
#                 return neighbor
# 
# game = OldMaidGame()
# game.play(["Allen","Betsy","Carl","Diane"])
# =============================================================================
# =============================================================================
# import turtle
# import random
# 
# class MisbehavingTurtle(turtle.Turtle):
#     
#     def left(self, angle):
#         """MisbehavingTurtle.left(angle) -> None
#         turns turtle left by angle 75% of the time, otherwise turn right by angle"""
#         if random.uniform(0,1) < 0.25:
#             turtle.Turtle.right(self, angle)
#         else:
#             turtle.Turtle.left(self, angle)
#     
#     def right(self, angle):
#         """MisbehavingTurtle.right(angle) ->None
#         turns turtle right by angle 75% of the time, otherwise turn left by angle"""
#         if random.uniform(0,1) < 0.25:
#             turtle.Turtle.left(self, angle)
#         else:
#             turtle.Turtle.right(self, angle)
#             
#             
# # test case
# # drawing an octagon and a square
# def drawing_test(t):
#     '''drawing_test(t)
#      draws an octagon and square with t'''
#     for i in range(8):
#         t.forward(30)
#         t.left(45)
#     t.right(45)
#     for i in range(4):
#         t.forward(50)
#         t.right(90)
#         
# # one nice turtle and one not-so-nice turtle
# wn = turtle.Screen()
# sugar = turtle.Turtle()
# sugar.color('green')
# drawing_test(sugar)
# spice = MisbehavingTurtle()
# spice.color('red')
# drawing_test(spice)
# wn.mainloop()
# =============================================================================
import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''
    faces = ["dino", "leaf", "foot"]
    
    def __init__(self, color):
        """DinoDie(color) -> DinoDie
        initializes a dino die of color"""
        self.color = color
        if (color == "green"):
            Die.__init__(self,[0,0,0,1,1,2])
        elif (color == "red"):
            Die.__init__(self,[0,1,1,2,2,2])
        else:
            Die.__init__(self,[0,0,1,1,2,2])
    
    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return DinoDie.faces[self.top]
        
    def __str__(self):
        """str(DinoDie) -> str
        Returns a string representation of this die"""
        return f"A {self.color} Dino die with a {DinoDie.faces[self.top]} on top."
        
class DinoDiePile():
    """implements a set of Dino Die for Dino Hunt"""
    
    def __init__(self):
        """DinoDiePile() -> DinoDiePile
        initializes a set of Dino Die for a game of Dino Hunt"""
        self.pile = []
        for i in range(6):
            self.pile.append(DinoDie("green"))
        for i in range(4):
            self.pile.append(DinoDie("yellow"))
        for i in range(3):
            self.pile.append(DinoDie("red"))
            
    def is_empty(self):
        """DinoDiePile.is_empty() -> bool
        returns True if pile is empty"""
        return len(self.pile) == 0
        
    def roll_dice(self):
        """DinoDiePile() -> list
        rolls 3 Dino Die and returns them"""
        random.shuffle(self.pile)
        rolls = min(3, len(self.pile))
        for i in range(rolls):
            self.pile[i].roll()
        return [self.pile[i] for i in range(rolls)]
        
    def __str__(self):
        """str(DinoDiePile) -> str
        returns a string representation  of DinoDiePile"""
        s = f"You have {len(self.pile)} dice remaining. \n"
        green = 0
        red = 0
        yellow = 0
        for die in self.pile:
            if (die.color == "green"):
                green+=1
            elif (die.color == "yellow"):
                yellow +=1
            else:
                red +=1
        s += f"{green} green, {yellow} yellow, {red} red"
        return s
        
    def remove(self, dice):
        """DinoDiePile.remove(dice) -> None
        Remove dice from pile"""
        for die in dice:
            if (die in self.pile):
                self.pile.remove(die)
                
    def get_pile(self):
        return self.pile

class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__(self, name):
        """DinoPlayer(name) -> DinoPlayer
        initializes a DinoPlayer with name"""
        self.name = name
        self.score = 0
        self.aside =[]
    
    def __str__(self):
        """str(DinoPlayer) -> str
        returns a string representation of DinoPlayer"""
        return f"{self.name} has {self.score} points."
    
    def get_score(self):
        """DinoPlayer.get_score() -> int
        return score of DinoPlayer"""
        return self.score
    
    def get_name(self):
        """DinoPlayer.get_name() -> str
        return name of DinoPlayer"""
        return self.name
    
    def print_rolls(self, rolls):
        """DinoPlayer.print_rolls(rolls) -> None
        prints rolls"""
        for die in rolls:
            print(die)
    
    def get_aside(self):
        """DinoPlayer.get_aside() -> tuple
        return tuple number of dinos and feet set aside"""
        dinos, feet = 0,0
        for die in self.aside:
            if (die.get_top() == "foot"):
                feet += 1
            elif (die.get_top() == "dino"):
                dinos += 1
        return dinos, feet
    
    def set_aside(self, dice, pile):
        """DinoPlayer.set_aside(dice, pile) -> None
        remove non-leaf dice from pile and set them aside"""
        copyDice = dice[:]
        for die in copyDice:
            if (die.get_top() == "leaf"):
                dice.remove(die)
        self.aside.extend(dice)
        pile.remove(dice)
        
    def reset_pile(self, pile):
        """DinoPlayer.reset_pile(pile) -> None
        put dice set aside back into pile"""
        pile.get_pile().extend(self.aside)
        self.aside = []
            
    def take_turn(self, pile):
        """DinoPlayer.take_turn() -> int
        returns score of player this turn"""
        print("\n")
        print(self.name + ", it's your turn!")
        turn_score = 0
        print(pile)
        input("Press enter to select dice and roll.")
        rolls = pile.roll_dice()
        self.print_rolls(rolls)
        self.set_aside(rolls, pile)
        dinos, feet = self.get_aside()
        while True:
            if (feet >=3):
                print("Too bad -- you got stomped!")
                turn_score = 0
                break
            elif (pile.is_empty()):
                print("No more dice to roll!")
                break
            print(f"This turn so far: {dinos} dinos and {feet} feet")
            print(pile)
            again = input("Do you want to roll again? (y/n) ")
            if (again == "n"):
                break
            input("Press enter to select dice and roll.")
            rolls = pile.roll_dice()
            self.print_rolls(rolls)
            self.set_aside(rolls, pile)
            dinos,feet = self.get_aside()
            turn_score = dinos
        print("You earned " + str(turn_score) + " points this turn!")
        self.score += turn_score
        self.reset_pile(pile)
        
def print_scores(playerList):
    for player in playerList:
        print(player)
        
def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
      
    pile = DinoDiePile()
    playerList = []
    for i in range(numPlayers):
        name = input("Player " + str(i+1) + ", enter your name: ")
        playerList.append(DinoPlayer(name))
    
    for i in range(numRounds):
        print("ROUND " + str(i+1))
        print_scores(playerList)
        
        for turn in range(numPlayers):
            playerList[turn].take_turn(pile)
    
    winner = ""
    maxPts = 0
    for player in playerList:
        if (player.get_score() > maxPts):
            winner = player.get_name()
            maxPts = player.get_score()
    
    print("We have a winner!")
    print(f"{winner} has {maxPts} points.")

play_dino_hunt(2,3)