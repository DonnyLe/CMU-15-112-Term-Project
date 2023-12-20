#dont need to import anything
import string
def stringTest(s):
    #returns string with first letter capitlized 
    s= s.capitalize()
    #print(s)
    
    

    #lower and casefold do the same thing, returns a string with all letters lowercase
    s = s.lower()
    s = s.casefold()
    #print(s) 



    #sensitive to spaces, can detect \n in a string with three quotation marks,
    #cannot detect \t even with repr, only works if \t typed in string explicitly
    #counts the number of times a substring is in the string
    
    s = """
                    Hello"""

    num = s.count("\n")
    #prnt(num)
    
    
    
    #sensitive to spaces, can detect \n in a string with three quotation marks,
    #cannot detect \t even with repr, only works if \t typed in string explicitly
    #returns true or false if 
    s = """hello


"""

    #print(repr(s))
    #print( s.endswith("\n"))
  
    ##creates a new string the size of the first parameter and puts the string
    #that is being called into the center, second parameter is the character to
    #fill in the empty space
    s = "banana"
    #print( s.center(20, "*"))
    

    #gives the index of the first occurance of the string in parameter, 
    #if not found, returns -1, two other parametres for where to start search (inclusive)
    # and where to end the search (no index out of bound error), default = 
    # len(str), exclusive 
    s = "this1theisfesajfsf9"
    print(s.find("12"))



    #isalpha returns true if all chars in string are in the alphabet, includes space 
    #so if space, returns false
    #isalnum returns true if all chars in string are in the alphabet or nums, includes 
    #space so if space, returns false
    s = "hellamynameisjimmy1234589"
    #print( s.isalpha())
    #print(s.isalnum())



    """\r means the stuff after it to the beginning"""

    #isindentifer returns ture if the number only contains alphanum letters or underscores (_)
    #cannot start with a number or contain spaces

    '''a = "MyFolder"
    b = "Demo002"
    c = "2bring"
    d = "my demo"

    print(a.isidentifier())
    print(b.isidentifier())
    print(c.isidentifier())
    print(d.isidentifier())
'''

    #almost indentical to center, aligns string to the left and adds spaces (default)
    #first parameter is the length of the ENTIRE STRING
    txt = "banana"
    x = txt.ljust(20, "*")

    #print(x, "is my favorite fruit.")

    #lstrip removes any left leading characters, input a set of characters and will delete any 
    #leading characters that is in the set of charactesr
    txt = ",,,,,ssaaww.....banana"

    x = txt.lstrip(",.saw")

    # print(x)


    #split: splits a string by a specific separator, second parameter is the number of splits 
    #to be done
    #rsplit: does the same thing as split except it SPLITS from right to left (returns 
    # the same as split unless using the second paramter)
    """
    txt = "this is a test"
    # for string in txt.split(" "):
    #     print(string)
  
    print(txt.rsplit(" ", 1)) #splits 1 time from the right
    print(txt.split(" ", 1)) #splits 1 time from the left

    # for string in txt.rsplit(" "):
    #     print(string)
    """


    #spltlines: splits string by the line, same thing as doing split("\n")
    txt = """hello this is a
    beyblade
    test
    """
    # for i in txt.splitlines():
    #     print(i)
    #     print("split")

    # #same thing 
    
    # for line in txt.split("\n"):
    #     print(line)
    #     print('split')

    s = "\n"
    print(s.isspace())
    

stringTest("t\n")