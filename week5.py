import random

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 12
      color: string
      rank 10 = skip card
      rank 11 = reverse card
      rank 12 = draw two card
      rank 13 = wild card
      rank 14 = wild draw four card'''
    
    cardTypes = ["Skip", "Reverse", "Draw Two", "Wild", "Wild Draw Four"]
    
    def __init__(self, rank, color):
        '''UnoCard(rank, color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        rank = self.rank
        if (rank >=10):
            rank = self.cardTypes[rank-10]
        return(str(self.color) + ' ' + str(rank))

    def is_match(self, other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        return (self.color == other.color) or (self.rank == other.rank)
    
    def get_type(self):
        """UnoCard.get_type() -> string
        returns the type of card"""
        if (self.rank<10):
            return "Normal"
        else:
            return self.cardTypes[self.rank-10]
    
    def set_wild_color(self, color):
        """set_wild_color(color) -> None
        set color of UnoCard if it is a Wild or Wild Draw Four type, do nothing otherwise"""
        if (self.get_type() == "Wild" or self.get_type() == "Wild Draw Four"):
            self.color = color
        

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
            self.deck.append(UnoCard(13, color)) # 4 wild cards that can take any color
            self.deck.append(UnoCard(14, color)) # 4 wild draw four cards that can take any color
            for i in range(2):
                for n in range(1, 13):  # two of each of 1-12 of each color
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
        if len(self.deck) != 0:
            return
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

    def __init__(self, name, deck, AI = False):
        '''UnoPlayer(name, deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]
        self.AI = AI

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards.'
    
    def is_AI(self):
        """UnoPlayer.is_AI(self) -> bool
        returns True if AI controlled, False otherwise"""
        return self.AI

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

    def draw_card(self, deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self, card, pile):
        '''UnoPlayer.play_card(card, pile) -> string
        plays a card from the player's hand to the pile
        and returns type of the card played
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)
        return card.get_type()

    def take_turn(self, deck, pile):
        '''UnoPlayer.take_turn(deck, pile) -> str
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile
          returns the card type of the played card, empty str if nothing played'''
        # print player info
        print(self.name + ", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.is_match(topcard)]
        playCardType = ""
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
                # print the playable cards with their number
                print(str(index + 1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            if (self.AI):
                choice = random.randint(1, len(matches))
                print(self.name + " played " + str(matches[choice - 1]))
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            playCardType = self.play_card(matches[choice - 1], pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            if (not self.AI):
                input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            print("You drew: "+ str(newcard))
            if newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                playCardType = self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")
            if (not self.AI):
                input("Press enter to continue.")
        return playCardType
    
def draw_cards(player, deck, n):
    """draw_cards(player, deck, n) -> None
    makes player draw n cards from deck"""
    for i in range(n):
        newcard = player.draw_card(deck)
        print(player.get_name() + " drew " + str(newcard))
        
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
        AI = input("Should this player be computer controlled? (y/n) ")
        if (AI == 'y'):
            playerList.append(UnoPlayer(name,deck, True))
        else:
            playerList.append(UnoPlayer(name,deck))
    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers)
    #order = 1 means normal order, order = -1 means reverse order
    order = 1 
    # play the game
    while True:
        # print the game status
        print('-------')
        for player in playerList:
            print(player)
        print('-------')
        # take a turn
        playCardType = playerList[currentPlayerNum].take_turn(deck, pile)
        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing!")
            break
        # check card type played
        if (playCardType == "Skip"):
            #skip player turn
            currentPlayerNum = (currentPlayerNum + order*1) % numPlayers
            print("A skip card was played, so " + playerList[currentPlayerNum].get_name() + "'s turn is skipped.")
            if (not playerList[currentPlayerNum].is_AI()):
                input("Press enter to skip turn")
        elif (playCardType == "Reverse"):
            #reverse order of play
            order = -order
            print("The order of play has been reversed.")
        elif (playCardType == "Draw Two"):
            #next player draw two cards and lose turn
            currentPlayerNum = (currentPlayerNum + order*1) % numPlayers
            print(playerList[currentPlayerNum].get_name() + " must draw two cards and loses his turn.")
            draw_cards(playerList[currentPlayerNum], deck, 2)
            
        elif (playCardType == "Wild" or playCardType == "Wild Draw Four"):
            #give option to change color of Wild card 
            print("You played a " + playCardType + " card, which color would you like to change to?")
            response = 'x'
            if (playerList[currentPlayerNum].is_AI()):
                response = random.choice(["red", "blue", "green", "yellow"])
                print(playerList[currentPlayerNum].get_name() + " has chosen " + response)
            while response not in ["red", "blue", "green", "yellow"]:
                print("Choose one of red, blue, green or yellow ")
                response = input("Enter color : ")
            
            pile.top_card().set_wild_color(response)
            #next player draws four cards and loses turn
            if (playCardType == "Wild Draw Four"):
                currentPlayerNum = (currentPlayerNum + order*1) % numPlayers
                print("Next player " + playerList[currentPlayerNum].get_name() + " draws four cards and loses their turn.")
                draw_cards(playerList[currentPlayerNum], deck, 4)
        
                
        currentPlayerNum = (currentPlayerNum + order*1) % numPlayers
        
play_uno(3)