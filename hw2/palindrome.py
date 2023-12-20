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


def isPalindromicNumber(n):
    length = 0
    i = 0
    booleanVal = True
    

    while booleanVal==True:
        if(10**i <= n):
            length+=1
            i = i + 1
            
        else:
            booleanVal = False

    for i in range(0, roundHalfUp((length)/2)):
        num1 = abs(n) % (10 ** (i+1))
        num1 = num1 // 10 ** (i)
        j = (length-1) - i
        num2 = abs(n) % (10 ** (j+1))
        num2 = num2 // 10 ** (j)
        print("Num1: ", num1, "Num2: ", num2)
        if (num1 != num2):
            return False
    return True

def nthPalindromicPrime(n):
    guess = 0
    found = 0
    while found<=n :
        guess += 1
        print(guess)
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


print(nthPalindromicPrime(5))