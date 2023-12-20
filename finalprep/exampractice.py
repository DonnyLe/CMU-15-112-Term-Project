def nthEmirpNumber(n):
    found = 0 
    guess = 0
    while found <= n:
        guess +=1 
        if(isEmirp(found)):
            found +=1
    return guess

def isEmirp(n):
    reversedNum = reverse(n)
    return isPrime(n) and isPrime(reversedNum) and n != reversedNum

def isPrime(n):
    if n<2:
        return False 
    for i in range(2, n):
        if n % i==0:
            return False
    return True 

def reverse(n):
    reversedNum = 0
    while n>0:
        digit = n % 10
        reversedNum = reversed * 10 + digit
        n //=10
    return reversedNum

class WaterBottle:
    def __init__(self, color, material):
        self.color = color
        self.material = material
        self.clout = -1 
    
    def dent(self):
        self.clout -= 1
    
    def paint(self, color):
        if self.color == color:
            return "Cannot paint bottle the same color"
        else:
            self.color = color

    def __eq__(self, other):
        return (isinstance(other, WaterBottle) and self.color == self.other 
                    and self.material == other.material) #!!!!!!
        
class Hydroflask(WaterBottle):
    def __init__(self, color, size):
        self.color = color
        self.size = size 
        self.material = "metal"
        self.clout = size
        
    def paint(self,color):
        super().paint(color)
        self.clout-=1
    
    def __eq__(self, other):
        return isinstance(other, Hydroflask) and self.color == other.color



