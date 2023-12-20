def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.cellwidth = 50

def getCellBounds(app, row, col):
    x0, y0 = app.cellwidth * row, app.cellwidth * col
    x1, y1 = app.cellwidth * (row+1), app.cellwidth * (col+1)
    return x0, y0, x1, y1
def drawCells(app, canvas):
    for r in app.rows:
        for c in app.cols:
            canvas.create_rectangle(getCellBounds(app, r, c))

def redrawAll(app, canvas):
    drawCells(app, canvas)


def isPrime(n):
    if n<2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

def nthPrime(n):
    guess = 0
    found = 0
    while (found < n):
        guess += 1
        if(isPrime(n)):
            found+=1 
    return guess

