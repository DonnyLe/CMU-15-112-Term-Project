"""def generateFizzBuzz():
    yield('Fizz')
    yield('Buzz')
    yield('FizzBuzz')
f = generateFizzBuzz()

input()
print(next(f))
input()
print(next(f))
input()
print(next(f))

def storeGen():
    x = input()
    yield()

def infiniteRange( start, step):
    i = start
    while True:
        yield i
        i+= step
    
for i in infiniteRange(0,10):
    print(i)
    if i>=1000: 
        break

def triangle():
    total = 0
    i = 0
    while True:
        i+=  1
        total += i 
        yield total

def testTriangle():
    t = triangle() 
    next(t) 

"""


import math 
def fibonacci():
    a = 0
    b = 1
    while True: 
        yield a
        a, b = b, a+ b #simultaneously

jim = fibonacci()
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))
print(next(jim))

def rationals():
    numer = 1
    denom = 1
    while True:
        for denom in range(1,numer + 1):
            if (math.gcd(numer, denom) != 1):
                continue
            yield numer, denom 
            yield denom, numer
        numer += 1

def decToFrac(f,e):
    a, b =frac
    for frac in rationals():
        if abs(a/b-f)<= e:
            return frac


import random 
random.seed(8)
print(random.random())
print(random.random())
print(random.random())
print(random.random())
