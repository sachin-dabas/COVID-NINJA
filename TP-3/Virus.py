
class Virus(object):
    def __init__(self, pos, speed, sliced, globalID): 
        self.pos = pos
        self.speed = speed
        self.gravity = 500
        self.sliced = sliced
        self.globalID = globalID

# gravity code referenced from 
# https://www.bing.com/videos/search?q=gravity+*+time+python&&view=detail&mid=2A38
# 53C0B5A9956B3D0C2A3853C0B5A9956B3D0C&rvsmid=A8BB306E3F119147E02FA8BB306E3F119147
# E02F&FORM=VDRVRV



    def move(self, time):
        x,y = self.pos
        dx, dy = self.speed
        #gravitational pull
        self.speed = (dx, dy+(self.gravity)*time) 
        # position change
        self.pos = (x+(dx*time), y+(dy*time))

    # def moveUp(self, time):
    #     x,y = self.pos
    #     dx, dy = self.speed
    #     # gravitational pull
    #     self.speed = (dx, -(dy+(self.gravity)*time)) 
    #     # position change
    #     self.pos = (x+(dx*time), -(y+(dy*time)))

    def updateShape(self,shape,pos,vel,sliced):
        self.myShape = shape
        self.pos = pos
        self.speed = vel
        self.sliced = sliced
