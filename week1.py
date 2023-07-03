"""PROBLEMS"""
# =============================================================================
# numAnswered = int(input("Enter the number of questions answered: "))
# numCorrect = int(input("Enter the number of questions correct: "))
# score = numCorrect*6 + 1.5*(25-numAnswered)
# print("The student's score is: " + str(score))
# =============================================================================
# =============================================================================
# for n in range(110, 1000, 11):
#     firstDigit = n%10
#     secondDigit = (n//10)%10
#     thirdDigit = (n//100)
#     SSDigits = firstDigit**2 + secondDigit**2 + thirdDigit**2
#     if (SSDigits == n/11):
#         print(n)
#         
# =============================================================================
# =============================================================================
# def sum_proper_divs(n):
#     """sum_proper_divs(n) -> int
#     returns the sum of the proper divisors of positive integer n"""
#     if (n==1):
#         return 0
#     tot = 0
#     for i in range(1,n-1):
#         if (n%i == 0):
#             tot += i
#     return tot
# 
# for n in range(100, 1000):
#     if (sum_proper_divs(n) == 2*n):
#         print(n)
# =============================================================================
# =============================================================================
# import random
# print("I'm thinking of a number between 0 and 100")
# rand = random.randint(0, 101)
# guesses = 0
# while True:
#     pick = int(input("Enter your guess: "))
#     guesses+=1
#     if (pick > rand):
#         print("Sorry, " + str(pick) + " is too high.")
#     elif (pick < rand):
#         print("Sorry, " + str(pick) + " is too low.")
#     else:
#         print("Good job! " + str(rand) + " is my number.")
#         print("It took you " + str(guesses) + " guesses.")
#         break
# =============================================================================
# =============================================================================
# import random
# print("Think of a number between 0 and 100")
# input("Hit enter when you have it.")
# a = 0
# b = 100
# guesses = 0
# while True:
#     rand = random.randrange(a,b+1)
#     guesses += 1
#     print("I guess " + str(rand))
#     feed = input("Is this high, low, or correct? ")
#     if (feed == "low"):
#         a = rand+1
#     elif (feed == "high"):
#         b = rand-1
#     else:
#         print("I knew it!")
#         print("It took me " + str(guesses) + " guesses.")
#         break
#     
# =============================================================================
# =============================================================================
# def remove_letter(string,letter):
#     '''remove_letter(string,letter) -> str
#     returns string with all occurrences of letter removed'''
#     res = ""
#     for char in string:
#         if (char != letter):
#             res += char
#     return res
#  
# # test cases
# print(remove_letter('This is a test','t'))  # should print 'This is a es'
# print(remove_letter('Hello World!','l'))    # should print 'Heo Word!'
# print(remove_letter('I like Python','q'))   # should print 'I like Python'
# =============================================================================
# =============================================================================
# inFile = open("wordlist.txt")
# count = 0
# for word in inFile:
#     word = word.strip()
#     if (len(word) == 10):
#         count+=1
# print(count)
# inFile.close()
# =============================================================================
# =============================================================================
# def compute_score(word):
#     """compute_score(word) -> int
#     returns the score of the scrabble word"""
#     score = 0
#     for letter in word:
#         if (letter.upper() == "Z"):
#             return 0
#         score += values[letter.upper()]
#     return score
# 
# values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
#           'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
#           'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
# inFile = open("wordlist.txt")
# highestScore = 0
# highestWord = ""
# for word in inFile:
#     word = word.strip()
#     if (len(word) == 7 and compute_score(word) > highestScore):
#         highestScore = compute_score(word)
#         highestWord = word
# print(highestWord)
#     
# =============================================================================

def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    rails = []
    for i in range(numRails):
        ithRail = ""
        for j in range(i, len(plaintext), numRails):
            ithRail += plaintext[j]
        rails.append(ithRail)
    scrambled = ""
    for i in reversed(range(numRails)):
        scrambled += rails[i]
    return scrambled
 
def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    rails = []
    right = len(ciphertext)
    for i in range(numRails):
        ithLen = len(list(range(i, len(ciphertext), numRails)))
        ithRail = ciphertext[right-ithLen:right]
        right -= ithLen
        rails.append(ithRail)
    decipherList = [""]*len(ciphertext)
    for i in range(numRails):
        idx = 0
        for j in range(i, len(ciphertext), numRails):
            decipherList[j] = rails[i][idx]
            idx +=1
    return "".join(decipherList)
     
def valid_words(decipher, wordfilename):
    """valid_words(decipher) -> int
    returns the number of valid words in decipher"""
    inFile = open(wordfilename)
    decipherWords = decipher.split()
    wordDict = {}
    for word in inFile:
        word = word.strip()
        wordDict[word.lower()] = 1
    inFile.close()
    count = 0
    for word in decipherWords:
        if (word.lower() in wordDict):
            count +=1
    return count
            
 
def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    maxWords = 0
    bestDecipher = ""
    for numRails in range(1,11):
        decipher = decipher_fence(ciphertext, numRails)
        nWords = valid_words(decipher, wordfilename)
        if (nWords > maxWords):
            bestDecipher = decipher
            maxWords = nWords
    return bestDecipher
 
# test cases
 
# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou
print(encipher_fence("O, that this too, too sullied flesh would melt, Thaw, and resolve itself into a dew.", 3))
# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!
 
# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
print(decode_text(" atso oui e u l a del sfn d.,h it,osldlhode,h,nroetlio wOtth ot lefswlmtTwa svie tae", 'wordlist.txt'))