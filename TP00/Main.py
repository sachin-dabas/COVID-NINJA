# battle of pathogens- 0.1
# testing initial functions for the design of game

###########################################
#! I.  drawViruses
#! II. change score when clicking
###########################################

# modes reference- https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes

# import libraries
from cmu_112_graphics import *
import random
import math
from PIL import ImageTk, Image

# splashScreenMode
def splashScreenMode_redrawAll(app,canvas):
    canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
                             font = 'Arial 24 bold', fill='brown')
    canvas.create_text(app.width//2,app.height//2+100, text = "Press any key",
                             font = 'Arial 18 bold', fill='brown')

def splashScreenMode_keyPressed(app,event):
    app.mode = 'gameMode'

# gameMode
def gameMode_redrawAll(app,canvas):
    canvas.create_image(200, 400, image=ImageTk.PhotoImage(app.image2))
    canvas.create_text(app.height-75,30,text = 'Score',fill = 'black')
    canvas.create_text(app.height-75,50,text = f'{app.score}',fill = 'black')
    canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
                       fill=app.color)

def gameMode_mousePressed(app, event):
    # calculate distance 
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
    app.image1 = app.loadImage('background.jpg')
    app.image2 = app.scaleImage(app.image1, 1.5)
    app.score = 0
    app.timerDelay = 40
    app.virusShape = [
                    [20,20,10,'red'],
                    [100,40,20,'green'],
                    [60,60,40,'pink']
                     ]
    initVirus(app)
    app.dx = random.randint(6,12)
    app.dy = random.randint(12,24)
    # app.dx = random.choice([+1,-1])*random.randint(3,6)
    # app.dy = random.choice([+1,-1])*random.randint(3,6)

def initVirus(app):
    shape = getRandomVirus(app)
    (app.x,app.y,app.r,app.color) = (shape[0],shape[1],shape[2],shape[3])

def getRandomVirus(app):
    n = random.randint(0,2)
    return(app.virusShape[n])

def moveVirus(app):
    app.y -= app.dy
    if (app.x < 0) or (app.x > app.width): 
        app.dx  = -app.dx
        app.dy += app.dy
    if (app.y < 0) or (app.y > app.height): 
        app.dy = -app.dy


# This runs the app
runApp(width=600, height=600)
