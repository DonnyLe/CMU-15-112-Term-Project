#################################################
# extra_practice2.py
#################################################

import cs112_n22_week2_linter
import math, random, string

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
# ep2-p1-functions
#################################################

def finalLocation(path):
    num = 0
    xdir = 0
    ydir = 0
    x = 0
    y = 0
    for word in path.split(): 
        word = word.lower()
        if word in string.digits:
            num = int(word)
        if word == "right":
            xdir = +1
        if word == "left":
            xdir = -1
        if word == "up":
            ydir = +1
        if word == "down":
            ydir = -1
        
        x += num * xdir
        y += num * ydir 
        
        xdir = 0
        ydir = 0

    return x, y

print(finalLocation("Go 5 up"))

def isPal(s):
    for i in range(len(s)//2):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True

def lowercasePal(s):
    res = ""
    for char in s:
        if (not char in string.ascii_uppercase and not char in string.digits
        and not char in string.whitespace):
            res += char
    print(res)
    return isPal(res)


print(lowercasePal('YES!'))

def getBestAvg(scores):
    highestscore = 0
    currentscore = 0
    for score in scores.split(","):
        currentscore = int(score)
        highestscore = currentscore if currentscore > highestscore else highestscore
        currentscore = 0
    return highestscore

print(getBestAvg("5,10,15,2,3,4"))



def ct2(r, s):
    t = ''
    for i in range(0, len(r), 2):
        t += str(s.find(r[i]))

    result = f'{t}=={eval(t)}'
    return result
print(ct2('amazing', 'zambia'))   

# def rc1(s):
#     n, c = ord(s[0]), 0
#     while s != '':
#         assert(ord(s[0]) == n)
#         n -= 1
#         c += 1
#         s = s[1:]
#     return (chr(n) == 'B') and (c == 4)

# rc1("cdef")

def ct(s):
      r = ''
      t = ''
      for i in range(len(s)):
          if (s[i] in s[i+1:]):
              n = s[i:]
              n = n.count(s[i])
              print(str(i)+str(n))
              r += s[i]
          else:
              t = s[i] + t
      return r + ',' + t
print(ct('xyzxyx'))
  
def ct1(s): 
    d =1
    t = ''
    for c in s.upper():
        if c.isspace():
            d -= 1
        elif c.isalpha():
            t += chr(ord(c) + d)
            d += 1
    return t
    
print(ct1('A\ne g!'))

def ct2(s): 
    t =s
    s += s[:2]
    t += s[::-1]
    print(t)
    print(t.replace('cb','f'))
    return t.find('fa')
    
print(ct2('abc'))

def ct1(s):
  t = ''
  u = t
  n = 0
  s = s[1:]
  for c in s:
    if c.isspace():
      n += 1
    elif c.islower():
      t += c.upper() * n
    elif c.isalpha():
      u += c
  return f'{t}-{u}-{n}'

print(ct1('eF! g\tH! MN'))

def ct1(s, t): 
    t0 = t
    for i in range(len(s)):
        if (s[i] == t[-1]):
            print(i)
        else:
            t = s[i].upper() + t 
    return t.replace(t0, 'Z')

print(ct1('abc', 'ab'))