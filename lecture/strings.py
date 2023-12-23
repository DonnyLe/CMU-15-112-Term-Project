# s = "Axolotls are pretty cute!"

# # for i in range(0, len(s), 2):
# #     print(s[i])

# s2 = s[len(s)::-1]
# print(s2)

# s3 = ""
# s3 = s[0:5]
# print(s3)

# # print(s[0:len(s)-1:2])

s = "abcde"
x = 3
sa = s[:x]
sb = s[x:]
print(sb,sa)
def reverse(s):
    return s[::-1]

print(reverse("taters for everyone"))

def vowels(s):
    result = ""
    for c in s:
        if c in "aeiou":
            result+=c
    return result

print(vowels("I like axolotls but not mondays"))

import string

def lowercase(s):
    result = ""
    for c in s:
        if c in string.ascii_lowercase:
            result+=c
    return result

def removeWhitespace(s):
    result = ""
    for c in s:
        if not c.isspace():
            result+=c
        return result
         
print(removeWhitespace("I like axolotls but not mondays"))