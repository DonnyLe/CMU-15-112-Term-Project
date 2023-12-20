#################################################
# hw6.py
#
# name: Donny Le
# andrew id: dmle
#################################################

import cs112_n22_week3_linter
import math, copy, string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# hw6-standard functions
#################################################

#returns the middle value of a list
#or returns the avg of the middle vals of a list
def median(L):
    list2 = copy.copy(L)
    list2.sort()
    #edge case
    if len(list2) == 0:
        return None

    listLength = len(list2)

    #first "if" returns middle value if length == odd
    #else returns the average of the two middle vals if len == even
    return list2[listLength//2] if listLength % 2 == 1 else (
            (list2[listLength//2-1] + list2[listLength//2])/2
    )

#returns the smallest distance (absolute val) of two numbers in a list
def smallestDifference(L):
    if len(L)<2:
        return -1 
    
    #intializes smallestDiff as the first difference
    #subtracts the max by min of first two vals in list
    smallestDiff = abs(max(L[0], L[1])- min(L[0],L[1]))
    for i in range(1,len(L)):
        for j in range (i+1, len(L)):
            #subtracts the max by min of first two vals in list
            currentDiff = abs(max(L[i], L[j])- min(L[i],L[j]))
            if currentDiff <= smallestDiff:
                smallestDiff = currentDiff
    return smallestDiff

#non-destructively removes repeat chars in list
def nondestructiveRemoveRepeats(L):
    res = []
    i = 0

    while i < len(L):
        #checks if L[i] is not a repeat
        if(not L[i] in res):
            res.append(L[i])

        i+=1 

    return res

#destructively removes repeat chars in list
def destructiveRemoveRepeats(L):
    i = 0
    repeatCount = 0

    while i<len(L):
        #counts the number of times a char repeats in list
        repeatCount = L.count(L[i])
        #enters "if" when a char has repeat chars
        if repeatCount > 1:
            #loops for num of repeat chars
            for j in range(repeatCount-1):
                #finds index of repeat chars
                #excludes first appearance of char
                indexRepeat = L[i+1:].index(L[i])
                #removes repeat char
                L.pop(indexRepeat+i+1)
        i+=1
        
            
#counts the number of the same consecutive nums
#adds the count and the number to a tuple
#adds tuples to newlist and returns list

def lookAndSay(L):
    #edge case
    if (len(L) == 0):
        return L

    #initializes pastNum at first num in list
    pastNum = L[0]
    counter = 1
    res = []

    #index begins at 1 b/c pastNum == L[0]
    for i in range(1,len(L)):
        
        #checks if a num repeats consecutively
        if pastNum == L[i]:
            counter += 1
        
        #creates tuple and adds tuple to list
        elif pastNum != L[i]:
            tuplePair = (counter, pastNum) 
            res.append(tuplePair)
            counter = 1

        pastNum = L[i]
    
    tuplePair = (counter, pastNum) 
    res.append(tuplePair)
    
    return res

#reverses operation done by previous function 
def inverseLookAndSay(L):
    numAmount = 0
    res = []

    for tup in L:
        #gets the number counter in the tuple 
        numAmount = tup[0]

        for i in range(numAmount):
            res.append(tup[1])
    return res

#helper function
#adds two lists
#adds trailing zeros
def addLists(p1, p2):
    lenList1 = len(p1)
    lenList2 = len(p2)

    #if, else, adds trailing zeros 
    if(lenList1 < lenList2):
        difference = lenList2-lenList1
        p1 += [0]*difference
    else:
        difference = lenList1-lenList2
        p2 += [0]*difference 

    res = []

    #adds lists 
    for i in range(len(p1)):
        res.append(p1[i]+ p2[i])
    return res

#multiplies two polynomials
#returns coefficients 
def multiplyPolynomials(p1, p2):
    finalList = []
    
    
    for i in range(len(p1)):
        #creates new list for every distribution multiplication cycle
        partialList = [0] * i
        for j in range(len(p2)): 
            partialList.append(p1[i]*p2[j])

        #helper function call, accumulates the finallist
        finalList = addLists(finalList, partialList)
        
    return finalList

#helper function
#checks if the word is in the hand
def wordinHand(word, hand):
    #non-destructive copy
    handCopy = copy.copy(hand)

    for i in range(len(word)):
        if not word[i] in handCopy:
            return False
        #removes letters to prevent duplicates
        elif word[i] in hand:
            handCopy.remove(word[i])
    return True 

#calculates word score based on letterScores list
def calculateWordScore(letterScores, word):
    total = 0

    for i in range(len(word)):
        wordVal = ord(word[i])-97
        letterScore = letterScores[wordVal]
        total += letterScore

    return total
    
def bestScrabbleScore(dictionary, letterScores, hand):
    maxScore = 0
    #list if there are two max scores
    multipleMax = []

    for i in range(len(dictionary)):
        if wordinHand(dictionary[i], hand):
            currentScore = calculateWordScore(letterScores, dictionary[i])
            
            if(currentScore>maxScore):
                multipleMax.append(dictionary[i])
                maxScore = currentScore
                maxWord = dictionary[i]
            
            #if multiple maxes, add to multipleMax
            elif currentScore == maxScore:
                multipleMax.append(dictionary[i])
    
    #if no valid words, return None
    if(maxScore) == 0:
        return None
    #checks if there are more than 1 words in multipleMax
    #return tuple
    if len(multipleMax)>1: 
        return (multipleMax, maxScore)
    
    return (maxWord, maxScore)

#################################################
# Bonus/Optional
#################################################

def linearRegression(pointsList):
    return 42

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    assert(almostEqual(median([-2, -4, 0, -6]), -3))
    assert(almostEqual(median([1.5, 2.5]), 2.0))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([5]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    assert(nondestructiveRemoveRepeats([]) == [])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    c = []
    assert(destructiveRemoveRepeats(c) == None)
    assert(c == [])
    print("Passed!")

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

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
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testBestScrabbleScore()

    # Bonus:
    #testLinearRegression()
    #testRunSimpleProgram() 

def main():
    cs112_n22_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
