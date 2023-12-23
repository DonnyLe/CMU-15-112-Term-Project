# L = [1,2,3,4,5, 'a', 'b', 'c']

# L2 = L[:]
# print(L2)
# print(L2 is L)

def lockerProblem(n):
    isOpen= [False] * (n+1)
    students = len(isOpen) #n+1
    for student in range(1,students+1):
        for locker in range(student, n+1, student):
            isOpen[locker] = not isOpen[locker]
    result = []
    for i in range(len(isOpen)):
        if isOpen[i] == True:
            result.append(i)
    return result

def letterCounts(s):
    counts = [0] * 26
    for ch in s.upper():
        if ch.isalpha():
            counts[ord(ch)-ord("A")]+=1 
    return counts
    
print(lockerProblem(20))