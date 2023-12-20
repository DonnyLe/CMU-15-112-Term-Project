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
#col number = 5
#row number = 5
#margin = 5

def appStarted(app):
    app.cols = 5
    app.rows = 5
    app.margin = 5
    app.cellLength = (app.width - app.margin)/app.rows
    app.row = 0 
    app.col = 0

def mousePressed(app, event):
    pass

def keyPressed(app,event):
    pass


def timerFired(app,event):
    pass

def drawCells(canvas,app):
    for r in range (app.rows):
        for c in range(app.cols):
            canvas.create_rectangle(getCellBounds(app, r, c))

def getCellBounds(app, row, col):
    x0,y0 = (app.margin + app.cellLength * app.col, 
            app.margin + app.cellLength * row)

    x1, y1 = (app.margin + app.cellLength * (app.col+1), 
             app.margin + app.cellLength * (app.row+1))
    return x0, y0, x1, y1


def redrawAll(canvas,app):
    drawCells(canvas,app)
    
def main():
    cs112_n22_week2_linter.lint()
    runApp(width=510, height=540)

if __name__ == '__main__':
    main()