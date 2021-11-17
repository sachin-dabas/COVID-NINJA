# Battle of pathogens- 1.0
# testing initial functions for the design of game

###################################################
# TP-01
###################################################

# import libraries
import math
import time
import random
from PIL import ImageTk, Image
from cmu_112_graphics import *

def splashScreen(app,canvas):
    canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
                             font = 'Arial 24 bold', fill='white')
    canvas.create_text(app.width//2,app.height//2+100, text = "Press any key",
                             font = 'Arial 18 bold', fill='white')

def appStarted(app):
    app.score = 0
    app.lastWave = time.time()
    app.timeBetweenWaves = 3
    app.num = 3
    app.timerDelay = 1
    app.prevTime = time.time()
    app.virusShape = [
            [(0,-25),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)],
            [(0,-50),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)],
            [(0,-50),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40),],
                    ]
    app.virusTypes = [
                    "bacteria",
                    "amoeba",
                    "ebola",
                    ]
    initVirus(app)
    # app.mode = 'splashScreenMode'

def getVirus(app):
    i = random.randint(0,2)
    return (app.virusTypes[i],app.virusShape[i])

def initVirus(app):
    app.virus = []
    (f, shape) = getVirus(app)
    waveViruses(app)
    app.sliced = False
    app.grav = 600

def waveViruses(app,num=3):
    for i in range(num):
        xCoord = random.randint(int(app.width/6),int(app.width*(5/6))) #!change logic
        dx,dy = float(random.randint(-app.width//10,app.width//10)), -float(random.randint(int(app.height*7/8),app.height)) #!change logic
        # drawing viruses on the screen
        if (xCoord < app.width): 
            dx += dx
        else: dx = -dx
        makeNewVirus(app,xCoord,dx,dy)

def makeNewVirus(app,xCoord,dx,dy):
    virusesList = [ ]
    (type, shape) = getVirus(app)
    newVirus = Virus(shape, (xCoord,app.height), (dx,dy), type, True)
    virusesList.append(newVirus)
    app.virus.extend(virusesList)

def mousePressed(app, event):
    start = (event.x, event.y)

def mouseReleased(app, event):
    app.mousePress = False

def timerFired(app):
    doStep(app)       
            
def doStep(app):
    if((time.time() - app.lastWave) > app.timeBetweenWaves):
        #draw random num of viruses
        i = random.randint(1,5)
        app.num = i + app.score//30
        if(app.num > 8):
            app.num = 8
        waveViruses(app,app.num)
        app.lastWave = time.time()
    for f in app.virus:
        f.move(app.grav, (time.time()-app.prevTime))
    app.prevTime = time.time()

def redrawAll(app, canvas):
    splashScreen(app,canvas)
    drawBackdrop(app,canvas)
    drawViruses(app, canvas)
    drawScore(app,canvas)

def drawScore(app,canvas):
    margin = 100
    canvas.create_text(app.width-margin, margin, text= f"{app.score}",
                     font='Arial 60 bold', fill = "grey")

def drawBackdrop(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')

def drawViruses(app, canvas):
    for f in app.virus:
        (cx, cy) = f.pos
        coords = localToGlobal(f.points,cx,cy)
        canvas.create_polygon(coords, fill='red',width=1)

def globalToLocal(points,cx,cy): #canvas coordinates to centroid
    result = copy.deepcopy(points)
    for i in range(len(result)):
        (x,y) = result[i]
        result[i] = (x-cx, y-cy)
    return result

def localToGlobal(points,cx,cy): #centroid coordinates to canvas
    result = copy.deepcopy(points)
    for i in range(len(result)):
        (x,y) = result[i]
        result[i] = (x+cx, y+cy)
    return result

class Virus(object):
    def __init__(self, points, pos, vel, virusType, uncut):
        self.points = points
        self.pos = pos
        self.vel = vel
        self.VirusType = virusType
        self.uncut = uncut

    def move(self, grav, dt): #grav = pixels/frame, pre-calculated
        dx, dy = self.vel
        x,y = self.pos
        self.pos = (x+dx*dt, y+dy*dt) #!change position based on velocity
        self.vel = (dx, dy+grav*dt) #!gravitational acceleration

runApp(width=1100, height=800)


# # splashScreenMode
# def splashScreenMode_redrawAll(app,canvas):
#     canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
#                              font = 'Arial 24 bold', fill='brown')
#     canvas.create_text(app.width//2,app.height//2+100, text = "Press any key",
#                              font = 'Arial 18 bold', fill='brown')

# def splashScreenMode_keyPressed(app,event):
#     app.mode = not app.mode