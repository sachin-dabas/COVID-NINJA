# battle of pathogens- 0.1
# testing initial functions for the design of game

###########################################
#TP-1
###########################################

# modes reference: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes

# import libraries
from cmu_112_graphics import *
import random
import math
from PIL import ImageTk, Image


import splashScreenMode
import Virus

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
    # canvas.create_image(200, 400, image=ImageTk.PhotoImage(app.image2))
    canvas.create_text(50,app.height-50,text = 'Score',fill = 'black')
    canvas.create_text(50,app.height-100,text = f'{app.score}',fill = 'black',font = app.font)
    # canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
    #                    fill=app.color)

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
    moveViruses(app)

# Main File
def appStarted(app):
    #define splash screen
    # app.mode = 'splashScreenMode'
    #load images for background
    #! app.image1 = app.loadImage('background.jpg')
    #! app.image2 = app.scaleImage(app.image1, 1.5)
    # initialize app score
    app.score = 0
    app.timerDelay = 40
    app.font = 'Arial 50 bold'
    # define virus and types
    app.virusShape = [
        [(0,-50),(-39,-31),(-49,11),(-22,45),(22,45),(49,11),(39,-31)],
        [(-50,0),(-35,30),(0,40),(35,30),(50,0),(35,-30),(0,-40),(-35,-30)],
        [(-50,0),(-35,30),(0,40),(35,30),(50,0),(35,-30),(0,-40),(-35,-30)],
                     ]
    app.virusType = [
        ['Bacteria'],
        ['Pathogen'],
        ['Virus'],
                    ]
    initVirus(app)
    app.dx = random.randint(6,12)
    app.dy = random.randint(12,24)

def initVirus(app):
    (f, outline) = getRandomVirus(app)
    app.viruses = [ ]

def getRandomVirus(app):
    i = random.randint(0,2)
    return(app.virusShape[i], app.virusType[i])

def moveViruses(app): #! create wave
    # app.y -= app.dy
    # if (app.x < 0) or (app.x > app.width): 
    #     app.dx  = -app.dx
    #     app.dy += app.dy
    # if (app.y < 0) or (app.y > app.height): 
    #     app.dy = -app.dy
    newViruses = []
    numFruits = 3
    for i in range(numFruits):
        (f, outline) = getRandomVirus(app)
        x = random.randint(int(app.width/6),int(app.width*(5/6)))
        dx,dy = float(random.randint(-app.width//10,app.width//10)), -float(random.randint(int(app.height*7/8),app.height))
        if(x < app.width/2):
            dx = abs(dx)
        else:
            dx = -abs(dx)
        newVirus = Virus.Virus(outline, (x,app.height), (dx,dy), f, True)
        newViruses.append(newVirus)

    app.viruses.extend(newViruses)


def drawVirus(app, canvas):
    for f in app.viruses:
        (cx, cy) = f.pos
        coords = Virus.localToGlobal(f.points, cx,cy)
        canvas.create_polygon(coords, fill='black',width=4)

# This runs the app
runApp(width=600, height=600)
