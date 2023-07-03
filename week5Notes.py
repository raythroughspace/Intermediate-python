"""Composition of class, class attributes,== uses  __eq__ overload"""
# =============================================================================
# class Card:
#     """Represents a Card"""
#     
#     suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     ranks = ["narf", "Ace", "2", "3", "4", "5", "6",
#              "7", "8", "9", "10", "Jack", "Queen", "King"]
#     
#     def __init__(self, suit, rank):
#         """Card(suit, rank) -> Card
#         initializes a card with suit and rank"""
#         self.suit = suit
#         self.rank = rank
#         
#     def __str__(self):
#         """str(Card) -> str
#         returns a string representation of this card"""
#         return Card.ranks[self.rank] + " of " + Card.suits[self.suit]
#     
#     def cmp(self, other):
#         """Card.cmp(other) -> int
#         returns 1 if Card > other, 0 if Card == other, -1 otherwise"""
#         if (self.suit > other.suit):
#             return 1
#         elif (self.suit < other.suit):
#             return -1
#         else:
#             if (self.rank < other.rank):
#                 return -1
#             elif (self.rank > other.rank):
#                 return 1
#             else:
#                 return 0
#     
#     def __eq__(self, other):
#         return self.cmp(other) == 0
#     
#     def __gt__(self, other):
#         return self.cmp(other) == 1
#     
#     def __lt__(self, other):
#         return self.cmp(other) == -1
#     
#     def __neq__(self, other):
#         return self.cmp(other) != 0
#     
#     def __le__(self, other):
#         return self.cmp(other) <=0
#     
#     def __ge__(self, other):
#         return self.cmp(other) >=0
#     
# class Deck:
#     """Represents a Deck"""
#     
#     def __init__(self):
#         """Deck() -> Deck
#         Initializes a new deck"""
#         self.deck = []
#         for i in range(4):
#             for j in range(1,13):
#                 self.deck.append(Card(i,j))
#         
#     def shuffle(self):
#         """Deck.shuffle() -> None
#         shuffle this deck"""
#         import random
#         random.shuffle(self.deck)
#         
#     def __str__(self):
#         """str(Deck) -> str
#         returns string representation of Deck"""
#         s = ""
#         for card in self.deck:
#             s+= str(card)
#         return s
#     
#     def remove(self, card):
#         """Deck.remove(card) -> bool
#         remove card from deck if found"""
#         if (card in self.deck):
#             self.deck.remove(card)
#             return True
#         else:
#             return False
#         
#     def pop(self):
#         """Deck.pop() -> Card
#         removes and returns top card"""
#         return self.deck.pop()
#     
#     def is_empty(self):
#         return self.cards== []
# myDeck = Deck()
# myDeck.shuffle()
# card1 = myDeck.pop()  # deal a card
# print(card1)
# print(myDeck.remove(card1))  # should print False becuase card was already dealt
# =============================================================================
import random

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9
      color: string'''
    ranks = [0,1,2,3,4,5,6,7,8,9, "Skip", "Reverse", "Draw Two", "Wild", "Wild Draw Four"]

    def __init__(self, rank, color = None):
        '''UnoCard(rank, color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color
        self.isWild = False
        if (self.rank >=13):
            self.isWild = True

    def __str__(self):
        '''str(Unocard) -> str'''
        if (self.isWild):
            return str(UnoCard.ranks[self.rank])
        return(str(self.color) + ' ' + str(UnoCard.ranks[self.rank]))
    
    def set_wild_color(self, color):
        """UnoCard.wild_set_color(color) -> None
        set color for wild card"""
        if (self.isWild):
            self.color = color
            
    def get_color(self):
        """UnoCard.get_color() -> str
        returns color of this card"""
        return self.color
            
    def is_match(self, other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        if (self.isWild):
            return True
        return (self.color == other.color) or (self.rank == other.rank)
    
    def action(self):
        """UnoCard.action() -> str
        returns the action of card"""
        if (self.rank <10):
            return "Normal"
        elif (self.rank == 10):
            return "Skip"
        elif (self.rank == 11):
            return "Reverse"
        elif (self.rank == 12):
            return "Draw Two"
        elif (self.rank == 13):
            return "Wild"
        elif (self.rank == 14):
            return "Wild Draw Four"
        

class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0, color))  # one 0 of each color
            self.deck.append(UnoCard(13))
            self.deck.append(UnoCard(14))
            for i in range(2):
                for n in range(1, 13):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n, color))
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck)) + ' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self, pile):
        '''UnoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self, deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has ' + str(self.pile[-1]) + ' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self, card):
        '''UnoPile.add_card(card) -> None
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self, name, deck):
        '''UnoPlayer(name, deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self, deck, pile):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        if (deck.is_empty()):
            print("Deck has no more cards to draw! Resetting pile...")
            deck.reset_deck(pile)
            input("Press enter to continue.")
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self, card, pile):
        '''UnoPlayer.play_card(card, pile) -> None
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)
        return card.action()
    
    def get_matches(self, topcard):
        """UnoPlayer.get_matches(matches) -> list
        returns list of matched playable cards"""
        matches = [card for card in self.hand if card.is_match(topcard) and card.action() != "Wild Draw Four"]
        WDF_playable = True
        for card in matches:
            if (card.get_color() == topcard.get_color() and card.action() != "Wild"):
                WDF_playable = False
        if (WDF_playable):
            for card in self.hand:
                if (card.action() == "Wild Draw Four"):
                    matches.append(card)
        return matches
    
    def take_turn(self, deck, pile):
        '''UnoPlayer.take_turn(deck, pile) -> None
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        # print player info
        print(self.name + ", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = self.get_matches(topcard)
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
                # print the playable cards with their number
                print(str(index + 1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            action = self.play_card(matches[choice - 1], pile)
            return action
            
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck, pile)
            print("You drew: "+str(newcard))
            if newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                action = self.play_card(newcard,pile)
                input("Press enter to continue.")
                return action
            else:   # still can't play
                print("Sorry, you still can't play.")
            input("Press enter to continue.")
         

def play_uno(numPlayers):
    '''play_uno(numPlayers) -> None
    plays a game of Uno with numPlayers'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []
    for n in range(numPlayers):
        # get each player's name, then create an UnoPlayer
        name = input('Player #' + str(n + 1) + ', enter your name: ')
        playerList.append(UnoPlayer(name,deck))
    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers)
    order = 1
    # play the game
    while True:
        # print the game status
        print('-------')
        for player in playerList:
            print(player)
        print('-------')
        # take a turn
        action = playerList[currentPlayerNum].take_turn(deck, pile)
        drawCards = 0
        if (action == "Skip"):
            print("A skip card was played, next player's turn is skipped!")
            currentPlayerNum = (currentPlayerNum + order) % numPlayers  
        elif (action == "Reverse"):
            print("A reverse card was played, reverse order of play!")
            order = -order
        elif (action == "Draw Two"):
            print("A draw two card was played, next player draws two cards and loses their turn!")
            currentPlayerNum = (currentPlayerNum + order) % numPlayers
            drawCards = 2
        elif (action in ["Wild", "Wild Draw Four"]):
            color = input("You played a " + action + " card! Pick a color: ")
            while (color not in ['green', 'yellow', 'red', 'blue']):
                color = input("Pick a color between green, yellow, red, blue:  ")
            pile.top_card().set_wild_color(color)
            if (action == "Wild Draw Four"):
                print("Next player draws 4 cards and loses their turn!")
                drawCards = 4
                currentPlayerNum = (currentPlayerNum + order) % numPlayers
                
        for i in range(drawCards):
            newcard = playerList[currentPlayerNum].draw_card(deck, pile)
            print(playerList[currentPlayerNum].get_name() + " drew: "+str(newcard))
                
        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing!")
            break
        # go to the next player
        currentPlayerNum = (currentPlayerNum + order) % numPlayers  
play_uno(3)

# =============================================================================
# SKIP GOOD 
# Reverse GOOD
# Draw Two GOOD
# Wild GOOD
# Wild Draw Four Good
# =============================================================================








