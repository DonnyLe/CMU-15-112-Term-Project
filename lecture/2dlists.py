import copy
a = [1,2,3]
b = [4,5,6]
L = [a,b]

# rows = len(L)
# cols = len(L[0])

# for row in L:
#     print(row)
def getCol(L,col):
    rows = len(L)
    cols = len(L[0])
    result = []
    for row in L:
        print(row[col])

getCol(L, 1)
