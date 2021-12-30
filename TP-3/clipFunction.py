

# reference from http://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping#Python


# find the polygon that is the intersection between an arbitrary polygon (the “subject polygon”) 
# and a convex polygon (the “clip polygon”)
def clip(subjectPolygon, clipPolygon):
    # get last coordinate of cut polygon list
    # and all points of main polygon
    x1 = clipPolygon[-1]
    result = subjectPolygon
    #loop through all vertices in clip polygon
    for vertices in clipPolygon:
        inputList = result
        if len(inputList) < 1:
            return None
        result = isInside(inputList,x1,vertices)
        x1 = vertices
    return (result)


#helper function for clip
#check for vertices if inside the polygon
def isInside(inputList,x1,vertices):
    result = [ ]
    lastElement = inputList[-1]
    for vertex in inputList:
        if inside(vertex,x1,vertices):
            if not inside(lastElement,x1,vertices):
                result.append(computeIntersection(x1,vertices,lastElement,vertex))
            result.append(vertex)
        elif inside(lastElement,x1,vertices):
            result.append(computeIntersection(x1,vertices,lastElement,vertex))
        lastElement= vertex
    return result

#helper function for clip
#based on hodman algorithm to find if point is inside
def inside(p,x1,x2):
    a = (x2[0]-x1[0])*(p[1]-x1[1])
    b = (x2[1]-x1[1])*(p[0]-x1[0])
    if a > b:
        return True
    return False

#helper function for clip to compute intersecting points
#based on hodman algorithm to find intersections
def computeIntersection(x1,x2,lastElement,vertex):
    a = [ x1[0] - x2[0], x1[1] - x2[1] ]
    b = [ lastElement[0] - vertex[0],lastElement[1] - vertex[1] ]
    n1 = x1[0] * x2[1] - x1[1] * x2[0]
    n2 = lastElement[0] * vertex[1] - lastElement[1] * vertex[0] 
    n3 = 1.0 / (a[0] * b[1] - a[1] * b[0])
    return (([(n1*b[0] - n2*a[0]) * n3, (n1*b[1] - n2*a[1]) * n3]))