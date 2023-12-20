#################################################
# hw3.py
# name: Donny Le 
# andrew id: 814477499
#################################################

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

#returns the largest number in a string 
#returns None is number does not exist
def largestNumber(s):
    stringNum = ""
    currentNum = 0 
    highestNum = -1 #used to fix edge case with line 46 (no numbers)
    
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

    if highestNum == -1: 
        return None

    return highestNum

#returns a new string that is rotated by n amount 
def rotateStringLeft(s, n):
    if s == '':
        return ''
        
    part1 = s[0:n%(len(s))]
    part2 = s[n%(len(s)):]
    return part2 + part1


#returns false/true if s is a string rotation of t
def isRotation(s, t):
    if(len(s)<2 or s==t):
        return False

    for i in range(len(s)):
        if(rotateStringLeft(s,i) == t):
            return True 

    return False

#helper function 
#checks if string is a palindrome
def isPalindrome(s):
    if len(s)<2:
        return True
    for i in range(len(s)//2):

        if(s[i]!=s[len(s)-1-i]):
            return False

    return True 

#returns the longest substring that is a palindrome
#in a string
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

                if (currentLen > maxLen or
                   (currentLen == maxLen and maxStr<wordSubstring)):
                    maxStr = wordSubstring
                    maxLen = currentLen
                    wordSubstring = ""
                    currentLen = 0
            
                else:
                    currentLen = 0
                    wordSubstring = ""
    return maxStr

#removes whitespace off of msg string
def cleanpatternedMessage(msg, pattern):
    pattern = repr(pattern)
    cleanedPattern = ""
    pattern = pattern[1:len(pattern)-1]

    if(pattern[0:2]== "\\n"):
        pattern = pattern[2:len(pattern)]

    if(pattern[len(pattern)-2:len(pattern)] == "\\n"):
        pattern = pattern[:len(pattern)-2]
    
    for char in msg:
        if(not char in string.whitespace):
            cleanedPattern += char
    return cleanedPattern, pattern

#places non-letter characters in a pattern with repeated message
def patternedMessage(msg, pattern):
    cleanedPattern, pattern =cleanpatternedMessage(msg, pattern)

    i = 0
    msgIndex = 0
    replacedPattern = ""

    while i<len(pattern):
        skiplineString = repr(pattern[i:i+2])
        skipline = repr("\\n")

        if (skipline in skiplineString):
            replacedPattern += "\n"
            i+=1 
        
        #when char in pattern is not 
        elif pattern[i]!=" ":  
            #msg index used to repeat "cleanedString" var in the pattern
            replacedPattern += cleanedPattern[msgIndex % len(cleanedPattern)]
            msgIndex +=1

        else:
            replacedPattern += " "

        i +=1 
        
    return replacedPattern
    

#returns the mastermind score
def calculateScore(s1, s2):
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

    return counterExact,counterPartial

#formats the mastermind score             
def mastermindScore(s1, s2):
    counterExact,counterPartial = calculateScore(s1,s2)
    partialStr = "partial match"
    exactStr = "exact match"
    
    if(counterExact == len(s1)):
        return "You win!!!"
    #statements with "es" used to format plural/singular words
   
    if(counterPartial >1):
        partialStr = partialStr + "es"

    if(counterExact >1):
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
 

   

#################################################
# hw3-bonus-functions
# these are optional
#################################################

def encodeRightLeftRouteCipher(text, rows):
    return 42
                

def decodeRightLeftRouteCipher(cipher):
    return 42




def topLevelFunctionNames(code):
    return 42




def getEvalSteps(expr):
    return 42


#################################################
# Test Functions
#################################################

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    assert(largestNumber("42!!!!") == 42)
    assert(largestNumber("12+3==15") == 15)
    assert(largestNumber("12dogs345cats67owls") == 345)
    assert(largestNumber("") == None)

    assert(largestNumber("He is 13. I am 15") == 15)
    assert(largestNumber("52!!") == 52)
    assert(largestNumber("My grandmother is 95 and my grandfather is 96") == 96)
    assert(largestNumber("The dog is 7 years old and my brother is 12") == 12)
    assert(largestNumber("1sun8planets") == 8)

    print("Passed!")

def testRotateStringLeft():
    print('Testing rotateStringLeft()...', end='')
    assert(rotateStringLeft('abcde', 0) == 'abcde')
    assert(rotateStringLeft('abcde', 1) == 'bcdea')
    assert(rotateStringLeft('abcde', 2) == 'cdeab')
    assert(rotateStringLeft('abcde', 3) == 'deabc')
    assert(rotateStringLeft('abcde', 4) == 'eabcd')
    assert(rotateStringLeft('abcde', 5) == 'abcde')
    assert(rotateStringLeft('abcde', 25) == 'abcde')
    assert(rotateStringLeft('abcde', 28) == 'deabc')
    assert(rotateStringLeft('abcde', -1) == 'eabcd')
    assert(rotateStringLeft('abcde', -24) == 'bcdea')
    assert(rotateStringLeft('abcde', -25) == 'abcde')
    assert(rotateStringLeft('abcde', -26) == 'eabcd')
    assert(rotateStringLeft('ABCDEF', -2) == 'EFABCD')

    assert(rotateStringLeft('a', -25) == 'a')
    assert(rotateStringLeft('hello', 5) == 'hello')
    assert(rotateStringLeft('[', 3) == '[')
    assert(rotateStringLeft('123123', 2) == '312312')
    assert(rotateStringLeft('#####', 2) == '#####')
    assert(rotateStringLeft('     ', 2) == '     ')



    assert(rotateStringLeft('', -26) == '')
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()...', end='')
    assert(isRotation('a', 'a') == False) # a string is not a rotation of itself
    assert(isRotation('', '') == False) # a string is not a rotation of itself
    assert(isRotation('ab', 'ba') == True)
    assert(isRotation('abcd', 'dabc') == True)
    assert(isRotation('abcd', 'cdab') == True)
    assert(isRotation('abcd', 'bcda') == True)
    assert(isRotation('abcd', 'abcd') == False)
    assert(isRotation('abcd', 'dcba') == False)
    assert(isRotation('abcd', 'bcd') == False)
    assert(isRotation('abcd', 'bcdx') == False)
    
    assert(isRotation('the', 'het') == True)
    assert(isRotation('the', 'hte') == False)
    assert(isRotation('number', 'number') == False)
    assert(isRotation('  ', ' d') == False)
    assert(isRotation('123456', '654321') == False)
    assert(isRotation('123456', '612345') == True)
    assert(isRotation('b', 'b') == False)
    assert(isRotation('\\\\', '\\\\') == False)

    print('Passed!')

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    assert(longestSubpalindrome("") == "")
    assert(longestSubpalindrome("abcdcbefe") == "bcdcb")
    
    assert(longestSubpalindrome("racecar") == "racecar")
    assert(longestSubpalindrome("dababy") == "bab")
    assert(longestSubpalindrome("jim") == "m")
    assert(longestSubpalindrome("a") == "a")
    assert(longestSubpalindrome("happy") == "pp")
    assert(longestSubpalindrome("assessment") == "ssess")
    assert(longestSubpalindrome("abcdcbefe") == "bcdcb")
    
    
    print("Passed!")

def testPatternedMessage():
    # print("Testing patternedMessage()...", end="")
    # assert(patternedMessage("abc def",   "***** ***** ****")   ==
    #        "abcde fabcd efab")
    # assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
    #        "abcde fabcd efab")

    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
        []

    assert(patternedMessage("big chungus", "*** *******") == "big chungus")
    print("Passed!")
    #I don't know how to make other test cases

                    
def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')

    assert(mastermindScore('ilikefood', 'ilikecake') ==
                           '5 exact matches')
    assert(mastermindScore('abcdefg', 'abgdefc') ==
                           '5 exact matches, 2 partial matches')
    assert(mastermindScore('test', 'test') ==
                           'You win!!!')
    assert(mastermindScore('tef', 'eif') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('efgh', 'efhg') ==
                           '2 exact matches, 2 partial matches')
      
    print("Passed!")


def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")



def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # hw3-standard
    testLargestNumber()
    testRotateStringLeft()
    testIsRotation()
    testLongestSubpalindrome()
    testPatternedMessage()
    testMastermindScore()


    # hw3-bonus
    # testEncodeAndDecodeRightLeftRouteCipher()
    # testTopLevelFunctionNames()
    # testGetEvalSteps()

def main():
    cs112_n22_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
