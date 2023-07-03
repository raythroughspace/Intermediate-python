def anagrams(string):
    """anagrams(string) -> list
    returns a list of anagrams of string"""
    if (len(string) == 1):
        return [string]
    substr = string[:-1]
    outList = []
    for subana in anagrams(substr):
        for i in range(len(string)):
            ana = subana[:i] + string[-1] + subana[i:]
            outList.append(ana)
    return outList

def jumble_solve(string):
    """jumble_solve(string) -> list
    returns a list of valid word anagrams of string"""
    rfd = open("wordlist.txt", "r")
    wordList = {}
    for word in rfd:
        word = word.strip()
        wordList[word] = 1
    rfd.close()
    
    validWords = {}
    for ana in anagrams(string):
        if (ana.lower() in wordList):
            validWords[ana] = 1
    return list(validWords.keys())

print(jumble_solve("CHWAT"))
print(jumble_solve("RAROM"))
print(jumble_solve("CEPLIN"))
print(jumble_solve("YAFLIM"))   
print(jumble_solve("DIWSMO"))      
print(jumble_solve("WISDOM"))   