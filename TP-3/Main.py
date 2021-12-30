'''COVID NINJA''' 
###############################################################################

''' Cover image taken from bing (and edited personally on Photoshop)
https://www.bing.com/images/search?view=detailV2&ccid=pUrYWey2&id=B706F414EB2C3
873E55BFA336A1E2979552FE8D1&thid=OIP.pUrYWey2Rx0svFO195b-NAHaEo&mediaurl=https%
3a%2f%2fth.bing.com%2fth%2fid%2fR.a54ad859ecb6471d2cbc53b5f796fe34%3frik%3d0egv
VXkpHmoz%252bg%26riu%3dhttp%253a%252f%252f2.bp.blogspot.com%252f-jvm5wL4m_mo%25
2fT5Jr7gTe5PI%252fAAAAAAAAACo%252fe33DxJ-Z0gk%252fs1600%252ffruit-ninja_1.jpg%2
6ehk%3dnnjLTlkP3P1%252fgUC5t52t6j7sbf6JQjLpDSyauYUkNTQ%253d%26risl%3d%26pid%3dI
mgRaw%26r%3d0%26sres%3d1%26sresct%3d1%26srh%3d800%26srw%3d1280&exph=480&expw=76
8&q=fruit+ninja&simid=608031218792727351&FORM=IRPRST&ck=CA92AE3BDB92847A9F21D34

39A5FC0B0&selectedIndex=6&ajaxhist=0&ajaxserp=0 '''

'''Mode image taken from bing (and edited personally on Photoshop)
https://www.bing.com/images/search?view=detailV2&ccid=aJ2MaPsX&id=A5481DC0484A5
8528076FEFF7F748F334292D541&thid=OIP.aJ2MaPsXq6c-EILftGcJdAHaDm&mediaurl=https%
3a%2f%2fimag.malavida.com%2fmvimgbig%2fdownload-fs%2ffruit-ninja-15259-1.jpg&cd
nurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.689d8c68fb17aba73e1082dfb4670974%3
frik%3dQdWSQjOPdH%252f%252f%252fg%26pid%3dImgRaw%26r%3d0&exph=1080&expw=2220&q=
fruit+ninja&simid=608042162368960310&FORM=IRPRST&ck=0C32777AC889BF4D2FDEEC0D11E
20650&selectedIndex=76&ajaxhist=0&ajaxserp=0
'''

'''Game background image taken from bing (and edited personally on Photoshop)
https://www.bing.com/images/search?view=detailV2&ccid=YcLAz9k6&id=79A4FD5F8CEBB
262BEC8FFE7B90E2069142117C8&thid=OIP.YcLAz9k6UnM-kPuZ5AdUXQHaEK&mediaurl=https%
3a%2f%2fth.bing.com%2fth%2fid%2fR.61c2c0cfd93a52733e90fb99e407545d%3frik%3dyBch
FGkgDrnn%252fw%26riu%3dhttp%253a%252f%252fwww.droid-life.com%252fwp-content%252
fuploads%252f2010%252f09%252ffruit-ninja1.png%26ehk%3d7ho8YX%252b5vzOmASCPMTGS8
vdPsCqzv6FQFrrFWSurv28%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=480&expw=854&
q=fruit+ninja&simid=608051748735947434&FORM=IRPRST&ck=84BD978DE4B14CA39E18FEAE9
605E0C1&selectedIndex=110&ajaxhist=0&ajaxserp=0
'''
###############################################################################

'''All the Graphics and Animations reference: 
https://www.cs.cmu.edu/~112/'''

'''Slicing Reference:
https://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping#Python
https://en.wikipedia.org/wiki/Sutherland%E2%80%93Hodgman_algorithm
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
http://kuanbutts.com/2020/07/07/subdivide-polygon-with-linestring/
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
https://www.geeksforgeeks.org/find-the-centroid-of-a-non-self-intersecting-closed-polygon/
'''
'''Game style and featutes reference (using pygame)
https://data-flair.training/blogs/fruit-ninja-game-python/?ref=morioh.com&utm_source=morioh.com'''

'''
AI and Open CV reference:
https://www.cs.cmu.edu/~112/schedule.html
https://github.com/LupascuAndrei/fruit_ninja_ai
'''

'''
Threading & subprocessing references:
https://www.includehelp.com/python/thread-is_alive-method-with-example.aspx
https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
https://stackoverflow.com/questions/24855335/understanding-thread-jointimeout
https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
https://stackoverflow.com/questions/24855335/understanding-thread-jointimeout
https://www.bogotobogo.com/python/Multithread/python_multithreading_Event_Objects_between_Threads.php
https://stackoverflow.com/questions/18485098/python-threading-with-event-object
https://www.geeksforgeeks.org/method-overriding-in-python/
https://stackoverflow.com/questions/62172227/how-to-close-subprocess-in-python
https://docs.python.org/3/library/subprocess.html
https://cmsdk.com/python/start-and-terminate-subprocess-from-python-function.html


'''

# Import Standard Libraries
import math
import time
import random
from PIL import ImageTk, Image
from cmu_112_graphics import *
from AI import AiCutter

# import other Python files
from clipFunction import *
from polygonCentroid import *
from Point import *
from Viruses import *
from SpecialItems import *
from Effects import *
import threading

RunAiThread = False
Screenshot = None

class AiThread(threading.Thread):
    def __init__(self, threadId, snapShotCallable, runThread):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.snapShot = snapShotCallable
        self.aicutter = AiCutter()
        self.runThread = runThread

    def run(self):
        try:
            # while RunAiThread:
            while self.runThread.is_set():
                # perform some action
                Screenshot = self.snapShot()
                if Screenshot is not None:
                    #print("cutting screeshot in AI mode")
                    self.aicutter.aiVirusCut(Screenshot)
                    # clear screen shot after cutting
                    Screenshot = None
                time.sleep(0.1)
                print("runThread=", self.runThread.isSet())
        except Exception as e:
            print("encountered exception in AiThread:\n", e)


# Main Function that runs game
class Main(App): 
    def appStarted(self):
        #game modes 
        self.gameMode = None
        self.runbackground = False
        self.level = 1
        self.globalID = 0
        self.inGame = False
        self.isnotLastLevel = True
        self.slice = False
        self.timerDelay = 100 #200
        self.mouseMovedDelay = 50
        self.useCachedImages = False
        self.aicutter = AiCutter()
        self.sliceAir = False

        #sounds
        self.gameStartSound = False
        self.gameMusic = False
        self.gameMusicStarted = False
        self.gameOverNum = 0

        # used for score
        self.score = 0
        self.difficulty = None
        self.accuracy = 0
        self.totalDrawnViruses = 0
        self.myLevelViruses = 0

        #record for previous slices
        self.cutResult1 = tuple()
        self.cutResult2 = tuple()
        self.cutResult3 = tuple()
        self.cutResult4 = tuple()
        self.cutResult5 = tuple()
        self.mySlices = [ ]
        self.comboSlicingActivated = False

        # keeps track of how many times user misses the target
        self.hits = 0
        self.totalHits = 0
        self.totalDrawnViruses = 0
        self.misses = 0

        # initialize the number of drawing viruses in the beginning
        self.num = 3 

        # initialize the knife time
        self.knife = [ ]
        self.knifeCurrentTime = [ ]
        self.knifeTime0 = 0
        self.knifeTime1 = 150
        self.mousePress = False
        
        #define game levels
        self.currentLevel = 1
        #define game over
        self.planetIsSafe = False

        #initializes game mode buttons
    #ORIGINAL MODE
        self.ox = self.width//2-20 #magic numbers based on background image position
        self.oy = self.height-550
        self.r1 = 175
    #BONUS MODE
        self.bx = self.width//2-650 #magic numbers based on background image position
        self.by = self.height-350
        self.r2 = 120
    #AI MODE
        #magic numbers based on background image position
        self.ax = self.width-325 
        self.ay = self.height-350
        self.r3 = 120

    # cover image
        # all images cited above
        self.image1 = self.loadImage('cover.jpg')
        self.image2 = self.scaleImage(self.image1,0.5)
        # menu image
        # self.image3 = self.loadImage('secondscreen.jpg')
        self.image3 = self.loadImage('menu.png')
        self.image4 = self.scaleImage(self.image3,0.5)
        # game play image

        self.image5 = self.loadImage('Artboard 2.png')
        self.image6 = self.scaleImage(self.image5,0.5)
        self.hitBomb = 0

        self.runAiThread = threading.Event()
        self.aiThread = None
        self.reset()

# reset the game 
# & clear the canvas after each level
    def reset(self):
        self.time = 15
        self.timer = self.time
        self.health = 3
        self.totalhealth = 0
        self.isPaused = False
        self.gameOver = False
        self.exit = False
        self.comboReset = False
        
        # used for tracking time
        self.prevTime = time.time()
        self.time0 = time.time() # define time for last draw
        # define the time between drawing of viruses
        self.time1 = 3 
        self.timePassed = 0
        #kill all and save the world
        self.virusInWorld = time.time() 

        #initialise empty list for viruses
        self.allViruses = [ ]

        if self.aiThread:
            RunAiThread = False
            self.aiThread.join()
            self.aiThread = None

# define the difficulty of the game 
    # difficulty level 1 based on user performance
    def level1(self):
        self.time1 = 5
        if self.hitBomb < 2:
            if (self.timer < 20) or (self.accuracy > 80):
                self.timerDelay = 25

    #difficulty level 2 based on user performance
    def level2(self):
        self.time1 = 3
        # status of game is not game over
        if self.hitBomb < 3:
            if self.timer < 20 or self.accuracy > 70:
                self.timerDelay = 20
    
    #difficulty level 3 based on user performance
    def level3(self):
        self.time1 = 1
        # status of game is not game over
        if self.hitBomb < 4:
            if self.timer < 20 or self.accuracy > 60:
                self.timerDelay = 10

#function to choose virus based on levels 
    def chooseViruses(self, pos, speed, sliced, globalID):
        totalVirus = [ ]
        # draw viruses based on levels
        if self.currentLevel == 1:
            newVirus = self.randomVirus(pos, speed, sliced, globalID)
            totalVirus += [newVirus]
        elif(self.currentLevel == 2):
            newVirus1 = self.randomVirus(pos, speed, sliced, globalID)
            newVirus2 = self.randomVirus(pos, speed, sliced, globalID)
            totalVirus += [newVirus1]
            totalVirus += [newVirus2]
        elif self.currentLevel == 3:
            newVirus1 = self.randomVirus(pos, speed, sliced, globalID)
            newVirus2 = self.randomVirus(pos, speed, sliced, globalID)
            newVirus3 = self.randomVirus(pos, speed, sliced, globalID)
            totalVirus += [newVirus2]
            totalVirus += [newVirus3]
        return totalVirus

#function to choose virus based on levels 
    def randomVirus(self, pos, speed, sliced, globalID):
        # call random viruses
        allViruses = self.makeVirus(pos, speed, sliced, globalID)
        # define the logic behind drawing viruses
        weight = self.virusPhysics() 
        randomVirusSelection = random.choices(allViruses, weights= weight, k=1)[0]
        return randomVirusSelection

#Game modes
    '''Original mode runs on number of lives
        Watch mode runs automatically by AI'''

#game is won if health is 0 
# or if player is on last level
    def originalModeRandom(self):
        if self.health <= 0 or self.isnotLastLevel == False:
            self.gameOver = True 
            if self.gameOverNum == 0:
                gameOverSound.play()
                self.gameOverNum += 1 
        if self.health > 0 and (self.level or self.currentLevel) == 3:
            self.isnotLastLevel = False
            self.timePassed += 1
        # if self.health > 0 and self.timePassed > 0 and self.inGame == True:
        #     self.takeStep()

#AI Mode with implemented threading
    def AIModeRandom(self):
        try:
            global RunAiThread
            if self.exit == True:
                print("exiting game")
                RunAiThread = False
                self.runAiThread.clear()
                print("waiting for AI thread to close...")
                self.aiThread.join(timeout=2)
                if self.aiThread.is_alive():
                    print("AiThread timedout...")
                else:
                    print("AiThread closed...")
                # if self.aiThread:
                #     print("waiting for AI thread to close...")
                #     self.aiThread.join()
                print("closing game...")
                self.gameOver = True
            else: 
                # if RunAiThread == False:
                if not self.runAiThread.is_set():
                    print("starting AI thread")
                    RunAiThread = True
                    self.runAiThread.set()
                    self.aiThread = AiThread(1, self.getSnapshot, self.runAiThread)
                    self.aiThread.start()
                self.takeStep()
                # screenCapture = self.getSnapshot()
                # self.aicutter.aiVirusCut(screenCapture)
                self.timePassed += 1
        except Exception as e:
            print("encountered exception in AIModeRandom:\n", e)

# # quit the program & testing (left print statements on purpose)
#     def quit(self):
#         self.runAiThread.clear()
#         print("waiting for AI thread to close...")
#         self.aiThread.join(timeout=2)
#         if self.aiThread.is_alive():
#             print("AiThread timedout...")
#         else:
#             print("AiThread closed...")
#         print("closing game...")
#         self.gameOver = True
#         App.quit(self)

#helper function for make new Virus
#condition: each level ends after 15 fruits are thrown
    def updateVirusAttributes(self,newVirus):
        for virus in newVirus:
            if isinstance(virus,Bomb) == False:
                self.totalDrawnViruses += 1
                self.myLevelViruses += 1
                if self.totalDrawnViruses > 0:
                    self.accuracy = (self.totalHits/self.totalDrawnViruses)*100
                # condition for advancing to next level
                if self.myLevelViruses > 25 and self.currentLevel != 3:
                    self.reset()
                    self.level += 1
                    self.currentLevel += 1
                    self.inGame = True 
                    self.myLevelViruses = 0 
                elif self.myLevelViruses > 30 and self.currentLevel == 3:
                    self.gameOver = True

# define the instances of all viruses aka polygons for selecting based on levels
    def makeVirus(self, pos, speed, sliced, globalID):
        allViruses = [ ]
        bacteria = Bacteria(pos, speed, sliced, globalID) #instance of class
        amoeba = Amoeba(pos, speed, sliced, globalID) #instance of class
        ebola = Ebola(pos, speed, sliced, globalID) #instance of class
        covid19 = Covid19( pos, speed, sliced, globalID) #instance of class
        covid21 = Covid21( pos, speed, sliced, globalID) #instance of class
        bomb = Bomb( pos, speed, sliced, globalID)
        specialVirus1 = SpecialVirus1( pos, speed, sliced, globalID)
        allViruses = [bacteria,amoeba,ebola,covid19,covid21,bomb,specialVirus1]
        return allViruses

# draw viruses in a loop and make new viruses
    def virusesChain(self,num=3):
        prevDigit = 0
        for index in range(num):
        # condition: draw viruses such that they donot overlap
            val = random.choices([1,2,4,8,16])
            if prevDigit != val[0]:
                prevDigit = val[0]
                x = self.width//val[0]
            else:
                continue
            #magic numbers used for right speed
            dx = random.randint(-self.width*1//x, self.width*1//3) 
            dy = -(random.uniform(self.height*0.9,self.height*1))
            # drawing viruses on the screen
            if (x < self.width): 
                dx = abs(dx)
            else: 
                dx= -abs(dx)
            self.globalID += 1
            self.makeNewVirus(x,dx,dy)
            #if game mode is Ai, then val can be 2 or 

#function to make a new virus and update game variables
    def makeNewVirus(self,xvalue,dx,dy):
        newVirus = self.chooseViruses((xvalue,self.height), (dx,dy), False, self.globalID)
        self.updateVirusAttributes(newVirus)
        self.allViruses.extend(newVirus)
        self.number = len(self.allViruses)

#controllers
    def keyPressed(self,event):
        if event.key == 'Enter':
            self.gameMode  = 'splashScreen'
        if self.gameMode == 'AI':
            if event.key == 'a':
                self.iAddVirusMyself()
            if event.key == 'f':
                self.exit = True
        # elif self.gameMode == 'original':
            
    def mousePressed(self,event):
        self.mousePress = True
        if (self.isInsideOriginalMode(event.x,event.y) and (self.gameMode=='splashScreen')):
            self.gameMode = "original"
            self.currentLevel = 1
            self.inGame = not self.inGame
        
        # elif(self.isInsideBonusMode(event.x,event.y) and (self.gameMode == 'splashScreen')):
        #     self.gameMode = "original"
        #     self.currentLevel = 1
        #     self.inGame = not self.inGame
        
        # elif(self.isInsideAIMode(event.x,event.y) and (self.gameMode == 'splashScreen')):
        #     self.gameMode = "AI"
        #     self.currentLevel = 1
        #     self.inGame = not self.inGame

    def mouseReleased(self,event):
        if self.planetIsSafe  == True or self.gameOver  == True or self.exit == True:
            return
        self.mousePress = False

    def mouseDragged(self,event):
        if (self.planetIsSafe == True or self.gameOver == True or self.exit == True) and not self.isnotLastLevel:
            return
        if self.mousePress == True:
            if self.sliceAir == False:
                bladeSound.play()
            x = event.x
            y = event.y
            self.knife.insert(0,(x,y))
            self.knifeCurrentTime.insert(0,time.time())
            for index in range(len(self.knife)-1):
                points1 = self.knife[index]
                points2 = self.knife[index+1]
                self.cutAllShapes(points1,points2)

    def timerFired(self):
        self.useCachedImages = True
        self.gameStartSound = True
        if self.gameMusicStarted == False:
            pygame.mixer.music.play(-1)
            self.gameMusicStarted = True
        if self.gameMode == 'AI' and self.exit == False and self.gameOver == False:
            self.useCachedImages = not self.useCachedImages
            # self.AIModeRandom()
        elif self.gameMode == 'original' and self.exit == False:
            if self.planetIsSafe == False and  self.gameOver == False:
                #set up the gameplay
                if self.currentLevel == 1:
                    self.level1()
                if self.currentLevel == 2:
                    self.level2()
                if self.currentLevel == 3:
                    self.level3()
                self.originalModeRandom()
                self.takeStep()

#adds a virus to the list based on key pressed
    def iAddVirusMyself(self):
        num = 1
        self.virusesChain(num) 
    
    def iAddVirusMyself(self):
        num = 2
        self.virusesChain(num) 

#helper function for timerfired
#condition: remove viruses if out of the screen aka empty list
    def takeStep(self):
        myTime = time.time() - self.time0
        if  myTime > self.time1:
            #play drawing sound once every drawn time
            if self.gameOver != True:
                drawSound.play()  
            # make a chain of viruses
            num = random.randint(1,5)
            self.virusesChain(num) 
            self.time0 = time.time()
        self.allViruses = self.updateVirusLife()
        self.moveVirus()
        self.takeStepKnife()
        
# helper function for takestep
# condition: loses points for missed viruses but not if
# cut even once
    def updateVirusLife(self):
        isvalidViruses = [ ]
        for virus in self.allViruses:
            if virus.sliced == False:
                if virus.pos[1] < 1.25*(self.height):
                    isvalidViruses.append(virus)
                else:
                    self.misses += 1
                    self.score -= 5
            elif virus.sliced == True:
                if virus.pos[1] < 1.25*(self.height):
                    isvalidViruses.append(virus)
        return isvalidViruses

# helper function for takeStep()q
    def moveVirus(self):
        for virus in self.allViruses:
            diff = time.time()-self.prevTime
            # if len(self.allViruses) <= 5:
            virus.move(diff)
            self.comboReset = False
        #reset the time
        self.prevTime = time.time() 

#function to smooth the tail of knife
#reference: https://stackoverflow.com/questions/52598998/canvas-a-line-with-a-thinner-tail
    def takeStepKnife(self,index = 0):
        self.knifeTime0 += 1
        while index < len(self.knife):
            startTime = self.knifeCurrentTime[index]
            span = (time.time() - startTime)
            # print(f'lengthofarray={len(self.knife)}')
            if self.knifeTime1 < span*400:
                self.knife.pop(index)
            else:
                index += 1
    
#helper functions for mousePressed to determine which mode user wants to play 
    def isInsideOriginalMode(self,x,y):
        distance = math.sqrt((self.ox - x)**2 + (self.oy- y)**2)
        return distance <= self.r1 
  
    def isInsideBonusMode(self,x,y):
        distance = math.sqrt((self.bx - x)**2 + (self.by- y)**2)
        return distance <= self.r2

    def isInsideAIMode(self,x,y):
        distance = math.sqrt((self.ax - x)**2 + (self.ay- y)**2)
        return distance <= self.r3 

#changes the coordinates
    def modifyCoordinates(self,virus,points):
        cx, cy = virus.pos 
        cordList1 = copy.copy(points)
        cordList2 = copy.copy(points)
        for coordinates in range(len(cordList1)):
            (x,y) = cordList1[coordinates]
            cordList1[coordinates] = (x+cx, y+cy)
            cordList2[coordinates] = (x-cx, y-cy)
        return (cordList1,cordList2)
        
#display my stats
    def drawStats(self,canvas):
        canvas.create_text(self.width//7,self.height//7, text= f'{self.score}', font='Arial 50 bold', fill = 'white')
        canvas.create_text(self.width//2,self.height//12, text=f'LEVEL: {self.level}',font='Arial 14 bold', fill="white")
        canvas.create_text(self.width//2,self.height//9, text=f'HEALTH: {self.health}',font='Arial 14 bold', fill="white")
        canvas.create_text(self.width//2,self.height//7,text=f'TOTAL HITS: {self.totalHits}',font='Arial 14 bold', fill="white")
        canvas.create_text(self.width//2,self.height//6, text= f'HIT BOMB: {self.hitBomb}', font='Arial 14 bold', fill = 'white')
        canvas.create_text(self.width//2,self.height//5.25,text=f'LEVEL VIRUSES: {self.myLevelViruses}',font='Arial 14 bold', fill="white")
        canvas.create_text(self.width//2,self.height//4,text=f'MISSES: {self.misses}',font='Arial 14 bold', fill="white")
        # canvas.create_text(self.width//2,self.height//10,fill='black',text=f'Total Unsliced Viruses = {self.number}')
        # canvas.create_text(self.width//2,self.height//8,fill='black',text=f'Sliced Viruses = 0')

    #draw combo slicing
    def drawComboSlicing(self,canvas):
        if self.comboReset == True:
            canvas.create_text(self.width//2,self.height//2,text="+ EXTRA SLICING POINTS",fill = "Black",font = 'Arial 50 bold')
            
# access all viruses and create polygons
# Polygon Reference - https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_polygon.html
    def drawViruses(self, canvas): 
        for virus in self.allViruses:
                cx,cy = virus.pos
                id = virus.globalID
                color = virus.color
                l = virus.length()//10
                myCordinates = self.modifyCoordinates(virus,virus.myShape)[0]
                if isinstance(virus,Bomb):
                    canvas.create_polygon(myCordinates, fill=color,width=4, outline = 'white', smooth = 1)
                elif isinstance(virus,Bacteria):
                    canvas.create_polygon(myCordinates, fill=color,width=6, outline ='black', smooth = 1) 
                    canvas.create_line(myCordinates[0][0],myCordinates[0][1],myCordinates[1][0],myCordinates[1][1], fill='black',width=0.25, dash=(4,2)) 
                    canvas.create_line(myCordinates[0][0],myCordinates[0][1],myCordinates[2][0],myCordinates[2][1], fill='black',width=0.25, dash=(4,2)) 
                    canvas.create_line(myCordinates[1][0],myCordinates[1][1],myCordinates[2][0],myCordinates[2][1], fill='black',width=0.25, dash=(4,2)) 
                else: 
                    canvas.create_polygon(myCordinates, fill=color,width=6, smooth = 0,outline = 'black') 
                    canvas.create_line(myCordinates[0][0],myCordinates[0][1],myCordinates[1][0],myCordinates[1][1], fill='black',width=0.25, dash=(4,2)) 
                    canvas.create_line(myCordinates[0][0],myCordinates[0][1],myCordinates[2][0],myCordinates[2][1], fill='black',width=0.25, dash=(4,2)) 
                    
                    # canvas.create_line(myCordinates[0][0],myCordinates[0][1],myCordinates[3][0],myCordinates[3][1], fill='black',width=0.25) 
                # display global ID
                canvas.create_text(cx,cy,text=f'{virus.globalID}',fill = 'white')


# function used to draw knife on the canvas
# reference: https://stackoverflow.com/questions/52598998/canvas-a-line-with-a-thinner-tail
    def drawKnife(self,canvas,index= 0):
        length = len(self.knife)       
        while index < length-1: 
            r = (length-index)+3
            (x0,y0),(x1,y1) = (self.knife[index]),(self.knife[index+1])
            # draw the blade and smoothen it
            canvas.create_oval(x0-(r*0.5), y0-(r*0.5), x0+(r*0.5), y0+(r*0.5), fill = "white", width=0)
            canvas.create_line(x0,y0,x1,y1, width=r, fill = "white")
            index+=1
        

#first screen that welcomes the user (requires user to press Enter)
    def drawWelcomeScreen(self,canvas):
        if (self.useCachedImages):
            photoImage = self.getCachedPhotoImage(self.image2)
        else:
            photoImage = ImageTk.PhotoImage(self.image2)
        canvas.create_image(self.width//2, self.height//2, image=photoImage)
        canvas.create_image(self.width//2,self.height//2, image=photoImage)
        canvas.create_text(self.width//2,self.height*11/12,text='Press Enter to continue', font = 'Arial 12 bold', fill = 'black')
        
    
#second screen that welcomes the user (requires user to click)
    def drawSplashScreen(self,canvas):
        if (self.useCachedImages):
            photoImage = self.getCachedPhotoImage(self.image4)
        else:
            photoImage = ImageTk.PhotoImage(self.image4)
        self.originalMode(canvas)
        self.bonusMode(canvas)
        self.aiMode(canvas)
        canvas.create_image(self.width//2,self.height//2, image=photoImage)

#helper function for original mode
    def drawScreen(self,canvas):
        self.drawViruses(canvas)
        self.drawStats(canvas)
        self.drawKnife(canvas)

#helper function for casched images
    def getCachedPhotoImage(self, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

#original mode (works on player lives)
    def drawOriginalModeLevel(self,canvas):
        if (self.useCachedImages):
            photoImage = self.getCachedPhotoImage(self.image6)
        else:
            photoImage = ImageTk.PhotoImage(self.image6)
        canvas.create_image(self.width//2, self.height//2, image=photoImage)
        self.drawScreen(canvas)

#bonus mode (works on time)
    def drawBonusModeLevel(self,canvas):
        if (self.useCachedImages):
            photoImage = self.getCachedPhotoImage(self.image6)
        else:
            photoImage = ImageTk.PhotoImage(self.image6)
        canvas.create_image(self.width//2, self.height//2, image=photoImage)
        canvas.create_rectangle(0,0,self.width,self.height,fill='grey', dash=(6,5), outline = 'white')
        self.drawScreen(canvas)
        canvas.create_rectangle(0,self.height*10/12,self.width,self.height,fill='black', dash=(6,5), outline = 'white')

#ai mode (works on keyPresses)
    def drawAIModeLevel(self,canvas):
        if (self.useCachedImages):
            photoImage = self.getCachedPhotoImage(self.image6)
        else:
            photoImage = ImageTk.PhotoImage(self.image6)
        canvas.create_image(self.width//2, self.height//2, image=photoImage)
        # canvas.create_rectangle(0,0,self.width,self.height,fill='white')
        self.drawScreen(canvas)

# draws game over in the end
    def gameIsWon(self,canvas):
        #displays game over screen
        if self.planetIsSafe == True:
            canvas.create_rectangle(self.width*1/5,self.height*1/5,self.width*4/5,self.height*4/5, fill="Black")
            canvas.create_text(self.width//2,self.height//2,text="You Won!!", font = "Arial 50 bold",fill="white")

# draws game over in the end
    def gameIsOver(self,canvas):
        #displays game over screen
        if (self.gameOver or self.exit) == True:
            canvas.create_rectangle(self.width*1/5,self.height*1/5,self.width*4/5,self.height*4/5, fill="Black")
            canvas.create_text(self.width//2,self.height//2,text="You Lose!!", font = "Arial 50 bold",fill="white")
            pygame.mixer.music.stop() 
            

# view method
# condition: draw based on gameModes
    def redrawAll(self, canvas):
        if self.gameMode == None:
            self.drawWelcomeScreen(canvas)
            if self.gameStartSound == False:
                startGameSound.play()

        elif self.gameMode == 'splashScreen':
            self.drawSplashScreen(canvas)

        elif self.gameMode == "original" and (self.inGame == True):
             if self.currentLevel == 1 or self.currentLevel == 2 or self.currentLevel == 3:
                self.drawOriginalModeLevel(canvas)
             if self.comboSlicingActivated == True:
                self.drawComboSlicing(canvas)

        elif self.gameMode == "bonus" and (self.inGame == True):
             if self.currentLevel == 1:
                self.drawBonusModeLevel(canvas)

        elif self.gameMode == "AI" and (self.inGame == True):
             if self.currentLevel == 1:
                self.drawAIModeLevel(canvas)
        self.gameIsOver(canvas)
        self.gameIsWon(canvas)

# original mode for the game
    def originalMode(self,canvas):
        canvas.create_oval(self.ox-self.r1,self.oy-self.r1, self.ox+self.r1,self.oy+self.r1,fill='white',stipple='gray50')
        canvas.create_text(self.ox,self.oy,text="original", font = "Roboto 30 bold", fill = "black")
    
# bonus mode for the game
    def bonusMode(self,canvas):
        canvas.create_oval(self.bx-self.r2,self.by-self.r2, self.bx+self.r2,self.by+self.r2,fill='white',stipple='gray50')
        canvas.create_text(self.bx,self.by,text="bonus", font = "Roboto 30 bold", fill = "black")

# AI mode for the game
    def aiMode(self,canvas):
        canvas.create_oval(self.ax-self.r3,self.ay-self.r3, self.ax+self.r3,self.ay+self.r3,fill='white',stipple='gray50')
        canvas.create_text(self.ax,self.ay,text="ai", font = "Roboto 30 bold", fill = "black")

    def virusPhysics(self):
        #accuracy is highest
        # easy shapes left to right
        if self.timer < 10 and self.accuracy > 80:
            # condition: donot draw difficult virus
            self.weight = [1,1,1,1,1,10,random.randint(30,40)]
        
        #accuracy is little smaller
        elif self.timer < 20 and self.accuracy > 60:
            self.weight = [15,10,15,10,10,5,random.randint(20,30)]
        
        #accuracy is little smaller
        elif self.timer < 20 and self.accuracy > 40:
            self.weight = [15,15,15,15,10,5,random.randint(10,20)]
        
        #accuracy is little smaller
        elif(self.timer < 20 and self.accuracy >= 0):
            self.weight = [20,20,10,10,20,5,random.randint(5,10)]

        #accuracy is little smaller
        elif(self.timer < 20 and self.accuracy >= 0):
            self.weight = [10,20,30,20,10,5,random.randint(0,5)]
        return self.weight

# function to cut all Shapes based on mouse positions
    def cutAllShapes(self,mouse1,mouse2,index = 0):
        (x1, y1) = mouse1
        (x2, y2) = mouse2
        while index < len(self.allViruses):
            myVirus = self.allViruses[index]
            myShape = self.modifyCoordinates(myVirus,myVirus.myShape)[0]
            point1 = Point(x1, y1)
            point2 = Point(x2, y2)
            # check for cut condition
            if self.cutIntersectShape(myShape,point1, point2):
                self.totalHits += 1
                self.sliceViruses(myVirus, index, mouse1, mouse2)
                self.score += 1
                index += 1
            index += 1

# helper function for cutAllShapes
    def sliceViruses(self, virus, index, mouse1, mouse2):
        self.sliceAir = True
        if isinstance(virus,Bomb) == True:
            self.health -= 1
            self.hitBomb += 1
        virus.sliced = True
        #play the sliced sound
        sliceSound.play() 
        self.sliceAir = False
        cutResult = self.cut(virus,mouse1, mouse2)
        
        if cutResult != None:
            mySlices = self.helperComboSlicing(mouse1,mouse2)
            bestCount = self.comboSlicing(mySlices)
            if bestCount >= 2:
                self.comboSlicingActivated = True
                self.comboReset = True
                mySlices = [ ]
                self.score += bestCount
            (cutShape1, cutShape2) = cutResult
            self.allViruses.remove(virus)
            self.allViruses.insert(index,cutShape1) 
            self.allViruses.insert(index,cutShape2)
           

#keep track of previous mouse clicks
    def helperComboSlicing(self,mouse1,mouse2):
        # keep track of the same points
        if self.cutResult1 == (0,0):
            self.cutResult1 = (mouse1, mouse2)
        elif self.cutResult2 == (0,0):
            self.cutResult2 = (mouse1, mouse2)
        elif self.cutResult3 == (0,0):
            self.cutResult3 = (mouse1, mouse2)
        elif self.cutResult4 == (0,0):
            self.cutResult4 = (mouse1, mouse2)
        elif self.cutResult5 == (0,0):
            self.cutResult5 = (mouse1, mouse2)
        else:
            self.cutResult5 = (0,0)
            self.cutResult4 = (0,0)
            self.cutResult3 = (0,0)
            self.cutResult2 = (0,0)
            self.cutResult1 = (mouse1,mouse2)
        self.mySlices = [self.cutResult1,self.cutResult2,self.cutResult3,self.cutResult4,self.cutResult5]
        return self.mySlices

#check for combo slicing
    def comboSlicing(self,myPoints):
        d = dict()
        for i in range(len(myPoints)):
            if myPoints[i] != (0,0):
                d[myPoints[i]] = d.get(myPoints[i],0)+1

        #get the number of cut shapes from dictionary
        bestCount = 0
        for key in d:
            if d[key] > bestCount:
                bestCount = d[key]
        return bestCount


#Point code referenced from 
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# code to check if polygon is cut by two mouse points 
    def cutIntersectShape(self, myShape, mouse1, mouse2):
        for i in range(len(myShape)):
            p1 = myShape[i]
            # formula referened from centroid algorithm from polygonCentroid
            p2 = myShape[(i + 1)%len(myShape)] 
            (a1, b1),(a2, b2) = p1,p2
            mousePoint3 = Point(a1, b1)
            mousePoint4 = Point(a2, b2)
            # check if the points intersect
            if Point.doIntersect(mouse1, mouse2, mousePoint3, mousePoint4):
                return True
        return False

    def cutPolygon(self,polyList, mouse1, mouse2):
        #get cut polygons
        if self.getCutPolygons(mouse1, mouse2) == None:
            return None  
        else:
            poly1, poly2 = self.getCutPolygons(mouse1, mouse2)
        #get clipped (closed) polygons and return None if not available
        poly1 = clip(polyList, poly1)
        poly2 = clip(polyList, poly2)
        if poly1 == None or poly2 == None:
            return None
        return poly1, poly2
        
# helper function for cutPolygon
    def getCutPolygons(self,mouse1, mouse2):
        (x0,y0) = mouse1
        (x1,y1) = mouse2
        topPolygonList = [ ]
        bottomPolygonList = [ ]
        # check for the value of dx and dy where it is non zero
        # since we need slope
        dx = (x1 - x0)
        dy = (y1 - y0)
        if dx == 0 or dy == 0:
            topPolygonList.append(self.moveInLine(x0,y0,dx,dy,1))
            topPolygonList.append(self.moveInLine(x0,y0,dx,dy,-1))
            bottomPolygonList.append(self.moveInLine(x0,y0,dx,dy,1))
            bottomPolygonList.append(self.moveInLine(x0,y0,dx,dy,-1))
            if dx ==0:
                topPolygonList.append((0,0))
                topPolygonList.append((0,self.height))
                bottomPolygonList.append((self.width,0))
                bottomPolygonList.append((self.width,self.height))
            elif dy == 0:
                topPolygonList.append((0,0))
                topPolygonList.append((self.width,0))
                bottomPolygonList.append((0,self.height))
                bottomPolygonList.append((self.width,self.height))
        else:
            slope = (dy/dx)
            intercept = (y0) - (slope*x0)
            topPolygonList.extend(self.getIntercepts(slope,intercept))
            bottomPolygonList.extend(self.getIntercepts(slope,intercept))
            
            for xEnd,yEnd in [(0,0),(self.width,0),(self.width,self.height),(0,self.height)]:
                # check if the point is above line
                if yEnd>slope*xEnd+intercept:
                    bottomPolygonList.append((xEnd,yEnd))
                else:
                    topPolygonList.append((xEnd,yEnd))
            
            return self.orderClockwise(topPolygonList), self.orderClockwise(bottomPolygonList)

#helper function for cutShapePolygons
#condition check for validity if on screen
    def moveInLine(self,x,y,dx,dy,line):
        if x >= 0 and y >= 0 and x <= self.width and y <= self.height:
            # add to the coordinate
            x += dx*line
            y += dy*line
        return (x,y)

# helper function for cut shape
# to get the slope and intercept coordinates 
# reference: https://stackoverflow.com/questions/28789614/x-and-y-intercepts-from-slopes-python
    def getIntercepts(self,slope,intercept):
        result = [ ]
        a = ( 0, intercept )
        b = ( ((- intercept) / slope),0)
        c = (self.width, (slope*self.width+intercept))
        d = (((self.height-intercept)/ slope) , 0)
        #condition: return if present on teh screen
        for x,y in [a,b,c,d]:
            if x >= 0 and y >= 0 and x <= self.width and y <= self.height:
                result.append((x,y))
        return result

#helper function for cut
#get the modified coordinates and return shapes
    def getmyShape(self, virus, shape, mouse1, mouse2):
        myShape = self.modifyCoordinates(virus,shape)[0]
        polyList = self.cutPolygon(myShape, mouse1, mouse2)
        if polyList == None:
            return None
        polyList1, polyList2 = polyList
        return (polyList1,polyList2)

# main function for slice viruses to get 2 shapes
    def cut(self, virus, mouse1, mouse2):
        (x,y) = virus.pos
        shape = virus.myShape
        #get modified coordinates and check for validity of polygon
        result = self.getmyShape(virus,shape,mouse1, mouse2)
        if result == None:
            return None
        polyList1 = self.modifyCoordinates(virus,result[0])[1]
        polyList2 = self.modifyCoordinates(virus,result[1])[1]
        
        #shift new center of mass
        centroid1 = findCentroid(polyList1)
        centroid2 = findCentroid(polyList2)
        if centroid1 is None or centroid2 is None:
            return None 
        else:
            solution = self.pointsAround(virus,result[0],result[1],centroid1,centroid2,mouse1,mouse2)
            return solution

# helper function for pointsAround
    def getModifiedCoordinates(self,x1,y1,x2,y2,polyList1,polyList2):
        (xcenter1, ycenter1) = findCentroid(polyList1)
        (xcenter2, ycenter2) = findCentroid(polyList2)
        position1 = (x1+xcenter1, y1+ycenter1) 
        position2 = (x2+xcenter2, y2+ycenter2)

        #change the centroids to new location based on centroids
        for i in range(len(polyList1)):
            (x, y) = polyList1[i]
            polyList1[i] = (x - xcenter1, y - ycenter1)

        for i in range(len(polyList2)):
            (x, y) = polyList2[i]
            polyList2[i] = (x - xcenter2, y - ycenter2)
        return polyList1, polyList2, position1, position2

# helper function for cut
# Calculating centroid of polygon taken from 
# https://www.geeksforgeeks.org/find-the-centroid-of-a-non-self-intersecting-closed-polygon/
# reference to finding slope:
# https://stackoverflow.com/questions/41462419/python-slope-given-two-points-
# find-the-slope-answer-works-doesnt-work
    def pointsAround(self,virus,polyList1,polyList2,centroid1,centroid2,mouse1,mouse2):
        #get the centroid coordinates
            x1,y1 = centroid1[0],centroid1[1]
            x2,y2 = centroid2[0],centroid1[1]
            #get the centroid of cut polygons
            result = self.getModifiedCoordinates(x1,y1,x2,y2,polyList1,polyList2)
            (x0, y0) = mouse1
            (x1, y1) = mouse2
            slope = (y1-y0)/(x1-x0)
            speed = -1/slope
            
            (getXVelocityVector, getYVelocityVector) = self.velocityVector(speed)
            (xSpeed, ySpeed) = virus.speed
            x1,y1 = result[2]
            x2,y2 = result[3]
            # condition: check the positions of cut pieces 
            # and return the positions
            if x1 > x2:
                speed1 = (xSpeed+getXVelocityVector, ySpeed+getYVelocityVector) 
                speed2 = (xSpeed-getXVelocityVector, ySpeed-getYVelocityVector)
            else:
                speed1 = (xSpeed-getYVelocityVector, ySpeed-getYVelocityVector) 
                speed2 = (xSpeed+getYVelocityVector, ySpeed+getYVelocityVector)

            #update the virus
            copy1 = copy.deepcopy(virus)
            copy2 = copy.deepcopy(virus)
            copy1.updateShape(result[0], result[2], speed1, True)
            copy2.updateShape(result[1], result[3], speed2, True)
            return copy1, copy2

#helper function for test to calculate
#https://stackoverflow.com/questions/31735499/calculate-angle-clockwise-between-two-points
    def velocityVector(self,slopeVelocity):
        maxVelocity = 100
        slope = math.atan(slopeVelocity)
        getXVelocityVector = math.cos(slope)*maxVelocity
        getYVelocityVector = math.sin(slope)*maxVelocity
        return (getXVelocityVector,getYVelocityVector)

#function to calculate if polygonal points are in clockwise order
# https://stackoverflow.com/questions/1165647/how-to-determine-if-
# a-list-of-polygon-points-are-in-clockwise-order
    def orderClockwise(self,polyList):
        #condition: if less than 3 points, its not a polygon
        if len(polyList) < 3:
             return None
        else:
            result = [ ]
            leftPoint = self.firstPoint(polyList)
            pointOn = leftPoint
            currPoint = 0
            while True:
                result.append(polyList[pointOn])
                currPoint = (pointOn+1)%len(polyList)
                for i in range(len(polyList)):
                    if (self.orientTrack(polyList[pointOn],polyList[i],polyList[currPoint]) == 2):
                        currPoint = i
                pointOn = currPoint
                if (pointOn == leftPoint): #when we found all points
                    break 
        return result

# function to check the orientation of 3 points using formula
# https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/  
# 0  if colinear, 1 if clockwise, 2 if counterclockwise
    def orientTrack(self,a,b,c):
        orientation = ((b[1]-a[1]) * (c[0]-b[0])) - ((b[0]-a[0]) * (c[1]-b[1]))
        if orientation == 0:
            return 0
        elif orientation > 0:
             return 1
        #condition: needed counterclockwise points
        else: 
            return 2

# function to compare the x values of polygons
# to determine the left point
    def firstPoint(self,polyList):
        xcoordinate = 0
        for i in range(1,len(polyList)): 
            if polyList[i][0] < polyList[xcoordinate][0]: 
                xcoordinate = i 
            elif polyList[i][0] == polyList[xcoordinate][0]: 
                if polyList[i][1] > polyList[xcoordinate][1]: 
                    xcoordinate = i 
        return xcoordinate 


try:
    print("starting program...")
    Main(width=800, height=600)
    print("finished program...")
except Exception as e:
    print("Failed to start program!\n", e)