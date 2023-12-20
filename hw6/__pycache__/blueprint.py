import copy


def smallestDifference(L):
    if len(L)<2:
        return -1 
    smallestDiff = abs(max(L[0], L[1])- min(L[0],L[1]))
    for i in range(1,len(L)):
        for j in range (i+1, len(L)):
            currentDiff = abs(max(L[i], L[j])- min(L[i],L[j]))
            if currentDiff <= smallestDiff:
                smallestDiff = currentDiff
    return smallestDiff


def nondestructiveRemoveRepeats(L):
    res = []
    i = 0
    while i < len(L):
        if(not L[i] in res):
            res.append(L[i])
        i+=1 
    return res

def destructiveRemoveRepeats(L):
    i = 0
    repeatCount = 0
    while i<len(L):

        repeatCount = L.count(L[i])
        if repeatCount > 1:
            for j in range(repeatCount-1):
                indexRepeat = L[i+1:].index(L[i])
                L.pop(indexRepeat+i+1)
        i+=1
    



def lookAndSay(L):
    pastNum = L[0]
    counter = 1
    
    res = []

    for i in range(1,len(L)):
        

        if pastNum == L[i]:
            counter += 1
            
        elif pastNum != L[i]:
            tuplePair = (counter, pastNum) 
            res.append(tuplePair)
            counter = 1

        pastNum = L[i]
    
    tuplePair = (counter, pastNum) 
    res.append(tuplePair)
    
    return res



def inverseLookAndSay(L):
    numAmount = 0
    res = []
    for tup in L:
        numAmount = tup[0]
        for i in range(numAmount):
            res.append(tup[1])
    return res

def addLists(p1, p2):
    lenList1 = len(p1)
    lenList2 = len(p2)

    if(lenList1 < lenList2):
        difference = lenList2-lenList1
        p1 += [0]*difference
    else:
        difference = lenList1-lenList2
        p2 += [0]*difference 

    res = []
    for i in range(len(p1)):
        res.append(p1[i]+ p2[i])
    return res




def multiplyPolynomials(p1, p2):
    finalList = []
    
    for i in range(len(p1)):
        partialList = [0] * i
        for j in range(len(p2)):
         
            partialList.append(p1[i]*p2[j])
        finalList = addLists(finalList, partialList)
        # print(partialList)
    return finalList

def wordinHand(word, dictionary, hand):
    handcopy = copy.copy(hand)
    for i in range(len(word)):
        if not word[i] in handcopy:
            return False
        elif word[i] in hand:
            handcopy.remove(word[i])
    return True 


def calculateWordScore(letterScores, word):
    total = 0
    for i in range(len(word)):
        wordVal = ord(word[i])-97
        letterScore = letterScores[wordVal]
        total += letterScore
    return total
    
def bestScrabbleScore(dictionary, letterScores, hand):
    maxScore = 0
    multipleMax = []
    for i in range(len(dictionary)):
        if wordinHand(dictionary[i], dictionary, hand):
            currentScore = calculateWordScore(letterScores, dictionary[i])
            if(currentScore>maxScore):
                multipleMax.append(dictionary[i])
                maxScore = currentScore
                maxWord = dictionary[i]
                # print(calculateWordScore(letterScores, hand[i]))
            elif currentScore == maxScore:
                multipleMax.append(dictionary[i])
                
    if(maxScore) == 0:
        return None
    if len(multipleMax)>1:
        return (multipleMax, maxScore)
    
    return (maxWord, maxScore)
def dictionary1(): return ["a", "b", "c"]
def letterScores1(): return [1] * 26
def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
def letterScores2(): return [1+(i%5) for i in range(26)]
print(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")))    

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    print(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")))    
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")
testBestScrabbleScore()