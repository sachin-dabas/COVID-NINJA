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

class Main(App):
    def appStarted(self):
        self.score = 0
        self.time = time.time()
        self.prevTime = time.time()
        self.time0 = time.time() #define time for last draw
        self.time1 = 3 # define the time between drawing of viruses
        self.num = 3 #initialize the number of drawing viruses in the beginning
        self.timerDelay = 1 
        # app.mode = 'splashScreenMode'
        #define the shape of viruses
        self.virusShape = [
                [(0,-25),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)],
                [(0,-50),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)],
                [(0,-75),(-40,-40),(-75,10),(-25,45),(25,45),(70,10),(40,-40)],
                        ]
        #define the types of viruses
        self.virusTypes = [
                        "bacteria",
                        "amoeba",
                        "ebola",
                        ]
        #define the colors of viruses
        self.virusColors = [ "red", "yellow", "magenta", "pink", "cyan", 
                            "green", "orange" ]                
        Main.initVirus(self)


    
    def initVirus(self):
        self.allViruses = [ ] #initialise empty list for viruses
        (type, shape) = Main.getRandomVirus(self)
        Main.virusesChain(self)

    #helper function for initVirus    
    def getRandomVirus(self):
        randomIndex = random.randint(0,2)
        return (self.virusTypes[randomIndex],self.virusShape[randomIndex])


    def timerFired(self):
        Main.takeStep(self)
       
    def takeStep(self):
        if((self.time - self.time0) > self.time1):
            #draw random num of viruses
            num = random.randint(1,5)
            Main.virusesChain(self,num)# make a chain of viruses
            self.time0 = time.time() #reset the time // this can be used in special mode 
        Main.moveVirus(self)
        
    def moveVirus(self):    
        for virus in self.allViruses:
            virus.move((time.time()-self.prevTime))
        self.prevTime = time.time()

    #helper function for virusesChain    
    def makeNewVirus(self,xvalue,dx,dy):
        virusesList = [ ]
        (type, shape) = Main.getRandomVirus(self)
        color = self.virusColors[random.randint(0,5)]
        newVirus = Virus(shape, (xvalue,self.height), (dx,dy), type, color)
        virusesList.append(newVirus)
        self.allViruses += virusesList

    #draw viruses in a loop
    def virusesChain(self,num=3):
        for i in range(num):
            val = random.randint(2,6)
            x = self.width//val
            dx = random.randint(-self.width//20, self.width//20)
            dy = -(random.randint(self.height//3,self.height))
            # drawing viruses on the screen
            if (x < self.width): 
                dx += dx
            else: dx = -dx
            #make new virus
            Main.makeNewVirus(self,x,dx,dy)

    def redrawAll(self, canvas):
        # splashScreen(app,canvas)
        canvas.create_image(200, 400, image=ImageTk.PhotoImage(self.image2))
        canvas.create_rectangle(0,0,self.width,self.height,fill='black')
        Main.drawViruses(self, canvas)
        Main.drawScore(self,canvas)

    def drawScore(app,canvas):
        margin = 100
        canvas.create_text(app.width-margin, margin, text= f"{app.score}",
                        font='Arial 60 bold', fill = "grey")

    def modifyCoordinates(self,points,cx,cy): #centroid coordinates to canvas
        result = copy.deepcopy(points)
        for coordinates in range(len(result)):
            (x,y) = result[coordinates]
            result[coordinates] = (x+cx, y+cy)
        return result

    def mousePressed(self,event):
        Main.bladeMouse(self, event)
        self.slice[0] = (event.x, event.y)

    def mouseReleased(self, event):
        pass

    def bladeMouse(self, event):
        if not self.mousePress:
            self.mousePress = True
            self.t0 = time.time()

    # access all viruses and create polygons
    def drawViruses(self, canvas):
        for virus in self.allViruses:
                (cx, cy) = virus.pos
                color = virus.color
                myCordinates = Main.modifyCoordinates(self,virus.myShape,cx,cy)
                canvas.create_polygon(myCordinates, fill=color,width=1)

    # clip function code copied from 
    # https://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping#Python
    
    def clip(subjectPolygon, clipPolygon):
        def inside(p):
            return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
        
        def computeIntersection():
            dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
            dp = [ s[0] - e[0], s[1] - e[1] ]
            n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
            n2 = s[0] * e[1] - s[1] * e[0] 
            n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
            return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
        
        outputList = subjectPolygon
        cp1 = clipPolygon[-1]
        
        for clipVertex in clipPolygon:
            cp2 = clipVertex
            inputList = outputList
            outputList = []
            s = inputList[-1]
        
            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e):
                    if not inside(s):
                        outputList.append(computeIntersection())
                        outputList.append(e)
                elif inside(s):
                    outputList.append(computeIntersection())
                s = e
            cp1 = cp2
        return(outputList)

class Virus(object):
    
    def splashScreen(self,canvas):
        canvas.create_text(self.width//2,self.height//2, text = "Battle of Pathogens",
                                font = 'Arial 24 bold', fill='white')
        canvas.create_text(self.width//2,self.height//2+100, text = "Press any key",
                                font = 'Arial 18 bold', fill='white')
    def __init__(self, shape, pos, speed, virusType, color): # newVirus = Virus(shape, (xvalue,self.height), (dx,dy), type)
        self.myShape = shape 
        self.pos = pos
        self.speed = speed
        self.VirusType = virusType
        self.grav = 600
        self.color = color

    def move(self, dt): #grav = pixels/frame, pre-calculated
        dx, dy = self.speed
        x,y = self.pos
        self.pos = (x+dx*dt, y+dy*dt) #!change position based on velocity
        self.speed = (dx, dy+(self.grav)*dt) #!gravitational acceleration









#inheritance
class Bacteria(Virus):
    def __init__(self, points, pos, speed, virusType):
        self.points = [(0,-25),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)]

class amoeba(Virus):
    def __init__(self, points, pos, speed, virusType):
        self.points = [(0,-50),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)]

class ebola(Virus):
    def __init__(self, points, pos, speed, virusType):
        self.points = [(0,-75),(-40,-40),(-75,10),(-25,45),(25,45),(70,10),(40,-40),]

Main(width=1100, height=800)

# # splashScreenMode
# def splashScreenMode_redrawAll(app,canvas):
#     canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
#                              font = 'Arial 24 bold', fill='brown')
#     canvas.create_text(app.width//2,app.height//2+100, text = "Press any key",
#                              font = 'Arial 18 bold', fill='brown')

# def splashScreenMode_keyPressed(app,event):
#     app.mode = not app.mode