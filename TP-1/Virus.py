from cmu_112_graphics import *

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
        self.virusType = virusType 
        self.uncut = uncut



