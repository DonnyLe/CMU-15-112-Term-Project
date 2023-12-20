#################################################
# hw2.py
#
# Your name: Donny Le 
# Your andrew id: 814477499
#################################################

import hw2.cs112_n22_week1_hw2_linter as cs112_n22_week1_hw2_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

############################
# hw2 required problems
############################
def getKthDigit(n, k):
    n = abs(n) % (10 ** (k+1))
    n = n // 10 ** (k)
    return n 

def lengthOfNum(n):
    length = 0
    i = 0
    booleanVal = True
    while booleanVal==True:
        if(10**i <= n):
            length+=1
            i = i + 1 
        else:
            booleanVal = False
    return length 

def isPalindromicNumber(n):
    length = lengthOfNum(n)
    for i in range(0, roundHalfUp((length)/2)):
        num1 = getKthDigit(n, i)
        j = (length-1) - i
        num2 =  getKthDigit(n, j)
        if (num1 != num2):
            return False
    return True

def nthPalindromicPrime(n):
    guess = 0
    found = 0
    while found<=n :
        guess += 1
        if isPrime(guess) and isPalindromicNumber(guess):
            found+= 1
    return guess 

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if(n%i==0):
            return False 
    return True 



def hasConsecutiveDigits(n):
    length = lengthOfNum(abs(n))
    for i in range (0, length-1):
        if getKthDigit(n, i) == getKthDigit(n, i+1):
            return True
    return False

def setKthDigit(n, k, d):
    neg = False
    if n*(-1)>0:
        neg = True
    n = abs(n)
    n1 = getKthDigit(n, k) * 10**(k)
    n = n - n1
    n = n+ (d*10**(k))
    if neg==True: 
        return n*-1
    else: 
        return n  

def carrylessAdd(x1, x2):
    length1 = lengthOfNum(x1)
    length2 = lengthOfNum(x2)
    highlen = 0

    if(length1> length2):
        highlen = length1
    else:
        highlen = length2
       
    newnum = 0
    for i in range(highlen): 
        digit1 = getKthDigit(x1, i)
        digit2 = getKthDigit(x2, i)
        sum = (digit1 + digit2) % 10
        newnum = setKthDigit(newnum, i, sum)
    return newnum 



def longestDigitRun(n):
   #four variables 
   #max digit, currentcounter, maxcounter
   #while n>0
   #mod 10 
   #//10 
    n = abs(n)
    if(n>9):
        maxdigit = 0
        currentcounter = 1
        maxcounter = 1
        digit1 = n%10
        n = n//10
    
        while (n>0):
            digit2 = n % 10 
            n = n//10 
            if digit1 == digit2:
                currentcounter += 1
            elif currentcounter == maxcounter: 
                maxdigit = min(maxdigit, digit1)
                currentcounter = 1

            elif currentcounter > maxcounter: 
                maxcounter = currentcounter
                maxdigit = digit1
                currentcounter = 1      
            else:
                currentcounter = 1


            digit1 = digit2
        ## repeat if statements for after the loop when
        #  the largest sequence of numbers is at the left 
        ##end of the number 
        if currentcounter == maxcounter: 
                maxdigit = min(maxdigit, digit1)
                currentcounter = 1
        elif currentcounter > maxcounter: 
                maxcounter = currentcounter
                maxdigit = digit1
                currentcounter = 1  
        return maxdigit
    else:
        return n
    



  
        
############################
# hw2 bonus nthSmithNumber
############################

def nthPrime(n):
    guess = 0
    found = 0
    while found<=n :
        guess += 1
        if isPrime(guess) == True:
            found+= 1
    return guess

def sumDigits(n):
    sum = 0
    while n>0:
        digit = n % 10 
        n = n//10
        sum += digit
    return sum


def isSmithNumber(n):
    primefactorSum = 0
    tempn = n
    while n>1:
        e = 0
        while n % nthPrime(e) != 0:
            e = e+1 
        primefactorSum += sumDigits(nthPrime(e))
        n = int(n/nthPrime(e))

        if(nthPrime(e)==tempn):
            primefactorSum-= tempn

    if primefactorSum == (sumDigits(tempn)):
        return True
    else:
        return False




def nthSmithNumber(n):
    guess = 0
    count = 0
    while n>=count:
        guess += 1
        if(isSmithNumber(guess)):
            count +=1 

    return guess


############################
# hw2 bonus integerDataStructures
############################
def intCat(n , m):
    lengthm = lengthOfNum(m)
    if(m == 0):
        lengthm = 1
    newnum = 10**lengthm * n + m 
    return newnum

def lengthEncode(n):
    pos = 2
    if( n >= 0):
        pos = 1
    count = lengthOfNum(abs(n))
    if(n==0):
        count = 1
    countcount = lengthOfNum(count)
   
    return (intCat(intCat(
        intCat(pos, countcount), count), abs(n)))



#from left to right

def lengthDecode(n):
    n = abs(n)
    nlength = lengthOfNum(n)
    posneg = n // (10**(nlength-1))
    n = n - posneg * 10 ** (nlength-1)
    countcount = n // (10**(nlength-2))
    n = n - posneg * 10 ** (nlength-2)
    n = n % (10 ** (nlength-2-countcount))
    if posneg == 2:
        return n * -1
    return n

#p is value from right to left


def lengthDecodeLeftmostValue(n):
    n = abs(n)
    nlength = lengthOfNum(n)
    posneg = n // (10**(nlength-1))
    n = n - posneg * 10 ** (nlength-1)
    countcount = n // (10**(nlength-2))
    n = n - posneg * 10 ** (nlength-2)
    count = n // (10**(nlength-2-countcount))
    n = n - countcount * 10 ** (nlength-2-countcount)
    n = n % (10 ** (nlength-2-countcount))
    encoded = n // (10 ** (nlength-3-count*countcount))
    nextValue = n - encoded*(10**(nlength-3-count*countcount))
    return encoded, nextValue

#this version of the function does not return next value
def lengthDecodeLeftmostValueOnly(n): 
    n = abs(n)
    nlength = lengthOfNum(n)
    posneg = n // (10**(nlength-1))
    n = n - posneg * 10 ** (nlength-1)
    countcount = n // (10**(nlength-2))
    n = n - posneg * 10 ** (nlength-2)
    count = n // (10**(nlength-2-countcount))
    n = n - countcount * 10 ** (nlength-2-countcount)
    n = n % (10 ** (nlength-2-countcount))
    encoded = n // (10 ** (nlength-3-count*countcount))
    return encoded
    

def leftMostValueSubtract(n): 
    n = abs(n)
    nlength = lengthOfNum(n)
    posneg = n // (10**(nlength-1))
    n = n - posneg * 10 ** (nlength-1)
    countcount = n // (10**(nlength-2))
    n = n - posneg * 10 ** (nlength-2)
    count = n // (10**(nlength-2-countcount))
    n = n - countcount * 10 ** (nlength-2-countcount)
    n = n % (10 ** (nlength-2-countcount))
    encoded = n // (10 ** (nlength-3-count*countcount))
    n = n - encoded * (10 ** (nlength-3-count*countcount))
    return n, encoded, nlength, count, countcount

def newIntList():
    return lengthEncode(0)

def intListLen(L):
    value, placeholder = lengthDecodeLeftmostValue(L)
    return value

#this function does not include the first encoded value in a list 
def intListGet(L,i):
    counter = -1
    while (counter< i ):
    
        L, encodedval, nlength, count, countcount = leftMostValueSubtract(L)
        counter = counter + 1
        if(L == 0):
            return "index out of range"
    value = lengthDecodeLeftmostValueOnly(L)
    return value

#this function includes the first encoded value in a list 
def intListGet2(L,i): 
    counter = 0
    
    while (counter< i ):
        
        L, encodedval, nlength, count, countcount = leftMostValueSubtract(L)
        counter = counter + 1
        if(L == 0):
            return "index out of range"
    value = lengthDecodeLeftmostValueOnly(L)
    return value




def helperSetLeftMostList(L, v):
    L, encoded, nlength, count, countcount = leftMostValueSubtract(L)
    L = L + v * (10 ** (nlength-3-count*countcount))
    return L 

def intListSet(L,i,v):
    counter = 0
    val1 = 0
    val2 = 0
    while (counter< i+1 ):
        lengthL = lengthOfNum(L)
        val1 = intListGet2(L,counter)
        if(L == 0 or type(val1)==str):
            return "index out of range"

        val1 = lengthEncode(val1)
        lengthVal = lengthOfNum(val1)
        counter = counter + 1

    L, encodedval, nlength, count, countcount = leftMostValueSubtract(L)
    L = lengthEncode(v) 
    lengthL = lengthOfNum(L)
    power = lengthL
      
    value = helperSetLeftMostList(L, lengthEncode(v))
    value += val2
    return value




def intListAppend(L,v):
    v = lengthEncode(v)
    lengthV = lengthOfNum(v)
    L = L * 10**lengthV
    L += v
    L = L + 10 ** (lengthOfNum(L)-4)
    return L






def intListPop(L):
    val1 = intListGet2(L,0)
    val1 = lengthEncode(val1)
    i = getKthDigit(val1,lengthOfNum(val1)-4)
    counter = 1
    val1 = setKthDigit(val1,lengthOfNum(val1)-4,i-1)
    M = newIntList()
    M = intListSet(M,-1,val1)

    while(counter<i):
        M = intListAppend(M, lengthEncode(intListGet2(L, counter)))
        counter = counter+1
    L = intListSet(L,-1,val1)
    lengthL = lengthOfNum(L)
    lengthM = lengthOfNum(M)
    diff = lengthL - lengthM
    valPopped = lengthDecode(L - M*10**diff)
    return valPopped, M





    

    

#Add remaining functions as needed

#################################################
# Test Functions
# ignore_rest (tells autograder to ignore everything below here)
#################################################

def testIsPalindromicNumber():
    print('Testing isPalindromicNumber()...', end='')
    assert isPalindromicNumber(0) == True
    assert isPalindromicNumber(4) == True
    assert isPalindromicNumber(10) == False
    assert isPalindromicNumber(101) == True
    assert isPalindromicNumber(1001) == True
    assert isPalindromicNumber(10010) == False
    print('Passed.')


def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(111222111) == 1)
    assert(longestDigitRun(22222) == 2)
    
    print('Passed.')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    assert(nthSmithNumber(15) == 382)
    print('Passed.')

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length-encoded 0
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # [1, 42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')
    
    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # [1, 567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # [1, 9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # [1, 9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # [ 0 ]
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # [1, 65]
    assert(encodeString('f') == 1111113102) # [1, 102]
    assert(encodeString('3') == 111111251) # [1, 51]
    assert(encodeString('!') == 111111233) # [1, 33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # [4,65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # [ 0 ]
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # [ 2, 42, 73 ]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # [ 2, 42, 98765 ]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # [ 4, 42, 98765, 99, 0 ]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # 6* -> 1
    fsm = setTransition(fsm, 1, 7, 2) # 7 -> 2
    fsm = setTransition(fsm, 2, 7, 2) # 7* -> 2
    fsm = setTransition(fsm, 2, 8, 3) # 7* -> 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')


def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testEncodeDecodeStrings()
    testIntMap()
    testIntFSM()
    testAccepts()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!

    # hw2
    testIsPalindromicNumber()
    testNthPalindromicPrime()
    testHasConsecutiveDigits()
    testCarrylessAdd()
    testLongestDigitRun()

    # hw2-bonus (uncomment to test)
    testNthSmithNumber()
    testIntegerDataStructures()


def main():
    testAll()
    cs112_n22_week1_hw2_linter.lint()

if __name__ == '__main__':
   main()