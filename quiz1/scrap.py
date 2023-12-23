def countDigits(n):
    counter = 0
    while n>0:
        n //= 10
        counter +=1
    return n

print(12345)

def addDigits(n):
    sum = 0
    while n>0:
        sum += n % 10
        n //= 10
    return sum

print(addDigits(12345))
