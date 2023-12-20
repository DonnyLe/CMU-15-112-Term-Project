#################################################
# hw7: One-Dimensional Connect Four
# name: Donny Le 
# andrew id: dmle
# 
#################################################

import cs112_n22_week3_linter
from cmu_112_graphics import *
import random, string, math, time

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# main app
#################################################

#started when app is called
def appStarted(app):
    app.errorMessage = ""
    app.selectionCenter = 0
    app.selectionIsLegal = 0
    app.winningRunStartIndex = 0
    app.boardLength = 10
   
    app.whitespace = app.boardLength*0.2
    app.radius = (app.boardLength-app.whitespace)/2
    
    app.playerTurn = 0 #0 is blue, 1 is green
    app.boardLength = 10
    app.blockSelected = False
    app.gameOver = False
    appRestart(app)

#called when R is pressed 
def appRestart(app):
    app.boardList = []
    startBool = random.choice([0,1])
    app.playerTurn = 0 if startBool == 0 else 1
    
    #creates list with first val being random
    for i in range(0,app.boardLength,2):
        if startBool == 0:

            app.boardList.append(0)
            app.boardList.append(1)
        else:
            app.boardList.append(1)
            app.boardList.append(0)
        

#calls when mouse is pressed
#d
def mousePressed(app, event):
    if app.gameOver== True:
        return

    mx = event.x
    my = event.y
    print(app.selectionCenter)
    i = getPieceIndex(app, mx, my)
    if(i == None):
        return 
    #checks if clicked on end piece
    if (i != 0 and i != app.boardLength-1):
        app.selectionCenter = i
        beginningSelectionCheck = app.selectionCenter != 0 
        endSelectionCheck = app.selectionCenter != app.boardLength -1

        #checks if selection includes at least one of the 
        #players dots
        if(beginningSelectionCheck and endSelectionCheck): 

            middeCheck = app.boardList[app.selectionCenter] == app.playerTurn
            leftCheck = app.boardList[app.selectionCenter - 1] == app.playerTurn
            rightCheck = (app.boardList[app.selectionCenter + 1] 
                            == app.playerTurn)

            if(leftCheck or middeCheck or rightCheck):
                app.errorMessage = "Select end to move block"
                app.blockSelected = True

            else:
                app.errorMessage = "Block must contain current player"

    #conditions after having 3 pieces selected and 
    #clicking on a end piece
    elif (app.blockSelected == True):
        if i== 0:
            print("leftside")
            moveSelection(app, 1)
            checkWin(app)

        else:
            print("rightside")
            moveSelection(app, 0)
            checkWin(app)

    else:
        app.errorMessage = "End cannot be in block"



        


    
        
#calls when key is pressed
def keyPressed(app, event):
    #reset
    if(event.key == "r"):
        appRestart(app)
    #sets selection to current players color
    if(event.key == "c" and app.selectionCenter !=0):
        app.boardList[app.selectionCenter+1] = app.playerTurn
        app.boardList[app.selectionCenter] = app.playerTurn
        app.boardList[app.selectionCenter-1] = app.playerTurn

    #switches player
    if(event.key == "p"):
        app.playerTurn = 0 if app.playerTurn == 1 else 1
    
    #increases/decreases number of dots in  row
    if(event.key == "Up" and app.boardLength <20):
        app.boardLength += 2
        appRestart(app)

    if(event.key == "Down" and app.boardLength >6):
        app.boardLength -= 2
        appRestart(app)

#returns radius and center coords of dot
def getPieceCenterAndRadius(app, pieceIndex):
    if app.gameOver== True:
        return

    gridLen = app.width/app.boardLength
    whitespace =gridLen*0.2
    radius = (gridLen-whitespace)/2

    x = (whitespace/2 + 
        radius + (whitespace)* pieceIndex  + radius * 2 * pieceIndex)
    y = app.height/2 
    
    return x, y, radius

#gets index of certain dot in list based on x and y 
def getPieceIndex(app, x, y):
    for i in range(app.boardLength):
        cx, cy, radius = getPieceCenterAndRadius(app, i)
        distanceFormula = ((cx-x)**2+(cy-y)**2)**0.5

        if(distanceFormula < radius):
            return i

    
#checks if there is four in a row
def checkWin(app):
    x0 = 0 
    y0 = 0 
    x1 = 0 
    y1 = 0 
    counter = 0
    for i in range (len(app.boardList)-1):
        if(app.boardList[i] == app.boardList[i+1]):
            counter +=1 
        else:
            counter = 0

        if(counter == 3):       
            app.gameOver = True
            app.errorMessage = "Game Over!!!!"

#returns the dots coords that were part of the four in a row
def giveWinDots(app):
    x0 = 0 
    y0 = 0 
    x1 = 0 
    y1 = 0 
    counter = 0
    for i in range (len(app.boardList)-1):
        if(app.boardList[i] == app.boardList[i+1]):
            counter +=1 
        else:
            counter = 0

        if(counter == 3):       
            lastindex = i+1
            x0, y0, _ = getPieceCenterAndRadius(app, lastindex)
            x1, y1, _ = getPieceCenterAndRadius(app, lastindex-3)
    return x0, y0, x1, y1

#draws the line over the winning dots
def drawWin(app,canvas):
    x0, y0, x1, y1 = giveWinDots(app)
    canvas.create_line(x0,y0,x1,y1)
    
#calls every draw function
def redrawAll(app, canvas):
    if app.gameOver== False:
        
        drawOutline(app, canvas)      
        drawTitle(app, canvas)
        drawInstructions(app, canvas)
        drawCurrentPlayerAndMessage(app, canvas)
        drawBoard(app, canvas)
        drawRules(app, canvas)
        drawWin(app, canvas)

#draws main title
def drawTitle(app, canvas):
    titleStr = "One-Dimensional Connect Four!"
    canvas.create_text(app.width/2, app.height/15,
                     text=titleStr, anchor="c", font="Arial 25 bold")

#draws instructions
def drawInstructions(app, canvas):
    messages = ['See rules below.',
                'Click interior piece to select center of 3-piece block.',
                'Click end piece to move that block to that end.',
                'Change board size (and then restart) with arrow keys.',
                'For debugging, press c to set the color of selected block.',
                'For debugging, press p to change the current player.',
                'Press r to restart.',
               ]
    for i in range(len(messages)):
        canvas.create_text(app.width/2, app.height/15+18 * (i+1), 
                        text = messages[i], anchor="c", font="Arial 12 bold")

#draws rules in bottom left
def drawRules(app, canvas):
    messages = [
  "The Rules of One-Dimensional Connect Four:",
  "Arrange N (10 by default) pieces in a row of alternating colors.",
  "Players take turns to move three pieces at a time, where:",
  "      The pieces must be in the interior (not on either end)",
  "      The pieces must be adjacent (next to each other).",
  "      At least one moved piece must be the player's color.",
  "The three pieces must be moved in the same order to either end of the row.",
  "The gap must be closed by sliding the remaining pieces together.",
  "The first player to get four (or more) adjacent pieces of their color wins!",
               ]
    for i in range(len(messages)):
        canvas.create_text(18, app.height-18 * (i+1), 
                            text = messages[i], anchor="sw", 
                                font="Arial 12 bold")

#draws current player and message above dots
def drawCurrentPlayerAndMessage(app, canvas):
    currPlayerStr = "CurrentPlayer"
    colorFill = "blue" if app.playerTurn == 0 else "green"
    canvas.create_text(app.width/2-100, app.height/2 - 75, 
                    text = f'Current Player:  {app.playerTurn}', fill=colorFill)
    canvas.create_text(app.width/2+ 100, app.height/2 - 75, 
                    text = app.errorMessage, fill=colorFill)

def drawOutline(app, canvas):
    if(app.blockSelected):
        i = app.selectionCenter
        x0, y0, r0 = getPieceCenterAndRadius(app, i-1)
        x1, y1, r1 = getPieceCenterAndRadius(app, i+1)
        canvas.create_rectangle(x0-r0-10, y0-r0-10, 
                            x1+r0+10,y1+r0+10, fill = "yellow", width = "0")



#draws the row of dots
def drawBoard(app, canvas):
    
    for i in range(len(app.boardList)):
        if app.boardList[i] == 0:
            colorFill = "lightBlue"
            colorOutline = "blue"
        else: 
            colorFill = "lightGreen"
            colorOutline = "green"

        cx, cy, radius= getPieceCenterAndRadius(app, i)
        canvas.create_oval(cx-radius, cy-radius,
                         cx + radius, cy+radius, 
                     fill=colorFill, outline=colorOutline,
                      width = 0.05 * radius)

#moves the selected dots into the correct place
def moveSelection(app, moveToLeftEnd):
    print("select")
    boardList2 = copy.copy(app.boardList)
    
    app.boardList.pop(app.selectionCenter+1)
    app.boardList.pop(app.selectionCenter)
    app.boardList.pop(app.selectionCenter-1)

    if(moveToLeftEnd):
        app.boardList.insert(0,boardList2[app.selectionCenter+1])
        app.boardList.insert(0,boardList2[app.selectionCenter])
        app.boardList.insert(0,boardList2[app.selectionCenter-1])
        
    else: 
        app.boardList.insert(app.boardLength-1,
                        boardList2[app.selectionCenter-1])
        app.boardList.insert(app.boardLength-1,
                        boardList2[app.selectionCenter])
        app.boardList.insert(app.boardLength-1,
                        boardList2[app.selectionCenter+1])

    app.playerTurn = 0 if app.playerTurn == 1 else 1
    app.blockSelected = False
def main():
    cs112_n22_week3_linter.lint()
    runApp(width=800, height=550)

if __name__ == '__main__':
    main()