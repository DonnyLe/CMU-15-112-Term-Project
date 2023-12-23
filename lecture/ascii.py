# def letterDistance(c1,c2):
#     c1 = c1.lower()
#     c2 = c2.lower()

#     return abs(ord(c1) - ord(c2))

# print(letterDistance("a","b"))

# def ct(s):
#     x = ""
#     for c in s:
#         x+= chr(ord(c)+x)
#     return x 

# print(ct("abcde"))
    
def printAllSubstrings(s):
    for start in range(len(s)):
        for end in range(start,len(s)):
            print(s[start:end+1])

printAllSubstrings('do you like taters')