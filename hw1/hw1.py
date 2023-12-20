#################################################
# hw1.py
# name: Donny Le 
# andrew id: 814477499
#################################################

import hw1.cs112_n22_week1_hw1_linter as cs112_n22_week1_hw1_linter
import math
import cmath

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
# hw1-standard-functions
#################################################

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    if d <= (r1+r2):
        return True
    else:
        return False

def getKthDigit(n, k):
    
    n = abs(n) % (10 ** (k+1))
    n = n // 10 ** (k)
    return n 


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




def fabricYards(inches):
    conversion = inches/36
    if ((conversion)%1>0):
        return int(conversion) +1
    else:
        return int(conversion)
 
def fabricExcess(inches):
    amount = 36*fabricYards(inches)
    excess = amount - inches
    return excess



#################################################
# hw1-bonus-functions
# these are optional! You may (and should) write 
# and use additional helper functions!
#################################################

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = xIntersection(m1, b1, m2, b2)
    x2 = xIntersection(m2, b2, m3, b3)
    x3 = xIntersection(m3, b3, m1, b1)
    y1 = yIntersection(m1, b1, m2, b2)
    y2 = yIntersection(m2, b2, m3, b3)
    y3 = yIntersection(m3, b3, m1, b1)
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)

    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area 

def xIntersection(m1, b1, m2, b2):
    x = (b1-b2)/(m2-m1)
    return x 

def yIntersection(m1,b1,m2,b2):
    x = xIntersection(m1,b1,m2,b2)
    y = x * m1 + b1
    return y 

def colorBlender(rgb1, rgb2, midpoints, n):
    if(n>=0 and n<=midpoints+1):
        b1 = rgb1 % 10**3
        g1 = (rgb1 % 10**6 - rgb1 % 10**3)//10**3 
        r1 = (rgb1 % 10**9 - rgb1 % 10**6) //10**6 
        b2 = rgb2 % 10**3
        g2 = (rgb2 % 10**6 - rgb2 % 10**3)//10**3 
        r2 = (rgb2 % 10**9 - rgb2 % 10**6) //10**6 

        spacingRed = (r1-r2)/(midpoints+1)
        spacingGreen = (g1-g2)/(midpoints+1)
        spacingBlue = (b1-b2)/(midpoints+1)

        r3 = roundHalfUp(r1 - spacingRed * n )
        g3 = roundHalfUp(g1 - spacingGreen * n) 
        b3 = roundHalfUp(b1 - spacingBlue * n )
        return (r3*10**6+ g3*10**3+b3)
    else: 
        return None
    

def findIntRootsOfCubic(a, b, c, d):
    p = (-b)/(3*a)
    q = p**3 + ((b*c - 3*a*d)/(6*a**2))
    r = c/(3*a) 
    root1 = (q+(q**2+(r-p**2)**3)**(1/2))**(1/3)
    root1 +=(q-(q**2+(r-p**2)**3)**(1/2))**(1/3)+p
    
    root1 = 1*root1.real
    root2 = -b-root1*a
    root2 = (root2+(cmath.sqrt(b**2-4*a*c-2*a*b*root1-3*a**2*root1**2)))/(2*a)
    root3 = -b-root1 * a
    root3 = (root3-(cmath.sqrt(b**2-4*a*c-2*a*b*root1-3*a**2*root1**2)))/(2*a)

    root2 = roundHalfUp(root2.real)
    root3= roundHalfUp(root3.real)
    root1 = roundHalfUp(root1)
    if(root1<=root2 and root2<=root3):
        return (root1, root2, root3)
    elif(root1>=root2 and root2>=root3):
        return (root3, root2, root1)
    elif(root1<=root3 and root3<=root2):
        return(root1, root3,root2)
    elif(root3<=root2 and root2<=root1):
        return root3,root2,root1
    elif(root3<=root1 and root1<=root2):
        return root3, root1, root2
    else:
        return root2, root3,root1 
    

    # you are assured a != 0
    # you are also assured the answer will be 3 integers!


#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')



def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3): #helper-fn
    # helper function for testFindIntRootsOfCubic
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3): #helper-fn
    # helper function for testFindIntRootsOfCubic
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = findIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2) #helper-fn
    testFindIntRootsOfCubicCase(2, 5, 33, 7) #helper-fn
    testFindIntRootsOfCubicCase(-18, 24, 3, -8) #helper-fn
    testFindIntRootsOfCubicCase(1, 2, 3, 4) #helper-fn
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetKthDigit()
    testSetKthDigit()
    testFabricYards()
    testFabricExcess()
    testThreeLinesArea()
    testColorBlender()
    testFindIntRootsOfCubic()

def main():
    testAll()
    cs112_n22_week1_hw1_linter.lint()


main()





