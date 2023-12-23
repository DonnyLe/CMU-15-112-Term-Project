# from array import array
# import re


# def forloop():
#     array = [1,2,3,4,5,6,7,8,9]
#     for i in array:
#         print("For loop forwards" , i)
#     print("")
#     for i in range(8,0,-1):
#         print("For loop backwards: ", array[i])
#     print("")

# def string(newString): 
#     print("This is the string: ", newString)
#     print("This is the last letter of the string: ", newString[len(newString)-1::])
#     if ord(newString[0:1])>111:
#         print("The last letter is greater than 111 in ASCII")
#     elif ord(newString[0:1])<105:
#         print("The last letter is less than 105 in ASCII")
#     else:
#         print("The last letter is between 105 and 111 in ASCII")
#     print("")

# def whileloop():
#     array = [1,2,3,4,5,6,7,8,9]
#     i = 0
#     while i<9:
#         print("While loop: ", array[i])
#         i+=1
#     print("")


# x = lambda e : e * 5

# def unpackedtuple(fruits):
#     (green, yellow, red) = fruits
#     print("Unpacked Tuple: ", green)
#     print("Unpacked Tuple: ", yellow)
#     print("Unpacked Tuple: ", red)
#     print("")

# def appendingtuple(fruits): 
#     y = list(fruits)
#     y.append("orange")
#     fruits = tuple(y)
#     print("Appending to a tuple: ", fruits)
#     print("")

# def dictionary(car, key): 
#     print("Dictionary: ", car)
#     print("")
#     print("This is the accessed item in the dictionary: ",car[key])

# def returnKeys(car): 
#     print("These are the keys: ",car.keys()) 

# def ifin(string1, string2):
#     if string1 in string2:
#         print("\"", string1, "\"", "is in ", string2, "\"")
#     else:
#         print("\"", string1, "\"", "is not in ", string2, "\"")



# forloop()
# string("hello")
# whileloop() 
# print("This is an equation for x(5)", x(15))
# unpackedtuple(("apple", "banana", "cherry"))
# appendingtuple(("apple", "banana", "cherry"))
# dictionary({"brand": "Ford", "model" : "Mustang", "year" : 1999},"brand")
# ifin("hello this","hello this is a test")

# import re

# txt = "The rain in Spain"
# e = re.search("^The.*Spain$", txt)

# if e:
#   print("YES! We have a match!")
# else:
#   print("No mat)

# def test():
#     string2 = ""
#     string = " hello \n"
#     for i in range(len(string)):
#         string2 += "\n"
#     string2 += "e"
#     return string2
# print(test())

# def test():
#     for i in range (4):
#         for j in range(i, 6+i):
#             print(j, end="")
#         print()
   
# test()
