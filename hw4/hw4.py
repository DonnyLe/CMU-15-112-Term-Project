#################################################
# hw4.py
# name: Donny Le 
# andrew id: 814477499
#################################################

import cs112_n22_week2_linter
import math, string

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

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# hw4-standard-functions
#################################################

#draws cross pattern 
def drawPattern1(canvas, width, height, points):
    for i in range(-1*points,points):
        x1 = (width/points) * i
        y1 = (height/points) * i 
        canvas.create_line(x1, 0, width, height - y1)
   
    for j in range(-1*points, points):
        x1 = (width/points) * j
        y1 = (height/points) * j 
        canvas.create_line(0, height - y1, width - x1, 0)



#returns vals for robot's body 
def body(cx, cy):
    bodywidth, bodyheight = 150, 200
    bodyX1, bodyY1, = cx-bodywidth/2, cy-bodyheight/2
    bodyX2, bodyY2, = cx+bodywidth/2, cy+bodyheight/2
    return bodyX1, bodyY1, bodyX2, bodyY2, 

#returns vals for robot's neck
def neck(canvas, width, height, cx,cy):
    _, bodyY1, _, _ = body(cx,cy)
    neckwidth, neckheight = 40,25
    neckX1, neckY1 = cx-neckwidth/2, bodyY1- neckheight
    neckX2, neckY2 = cx+neckwidth/2, bodyY1
    return neckX1, neckY1,neckX2, neckY2
   
#returns vals for robot's square head
def head(canvas, width, height, cx,cy):
    _, neckY1,_, _ = neck(canvas, width, height, cx,cy)
    headwidth = 125
    headX1, headY1 = cx - headwidth/2, neckY1 - headwidth
    headX2, headY2 = cx + headwidth/2, neckY1 
    return headX1, headY1, headX2, headY2

#antenna triangle on top of robot's head
def antennaTriangle(canvas, width, height, cx,cy):
  
    _, headY1, _, _ = head(canvas, width, height, cx,cy)
    trianglebase, triangleheight = 20, 30

    triangleX1, triangleY1 = cx - trianglebase/2, headY1
    triangleX2, triangleY2 = cx + trianglebase/2, headY1
    triangleX3, triangleY3 = cx, headY1-triangleheight
    
    return ( triangleX1, triangleY1, triangleX2, triangleY2, 
    triangleX3, triangleY3)

#returns vals for circle on top of head 
def antennaCircle(canvas, width, height, cx,cy):
    _, _, _, _, _, triangleY3 = antennaTriangle(canvas, width, height, cx,cy)

    verticalShift = 15
    radiusAntenna = 15
    circleX1, circleY1 = (cx - radiusAntenna, triangleY3-radiusAntenna*2+
                          verticalShift)
    circleX2, circleY2 = cx + radiusAntenna, triangleY3+verticalShift
    
    return circleX1, circleY1, circleX2, circleY2 
    
#draws body circle lights
def lightsCircles(canvas, cx,cy):
    bodywidth = 150
    radiusBodyLights = 15
    betweenWhiteSpace = 15
    bodyX1, bodyY1, _, bodyY2 = body(cx,cy)

    endWhitespace = (bodywidth - radiusBodyLights*3*2 - betweenWhiteSpace*2) /2 
    for i in range(3):
        color = ""
        if i == 1:
            color = "blue"
        elif i == 2:
            color = "green"
        else:
            color = "orange"
        lightsX1, lightsY1 = (endWhitespace + bodyX1 + i* 2 * 
                        radiusBodyLights + i* betweenWhiteSpace, 
                        (bodyY1+bodyY2)/2+radiusBodyLights)

        lightsX2, lightsY2 = (endWhitespace + bodyX1 + (i+1)* 2 * 
                        radiusBodyLights + i* betweenWhiteSpace, 
                        (bodyY1+bodyY2)/2-radiusBodyLights)

        canvas.create_oval(lightsX1, lightsY1, lightsX2, lightsY2, fill=color)

#draws eyes
def eyes(canvas, width, height, cx,cy):
    headX1, headY1, _, headY2 = head(canvas, width, height, cx,cy)
    headwidth = 125
    radiusEye = 15
    betweenWhiteSpace = 15
    endWhitespace = (headwidth - radiusEye*2*2 - betweenWhiteSpace) /2 
    for i in range(2):
   
        eyeX1, eyeY1 = (endWhitespace + headX1 + i* 2 * 
                        radiusEye + i* betweenWhiteSpace, 
                        (headY1+headY2)/2+radiusEye)
        eyeX2, eyeY2 = (endWhitespace + headX1 + (i+1)* 2 * 
                        radiusEye + i* betweenWhiteSpace, 
                        (headY1+headY2)/2-radiusEye)

        canvas.create_oval(eyeX1, eyeY1 , eyeX2, eyeY2,fill="white")

#returns vals for mouth
def mouth(canvas, width, height, cx,cy):
    _, headY1, _, _ = head(canvas, width, height, cx,cy)
    betweenWhiteSpace = 15
    headwidth = 125

    mouthX1, mouthY1 = cx-betweenWhiteSpace/2, headY1 + headwidth * 3/4
    mouthX2, mouthY2 = cx+betweenWhiteSpace/2, headY1 + headwidth * 3/4

    return  mouthX1, mouthY1, mouthX2, mouthY2

#draws two arms
def arms(canvas, width, height, cx,cy):
    bodyX1, bodyY1, _, bodyY2 = body(cx,cy)
    #arms
    armLength = 150
    armWidth = 40
    bodywidth = 150
    ydistanceFromBody = 10

    for i in range(0,2):
        armX1, armY1 = (bodyX1 - armWidth + 2*armWidth * i + bodywidth*i, 
                        bodyY1+ ydistanceFromBody)
        armX2, armY2 = (bodyX1 +bodywidth*i, bodyY1+ 
                        ydistanceFromBody + armLength)
    
        canvas.create_rectangle(armX1, armY1,  armX2, armY2,fill="gray")

#code is generalized (dimensions can be changed)
#creates a robot in tkinter 
def drawNiceRobot(canvas, width, height):
    cx, cy = width/2, height/2+100
    canvas.create_rectangle(body(cx, cy), fill="gray")
    canvas.create_rectangle(neck(canvas, width,height, cx,cy),fill="gray")
    canvas.create_rectangle(head(canvas, width, height, cx, cy),fill="gray")
    canvas.create_polygon(antennaTriangle(canvas, width, height, cx,cy),
                                            fill="black")
    canvas.create_oval(antennaCircle(canvas, width, height, cx,cy),fill="black")
    canvas.create_line(mouth(canvas, width, height, cx,cy),fill="black")
    lightsCircles(canvas, cx,cy)
    eyes(canvas, width, height, cx,cy)
    arms(canvas, width, height, cx,cy)
    
#creates the flag of qatar using rectangles
def drawFlagOfQatar(canvas, x0, y0, x1, y1):
    # Replace all of this with your drawing of the flag of Qatar
    # Also: remember to add the title "Qatar" centered above the flag!
    canvas.create_rectangle(x0, y0, x1, y1, fill='orange')
    font = 'Arial 20 bold' if (x1 - x0 > 150) else 'Arial 12 bold'
    canvas.create_text((x0+x1)/2, (y0+y1)/2,
                       text='Draw the flag\nof Qatar here!',
                       font=font)

    whiteEdge = x1-(x1-x0)*4/6
    canvas.create_rectangle(x0, y0, x1, y1, fill='#8A1538')
    canvas.create_rectangle(x0, y0, whiteEdge, y1, fill='white')
    
    zigzag(x0, y0, x1, y1, whiteEdge, canvas, 9)

#helper function that creates the white zigzag
def zigzag(x0, y0, x1, y1, whiteEdge, canvas, n):
    trianglebase = (y1-y0)/n
    triangleheight = trianglebase

    for i in range(9):
        trianglex1, triangley1 = whiteEdge, y0 + i * trianglebase
        trianglex2, triangley2 = whiteEdge, y0 + (i+1) * trianglebase
        trianglex3, triangley3 = (whiteEdge + triangleheight, y0 + 
                                 (triangley2-triangley1)/2 + i * trianglebase)

        canvas.create_polygon(trianglex1, triangley1,trianglex3, triangley3,
        trianglex2, triangley2, fill="white")


#################################################
# hw4-bonus-functions
# these are optional
#################################################

#draws a "star" pattern
def drawPattern2(canvas, width, height, points):
    halfwidth = width/2
    halfheight = height/2 
    cx, cy = halfwidth,halfheight 
    canvas.create_line(width/2, 0, width/2, height)
    canvas.create_line(0, height/2, width, height/2)
    spacingAxisX = halfwidth/points
    spacingAxisY = halfheight/points

    #first quadrant
    for i in range(points):
        x1,y1 = (width -spacingAxisX * i,cy)
        x2,y2 = (cx,cy - spacingAxisY * i )
        canvas.create_line(x1, y1, x2, y2)

    #second quadrant
    for i in range(points):
        x1,y1 = (spacingAxisX * i,cy)
        x2,y2 = (cx,cy - spacingAxisY * i )
        canvas.create_line(x1, y1, x2, y2)

    #third quadrant
    for i in range(points):
        x1,y1 = (spacingAxisX * i,cy)
        x2,y2 = (cx,cy + spacingAxisY * i )
        canvas.create_line(x1, y1, x2, y2)

    #fourth quadrant
    for i in range(points):
        x1,y1 = (width -spacingAxisX * i,cy)
        x2,y2 = (cx,cy + spacingAxisY * i )
        canvas.create_line(x1, y1, x2, y2)


def drawFancyWheels(canvas, width, height, rows, cols):
    pass




#################################################
# Test Functions
#################################################

def testDrawPattern1(app, canvas):
    drawPattern1(canvas, app.width, app.height, app.points)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawPattern1' + 
            f'(canvas, {app.width}, {app.height}, {app.points})'))

def testDrawPattern2(app, canvas):
    drawPattern2(canvas, app.width, app.height, app.points)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawPattern2' + 
            f'(canvas, {app.width}, {app.height}, {app.points})'))

def testDrawFlagOfQatar(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfQatar(canvas, 50, 125, 350, 275)
    drawFlagOfQatar(canvas, 425, 100, 575, 200)
    drawFlagOfQatar(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-20, 
          text="Testing drawFlagOfQatar")
    canvas.create_text(app.width/2, app.height-10, 
          text="This does not need to resize properly!")


def testDrawNiceRobot(app, canvas):
    drawNiceRobot(canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-20, 
          text=('Testing drawNiceRobot' +
            f'(canvas, {app.width}, {app.height})'))
    canvas.create_text(app.width/2, app.height-10, 
          text=f'''Comment out these print lines if they mess up your art!''')

def testDrawFancyWheels(app, canvas, rows, cols):
    drawFancyWheels(canvas, app.width, app.height, rows, cols)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawFancyWheels' + 
            f'(canvas, {app.width}, {app.height}, {rows}, {cols})'))


def drawSplashScreen(app, canvas):
    text = f"""
Press the number key for the 
exercise you would like to test!

1. drawPattern1 ({app.points} points)
2. drawNiceRobot
3. drawFlagOfQatar

4. Bonus drawPattern2 ({app.points} points)
5. Bonus drawFancyWheels (1x1)
6. Bonus drawFancyWheels (4x6)


You can press the up or down arrows to change
the number of points for drawPattern1
and drawPattern2 between 3 and 20
"""

    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text,
                        font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.points = 5
    app.timerDelay = 10**10

def keyPressed(app, event):
    if event.key == "Up":
      app.points = min(20, app.points+1)
      print(f"Increasing points to {app.points}")
      if app.points >= 20: print("Maximum allowed points!")
    elif event.key == "Down":
      app.points = max(3, app.points-1)
      print(f"Decreasing points to {app.points}")
      if app.points <= 3: print("Minimum allowed points!")
    else:
      app.lastKeyPressed = event.key





def redrawAll(app, canvas):
    if app.lastKeyPressed == "1":
      testDrawPattern1(app, canvas)
    elif app.lastKeyPressed == "2":
      testDrawNiceRobot(app, canvas)
    elif app.lastKeyPressed == "3":
      testDrawFlagOfQatar(app, canvas)
    elif app.lastKeyPressed == "4":
      testDrawPattern2(app, canvas)
    elif app.lastKeyPressed == "5":
      testDrawFancyWheels(app, canvas, 1, 1)
    elif app.lastKeyPressed == "6":
      testDrawFancyWheels(app, canvas, 4, 6)
    else:
      drawSplashScreen(app, canvas)

#################################################
# main
#################################################

def main():
    cs112_n22_week2_linter.lint()
    runApp(width=600, height=600)

if __name__ == '__main__':
    main()
