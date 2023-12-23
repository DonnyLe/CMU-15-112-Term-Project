#################################################
# hw5.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_n22_week2_linter
from cmu_112_graphics import *

def appStarted(app):
    app.cols = 5
    app.rows = 5
    app.margin = 5
    app.cellLength = (app.width - 2*app.margin)/app.rows
    app.row = 0 
    app.col = 0
    
def getCellBounds(app, row, col):
    x0,y0 = (app.margin + app.cellLength * col, 
            app.margin + app.cellLength * row)

    x1, y1 = (app.margin + app.cellLength * (col+1), 
             app.margin + app.cellLength * (row+1))
    return x0, y0, x1, y1

def mousePressed(app, event):
    pass

def keyPressed(app, event):
    pass

def explosionIntersectsDot(app):
    pass

def moveDot(app):
    pass

def growExplosion(app):
    pass

def timerFired(app):
    pass

def doStep(app):
    pass

def drawTitleAndScore(app, canvas):
    canvas.create_text(app.width/2, 25, text="hello this is a test")

def drawGrid(app, canvas):
    for r in range (app.rows):
        for c in range(app.cols):
            canvas.create_rectangle(getCellBounds(app, r, c))
            

def drawDot(app, canvas):
    pass

def drawExplosion(app, canvas):
    pass

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