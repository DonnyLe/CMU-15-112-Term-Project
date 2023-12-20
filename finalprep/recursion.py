
#wrapper function, used to have default parameter with list 
def fib(n):
    return fibHelper(n, 0)

#
def fibHelper(n, depth):
    if depth > 10:
        return
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibHelper(n-2, depth + 1) + fibHelper(n-1,depth + 1)


#isPalindrome 

def isPalindrome(s):
    if len(s) < 2 :
        return True 
    else:
        # first = s[0]
        # last = s[-1]
        # return isPalindrome(s[1:-1]) if first == last else False
        return s[0] == s[-1] and (isPalindrome(s[1:-1]))

print(isPalindrome("racecar"))
   
   
   
def flatten(L):
    if L == []:
        return []

    if type(L[0]) != list:
        return [L[0]] + flatten(L[1:])
    
    return flatten(L[0]) + flatten(L[1:])

print(flatten([1,3,2,[3,1],1,2]))

def getCourseHelper(courseCatalog, courseNumber, path, i):

    if i == len(courseCatalog):
        return None

    if path == '':
        path += f'{courseCatalog[0]}'
    if type(courseCatalog[i]) == list:
        newPath = getCourseHelper(courseCatalog, courseNumber, "",0)
        if newPath:
            return path + newPath
    elif courseCatalog[i] == courseNumber:
        return path + courseNumber
    
    return getCourseHelper(courseCatalog, courseNumber, path, i + 1)

def getCourse(courseCatalog, courseNumber):
    return getCourseHelper(courseCatalog, courseNumber, " ", 0)






   