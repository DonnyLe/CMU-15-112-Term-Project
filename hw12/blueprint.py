#pseudocode
#pop the first element, if it is an integer, return the integer
#pop the first element, if it is a string, 
import copy

def evalPrefixNotation(L):
    
    if (isinstance(L[0], str)):
        operator = L.pop(0)
        if(operator == "*"):
            return(evalPrefixNotation(L) 
                    * evalPrefixNotation(L))
        elif(operator == "-"):
                return(evalPrefixNotation(L) 
                    - evalPrefixNotation(L))
        elif(operator == "+"):
                return(evalPrefixNotation(L) 
                    + evalPrefixNotation(L))
        else:
            raise Exception('Unknown operator: ' + operator) 

    elif (isinstance(L[0], int)):
        num = L.pop(0)
        return num 
    

    
# print(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5])) 

def knightsTourPath(L, row, col, visited, counter):   
    # print(f'L: {L}')
    # print(f'Visited: {visited}')

   

    if (row, col) in visited: 
        return False
    visited.add((row, col))

    #drow, dcol
    northLeftL = (-2, -1 )
    northRightL = (-2, 1 )
    southLeftL = (2, -1 )
    southRightL= (2, 1 )
    eastUpL = (1, 2)
    eastDownL = (-1, 2)
    westUpL = (1, -2)
    westDownL = (-1, -2)

    for dRow, dCol in [southLeftL, southRightL, northLeftL, northRightL, 
                                eastUpL, eastDownL, westUpL, westDownL]:
        nextRow, nextCol = row + dRow, col + dCol

        if nextRow < 0 or nextRow >= len(L):
            continue
        if nextCol < 0 or nextCol >= len(L[0]):
            continue
        
        L[row][col] = counter
        path = knightsTourPath(L, nextRow, nextCol, visited, counter+1)

        if(path):
            return L 

   
    if len(visited) == (len(L))*(len(L[0])):
        # print(f'len {(len(L))*len(L[0])}')
        # print(f'visited len {len(visited)}')
        return True
    visited.remove((row,col))
    
    return False

def knightsTour(rows, cols):
    L = []
    for row in range(rows):
        newRow = []
        for col in range(cols):
            newRow.append(None)
        L.append(newRow)
    L = copy.deepcopy(L)
    res = knightsTourPath(L, 0, 0, set(), 1)
    if( res != False):
        return res
    else:
        return None



print(knightsTour(4,3))
print(knightsTour(4,4))
print(knightsTour(4,5))
print(knightsTour(3,4))
print(knightsTour(3,6))
print(knightsTour(3,7))
print(knightsTour(5,5))


