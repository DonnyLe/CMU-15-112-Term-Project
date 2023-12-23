import math
import random

class Button():
    def __init__(self, cx, cy, width, height, text, color):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
        self.text = text
        self.color = color

    def isPressed(self, mouseX, mouseY):
        return (mouseX >= self.cx - self.width and mouseX <= self.cx + self.width
                and mouseY >= self.cy - self.height and mouseY <= self.cy + self.height)

        
    def drawButton(self,canvas):
        canvas.create_rectangle(self.cx - self.width, self.cy-self.height, self.cx + self.width, self.cy+self.height
                                , fill=self.color)
        canvas.create_text(self.cx, self.cy, text=self.text, fill="white", font="Arial 15 bold")

#parent class
class gameObjects():
    def __init__(self, cx, cy, width, height):
        self.cx = cx
        self.cy = cy
        self.width = width/2
        self.height = height/2
        self.alreadyInteracted = False
        #used for recommended path
        self.futurecx = cx
        self.futurecy = cy
        
    
    def move(self, dx, dy):
        self.cx += dx
        self.cy += dy
        self.futurecx = self.cx
        self.futurecy = self.cy
        hitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(hitboxCharacter)]
        #updates hitboxes
        hitboxCharacter = (self.cx, self.cy, self.width)
        self.hitboxes = [(hitboxCharacter)]
    
    #used for recommended path
    def moveFuture(self, dx, dy):
        self.futurecx += dx
        self.futurecy += dy
        #updates hitboxes
        hitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(hitboxCharacter)]
        
    
    def objectsIntersects(self, other, app):
        for characterCircle in other.hitboxes:
            for circles in self.hitboxes:
                cx0, cy0, r0 = circles
                cx1, cy1, r1 = characterCircle
                if (circlesIntersect(cx0, cy0, r0, cx1, cy1, r1)==True
                    ):
                    return True 
        return False

    #used for recommended path
    def objectsIntersectsFuture(self, other, app):
        for characterCircle in other.futureHitboxes:
            for circles in self.futureHitboxes:
                cx0, cy0, r0 = circles
                cx1, cy1, r1 = characterCircle
                if (circlesIntersect(cx0, cy0, r0, cx1, cy1, r1)==True
                    ):
                    return True
        
        return False
                
    #draws hitboxes
    def drawHitboxes(self, canvas):
        for hitbox in self.hitboxes:
            cx, cy, r = hitbox
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="green", width = "3")

class Drone(gameObjects):
    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy, width, height)
        hitboxCharacter = (self.cx, self.cy, self.width)
        #list of circles to fill up model
        self.hitboxes = [(hitboxCharacter)]
        self.dyFallingDrone = 0
        hitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(hitboxCharacter)]
        self.isRecommendedPath = False

    def drawDrone(self, canvas, app, color):
        #**temp
        if(self.alreadyInteracted):
            self.fallingAnimation(app)
        canvas.create_oval(self.cx - self.width, self.cy - self.height,
                                self.cx + self.width, self.cy + self.height,
                                fill=color)
    def drawPath(self, app, canvas):
        if self.isRecommendedPath == True:
            canvas.create_text(self.cx, self.cy, anchor='c',font="Arial 20 bold", text="Click Here")
    def fallingAnimation(self, app):
        self.dyFallingDrone += app.gravity
        super().move(0, self.dyFallingDrone)
        
    #checks if mouse clicks register on drone
    def isClicked(self, app):
        if (abs(app.mouseX - self.cx) <= self.width and
           abs(app.mouseY - self.cy) <= self.height
           and not self.alreadyInteracted
           ):
           return(True) 
        else:
            return (False)

class AngelDrone(Drone):
    def objectsIntersects(self, other, app):
        if super().objectsIntersects(other, app) and not self.alreadyInteracted:
            app.extraLife = True     
            app.charactercolor = "yellow"
            return True
    def drawDrone(self, canvas, app, color):
        #**temp
        super().drawDrone(canvas, app, "yellow")

class MissileDrone(Drone):
    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy, width, height)
        self.missileList = []
        self.loopChance = random.random()
        

    def missileLaunch(self, app):
        for bomblist in app.allBombList:
            for bomb in bomblist:
                missile = Missile(self.cx, self.cy, 15, 10, bomb)
                self.missileList.append(missile)
                
    def drawDrone(self, canvas, app, color):
        #**temp
        super().drawDrone(canvas, app, "orange")

    
class Missile(gameObjects):
    def __init__(self, cx, cy, width, height, bomb):
        super().__init__(cx, cy, width, height)
        self.negativeDx = 1
        self.negativeDy = 1
        self.dx = 0
        self.dy = 0 
        self.theta = None
        self.slope = None
        self.targetBomb = bomb
        self.velocity = 5
        self.foundBomb = False

    def trackBomb(self):
        bombcx, bombcy = self.targetBomb.cx, self.targetBomb.cy
        self.slope, self.negativeDx, self.negativeDy = calculateSlope(bombcx, bombcy, self.cx, self.cy, 
                                        self.negativeDx, self.negativeDy)
        self.theta = (self.slope)
        self.dx, self.dy = calculateVelocityComponents(self.theta, self.velocity, 
                                        self.negativeDx, self.negativeDy)
        
        self.move(self.dx, self.dy)
        app = None
        if self.objectsIntersects(self.targetBomb, app):
            self.targetBomb.exploded = True
            self.foundBomb = True

        
    def drawMissile(self, canvas):
        # rotatePolygon(self.width, self.theta, self.cx-self.height, self.cy, self.cx+self.height, self.cy)
        canvas.create_rectangle(self.cx-self.width, self.cy-self.width, self.cx+self.width, self.cy+self.height)

class ComboDrone(Drone):
    def objectsIntersects(self, other, app):
        if super().objectsIntersects(other, app) and not self.alreadyInteracted:
            app.combo += 1
            app.comboBoolean = True
            return True 
    def drawDrone(self, canvas, app, color):
            #**temp
            super().drawDrone(canvas, app, "green")

#sub class of gameObjects
class Character(gameObjects):
    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy, width, height)
        hitboxCharacter = (self.cx, self.cy, self.width)
        #list of circles to fill up model
        self.hitboxes = [(hitboxCharacter)]
        futurehitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(futurehitboxCharacter)]

    def move(self, dx, dy, app):
        #vertical-screen scrolling
        if(self.cy) <= app.scrollMargin and dy<0:
            app.scrollY = dy - 1 
            dy = 0
            super().move(dx, dy)
        else:
            #stops scrolling
            app.scrollY = 0
            super().move(dx, dy)

    # def moveFuture(self, dx, dy, app):
    #     #vertical-screen scrolling
    #     if(self.futurecy) <= app.scrollMargin and dy<0:
    #         app.futureScrollY = dy - 1
    #         dy = 0
    #         super().moveFuture(dx, dy)
    #     else:
    #         #stops scrolling
    #         app.futureScrollY = 0
    #         super().moveFuture(dx, dy)

    def drawCharacter(self, canvas, color):
        #**temp
        canvas.create_rectangle(self.cx - self.width, self.cy - self.height,
                                self.cx + self.width, self.cy + self.height,
                                fill = color)
    #draws circle where combos are registered
    def drawComboCircle(self, canvas, app):
        canvas.create_oval(self.cx - app.comboRadius-self.width, self.cy - app.comboRadius-self.width,
                                self.cx + app.comboRadius+self.width, self.cy + app.comboRadius+self.width
                                ,outline = "blue", width = 3
                                )

#sub class of gameObjects
class Bomb(gameObjects):
    def __init__(self, cx, cy, r ):
        super().__init__(cx, cy, r*2, r*2)
        #temporary hitboxes
        hitboxBomb1 = (self.cx, self.cy, self.width)
        self.hitboxes = [(hitboxBomb1)]
        #one bomb can only give one combo 
        self.comboTaken = False
        #player needs to be in the combo radius for 150 ms
        self.nearMissTime = 0
        self.theta = 0
        self.exploded = False
        hitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(hitboxCharacter)]
        

    def drawBomb(self, canvas):
        canvas.create_oval(self.cx - self.width, self.cy  - self.height,
                      self.cx + self.width, self.cy + self.height, fill = "red")
    
    #checks near misses
    def nearMiss(self,other, app):
        if not self.comboTaken:
            cx0, cy0,r0 = self.cx, self.cy, self.width
            cx1, cy1, r1= other.cx, other.cy, other.width
            distance = distanceFormula(cx0, cy0,r0, cx1, cy1, r1)
            if distance  -r0 - r1 <= app.comboRadius:
                return True 

    def drawExplosion(self, canvas, app):
        pass

class circlingBomb(Bomb):
    def __init__(self, cxsmall, cysmall, r, initialTheta, direction, cxlarge,cylarge, app):
        super().__init__(cxsmall, cysmall, r)
        self.tempcx = self.cx
        self.tempcy = self.cy
        self.theta = initialTheta
        self.direction = direction
        self.cxlarge = cxlarge
        self.cylarge = cylarge
        self.futurecx, self.futurecy = self.cx, self.cy
        self.futureTheta = self.theta

    def circle(self, radius, dtheta):
        
        self.theta +=  dtheta * self.direction
        newposX = radius * math.cos(math.radians(self.theta)) + self.cxlarge
        newposY = radius *  math.sin(math.radians(self.theta)) + self.cylarge
        self.cx = newposX
        self.cy = newposY
        self.futurecx = newposX
        self.futurecy = newposY

        hitboxBomb1 = (self.cx, self.cy, self.width)
        self.hitboxes = [(hitboxBomb1)]

        hitboxCharacter = (self.futurecx, self.futurecy, self.width)
        self.futureHitboxes = [(hitboxCharacter)]
    
    #used for recommended path
    def circleFuture(self, radius, dtheta):
        self.futureTheta +=  dtheta * self.direction
        newposX = radius * math.cos(math.radians(self.futureTheta)) + self.cxlarge
        newposY = radius *  math.sin(math.radians(self.futureTheta)) + self.cylarge
        self.futurecx = newposX
        self.futurecy = newposY


    def move(self, dx, dy):
        super().move(dx, dy)
        
        self.cxlarge += dx
        self.cylarge += dy
        
class sideToSideBomb(Bomb):
    def __init__(self, cx, cy, r, leftbound, rightbound):
        self.leftbound = leftbound
        self.rightbound = rightbound
        self.leftboundBool = False
        self.rightBoundBool = False
        self.sideToSideDX = -2
        self.leftboundFuture = leftbound
        self.leftboundBoolFuture = False
        self.rightboundFuture = rightbound
        self.rightboundBoolFuture = False
        self.sideToSideDXFuture = -2
        super().__init__(cx, cy, r) 
    
    def sideToSideMovement(self):
        if self.cx <= self.leftbound and self.leftboundBool == False:
            self.leftboundBool = True
            self.rightboundBool = False
            self.sideToSideDX = -self.sideToSideDX

        if self.cx >= self.rightbound and self.rightboundBool == False:
            self.leftboundBool = False
            self.rightboundBool = True
            self.sideToSideDX = -self.sideToSideDX
        super().move(self.sideToSideDX, 0)
    
    #used for recommended path
    def sideToSideFuture(self):
        if self.futurecx <= self.leftboundBoolFuture and self.leftboundBoolFuture == False:
            self.leftboundBoolFuture  = True
            self.rightboundBoolFuture = False
            self.sideToSideDXFuture  = -self.sideToSideDXFuture 

        if self.futurecx >= self.rightboundFuture and self.rightboundBoolFuture == False:
            self.leftboundBoolFuture = False
            self.rightboundBoolFuture = True
            self.sideToSideDXFuture  = self.sideToSideDXFuture 
        super().moveFuture(self.sideToSideDXFuture, 0)
        

def circlesIntersect(cx0, cy0, r0, cx1, cy1, r1):
    distance = distanceFormula(cx0, cy0, r0, cx1, cy1, r1)
    if distance <= (r0 + r1):
        return True 
    return False

def distanceFormula(cx0, cy0, r0, cx1, cy1, r1):
    return ((cx0 - cx1)**2 + (cy0 - cy1)**2)**0.5

#calculates slope, helper function
def calculateSlope(x0, y0, x1, y1, negativeDx, negativeDy):
    #**used to correct directions with negative and positive slopes
    #positive, positive
    if(y1-y0>=0 and x1-x0>=0):
        negativeDx = -1
        negativeDy = -1
    #negative, negative
    elif(y1-y0 < 1 and x1-x0<1):
        negativeDx = 1
        negativeDy = 1
    #positive, negative
    elif(y1-y0 >= 0 and x1-x0<1):
        negativeDx = 1
        negativeDy = 1
    elif(y1-y0 < 1 and x1-x0>0):
        negativeDx = -1
        negativeDy = -1
    if(x1-x0!=0):
        return (y1-y0)/(x1-x0), negativeDx, negativeDy
    return None, negativeDx, negativeDy

def calculateVelocityComponents(theta, velocity, negativeDX, negativeDY):
    dx =  math.cos(theta)*velocity * negativeDX
    dy = math.sin(theta)*velocity * negativeDY
    return dx, dy

def calculateTheta(slope):
    if slope == None:
        theta = math.pi/2
    else:
        theta =(math.atan(slope))
    return theta 

def rotatePolygon(r, theta, cx0, cy0, cx1, cy1):
    xprime0, yprime0 = r * math.cos(theta+math.pi/4) + cx0, r * math.sin(theta+math.pi/4) + cy0
    xprime1, yprime1 = r * math.cos(theta-math.pi/4) + cx0, r * math.sin(theta-math.pi/4) + cy0
    xprime2, yprime2 = r * math.cos(theta+math.pi/4) + cx1, r * math.sin(theta+math.pi/4) + cy1
    xprime3, yprime3 = r * math.cos(theta-math.pi/4) + cx1, r * math.sin(theta-math.pi/4) + cy1
    return xprime1, yprime1, xprime0, yprime0, xprime2, yprime2, xprime3, yprime3

