#################################################
# hw11.py
#
# Your name: Donny Le
# Your andrew id: dmle
#################################################

import cs112_n22_week5_linter
import math, copy

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

#counts number of odds in list
def oddCount(L):
    #basecase
    #if 
    if not L:
        return 0

    #recursive calls
    #checks if odd, adds 1
    elif L[0] % 2 == 1:
        return 1 + oddCount(L[1::])
    #else, remove first element
    else:
        return oddCount(L[1::])
    
#sums all odds
def oddSum(L):
    #base case
    #if L is empty
    if not L:
        return 0

    #recursive calls
    #if L[0] is odd, add to addition stack
    elif L[0] % 2 == 1:
        return L[0] + oddSum(L[1:])
        
    #else, remove L[0], call again
    else:
        return oddSum(L[1:])

#returns list of odds only
def oddsOnly(L):
    #base case
    #if L is empty, return empty list
    if not L:
        return []

    #recursive calls
    #if L[0] is odd, add element to new list,
    elif L[0] % 2 == 1:
        return [L[0]] + oddsOnly(L[1:])
    #remove first element, call again
    else:
        return oddsOnly(L[1:])

def maxOdd(L):
    #reassigns list of only odds
    L = oddsOnly(L)
    #base cases
    #if input list is empty, return None
    if not L:
        return None
    #if len L is 1, return val in list
    if len(L) == 1:
        return L[0]

    #recursive calls
    #compares first and last elements
    elif L[0] > L[-1]:
        return maxOdd(L[:-1])
    #else, removes first element
    else:
        return maxOdd(L[1:])

#################################################
# Test Functions
#################################################

def testOddCount():
    print('Testing oddCount()...', end='')
    assert(oddCount([ ]) == 0)
    assert(oddCount([ 2, 4, 6 ]) == 0) 
    assert(oddCount([ 2, 4, 6, 7 ]) == 1)
    assert(oddCount([ -1, -2, -3 ]) == 2)
    assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
    print('Passed!')

def testOddSum():
    print('Testing oddSum()...', end='')
    assert(oddSum([ ]) == 0)
    assert(oddSum([ 2, 4, 6 ]) == 0) 
    assert(oddSum([ 2, 4, 6, 7 ]) == 7)
    assert(oddSum([ -1, -2, -3 ]) == -4)
    assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
    print('Passed!')

def testOddsOnly():
    print('Testing oddsOnly()...', end='')
    assert(oddsOnly([ ]) == [ ])
    assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
    assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
    assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
    assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
    print('Passed!')

def testMaxOdd():
    print('Testing maxOdd()...', end='')
    assert(maxOdd([ ]) == None)
    assert(maxOdd([ 2, 4, 6 ]) == None) 
    assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
    assert(maxOdd([ -1, -2, -3 ]) == -1)
    assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testOddCount()
    testOddSum()
    testOddsOnly()
    testMaxOdd()

def main():
    cs112_n22_week5_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
