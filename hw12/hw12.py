#################################################
# hw12.py
#
# Your name: Donny Le 
# Your andrew id: dmle
#################################################

import cs112_n22_hw12_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

#evaluates prefix notation from a list
def evalPrefixNotation(L):
    
    #checks if first val is an operator
    if (isinstance(L[0], str)):
        operator = L.pop(0)

        #operations
        if(operator == "*"):
            return(evalPrefixNotation(L) 
                    * evalPrefixNotation(L))
        elif(operator == "-"):
                return(evalPrefixNotation(L) 
                    - evalPrefixNotation(L))
        elif(operator == "+"):
                return(evalPrefixNotation(L) 
                    + evalPrefixNotation(L))
        #if operator is not *, _ or + 
        else:
            raise Exception('Unknown operator: ' + operator) 

    #returns the numbers
    elif (isinstance(L[0], int)):
        num = L.pop(0)
        return num 

#main function
#recursive backtracking function that finds the route of a knight on each piece
# of an row*col chessboard 
def knightsTourPath(L, row, col, visited, counter):   

    #legal condition/base case
    #had to put this before visited.add 
    if (row, col) in visited: 
        return False
    visited.add((row, col))

    #knight directions 
    northLeftL = (-2, -1 )
    northRightL = (-2, 1 )
    southLeftL = (2, -1 )
    southRightL= (2, 1 )
    eastUpL = (1, 2)
    eastDownL = (-1, 2)
    westUpL = (1, -2)
    westDownL = (-1, -2)

    #loops through directions 
    for dRow, dCol in [southLeftL, southRightL, northLeftL, northRightL, 
                                eastUpL, eastDownL, westUpL, westDownL]:
        
        #adjusts the rows by drow and dcol
        nextRow, nextCol = row + dRow, col + dCol

        #row boundary check
        if nextRow < 0 or nextRow >= len(L):
            continue

        #col boundary check
        if nextCol < 0 or nextCol >= len(L[0]):
            continue
        
        #sets the certain spot that is valid to the counter 
        L[row][col] = counter
        
        boardIsFilled = knightsTourPath(L, nextRow, nextCol, visited, counter+1)

        #checks if the path is the right path, when the board is filled
        if(boardIsFilled):
            return L 

   #base case
   #placed at the end to fix off by one error
   #returns true if pieces are visited and filled
    if len(visited) == (len(L))*(len(L[0])):
        return True

    #removes knight from solution set, this is not where knight should go 
    visited.remove((row,col))
    
    #returns false if knight cannot move
    return False

#wrapper function 
def knightsTour(rows, cols):

    L = []
    for row in range(rows):
        newRow = []
        for col in range(cols):
            newRow.append(None)
        L.append(newRow)
    L = copy.deepcopy(L)
    res = knightsTourPath(L, 0, 0, set(), 1)

    #returns none if res == False when Knight's Tour not possible
    if( res != False):
        return res
    else:
        return None











#################################################
# Test Functions
#################################################

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)          # (42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)    # (3 + 4)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)   # (3 - 4)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)    # (4 - 3)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)   # (3 + (4 * 5))

    # ((2 * 3) + (4 * 5))
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    # ((2 + 3) * (4 + 5))
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    # ((2 + (3 * (8 - 7))) * ((2 * 2) + 5))
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    
    #Make sure to raise an error for operators that are not +, -, or *
    raisedAnError = False
    try:
        evalPrefixNotation(['^', 2, 3])
    except:
        raisedAnError = True
    assert(raisedAnError == True)
    print('Passed.')


def testKnightsTour():
    print('Testing knightsTour()....', end='')
    def checkDims(rows, cols, ok=True):
        T = knightsTour(rows, cols)
        s = f'knightsTour({rows},{cols})'
        if (not ok):
            if (T is not None):
                raise Exception(f'{s} should return None')
            return True
        if (T is None):
            raise Exception(f'{s} must return a {rows}x{cols}' +
                             ' 2d list (not None)')
        if ((rows != len(T)) or (cols != (len(T[0])))):
            raise Exception(f'{s} must return a {rows}x{cols} 2d list')
        d = dict()
        for r in range(rows):
            for c in range(cols):
                d[ T[r][c] ] = (r,c)
        if (sorted(d.keys()) != list(range(1, rows*cols+1))):
            raise Exception(f'{s} should contain numbers' +
                             ' from 1 to {rows*cols}')
        prevRow, prevCol = d[1]
        for step in range(2, rows*cols+1):
            row,col = d[step]
            distance = abs(prevRow - row) + abs(prevCol - col)
            if (distance != 3):
                raise Exception(f'{s}: from {step-1} to {step}' +
                                 ' is not a legal move')
            prevRow, prevCol = row,col
        return True
    assert(checkDims(4, 3))
    assert(checkDims(4, 4, ok=False))
    assert(checkDims(4, 5))
    assert(checkDims(3, 4))
    assert(checkDims(3, 6, ok=False))
    assert(checkDims(3, 7))
    assert(checkDims(5, 5))
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testEvalPrefixNotation()
    testKnightsTour()
def main():
    cs112_n22_hw12_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
