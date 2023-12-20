def isNarcNumber(n):
    digitCount = getDigitCount(n)
    result = 0
    og = n
    for i in range(digitCount):
        digit = n % 10
        result += digit**digitCount
        n //= 10 
    return result == og

def getDigitCount(n):
    count = 0
    while n> 0:
        count+= 1
        n//=10
    return count 




def nthNarcissisticNumber(n):
    found = guess = 0
    while found <= n:
        guess += 1
        if isNarcNumber(guess):
            found+=1 
        return guess

def addDigits(n):
    