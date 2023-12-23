#################################################
# hw5.py
#
# Your name: Donny Le 
# Your andrew id: 814477499
#################################################

import cs112_n22_week2_linter
from cmu_112_graphics import *
import string
import math

#called when program is run, initializes most vars
def appStarted(app):
    resetExplosion(app)
    app.rows = 10
    app.cols = 10
    app.gamePause = -1
    app.stepBoolean = -1
    app.score = 0 
    app.marginTop = 35
    app.marginBottom = 5
    app.marginLeft = 5
    app.marginRight = 5
    app.widthMain = app.width - app.marginBottom*2
    app.heightMain = app.height - app.marginBottom - app.marginTop
    app.cellLength = app.widthMain / app.rows
    app.stepBoolean = -1
    app.timerDelay = 16
    restartApp(app)


#restarts the score, calls restart Dot 
def restartApp(app):
    app.widthMain = app.width - app.marginBottom*2
    app.heightMain = app.height - app.marginBottom - app.marginTop
    app.cellLength = app.widthMain / app.rows

    """stepused to allow moveDot to work when game 
    is paused + doStep is called"""
    app.stepBoolean = -1

    #var used to switch colors
    app.colorPicker = 1
    restartDot(app)
    app.score = 0

"""returns the dot back to the to pleft + changes the color 
depending on conditions"""
def restartDot(app):
    app.direction = 1
    app.dotRow = 0
    app.dotCol = 0 
    if app.explosionBoolean == True:
        app.colorPicker = -app.colorPicker
    
    app.color = "blue" if app.colorPicker == 1 else "red"

    resetExplosion(app)


#restarts the explosion animation
def resetExplosion(app):
    app.cxExplosion = 0
    app.cyExplosion = 0
    app.rExplosion = 10
    app.explosionBoolean = False


#returns coords for cells
def getCellBounds(app, row, col):
    x0 = app.marginLeft + app.cellLength*col
    y0 = app.marginTop + app.cellLength * row 
    x1 = app.marginLeft + app.cellLength*(col+1)
    y1 = app.marginTop + app.cellLength * (row+1) 
    return x0,y0, x1, y1 

#detects mouse press for explosions
def mousePressed(app, event):
    app.cxExplosion = event.x
    app.cyExplosion = event.y 
    app.rExplosion = 10
    app.explosionBoolean = True 

#used for pause, step, + changing grid size
def keyPressed(app, event):
    buttonPress = event.key.lower() 
   
    if(buttonPress == "r"):
        restartApp(app)

    if(buttonPress) in string.digits:

        if (buttonPress) in ("5,6,7,8,9"):
            app.rows = int(event.key)
            app.cols = int(event.key)
            restartApp(app)        
       
        else:
            app.rows = int(event.key) + 10
            app.cols = int(event.key) + 10
            restartApp(app)    

    if(buttonPress == 'p'):
        app.gamePause = -app.gamePause

    if(buttonPress == 's' and app.gamePause == 1):
        app.stepBoolean = 1
        doStep(app)
        app.stepBoolean = -1

#detects if explosion intersects with dot
def explosionIntersectsDot(app):
    
    x0,y0,x1,y1 = getCellBounds(app,app.dotRow, app.dotCol)
    space = 2

    x0,y0,x1,y1 = x0+ space,y0 + space,x1- space,y1 -space
    cx, cy = (x0 + x1)/2,(y0 + y1)/2 
   
    r = (x1 - x0)/2

    #calls circlesIntersect 
    if circlesIntersect(cx,cy, r,app.cxExplosion, app.cyExplosion, 
        app.rExplosion):

        #condition in circle is red, get 10 pts
        if(app.color == "red"):
            app.score = app.score + 10
        else: 
            #score depends on size of explosion
            app.score += app.rExplosion//10
        restartDot(app)
    #condition if all sizes of explosions miss, minus 1
    elif (app.rExplosion>=50):

        if(app.score>0):
            app.score -=1
        
#distance formula helper function
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#parameters: x, y, radius from cirles
#returns: true or false if circles intersect
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)

    if d <= (r1+r2):
        return True
        
    else:
        return False

#mvoes the dot in a snake pattern
def moveDot(app):
    if(app.gamePause == -1 or (app.gamePause == 1 
    and app.stepBoolean == 1)):

        if((app.dotCol == app.cols-1  and app.dotRow%2==0) or (app.dotCol == 0 
        and app.dotRow != 0 and app.dotRow%2==1)):

            app.dotRow+=1
            app.direction = -app.direction
            
        else:
            app.dotCol += app.direction

        if((app.dotRow == app.rows)):
            restartDot(app)

#increases radius of explosion by 10, up to 50
def growExplosion(app):
    explosionIntersectsDot(app)
    app.rExplosion += 10

    if(app.rExplosion>=50):
        resetExplosion(app)

#runs automatically, makes dot move
def timerFired(app):
    if(app.gamePause == -1 or (app.gamePause == 1 
    and app.stepBoolean == 1)):

        moveDot(app)

        if app.explosionBoolean == True:
            growExplosion(app)

    
#moves dot + explosion by one tick
def doStep(app): 
    moveDot(app)
    growExplosion(app)

#draws title + score in top portion
def drawTitleAndScore(app, canvas):
    canvas.create_text(app.marginLeft + app.widthMain/2, app.marginTop/2 , 
    text="hw5 Game", fill="black", font=('Helvetica 15 bold'))
    leftshift = 20
    canvas.create_text(app.widthMain - app.marginLeft - leftshift, 
    app.marginTop/2, text=f'Score {app.score}', fill="black", 
    font=('Helvetica 15 bold'))

#draws grid
def drawGrid(app, canvas):
    for r in range (app.rows):

        for c in range (app.cols):
            canvas.create_rectangle(getCellBounds(app,r,c))

#draws circle for dot, red/blue
def drawDot(app, canvas):
    x0,y0,x1,y1 = getCellBounds(app,app.dotRow, app.dotCol)
    space = 2
    x0,y0,x1,y1 = x0+ space,y0 + space,x1- space,y1 -space
    canvas.create_oval(x0,y0,x1,y1,fill=app.color)

#draws orange explosion, based on mouse click
def drawExplosion(app, canvas):
    if ( app.explosionBoolean == True    ):
        x0,y0 = (app.cxExplosion - app.rExplosion, 
        app.cyExplosion - app.rExplosion)

        x1, y1 = (app.cxExplosion + app.rExplosion, 
        app.cyExplosion + app.rExplosion)
        canvas.create_oval(x0,y0,x1,y1, fill = 'orange')

#draws entire scren
def redrawAll(app, canvas):
    drawTitleAndScore(app, canvas)
    drawGrid(app, canvas)
    drawDot(app, canvas)
    drawExplosion(app, canvas)

def main():
    cs112_n22_week2_linter.lint()
    runApp(width=510, height=540)

if __name__ == '__main__':
    main()