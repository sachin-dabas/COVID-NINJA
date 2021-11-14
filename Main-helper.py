# battle of pathogens- 0.1
# testing initial functions for the design of game

###########################################
#! I.  drawViruses
#! II. change score when cliking
###########################################

# modes and structure of code reference - https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes

# import libraries
from cmu_112_graphics import *
import random
import math

# splashScreenMode
def splashScreenMode_redrawAll(app,canvas):
    canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
                             font = 'Arial 25 bold', fill='brown')
    canvas.create_text(app.width//2+ 100,app.height//2+100, text = "Press Enter",
                             font = 'Arial 12 bold', fill='brown')

def splashScreenMode_keyPressed(app,event):
    # if event.key == 'h':
    app.mode = 'gameMode'

# gameMode
def gameMode_redrawAll(app,canvas):
    canvas.create_text(app.height-100,30,text = f'{app.score}',fill = 'black')
    canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
                       fill=app.color)
    canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
                       fill=app.color)

def gameMode_mousePressed(app, event):
    # distance between 
    d = math.sqrt((app.x - event.x)**2 + (app.y - event.y)
            **2)
    if (d <= app.r):
        app.score += 1
        initVirus(app)
    elif (app.score > 0):
        app.score -= 1

def gameMode_timerFired(app):
    moveVirus(app)

# Main File
def appStarted(app):
    app.mode = 'splashScreenMode'
    # app.mode = 'gameMode'
    app.score = 0
    app.timerDelay = 50
    app.virusShape = [
                    [20,20,10,'red'],
                    [30,40,20,'green'],
                    [60,60,40,'pink']
                     ]
    # from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
    app.dx = random.randint(6,12)
    app.dy = random.randint(6,12)
    initVirus(app)
    # app.dx = random.choice([+1,-1])*random.randint(3,6)
    # app.dy = random.choice([+1,-1])*random.randint(3,6)

def initVirus(app):
    shape = getRandomVirus(app)
    (app.x,app.y,app.r,app.color) = (shape[0],shape[1],shape[2],shape[3])

def getRandomVirus(app):
    n = random.randint(0,2)
    return(app.virusShape[n])

def moveVirus(app):
    app.x += app.dx
    if (app.x < 0) or (app.x > app.width): 
        app.dx = -app.dx
        app.dy += app.dy
    if (app.y < 0) or (app.y > app.height): 
        app.dy = -app.dy

# This runs the app
runApp(width=600, height=600)













