
from Virus import *
import random
import math
# inheritance from Main Class
class Bacteria(Virus):
    def __init__(self,  pos, speed, sliced, globalID):
        s = [(0,-50),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)]
        L = [ ]
        j = random.randint(1,3)
        for i in range(len(s)):
            a = s[i][0]*j
            b = s[i][1]*j
            L += [(a,b)]
        self.myShape = L        
        self.color = 'red'
        self.bestDist = 0 
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
        return self.bestDist

class Amoeba(Virus):
    def __init__(self,  pos, speed, sliced,globalID):
        s = [(50,25),(20,48),(50,75),(80,48)]
        L = [ ]
        j = random.randint(1,2)
        for i in range(len(s)):
            a = s[i][0]*j
            b = s[i][1]*j
            L += [(a,b)]
        self.myShape = L
        self.color = 'yellow'
        self.bestDist = 0  
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
        return self.bestDist

class Ebola(Virus):
    def __init__(self,  pos, speed, sliced,globalID):
        s = [(43,23),(17,41),(27,72),(60,72),(69,42)]
        L = [ ]
        j = random.randint(2,4)
        for i in range(len(s)):
            a = s[i][0]*j
            b = s[i][1]*j
            L += [(a,b)]
        self.myShape = L  
        self.color = 'magenta' 
        self.bestDist = 0  
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance
        return self.bestDist 

class Covid19(Virus):
    def __init__(self,  pos, speed, sliced, globalID):
        self.myShape = [(49,2),(52,29),(59,19),(61,24),(65,21),(64,30),
                (67,30),(66,35),(91,20),(69,39),(74,39),
                (68,44),(80,50),(69,56),(74,60),(69,61),(91,80),
                (66,65),(67,70),(65,70),(60,76),(60,80),(52,72),
                (50,100),(50,70),(38,76),(35,80),(35,70),(32,70),
                (35,65),(8,80),(28,62),(25,61),(30,57),(20,50),
                (30,44),(26,40),(30,40),(7,20),(34,36),(33,31),
                (35,30),(35,22),(38,25),(40,19),(47,30)]
        
        self.color = 'cyan' 
        self.bestDist = 0 
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
        return self.bestDist

# this gets killed by AI
class Covid21(Virus):
    def __init__(self,  pos, speed, sliced, globalID):
        s = [(47,11),(15,30),(15,66),(47,84),(79,66),(79,30)]
        L = [ ]
        j = random.randint(2.0,4.0)
        for i in range(len(s)):
            a = s[i][0]*j
            b = s[i][1]*j
            L += [(a,b)]
        self.myShape = L  
        self.color = 'cyan'  
        self.bestDist = 0 
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
        return self.bestDist

class SpecialVirus1(Virus):
    def __init__(self,  pos, speed, sliced, globalID):
        s = [(49,2),(52,29),(59,19),(61,24),(65,21),(64,30),
                (67,30),(66,35),(91,20),(69,39),(74,39),
                (68,44),(80,50),(69,56),(74,60),(69,61),(91,80),
                (66,65),(67,70),(65,70),(60,76),(60,80),(52,72),
                (50,100),(50,70),(38,76),(35,80),(35,70),(32,70),
                (35,65),(8,80),(28,62),(25,61),(30,57),(20,50),
                (30,44),(26,40),(30,40),(7,20),(34,36),(33,31),
                (35,30),(35,22),(38,25),(40,19),(47,30)]
        L = [ ]
        j = random.randint(1.0,2.0)
        for i in range(len(s)):
            a = s[i][0]*j
            b = s[i][1]*j
            L += [(a,b)]
        self.myShape = L  
        self.color = 'green' 
        self.bestDist = 0 
        super().__init__(pos, speed, sliced, globalID)

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
        return self.bestDist