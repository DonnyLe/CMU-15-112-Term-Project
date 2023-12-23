# def isPrime(n):
#     if n<2:
#         return False
#     elif n % 2 == 0:
#         return n == 2
#     for i in range(3,int(n**0.5)+1,2):
#         if(n%i==0):
#             return False 
#     return True 



assert(nthPrime(0)==2)
assert(nthPrime(1)== 3)
assert(nthPrime(2)==5)
assert(nthPrime(3)== 7)

print(nthPrime(50))



