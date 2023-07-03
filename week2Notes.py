# =============================================================================
# import turtle
# 
# def koch(t, order, size):
#     """ koch(t,order,size) -> None
#     Make t draw a koch fractal of order and size"""
#     
#     if (order == 0):
#         t.forward(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             t.left(angle)
#             koch(t, order-1, size/3)
# 
# wn = turtle.Screen()
# t = turtle.Turtle()
# koch(t, 3, 100)
# wn.mainloop()
# =============================================================================
# =============================================================================
# def r_sum(nested_list):
#     """r_sum(nested_list) -> int
#     returns the sum of all elements in the nested_list"""
#     ret = 0
#     for el in nested_list:
#         if (type(el) == list):
#             ret += r_sum(el)
#         else:
#             ret += el
#     return ret
# 
# print(r_sum([1,2,[11,13], 8]))
# =============================================================================
# =============================================================================
# def r_max(nested_list):
#     """r_max(nested_list) -> int
#     returns the largest value in nested_list"""
#     largest = 0
#     isInit = False
#     for el in nested_list:
#         if (type(el) == list):
#             subLargest = r_max(el)
#         else:
#             subLargest = el
#         if (not isInit):
#             isInit = True
#             largest = subLargest
#         else:
#             largest = max(subLargest, largest)
#     return largest
# 
# print(r_max([2, 9, [1, 13], 8, 6]))  # should be 13
# print(r_max([2, [[100, 7], 90], [1, 13], 8, 6]))  # should be 100
# print(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]))  # should be 100
# print(r_max(["joe", ["sam", "ben"]]))  # should be "sam"
# =============================================================================
# =============================================================================
# def fib(n):
#     if n<=1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# 
# print(fib(4))
# =============================================================================
# =============================================================================
# """Problems"""
# def gcd(a,b):
#     """gcd(a,b) -> int
#     returns the gcd of a and b"""
#     if (a<b):
#         a,b = b,a
#     if (b==0):
#         return a
#     else:
#         return gcd(a-b,b)
# print(gcd(90,80))        #should be 10
# print(gcd(1800,9))       #should be 9
# print(gcd(142857,12321)) # should be 333
# =============================================================================
# =============================================================================
# def get_base_number(num,base):
#     '''get_base_number(num,base) -> int
#     returns value of num as a base number in the given base'''
#     if (len(num) == 0):
#         return 0
#     lastDigit = int(num[-1])
#     newNum = num[:-1]
#     return lastDigit + base*get_base_number(newNum, base)
#     
#  
# # test cases
# print(get_base_number('10011',2))  # should be 19
# print(get_base_number('3202',5))   # should be 427
# print(get_base_number('611023',7))
# =============================================================================
# =============================================================================
# def catalan(n, dp):
#     """catalan(n, dp) -> int
#     returns the nth catalan number"""
#     if (n==0):
#         return 1
#     elif (n in dp):
#         return dp[n]
#     Cn = 0
#     for i in range(n):
#         Cn += catalan(i,dp)*catalan(n-i-1,dp)
#         dp[n] = Cn 
#     return Cn
# 
# dp = {}
# print(catalan(30, dp))
# =============================================================================
# =============================================================================
# def permute(inputList):
#     '''permute(inputList) -> list
#     returns list of all permutations of inputList'''
#     if (len(inputList) == 1):
#         return [inputList]
#     retList = []
#     for i in range(len(inputList)):
#         for perm in permute(inputList[:-1]):
#             toInsert = perm.copy()
#             toInsert.insert(i, inputList[-1])
#             retList.append(toInsert)
#     return retList
# 
# # test cases
# print(permute([1,2]))
# # should print [[1,2], [2,1]] in some order
# print(permute([1,2,3]))
# # should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order
# =============================================================================
# =============================================================================
# def anagrams(word):
#     """anagrams(word) -> list
#     returns list of all anagrams of word"""
#     if (len(word) == 1):
#         return [word]
#     substr = word[:-1]
#     retList = []
#     for i in range(len(word)):
#         for ana in anagrams(substr):
#             newAna = ana[:i] + word[-1] + ana[i:]
#             retList.append(newAna)
#     return retList
# 
# def jumble_solve(string):
#     """jumble_solve(string) -> list
#     returns list of all valid anagrams of word"""
#     inFile = open("wordlist.txt")
#     dictionary = inFile.readlines()
#     inFile.close()
#     validWords = {}
#     for ana in anagrams(string):
#         if (ana.lower()+"\n" in dictionary):
#             validWords[ana] = 1
#     return list(validWords.keys())
# 
# print(jumble_solve("CHWAT"))
# print(jumble_solve("RAROM"))
# print(jumble_solve("CEPLIN"))
# print(jumble_solve("YAFLIM"))   
# print(jumble_solve("DIWSMO"))      
# print(jumble_solve("WISDOM"))  
# =============================================================================
def min_number_coins(coins):
    """min_number_coins(change, coins) -> list
    returns the list of minimum number of coins needed to return change"""
    minList= [0]
    for i in range(1,100):
        minimum = 100*100
        for coin in coins:
            if (i-coin >=0):
                minimum = min(minimum, minList[i-coin] + 1)
        minList.append(minimum)         
    return minList

def best_average_change():
    """best_average_change() -> int
    returns best average"""
    best = 100
    for i in range(1,100):
        for j in range(i+1, 100):
            for k in range(j+1, 100):
                best = min(sum(min_number_coins([i,j,k]))/100, best)
    return best
    

print(best_average_change())

























