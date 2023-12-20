from cmu_112_graphics import * 

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/4
    app.r = 50
    app.text = "No key pressed yet"
    app.timerDelay = 16
    app.dx = 4
    app.dy = 3
    
# def mouseMoved(app,event):
#     app.cx = event.x
#     app.cy = event.y

def mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y



def timerFired(app):
    app.cx +=app.dx
    app.cx += app.dy
    checkWraparound(app)


def checkWraparound(app):
    app.cx = app.cx % (app.width+app.r)
    app.cy = app.cy % (app.width+app.r)
    

def keyPressed(app,event):
    # print(event.key)
    # print(type(event.key))
    #pass
    app.text = event.key
    if app.text == "Right": 
        app.cx += 10
    elif app.text == "Left": 
        app.cx -= 10
    elif app.text == "Down": 
        app.cy += 10
    elif app.text == "Up": 
        app.cy -= 10

    checkWraparound(app)
    
import math
def draw(canvas, width, height):
    canvas.create_line(200, 0, 200, 400) 
    canvas.create_line(0, 200, 400, 200) 
    x, y = 300, 200
    t=0
    for q in range(4):
        t += 90
        u, v, = x, y 
        x = 200 + 100* math.cos(math.radians(t))
        y = 200 -  100* math.sin(math.radians(t))
        canvas.create_line(u, v, x, y)

def redrawAll(app,canvas):
    canvas.create_oval(app.cx-app.r,app.cy-app.r,
                        app.cx+app.r,app.cy+app.r,
                        fill='violet' )
    canvas.create_text(app.width/2, app.height/2, 
                            text = app.text, 
                            font= "Arial 40")
    draw(canvas,400,400)
runApp(width=800, height=800)