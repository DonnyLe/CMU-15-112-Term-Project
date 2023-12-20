from cmu_112_graphics import *
import math
# def redrawAll(app,canvas):
#     canvas.create_oval(100,100,app.width/2,app.height/2, fill = 'green', outline = '#AAFFBB', width =10)
#     canvas.create_text(app.width/2,app.height/2, text = 'this is a test', anchor='c')

def redrawlAll(app, canvas):
    cx = app.width/2
    cy = app.height/2
    r = 200
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'cyan')
    theta = math.pi/4
    dx = cx + r * math.cos(theta)
    dy = cy + r * math.sin(theta)
    littleR = 20
    canvas.create_oval(dx-littleR, dy-littleR, dx+littleR, dy+littleR, fill='pink')

runApp()