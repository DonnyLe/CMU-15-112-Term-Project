#################################################
# Your name: Donny Le
# Your andrew id: dmle
#################################################

import math, copy, random
from cmu_112_graphics import *
from objects import *
from layers import *
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

#################################ad################
# Main Menu
#################################################
#main menu and menu code taken/learned from 15112 website
def mainMenu_redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height-app.height/5, text="Type your username\nin the console to start!", font="Arial 30 bold")
    canvas.create_text(app.width/2, app.height/4, text = "Grappling Garry Plus!", font="Arial 45 bold")
    for button in app.buttonList:
        button.drawButton(canvas)

#button check 
def mainMenu_timerFired(app):
    if app.mouseX != None and app.mouseY != None:
        for button in app.buttonList:
            if button.isPressed(app.mouseX, app.mouseY):
                if button == app.playGameButton:
                    app.recommendedPathMode = False
                    app.mode = "gameMode"
                if button == app.aimodeButton:
                    app.recommendedPathMode = True
                    app.mode = "gameMode"

#mouse pressed
def mainMenu_mousePressed(app, event):
    app.mouseX = event.x
    app.mouseY = event.y

#################################ad################
# Main App
#################################################
def appStarted(app):
    app.recommendedPathMode = False
    app.playGameButton = Button(app.width/2 ,app.height * 2/5, 75, 75, "Press to Play!", "blue")
    app.aimodeButton = Button(app.width/2, app.height * 3/5, 75, 75, "AI Help Mode \n (Not Functional)", "red")
     
    app.buttonList = [app.playGameButton, app.aimodeButton]
    app.mode = "mainMenu"
    app.username = None
    app.data = readFile("data.txt")
    app.timerDelay = 10
    app.time = 0
    
    app.highscore = None
    app.showHitBox = False
    app.comboRadius =50
    app.dataDict = dict()
    print("Enter Username")
    app.username = str(input())
    gameStarted(app)
    app.invincibility = False


#################################ad################
# Game Mode App
#################################################
def gameStarted(app):

    app.dataStr = ""
    startingLayer(app)
    app.droneIntersected = False
    app.score = 0
    app.extraLife = False
    app.framestime = 0
    #score multiplier 
    app.combo = 1
    app.thirdLayerPlaced = False
    app.secondLayerPlaced = False
    app.mouseX = None
    app.mouseY = None
    app.frames = 0
    app.gameOver = False
    app.gravity = 0.3
    app.velocity = 8
    app.grappleCoords1 = ()
    app.grappleCoords2 = ()
    app.grappleBoolean = False
    app.grappleTheta = None
    app.firstMove = True
    app.dx = 0
    app.dy = 0
    #used for physics 
    app.tempdx = 0
    app.tempdy = 0
    #used for sidescrolling, general idea came from 15112 sidescrolling section 
    app.scrollX = 0
    app.scrollY = 0
    app.scrollMargin = app.height * 2/3
    #used in falling animation

    app.futureScrollY = 0
    app.leftbound = 0
    app.rightbound = 0
    #used to correct directions with negative and positive slopes
    app.negativeDx = 1
    app.negativeDy = 1

    
    #amount of times player is able to cut the current grapple,
    #used as last ditch survival measure
    #press 5 to activate
    app.cutGrapple = 2
    
    app.currentDrone = None
    app.slope = None

    app.comboBoolean = False
    
    app.charactercolor = "white"
    if app.recommendedPathMode and len(app.allDroneList)>1:
        recommendedPathStarted(app)

#for recommended path
def recommendedPathStarted(app):
    app.direction = 0
    app.circlingPathRadius = 100
    app.circlingPathThetaChange = 1
    app.cxlarge, app.cylarge = 0, 0
    app.initialTheta = 0
    app.cx0, app.cy0 = None
    app.cx1, app.cy1 = None

#from Strings Pt1, Basic File IO on the 15112 course website
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

#from Strings Pt1, Basic File IO on the 15112 course website
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

#from Strings Pt1, Basic File IO on the 15112 course website
def writeContents(app):
    if app.username != None:
        contentsToWrite = app.data + f'{app.username},{app.score}/'
        writeFile("data.txt", contentsToWrite)
        app.data = readFile("data.txt")

#reads the data and organizes into a dictionary
def readData(app):
    for pair in app.data.split("/"):
        if len(pair) !=0:
            userNameScore = pair.split(",")
            name = userNameScore[0]
            score = userNameScore[1]
            #adds name and score to dictionary
            if name in app.dataDict: 
                app.dataDict.get(name).append(int(score))
            else:
                app.dataDict[name] = [int(score)]

#used mainly to select drones
def gameMode_mousePressed(app, event):
    app.mouseX = event.x
    app.mouseY = event.y
    for i in range(len(app.allDroneList)):
        for drone in app.allDroneList[i]:
            if drone.isClicked(app):
                selectDrone(app, drone)            
                getGrappleValues(app)

#selects the drone, helper function 
def selectDrone(app, drone):
    #gets the initial location of the clicked drone
    app.currentDrone = drone
    #used to prevent character from falling b/c gravity when game starts
    app.firstMove = False
    #starts all operations involving the grapple
    app.grappleBoolean = True
    #resets the initial velocity after grappling to 10 
    app.velocity = app.velocity


def gameMode_keyPressed(app, event):
    #brings to main menu
    key = event.key
    if key == "Escape":
        app.mode = "mainMenu"
        gameStarted(app)

    #cuts the current grapple, allows player to have a chance of surviving if 
    #they chose the wrong drone
    if key == "5":
        if app.cutGrapple != 0:
            app.grappleBoolean = False
            app.cutGrapple -= 1

    #invincibility for debugging
    if key == "g":
        app.invincibility = not app.invincibility

    #restarts app
    if key == 'r':
        gameStarted(app)

    #shows hitbox
    if key == 'h':
        app.showHitBox = not app.showHitBox
   
    #alternative controls, see README, not very effective at this moment
    if (key in {"1", "2", "3", "4"}):
        for i in range(len(app.allDroneList)):
            if int(key) <= len(app.allDroneList[i]) :
                drone = app.allDroneList[i][int(key)-1]
                if not drone.alreadyInteracted:
                    selectDrone(app, drone)
                    getGrappleValues(app)
                    break

#returns values needed for grappling mechanic
def getGrappleValues(app):
    #sets the grappleCoords to the drone's pos and character's pos 
    app.grappleCoords1 = (app.currentDrone.cx, app.currentDrone.cy)
    app.grappleCoords2 = (app.character.cx, app.character.cy)
    cx0, cy0 = app.grappleCoords1    
    cx1, cy1 = app.grappleCoords2
    #calculate slope and theta (in rads)
    app.slope, app.negativeDx, app.negativeDy = calculateSlope(cx0, cy0, 
                                    cx1, cy1, app.negativeDx, app.negativeDy)
    app.theta = calculateTheta(app.slope)
    

def gameMode_timerFired(app):
    #keeps the combo text up for 500 ms
    if app.comboBoolean:
        app.time+= app.timerDelay
        if app.time % 500 == 0 and app.time> 0:
            app.comboBoolean = False
            app.time = 0

    
    if app.gameOver and not app.invincibility:
        return 
    
    #calls helper functions
  
    bombChecks(app)
    droneChecks(app)
    if app.recommendedPathMode:
        recommendedPath(app)
    #moving the player
    if(not app.firstMove):
        if app.grappleBoolean:
            #updates grappleCoords  
            getGrappleValues(app)
            app.dx, app.dy = calculateVelocityComponents(app.theta, 
                            app.velocity, app.negativeDx, app.negativeDy)
            #temps used for game physics
            app.tempdx = app.dx
            app.tempdy = app.dy
            # print(app.dx, app.dy)

            #moves the character directly rto the given drone
            app.character.move(app.dx,app.dy, app)

        else:
            physics(app)
            app.character.move(app.dx,app.dy, app)
    
    #checks if player is off the screevn (with leeway)
    if (app.character.cx-150 > app.width or app.character.cx+150 < 0 
        or app.character.cy - 150 > app.height and not app.invincibility):
       
        writeContents(app)
        readData(app)
        if app.username != None:
            app.highscore = max(app.dataDict[app.username])
        app.gameOver = True

#second game mode where drones are highlighted to show where to press
#!not functional
def recommendedPath(app):
    for dronerow in app.allDroneList:
        for drone in dronerow:
            if drone != app.currentDrone and drone.alreadyInteracted == False:
                
                negativeDx, negativeDy = 1, 1
                app.cx0, app.cy0 = app.character.cx, app.character.cy
                app.cx1, app.cy1 = drone.cx, drone.cy
                slope, theta, negativeDx, negativeDy = getGrappleValuesRecommendedPath(app.cx0, app.cy0, app.cx1, app.cy1,  negativeDx, negativeDy)
                dx, dy = calculateVelocityComponents(theta, app.velocity, negativeDx, negativeDy)

                if bombCheckGrappleRecommendedPath(app, drone, dx, dy):
                    drone.isRecommendedPath = True
                    pass
                else:
                    drone.isRecommendedPath = False
       
def getGrappleValuesRecommendedPath(cx0, cy0, cx1, cy1, negativeDx, negativeDy):
    #calculate slope and theta (in rads)
    slope, negativeDx, negativeDy = calculateSlope(cx1, cy1, 
                                    cx0, cy0, negativeDx, negativeDy)
    theta = calculateTheta(slope)
    return slope, theta, negativeDx, negativeDy

def bombCheckGrappleRecommendedPath(app, drone, dx, dy):
    while app.character.objectsIntersectsFuture(drone, app) == False:  
        #!! i do not understand why this gives these values
        #!! this is the same way I did the movement with grappling
        #!! The direction of dy and dx follows the same way I did the grappling
        #!! This code makes perfect sense in my head but I can't seem to find the bug 
        #!! spent several hours trying to debug, most likely a logical error 
        #!! any help would be appreciated 
        # print(f'char pos {app.character.cx}, {app.character.cy}')
        # print(app.futureScrollY)
        print(f'char pos {app.character.futurecx}, {app.character.futurecy}')
        if app.futureScrollY !=0:
       


            drone.moveFuture(0, -app.futureScrollY)
            app.character.moveFuture(0, -app.futureScrollY)
        else:
            app.character.moveFuture(dx, dy)
        for bomblist in app.allBombList:
            for bomb in bomblist:
                if isinstance(bomb, circlingBomb):
                    bomb.circleFuture(100, 1)
                    

                if isinstance(bomb, sideToSideBomb):
                    bomb.sideToSideFuture()
                if app.futureScrollY !=0:
                    bomb.moveFuture(0, -app.futureScrollY)
            
                if app.character.objectsIntersectsFuture(bomb, app):
                    return False
        

       

        # i+=1 
    for bombrow in app.allBombList:
        for bomb in bombrow:
            bomb.futurecx = bomb.cx
            bomb.futurecy = bomb.cy
    app.character.futurecx = app.character.cx
    app.character.futurecy = app.character.cy
    for dronerow in app.allDroneList:
        for drone in dronerow:
            drone.futurecx = drone.cx
            drone.futurecy = drone.cy
    return True
    

#does all checks with drones, helper function
def droneChecks(app):
    for e in range(len(app.allDroneList)):
        for drone in app.allDroneList[e]:
            if isinstance(drone, MissileDrone) and drone.alreadyInteracted:
                #makes missiles fron missleDrone move to bomb
                for missile in drone.missileList:
                    if app.scrollY !=0:
                        missile.move(0, -app.scrollY)
                    missile.trackBomb()
                    if missile.foundBomb:
                        drone.missileList.remove(missile)
            if app.scrollY !=0:
                drone.move(0, -app.scrollY)
                
            #checks when the player touches the drone
            if (drone.objectsIntersects(app.character, app) == True 
                and not drone.alreadyInteracted):
                if isinstance(drone, MissileDrone):
                    drone.missileLaunch(app)
                    
                #stops grappling
                if drone == app.currentDrone:
                    app.grappleBoolean = False
                #stops the same drone from giving multiple points
                drone.alreadyInteracted = True
                app.score += 1 * app.combo
                if app.velocity < 25:
                    app.velocity += 0.05
    moveLayers(app)

#does all checks with bombs, helper function
def bombChecks(app):
    #while loops used since .pop is in function 
    k = 0
    while k < len(app.allBombList):
        i = 0
        while i < len(app.allBombList[k]):
            #y axis scrolling, moves all objects but player down 
            if app.scrollY !=0:
                app.allBombList[k][i].move(0, -app.scrollY)
            
            #moves bomb in circle path
            if isinstance(app.allBombList[k][i], circlingBomb):
                
                app.circlingPathRadius = 100
                app.circlingPathThetaChange = 1
                
                app.allBombList[k][i].circle(100, 1)
            #moves bomb in sidetoside path
            if isinstance(app.allBombList[k][i], sideToSideBomb):
                app.allBombList[k][i].sideToSideMovement()
                
            if ((app.allBombList[k][i].objectsIntersects(app.character, app) == True
                 and app.invincibility == False )
                and app.allBombList[k][i].alreadyInteracted == False):
                app.allBombList[k][i].alreadyInteracted = True
                if app.extraLife == False:
                    app.velocity = 0
                    writeContents(app)
                    readData(app)
                    if app.username != None:
                        app.highscore = max(app.dataDict[app.username])

                    app.gameOver = True
                else:
                    app.charactercolor = "white"
                    app.extraLife = False
            
            else:
                #near miss checksa
                if app.allBombList[k][i].nearMiss(app.character, app):
                    #player needs to be near the bomb continuously for 150 ms
                    app.allBombList[k][i].nearMissTime += app.timerDelay
                    if app.allBombList[k][i].nearMissTime >= 100:
                        #combo doubles points
                        app.combo += 1
                        
                        app.comboBoolean = True
                        #prevents singular bomb from giving multiple combos
                        
                        app.allBombList[k][i].comboTaken = True
                #resets near-miss time
                else:
                    app.allBombList[k][i].nearMissTime = 0

            if app.allBombList[k][i].exploded:
                app.allBombList[k].pop(i)
            else:
                i+=1
        k+=1 


#slows down the y velocity drastically after it touches drone 
#does not follow kinematics initially but works better for game
#accleration of gravity not accurate to real life
def physics(app):
    dySlowDown = 1 * app.velocity/10
    if app.dy<= 0:
        app.dy += dySlowDown
    else:
        app.dy += app.gravity
    
    dxSlowDown = 0.3 * app.velocity/10
    if app.tempdx > 0 and app.dx - dxSlowDown > app.tempdx//2:
        app.dx -= dxSlowDown
    if app.tempdx < 0 and app.dx + dxSlowDown < app.tempdx//2:
        app.dx += dxSlowDown

#moves the layers, press H to see layer lines
#helps allign the different layers of bombs/drones
def moveLayers(app):
    app.layerGuideLine1-= app.scrollY 
    #following if statements are for initially placing the layers
    if(app.secondLayerPlaced==False):
        if app.layerGuideLine1 > app.height/2.5:
            app.layerGuideLine2 = 0            
            app.secondLayerPlaced = True
            #calls function from layers.py
            addLayer(app, app.layerGuideLine2)

    elif(app.thirdLayerPlaced==False):
        if app.layerGuideLine2 > app.height/2.5:
            app.layerGuideLine3 = 0
            app.thirdLayerPlaced = True
            #calls function from layers.py
            addLayer(app, app.layerGuideLine3)

    else:
        if app.layerGuideLine1 > app.height+app.height/10:
            app.allDroneList.pop(0)
            app.allBombList.pop(0)
            app.layerGuideLine1 = app.layerGuideLine2
            app.layerGuideLine2 = app.layerGuideLine3
            app.layerGuideLine3 -= app.height/2.5
            #calls function from layers.py
            addLayer(app, app.layerGuideLine3)
    
    if app.secondLayerPlaced:
        app.layerGuideLine2 -= app.scrollY 
    if app.thirdLayerPlaced:
        app.layerGuideLine3 -= app.scrollY 
#draws score
def drawScore(app,  canvas):
    canvas.create_text(app.width/2, 50, text=f'{app.score}', font="Arial 30 bold" )

#draws current combo
def drawCombo(app, canvas):
        canvas.create_text(app.width/2, app.height/2, text=f'{app.combo}x', font="Arial 50 bold")
        if app.comboBoolean:
            canvas.create_text(app.character.cx ,app.character.cy, text=f'+1 Combo!', font="Arial 50 bold")

#draws gameover
def drawGameOver(app ,canvas):
    canvas.create_text(app.width/2, 150, text="You Lost",  font="Arial 50 bold" )
    canvas.create_text(app.width/2, 300, text=f'Your highscore is {app.highscore}',  font="Arial 25 bold", fill="green" )
    canvas.create_text(app.width/2, 450, text="Press R to restart",  font="Arial 20 bold", fill="black" )

#draws grapple hook
def drawGrappleHook(app, canvas):
    if app.gameOver and not app.invincibility:
        return 
    cx0, cy0 = app.grappleCoords1
    cx1, cy1 = app.grappleCoords2

    #rotates grapple hook to face drone
    #done this way instead of create_line so images can be added in the future
    canvas.create_polygon(rotatePolygon(5, app.theta, cx0, cy0, cx1, cy1))

#draws the layer guideline
def drawLayerGuideLine(app, canvas):
    canvas.create_line(0, app.layerGuideLine1, app.width, app.layerGuideLine1, width = 3)
    if app.thirdLayerPlaced:
        canvas.create_line(0, app.layerGuideLine3, app.width, app.layerGuideLine3, width = 3, fill = "blue")

    if app.secondLayerPlaced:
        canvas.create_line(0, app.layerGuideLine2, app.width, app.layerGuideLine2, width = 3, fill = "orange")

#draws if invincility is turned on, press G
def drawInvincibilityText(canvas):
    canvas.create_text(10, 10, anchor = "nw", text=f'Invincibility is On')

#draws everything
def gameMode_redrawAll(app, canvas):
    drawCombo(app, canvas)
    drawScore(app, canvas)
    
    if(app.grappleBoolean):
        drawGrappleHook(app, canvas)
    #draws bombs, at most 3 bomb lists at once
    for i in range(len(app.allBombList)):
        for bomb in app.allBombList[i]:
            bomb.drawBomb(canvas)
            if app.showHitBox:
                bomb.drawHitboxes(canvas) 
    #draws drones, at most 3 drone lists at once
    for j in range(len(app.allDroneList)):
        for drone in app.allDroneList[j]:
            if isinstance(drone, MissileDrone):
                for missile in drone.missileList:
                    missile.drawMissile(canvas)

            drone.drawDrone(canvas, app, "white")
            drone.drawPath(app, canvas)
            if app.showHitBox:
                drone.drawHitboxes(canvas) 
            
    app.character.drawCharacter(canvas, app.charactercolor)
    if app.showHitBox:
        app.character.drawComboCircle(canvas, app)
        app.character.drawHitboxes(canvas) 
        drawLayerGuideLine(app, canvas)
    if app.invincibility:
        drawInvincibilityText(canvas)
    if app.gameOver and not app.invincibility:
        drawGameOver(app, canvas)

#################################################
# main
#################################################

def main():
    runApp(width=500, height=800)

if __name__ == '__main__':
    main()
