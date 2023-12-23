import cs112_n22_week2_linter
import math, string, random

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
# hw3-standard-functions
#################################################

def largestNumber(s):
    stringNum = ""
    currentNum = 0
    highestNum = 0
    s += " " #used to fix edge case (max num at end of str)
    for i in range(len(s)-1):
        if s[i] in string.digits and s[i+1] in string.digits :
            stringNum += s[i]
        elif  s[i] in string.digits and not s[i+1] in string.digits: 
            stringNum += s[i]
            currentNum = int(stringNum)
            if highestNum< currentNum:
                highestNum = currentNum
            stringNum = ""
    return highestNum

def rotateStringLeft(s, n):
    part1 = s[0:n%(len(s))]
    part2 = s[n%(len(s)):]
    return part2 + part1


def isRotation(s, t):
    if(len(s)<2 or s==t):
        return False
    for i in range(len(s)):
        if(rotateStringLeft(s,i) == t):
            return True 
    return False

def isPalindrome(s):
    if len(s)<2:
        return True
    for i in range(len(s)//2):

        if(s[i]!=s[len(s)-1-i]):
            return False

    return True 


def longestSubpalindrome(s):
    wordSubstring = ""
    maxLen = 0
    currentLen = 0
    maxStr = ""

    for i in range(len(s)):
        for j in range(len(s)):
            if(s[i]==s[j]):
                wordSubstring = s[i:j+1]

                if(isPalindrome(wordSubstring)):
                    currentLen = len(wordSubstring)

                if currentLen > maxLen:
                    maxStr = wordSubstring
                    maxLen = currentLen
                    wordSubstring = ""
                    currentLen = 0
            
                elif currentLen == maxLen and maxStr<wordSubstring:
                    maxStr = wordSubstring
                    wordSubstring = ""
                    maxLen = currentLen
                    currentLen = 0
                
                else:
                    currentLen = 0
                    wordSubstring = ""
    return maxStr
            

def removeSpace(s):
    removedWhitespace = ""
    for char in s:
        if(not char in string.whitespace):
            removedWhitespace += char
    return removedWhitespace

def patternedMessage(msg, pattern):
    pattern = repr(pattern)

    pattern = pattern[1:len(pattern)-1]
    if(pattern[0:2]== "\\n"):
        pattern = pattern[2:len(pattern)]
    if(pattern[len(pattern)-2:len(pattern)] == "\\n"):
        pattern = pattern[:len(pattern)-2]
    
    msg = removeSpace(msg)

    i = 0
    j = 0
    newpattern = ""
    while i<len(pattern):
        skiplineString = repr(pattern[i:i+2])
        skipline = repr("\\n")
        if (skipline in skiplineString):
            newpattern += "\n"
            i+=1 
        elif pattern[i]!=" " and pattern[i]!="n":  
            newpattern += removedWhitespace[j % len(removedWhitespace)]
            j +=1
        else:
            newpattern += " "
        i +=1 
    return newpattern
    

def mastermindScore(s1, s2):
    counterExact = 0
    stringExactChars = ""
    for i in range(len(s1)):
        if (s1[i] == s2[i]):
            counterExact += 1
            stringExactChars += s2[i]

    stringPartialChars = ""
    counterPartial = 0 
    for j in range(len(s1)):
        for k in range(len(s1)):
            if (s1[j] == s2[k] and j!=k and not s2[k] in stringExactChars and 
            not s2[k] in stringPartialChars):
                stringPartialChars += s2[k]
                counterPartial +=1 
                

    partialStr = "partial match"
    exactStr = "exact match"

    if(counterExact == len(s1)):
        return "You win!!!"

    elif(counterPartial >1):
        partialStr = partialStr + "es"
    elif(counterExact >1):
        exactStr = exactStr + "es"
    elif(counterExact >1 and counterPartial >1):
        partialStr = partialStr + "es"
        exactStr = exactStr + "es"

    if counterPartial == 0 and counterExact == 0:
        return "No matches"

    if counterPartial == 0 or counterExact == 0:
        if(counterPartial == 0):
            return f'{counterExact} {exactStr}'
        return f'{counterPartial} {partialStr}' 
 

    return f'{counterExact} {exactStr}, {counterPartial} {partialStr}' 
 
def giveIndex(row, col, numrow, numcol):
    i = 0
    for indexCol in range(numcol):
        for indexRow in range(numrow):
            if(indexRow == row and indexCol == col):
                return i 
            else: 
                i +=1 



def encodeRightLeftRouteCipher(text, rows):
    text = removeSpace(text)
    res = ""        
    cols = math.ceil(len(text)/ rows)
    alphabet = string.ascii_lowercase
    lenAlpha = len(alphabet)

    for j in range(rows):

        rowLine = ""

        for k in range(cols):
            # print(f'rows = {j}, cols = {k}')
            index = giveIndex(j, k, rows, cols)
            print(index)
            if(index >= len(text)):
                res += alphabet[len(alphabet)-1]
                alphabet = alphabet[:len(alphabet)-1]
            else:
                rowLine += text[index]
        
                if(j%2==1):
                    rowLine = rowLine[::-1]

        res += rowLine

    return str(rows)+res

def decodeRightLeftRouteCipher(text):
    row = text[0]
    text = text[1::]

def drawFancyWheels(width, height, rows, cols):
    cellwidth = width/cols
    cellheight = height/rows
    halfwidth = width/2
    halfheight = height/2 
    r = min(cellwidth,height)/2 *0.9
    cx, cy = halfwidth,halfheight
    n = 0 
    for rowsIndex in range(rows):
        for colIndex in range(rowsIndex):
            print(colIndex)

drawFancyWheels(600, 600, 6, 4)

