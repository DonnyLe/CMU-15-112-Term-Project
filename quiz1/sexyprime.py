def isPrime(n):
    if n<2:
        return False
    for i in range(0,n):
        if (n% i == 0):
            return False
    return True


def areSexyPrimes(n, m):
    if(type(n) != int or type(m) != int):
        return False
    if(n<= 0 or m<= 0):
        return False
    if(not isPrime(n) or not isPrime(m)):
        return False
    if(abs(n-m)!=6):
        return False
    return True 

    
    
