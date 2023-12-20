#################################################
# hw9.py: Tetris!
#
# Your name: Donny Le
# Your andrew id: dmle
#
# Your partner's name: Christian Lam
# Your partner's andrew id: clamalva
#################################################

import cs112_n22_week4_linter
import math, copy, random

from cmu_112_graphics import *

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
def appStarted(app):   
    #calls gamedimensions, calculates width + other vals
    rows, cols, cellSize, margin = gameDimensions()
    
    #assigns vals from game dimensions
    app.rows = rows
    app.cols = cols
    app.cellSize = cellSize
    app.margin = margin

    #starting color grid
    app.emptyColor = "blue"

    #direction for moving block initialized
    app.drow = 0
    app.dcol = 0
    app.time = 0

    #booleans for pausing, stepping, gameOver
    app.pause = False
    app.step = False
    app.gameOver = False

    #final score
    app.scores = 0

    #game pieces
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    #tetrispieces list
    app.tetrisPieces = [ iPiece, jPiece, 
                    lPiece, oPiece, sPiece, tPiece, zPiece ]

    #colors for tetris pieces
    app.tetrisPieceColors = [ "red", "yellow", 
                        "magenta", "pink", "cyan", "green", "orange" ]

    newFallingPiece(app)

    #creates an empty list with empty color for each val 
    app.board = []
    for r in range(app.rows):
        newRow = []
        for c in range(app.cols):
            newRow.append(app.emptyColor)
        app.board.append(newRow)

#creates a new falling piece
def newFallingPiece(app):
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.numFallingPieceCols = len(app.fallingPiece[0])
    app.numFallingPieceRows = len(app.fallingPiece)
    app.fallingPieceRow = 0
    app.fallingPieceCol = ((app.cols)//2 - app.numFallingPieceCols//2) 
    app.rowchange = len(app.fallingPiece)
    app.colchange = len(app.fallingPiece[0])
    refreshFallingPiece(app)

def refreshFallingPiece(app):
    app.numFallingPieceCols = len(app.fallingPiece[0])
    app.numFallingPieceRows = len(app.fallingPiece)

#calculates the game dimensions based on vals given by user    
def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25
    return rows, cols, cellSize, margin

#calls when a key is pressed
def keyPressed(app, event):
    drow = 0
    dcol = 0

    #change the fallingpiece
    if(event.key == "b"):
        newFallingPiece(app)

    #restarts the app
    if(event.key == "r"):
        appStarted(app)
    
    #pauses the app 
    if(event.key == "p"):
        app.pause = not app.pause
    
    #steps the app by one frame
    if(event.key == "s" and app.pause):
        app.step = True
        moveFallingPiece(app, 1, 0)

    #movement keys
    if(event.key == "Down"):
        drow = 1
    if(event.key == "Right"):
        dcol = 1
    if(event.key == "Left"):
        dcol = -1

    #calls moveFallingPiece with directions from arrow presses
    moveFallingPiece(app,drow, dcol)

    #rotating piece
    if(event.key == "Up"):
        rotateFallingPiece(app)

    #hard drop
    if(event.key == "Space"):
        while True:
            app.fallingPieceRow += 1 
            if fallingPieceIsLegal(app)== False:
                break
        app.fallingPieceRow -=1   
            
 
#calls continuously, 100 ms
def timerFired(app):
    
    
    if(app.pause== False and app.gameOver == False):

        #moves piece down once ever 400 ms
        app.time += 100
        if app.time % 400 == 0:
            moveFallingPiece(app, 1, 0)

#calculates width/height based on gameDimensions()
def playTetris():
    rows ,cols, cellSize, margin = gameDimensions()
    width = cols*cellSize+margin*2
    height = rows* cellSize+margin*2 
    runApp(width=width, height=height)
    print('Replace this with your Tetris game!')

"""
replaces the boardList with colors of fallingPiece when
fallingPiece touches floor/other colors in list
"""
def placeFallingPiece(app):
    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            actualRow = r + app.fallingPieceRow
            actualCol = c + app.fallingPieceCol
            if(app.fallingPiece[r][c]
                ):
                app.board[actualRow][actualCol] = app.fallingPieceColor
                removeFullRows(app) 

#moves the fallingPiece
def moveFallingPiece(app, drow, dcol):
    if((app.pause== False or (app.pause and app.step)) 
            and app.gameOver == False):
        app.fallingPieceRow +=drow
        app.fallingPieceCol += dcol
        if fallingPieceIsLegal(app) == False:
            app.fallingPieceRow -=drow
            app.fallingPieceCol -= dcol
            if dcol == 0:
                placeFallingPiece(app)
                newFallingPiece(app)
                gameIsOver(app)

#checks if blocks on top of board is not emptyColor 
#ends game
def gameIsOver(app):
    lastrow = app.board[0]
    for block in lastrow:
        if block != app.emptyColor:
            app.gameOver = True

#returns false if fallingPiece hits out of bounds or other blocks
#returns true if fallingPiece is in legal pos
def fallingPieceIsLegal(app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            actualRow = i + app.fallingPieceRow
            actualCol = j + app.fallingPieceCol
            if(app.fallingPiece[i][j]):
                if (i+app.fallingPieceRow < 0 or j + app.fallingPieceCol< 0
                    or actualRow >= app.rows
                    or actualCol >= app.cols
                    or app.board[actualRow][actualCol] != app.emptyColor
                    ):
            
                    return False

    return True

#rotates the falling piece
def rotateFallingPiece(app):
    #temp vals used fallingPiece is not legal
    tempcol = app.colchange
    temprow = app.rowchange
    templist = copy.deepcopy(app.fallingPiece)

    #switches num of rows and cols during rotation
    app.rowchange = app.colchange
    app.colchange = temprow

    #creates newlist with correct dimensions in rotation
    newlist = []
    for i in range(app.rowchange):
        newlistrow = []

        for j in range(app.colchange):
            newlistrow.append(None)
        
        newlist.append(newlistrow)

    #used to correct the centering
    oldRow = app.fallingPieceRow
    oldCol = app.fallingPieceCol
    oldNumRows = app.numFallingPieceRows
    oldNumCols =  app.numFallingPieceCols

    #adds correct values from templist/app.fallingPiece to newlist
    #in correct sequence

    for row in range(len(newlist)):
        for col in range(len(newlist[row])):

            #(row+1)*-1 utilizes negative indices to reverse 
            newlist[row][col] = templist[col][(row+1)*-1]
        
    #assigns newlist to app.fallingPiece, completes rotation
    app.fallingPiece = newlist

    #values are recomputed 
    refreshFallingPiece(app)

    #fixes the point of rotation
    #follows tutorial 
    newNumRows = app.numFallingPieceRows
    newNumCols =  app.numFallingPieceCols

    newRow = oldRow + oldNumRows//2 - newNumRows//2
    newCol = oldCol + oldNumCols//2 - newNumCols//2


    app.fallingPieceRow = newRow
    app.fallingPieceCol = newCol

    #returns back to original state if rotation makes piece illegal

    if fallingPieceIsLegal(app)==False:
        app.fallingPiece = templist
        app.colchange = tempcol
        app.rowchange = temprow
        app.fallingPieceRow = oldRow
        app.fallingPieceCol = oldCol
    
#returns cellbounds for grid
def getCellBounds(app, row, col):
    x0 = app.cellSize * col + app.margin
    y0 = app.cellSize * row + app.margin
    x1 = app.cellSize * (col+1) + app.margin
    y1 = app.cellSize * (row+1) + app.margin
    return x0, y0, x1, y1



#draws falling piece
def drawFallingPiece(app,canvas):
    
    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            if(app.fallingPiece[r][c]== True):
              
                drawCell(app,canvas,r+app.fallingPieceRow,
                    c+app.fallingPieceCol, app.fallingPieceColor)

#draws fills grid with colored squares
def drawCell(app,canvas, row, col, color):
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0,y0, x1,y1, 
                    fill = color, width=4)

#draws grid with orange background
def drawBoard(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill="orange")
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.board[row][col]
            drawCell(app,canvas,row, col, color)

#draws black rectangle and text
def drawGameOver(app, canvas):
   
    
    
    canvas.create_rectangle(app.margin, app.margin+app.cellSize, app.margin 
                    + app.cellSize*app.cols, app.margin+app.cellSize * 3
                    , fill="black"
                    )
    canvas.create_text(app.width/2, 
                app.margin+app.cellSize*2, text="Game Over", 
                    anchor="c", font="Arial 20 bold", fill="yellow")

#removes rows that are filled
def removeFullRows(app):
    rowCompleteCount = 0
    newBoard = []
    
    #adds rows from current board to newBoard if rows are not filled
    for r in range(len(app.board)):

        if app.emptyColor in app.board[r]:
            newBoard.append(app.board[r])

        else:
            rowCompleteCount += 1
 
    for i in range(rowCompleteCount):
        print("entered")
        newBoard.insert(1,[app.emptyColor]*app.cols)

    app.board = newBoard
    #adds the number of rows to the power of 2 to total score
    print(rowCompleteCount)
    app.scores = app.scores + rowCompleteCount ** 2

#draws the score 
def drawScore(app, canvas):
    canvas.create_text(app.width/2, 
                app.margin/2, text=f'Score: {app.scores}', 
                    anchor="c", font="Arial 13 bold", fill="blue")


#draws game
def redrawAll(app,canvas):
    drawBoard(app,canvas)
    drawFallingPiece(app,canvas)
    if(app.gameOver):
        drawGameOver(app, canvas)
    drawScore(app, canvas)



#################################################
# main
#################################################

def main():
    cs112_n22_week4_linter.lint()
    playTetris()


if __name__ == '__main__':
    main()
