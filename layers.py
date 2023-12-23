from objects import *
from main import * 
import random

#starting layer
def startingLayer(app):
    app.droneWidth = app.width/7
    app.character = Character(app.width/2, app.height-30, 30, 100)
    app.layerGuideLine1 = app.height/5
    app.startingLayer = [Drone(app.width/2, app.layerGuideLine1,  app.droneWidth,  app.droneWidth)]
    app.allBombList = [[]]
    app.allDroneList = [app.startingLayer]
    app.layerGuideLine3 = None
    app.layerGuideLine2 = None
    app.easyprobability = 0.6
    app.mediumprobability = 0.3
    app.hardprobability = 0.1

#adds layer after other layer is off the screen
def addLayer(app, layer):
    difficulty, n = getLayerProbabilities(app)
    dronelist, bomblist = buildLayer(app, difficulty, layer, n)
    
    #updates drone and bomb lists in main.py
    app.allDroneList.append(dronelist)
    app.allBombList.append(bomblist)

#randomly generates the layers based on difficulty
def buildLayer(app, difficulty, layer, n):
    totalList = []
   
    mustHaveDroneCounter = 1
    dronelist = []
    bomblist = []
    

    option1Probability, option2Probability, option3Probability, option4Probability = getLayoutProbabilities(difficulty)

    cx = random.uniform(app.width/(n*2.5), app.width/(n*2))
    i = 0
    copyn = n
    while i< n:
        shift = random.uniform(-10, 10)
        randFloat = random.random()

        #adds a singular drone
        if randFloat < option1Probability:
            drone = chooseDroneType(app, cx, layer + shift, app.droneWidth, app.droneWidth, random.uniform(0,10), difficulty)
            totalList.append(drone)
            mustHaveDroneCounter -= 1
            cx += random.uniform(app.width/(copyn*1.25), app.width/(copyn)) if copyn != 1 else random.uniform(app.width/(5), app.width/4)
            i+= 1
        #adds a singular bomb
        elif randFloat >= option1Probability and randFloat <option1Probability + option2Probability:
            totalList.append(Bomb(cx, layer + shift, app.droneWidth/2))
            cx += random.uniform(app.width/(copyn*1.25), app.width/(copyn)) if copyn != 1 else random.uniform(app.width/(5), app.width/4)
            i+= 1
        #adds a circling bomb over a drone
        elif(randFloat >= option1Probability + option2Probability and randFloat <option1Probability + 
            option2Probability + option3Probability):
            i, cx= droneInsideCircularBomb(app, totalList, i, layer, shift, cx, copyn, difficulty)
        
        #adds a bomb that moves side-to-side between two drones
        else:
            if n-i> 2:
                i, cx, n = sideToSideSetUp(cx, layer, shift, totalList, app, i, n, difficulty)
   
    #has to have at least one drone by itself, makes sure that the layer is possible to get past
    if i==n and mustHaveDroneCounter > 0:
        cx -= random.uniform(app.width/(copyn*1.25), app.width/(copyn)) if copyn != 1 else random.uniform(app.width/(5), app.width/4)
        drone = chooseDroneType(app, cx, layer + shift, app.droneWidth, app.droneWidth, random.uniform(0,10), difficulty)
        totalList[n-1] = drone
    
    #turns 3D list into 1D list 
    flattenedList = flatten(totalList)

    #separates bombs and drones into separate lists 
    for gameobject in flattenedList:
        if isinstance(gameobject, Drone):
            dronelist.append(gameobject)
        else:
            bomblist.append(gameobject)

    return dronelist, bomblist

#**creates a drone with a bomb circling it
#**considered as one item in the layer
def droneInsideCircularBomb(app, totalList, i, layer, shift, cx, copyn, 
                            difficulty):
    circlingbomb = circlingBomb(cx, layer + shift, 
                                app.droneWidth/2, random.randrange(360), 
                                random.choice([-1, 1]), cx, layer + shift, app)
    circlingbomb.circle(100, 1)

    droneInCircle = chooseDroneType(app, cx, layer + shift, app.droneWidth, 
                            app.droneWidth, random.uniform(0,10), difficulty)
    pair = [circlingbomb, droneInCircle]
    totalList.append(pair)
    
    #cannot have two droneInsideCircularBomb next to eachother
    if (i>0 and isinstance(totalList[i], list) and isinstance(totalList[i-1], list) 
        and isinstance(totalList[i][0], circlingBomb) 
        and isinstance(totalList[i-1][0], circlingBomb)): 
        totalList.pop(i)
        
    else:
        i+= 1
        cx += random.uniform(app.width/(copyn*1.25), app.width/(copyn)) if copyn != 1 else random.uniform(app.width/(5), app.width/4)
    return i, cx

#**creates two drones with a bomb that moves between the two 
def sideToSideSetUp(cx, layer, shift, totalList, app, i,n, difficulty):
    drone1 = chooseDroneType(app, cx, layer + shift, app.droneWidth, app.droneWidth, random.uniform(0,10), difficulty)
    cx += random.uniform(app.width/(n*1.25), app.width/(n)) if n != 1 else random.uniform(app.width/(5), app.width/4)
    drone2 = chooseDroneType(app, cx, layer + shift, app.droneWidth, app.droneWidth, random.uniform(0,10), difficulty)
    leftbound = drone1.cx - 40
    rightbound = drone2.cx + 40
    sidebomb = sideToSideBomb((app.leftbound+app.rightbound)/2, layer + shift, app.droneWidth/2, leftbound, rightbound)
    
    pair = [drone1, drone2, sidebomb]
    totalList.append(pair)
    i+=1
    newn = n-1 
    cx += random.uniform(app.width/(n*1.25), app.width/(n))
    return i, cx, newn

#**taken from recursion review session, 15112
def flatten(L):
    if L == []:
        return []

    if type(L[0]) != list:
        return [L[0]] + flatten(L[1:])

    return flatten(L[0]) + flatten(L[1:])

#**choses the type of drone based on difficulty 
def chooseDroneType(app, cx, cy, width, height, randomNum, difficulty):

    if randomNum <= 1:
        option1Probability, option2Probability, option3Probability = getDroneTypeProbabilities(difficulty)

        if randomNum <  option1Probability:
            drone = ComboDrone(cx, cy, width, height)
            #adds a singular bomb
        elif randomNum < (option1Probability + option2Probability):
            drone = MissileDrone(cx, cy, width, height)
        elif randomNum < (option1Probability + option2Probability + option3Probability):
            drone = AngelDrone(cx, cy, width, height)
        else:
            drone = Drone(cx, cy, width, height)
    else:
        drone = Drone(cx, cy, width, height)
    return drone

#**helper function, gets probabilities for the types of drones
def getDroneTypeProbabilities(difficulty):
    #option1, combo
    #option2, missile
    #option3, extra life
    if difficulty == 1:
        option1Probability = 1/3
        option2Probability = 1/3
        option3Probability = 1/3

    elif difficulty == 2:
        option1Probability = 1/5
        option2Probability = 1/5
        option3Probability = 1/5

    else:
        option1Probability = 1/7
        option2Probability = 1/7
        option3Probability = 1/7
        
    return option1Probability, option2Probability, option3Probability

# ** gets the probabilities for the layout of the bombs/drones
def getLayoutProbabilities(difficulty):
    if difficulty == 1:
        option1Probability = 3/4
        option2Probability = 1/8
        option3Probability = 1/16
        option4Probability = 1/16

    elif difficulty == 2:
        option1Probability = 1/4
        option2Probability = 1/4
        option3Probability = 1/4
        option4Probability = 1/4

    else:
        option1Probability = 1/8
        option2Probability = 1/8
        option3Probability = 3/8
        option4Probability = 3/8
        
    return option1Probability, option2Probability, option3Probability, option4Probability

#**gets the probabilities for the number of drones/bombs in each layer
def getLayerProbabilities(app):
    if app.score >0:
        #difficulty level probability follows log function 
        probabilitychange = (6 * math.log2(app.score)) /100
        
        app.hardprobability = 0.1 + probabilitychange * 2/3
        app.mediumprobability = 0.3 + probabilitychange * 1/3
        app.easyprobability = 0.6 - probabilitychange

    
    randFloat = random.random()
    #sets difficulties and probability for the amount of bombs/drones in each layer
    if randFloat < app.hardprobability:
        difficulty = 3
        rowlen1probability = 1/8
        rowlen2probability = 1/8
        rowlen3probability = 3/8
        #rowlen4probability = 3/8

    elif randFloat <app.hardprobability + app.mediumprobability:
        difficulty = 2
        rowlen1probability = 1/4
        rowlen2probability = 1/4
        rowlen3probability = 1/4
        #rowlen4probability = 1/4
    elif randFloat <1:
        difficulty = 1
        rowlen1probability = 3/8
        rowlen2probability = 3/8
        rowlen3probability = 1/8
        #rowlen4probability = 1/8
    randomnumber = random.random()
    
    #finds bomb/drone size of the layer 
    if randomnumber <rowlen1probability:
        n = 1
    elif randomnumber <rowlen1probability + rowlen2probability:
        n =2 
    elif randomnumber <rowlen1probability + rowlen2probability + rowlen3probability:
        n = 3
    elif randomnumber<1:
        n = 4
    return difficulty, n