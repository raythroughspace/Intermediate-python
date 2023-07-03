# =============================================================================
# """modifiers, pure functions, overloading"""
# class MyTime:
#     """Represents time"""
#     
#     def __init__(self, hrs = 0, mins = 0, secs = 0):
#         """MyTime(hrs, mins, secs) -> None
#         initializes MyTime with hrs, mins, secs"""
#         total = hrs*3600 + mins*60 + secs
#         self.secs = total%60
#         self.mins = (total//60)%60
#         self.hrs = total//3600
#         
#     def to_seconds(self):
#         """MyTime.to_seconds() -> int
#         returns the total number of seconds in MyTime"""
#         return self.hrs*3600 + self.mins*60 + self.secs
#     
#     def __str__(self):
#         """str(MyTime) -> str
#         returns string representation of MyTime"""
#         return str(self.hrs) + ":" + str(self.mins) + ":" + str(self.secs)
#     
#     def __add__(self, other):
#         """MyTime + other -> MyTime
#         adds MyTime and other and returns the sum MyTime"""
#         return MyTime(0,0, self.to_seconds() + other.to_seconds())
#     
# currentTime = MyTime(6, 32, 40)
# breadTime = MyTime(3, 35, 50)
# doneTime = currentTime + breadTime
# print(doneTime)
# =============================================================================
"""PROBLEMS"""
# =============================================================================
# def is_prime(n):
#     '''is_prime(n) -> boolean
#     returns True if n is prime, False otherwise'''
#     if n < 2:
#         return False
#     for divisor in range(2,int(n**0.5)+1):
#         if n % divisor == 0:
#             return False
#     return True
#  
# def sum_of_prime_cubes(n):
#     '''sum_of_prime_cubes(n) -> int
#     returns sum of cubes of all primes <=n'''
#     return sum([p**3 for p in range(n+1) if is_prime(p)])
#  
# # test case
# print(sum_of_prime_cubes(11))   # should be 1834
# print(sum_of_prime_cubes(200))  # this is your answer
# =============================================================================
# =============================================================================
# 
# import random
# 
# class Die:
#     '''Die class'''
# 
#     def __init__(self, sides=6):
#         '''Die(sides)
#         creates a new Die object
#         int sides is the number of sides
#         (default is 6)
#         -or- sides is a list/tuple of sides'''
#         # if an integer, create a die with sides
#         #  from 1 to sides
#         if isinstance(sides, int):
#             self.numSides = sides
#             self.sides = list(range(1, sides + 1))
#         else:  # use the list/tuple provided
#             self.numSides = len(sides)
#             self.sides = list(sides)
#         # roll the die to get a random side on top to start
#         self.roll()
# 
#     def __str__(self):
#         '''str(Die) -> str
#         string representation of Die'''
#         return f'A {self.numSides}-sided die with {self.get_top()} on top'
# 
#     def roll(self):
#         '''Die.roll()
#         rolls the die'''
#         # pick a random side and put it on top
#         self.top = random.choice(self.sides)
# 
#     def get_top(self):
#         '''Die.get_top() -> object
#         returns top of Die'''
#         return self.top
# 
#     def set_top(self, value):
#         '''Die.set_top(value)
#         sets the top of the Die to value
#         Does nothing if value is illegal'''
#         if value in self.sides:
#             self.top = value
#     
#     def flip(self):
#         """Die.flip() -> None
#         flips the die"""
#         idx = self.sides.index(self.get_top())
#         newTop = self.sides[len(self.sides) - idx -1]
#         self.top = newTop
#         
# =============================================================================
# =============================================================================
# d = Die(8)
# d.set_top(3)
# d.flip()
# print(d.get_top()) 
# =============================================================================

# =============================================================================
# import random
# class Pokemon:
#     """Represents a Pokemon"""
#     
#     def __init__(self, name, health, att, defense):
#         """Pokemon(name, health, att, defense) -> None
#         Initializes Pokemon"""
#         self.name = name
#         self.health = health
#         self.att = att
#         self.defense = defense
#         
#     def __str__(self):
#         """str(Pokemon) -> str
#         returns string representation of Pokemon"""
#         return f"""Pokemon {self.name}, health: {self.health}, 
#     attack: {self.att}, defense: {self.defense}"""
#     
#     def calculate_damage(self, other):
#         """Pokemon.calculate_damage(other) -> int
#         returns amount of damage Pokemon inflicts on other if it attacks"""
#         A = self.att
#         D = other.defense
#         r = random.uniform(0.85, 1)
#         return (12/5 * (A/D) + 2)*r
#     
#     def attack(self, other):
#         """Pokemon.attack(other) -> None
#         Pokemon attacks other pokemon"""
#         damage = int(round(self.calculate_damage(other)))
#         if (other.health <= damage):
#             other.health = 0
#             print(other.name + " fainted!")
#         else:
#             other.health-=damage
#             print(self.name  + " does " + str(damage) + " damage!")
# 
# b = Pokemon("Bulbasaur", 45, 49, 49)
# c = Pokemon("Charmander", 39, 52, 43)
# c.attack(b)
# print(b)
# b.attack(c)
# print(c)
# 
# =============================================================================
# =============================================================================
# def most_freq(dice):
#     """most_freq(dice) -> int
#     returns the side in dice (excluding "W") with the highest count"""
#     sides = [dice[i].get_top() for i in range(10)]
#     count = 0
#     side = 0
#     for i in range(1,5):
#         if (sides.count(i) > count):
#             count = sides.count(i)
#             side = i
#     return side
# 
# def reroll(dice, mostFreq):
#     """reroll(dice, mostFreq) -> None
#     rerolls all dice that are not "W" or mostFreq"""
#     for i in range(10):
#         if (dice[i].get_top() == "W" or dice[i].get_top() == mostFreq):
#             continue
#         dice[i].roll()
# 
# def is_won(dice, mostFreq):
#     """is_won(dice, mostFreq) -> bool
#     returns True if game is won, False otherwise"""
#     for i in range(10):
#         if (dice[i].get_top() != mostFreq and dice[i].get_top() != "W"):
#             return False
#     return True
# 
# def print_dice(dice):
#     print([dice[i].get_top() for i in range(10)])
# 
# def europadice():
#     """europadice() -> None
#     Plays a game of europadice"""
#     dice = [Die([1,2,3,4, "W"]) for i in range(10)]
#     print_dice(dice)
#     mostFreq = most_freq(dice)
#     print("We're going for all " + str(mostFreq) + "s.")
#     rerolls = 1
#     while True:
#         print_dice(dice)
#         if (is_won(dice, mostFreq)):
#             print("You won!")
#             break
#         elif (rerolls == 4):
#             print("Sorry, didn't win")
#             break
#         else:
#             input("Reroll #" + str(rerolls) + ". Press enter to reroll.")
#             reroll(dice, mostFreq)
#             rerolls += 1
#             
# europadice()
#             
# =============================================================================
# =============================================================================
# 
# import random
# 
# class Die:
#     '''Die class'''
# 
#     def __init__(self,sidesParam=6):
#         '''Die([sidesParam])
#         creates a new Die object
#         int sidesParam is the number of sides
#         (default is 6)
#         -or- sidesParam is a list/tuple of sides'''
#         # if an integer, create a die with sides
#         #  from 1 to sides
#         if isinstance(sidesParam,int):
#             sidesParam = range(1,sidesParam+1)
#         self.sides = list(sidesParam)
#         self.numSides = len(self.sides)
#         # roll the die to get a random side on top to start
#         self.roll()
# 
#     def __str__(self):
#         '''str(Die) -> str
#         string representation of Die'''
#         return str(self.numSides)+'-sided die with '+str(self.top)+' on top'
# 
#     def roll(self):
#         '''Die.roll()
#         rolls the die'''
#         # pick a random side and put it on top
#         self.top = self.sides[random.randrange(self.numSides)]
# 
#     def get_top(self):
#         '''Die.get_top() -> object
#         returns top of Die'''
#         return self.top
# 
# 
# class Player():
#     """Player class for decathlon game"""
#     
#     def __init__(self, name):
#         """Player(name) -> None
#         initializes a new Player with name"""
#         self.name = name
#         self.rerolls = 5
#         self.score = 0
#         
#     def __str__(self):
#         """str(Player) -> str
#         returns a string representation of Player"""
#         return "Player " + self.name + " with " + str(self.score) + " score and "+ str(self.rerolls) + " rerolls left."
#     
#     def take_turn(self):
#         """Player.take_turn() -> None
#         play one round of decathlon"""
#         dice = [Die([1,2,3,4,5,-6]) for i in range(2)]
#         rolls = [dice[i].get_top() for i in range(2)]
#         
#         while True:
#             print(self.name + " rolled a " + str(rolls[0]) + " and a " + str(rolls[1]) + " for a score of " + str(sum(rolls)))
#             ans = input("Would you like to reroll? (y/n) ")
#             if (ans == "n"):
#                 break
#             if (self.rerolls == 0):
#                 print(self.name + " has no rerolls left!")
#                 break
#             self.rerolls-=1
#             for i in range(2):
#                 dice[i].roll()
#                 rolls[i] = dice[i].get_top()
#         
#         self.score += sum(rolls)
#         print(self.name + " score " + str(sum(rolls)) + " this turn for a total of " + str(self.score) + " score.")
#         
# 
# 
# def print_scores(playerList):
#     for player in playerList:
#         print(player)
# 
# def decathlon_400_meters():
#     '''decathlon_400_meters()
#     plays a multi-player version of Reiner Knizia's 400 Meters'''
#     numPlayers = int(input('Enter number of players: '))
#     playerList = []
#     for i in range(numPlayers):
#         name = input('Player ' + str(i+1) + ', enter your name: ')
#         playerList.append(Player(name))
#     # play the game
#     for turn in range(1,5):
#         print("Round " + str(turn))
#         for i in range(numPlayers):
#             print_scores(playerList)
#             playerList[i].take_turn()
#     print_scores(playerList)      
#         
# 
# decathlon_400_meters()
# =============================================================================
# =============================================================================
# class Fraction:
#     '''represents fractions'''
#  
#     def __init__(self,num,denom):
#         '''Fraction(num,denom) -> Fraction
#         creates the fraction object representing num/denom'''
#         if denom == 0: # raise an error if the denominator is zero
#             raise ZeroDivisionError
#         gcd = 1
#         if (denom < 0):
#             num = -num
#             denom = -denom
#         for i in range(1, max(abs(num), denom) + 1):
#             if (num%i == 0 and denom%i==0):
#                 gcd = i
#         self.num = num//gcd
#         self.denom = denom//gcd
#     
#     def __str__(self):
#         """str(Fraction) -> str
#         returns string representation of this Fraction"""
#         return str(self.num) + "/" + str(self.denom)
#     
#     def __eq__(self, other):
#         """Fraction == other -> bool
#         return True if Fraction equals other, False otherwise"""
#         if (self.num == other.num and self.denom == other.denom):
#             return True
#         return False
#     
#     def __float__(self):
#         """float(Fraction) -> float
#         returns the float representation of Fraction"""
#         return self.num/self.denom
#     
#     def __add__(self, other):
#         """Fraction + other -> Fraction
#         returns the sum of the two Fractions"""
#         a,b = self.num, self.denom
#         c,d = other.num, other.denom
#         return Fraction(a*d + b*c, b*d)
#     
#     def __sub__(self, other):
#         """Fraction - other ->Fraction
#         returns the subtraction of Fraction and other"""
#         a,b = self.num, self.denom
#         c,d = other.num, other.denom
#         return Fraction(a*d-b*c, b*d)
#     
#     def __mul__(self, other):
#         """Fraction * other -> Fraction
#         returns the multiplication of Fraction and other"""
#         a,b = self.num, self.denom
#         c,d = other.num, other.denom
#         return Fraction(a*c, b*d)
#     
#     def __truediv__(self, other):
#         """Fraction / other -> Fraction
#         returns the division of Fraction and other"""
#         a,b = self.num, self.denom
#         c,d = other.num, other.denom
#         return Fraction(a*d, b*c)
#  
# # examples
# p = Fraction(3,6)
# print(p)  # should print 1/2
# q = Fraction(10,-60)
# print(q)  # should print -1/6
# r = Fraction(-24,-48)
# print(r)  # should also print 1/2
# x = float(p)
# print(x)  # should print 0.5
# ### if overloading using special methods
# print(p+q)  # should print 1/3
# print(p-q)  # should print 2/3
# print(p-p)  # should print 0/1
# print(p*q)  # should print -1/12
# print(p/q)  # should print -3/1
# print(p==r) # should print True
# print(p==q) # should print False
# =============================================================================




































