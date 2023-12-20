import copy

L = [[1],[2]]
W = L
L = L + []
L[0] = [4]

def ct2(s): 
    r = ""
    while (len(s) > 1):
        r += s[:1] + s[2:4] + "-" 
        s = s[1:len(s)-1:2] 
        print(s)
    return r + s 
    
print(ct2("abcd123"))


# L = [[1],[2]]
# W = L
# L += [3]
# print(W)
# print(L)

# L = [[1], [2]]
# W = L
# L = list(reversed(L))
# print(W)
# print(L)

# L = [[1], [2]]
# W = copy.copy(L)

# L[0] 
# print(W)
# print(L)

# def ct1(s):
#     result = ""
#     total = 0
#     for c in s:
#         if c.isdigit():
#             total += int(c)
#         elif not c.isalpha():
#             result += chr(ord(s[total]) + 1)
#         else:
#             if c.upper() not in "WATERS":
#                 result += c
#     return result + str(total)

# s = "112TAsAreCOOL?!"
# print(ct1(s))