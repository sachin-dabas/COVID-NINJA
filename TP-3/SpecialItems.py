import random
import math


class Bomb(object):
    def __init__(self, pos, speed, sliced, globalID): # newVirus = Virus(shape, (xvalue,self.height), (dx,dy), type)
        self.pos = pos
        self.speed = speed
        self.gravity = 500
        self.sliced = sliced
        self.globalID = globalID

        s = [(0,-25),(-40,-40),(-50,10),(-25,45),(25,45),(50,10),(40,-40)]
        L = [ ]
        j = random.randint(1.0,2.0)
        for i in range(len(s)):
            a = s[i][0]*2
            b = s[i][1]*2
            L += [(a,b)]
        self.myShape = L        
        self.color = 'black' 
        self.bestDist = 0 

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
            return self.bestDist

    def move(self, time):
        x,y = self.pos
        dx, dy = self.speed
        #gravitational pull
        self.speed = (dx, dy+(self.gravity)*time) 
        # position change
        self.pos = (x+(dx*time), y+(dy*time))

    def updateShape(self,shape,pos,vel,sliced):
        self.myShape = shape
        self.pos = pos
        self.speed = vel
        self.sliced = sliced


class Fish(object):
    def __init__(self, pos, speed, sliced, globalID):
        self.pos = pos
        self.speed = speed
        self.gravity = 500
        self.sliced = sliced
        self.globalID = globalID
        s = [(6,42),(10,36),(15,31),(22,27),(27,24),
                        (31,29),(32,35),(32,39),(36,35),(32,23),
                        (36,25),(40,31),(42,40),(46,40),(44,29),
                        (40,23),(51,30),(51,36),(52,41),(56,41),
                        (55,36),(54,30),(51,24),(51,24),(56,28),
                        (59,35),(60,41),(65,41),(64,35),(65,41),
                        (64,35),(62,29),(66,33),(68,39),(68,41),
                        (68,41),(72,41),(72,37),(70,34),(74,37),
                        (75,41),(78,41),(81,37),(82,31),(85,26),
                        (92,23),(92,27),(94,33),(93,37),(88,43),
                        (92,46),(93,50),(94,55),(92,61),(87,60),
                        (81,49),(80,45),(75,45),(74,48),(71,51),
                        (72,48),(72,45),(67,45),(66,45),(66,51),
                        (66,55),(61,57),(63,52),(64,48),(63,45),
                        (60,45),(59,49),(58,53),(56,57),(51,59),
                        (53,54),(55,50), (56,45),(51,45),(41,50),
                        (47,54),(45,58),(41,61),(44,53),(46,48),
                        (47,45),(41,45) ,(40,50),(39,55),(36,58),
                        (33,61),(34,55),(36,51),(36,45),(32,45),
                        (30,53),(27,59),(19,56),(21,53),(20,51),
                        (16,54)
                        ]
        L1 = [ ]
        j = random.randint(1.0,2.0)
        for i in range(len(s)):
            a = s[j][0]*2
            b = s[j][1]*2
            L1 += [(a,b)]
        self.myShape = L1        
        self.color = 'black' 

    def move(self, time):
        x,y = self.pos
        dx, dy = self.speed
        #gravitational pull
        self.speed = (dx, dy+(self.gravity)*time) 
        # position change
        self.pos = (x+(dx*time), y+(dy*time))

    def updateShape(self,shape,pos,vel,sliced):
        self.myShape = shape
        self.pos = pos
        self.speed = vel
        self.sliced = sliced

    def length(self):
        for point in self.myShape:
            x1,y1 = point
            x0, y0 = self.pos
            distance = math.sqrt(((x1-x0)**2 + (y1-y0)**2))
            if distance > self.bestDist:
                self.bestDist = distance 
            return self.bestDist