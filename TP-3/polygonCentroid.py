# Calculating centroid of polygon taken from 
# https://www.geeksforgeeks.org/find-the-centroid-of-a-non-self-intersecting-closed-polygon/

def findCentroid(L): 
    result = [0, 0] 
    n = len(L) 
    signedArea = 0 
    for i in range(len(L)): 
        x0 = L[i][0] 
        y0 = L[i][1] 
        x1 = L[(i + 1) % n][0] 
        y1 =L[(i + 1) % n][1] 
        # Calculate value of A 
        # using shoelace formula 
        A = (x0 * y1) - (x1 * y0) 
        signedArea += A 

        # Calculating coordinates of 
        # centroid of polygon 
        result[0] += (x0 + x1) * A 
        result[1] += (y0 + y1) * A 

    if signedArea != 0:
        signedArea *= 0.5
        result[0] = (result[0]) / (6 * signedArea) 
        result[1] = (result[1]) / (6 * signedArea) 

    return result 