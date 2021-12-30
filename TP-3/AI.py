
# Reference code for virus Ninja AI ( https://www.youtube.com/watch?v=Vw3vU9OdWAs ) 
# The AI only loses when a bomb is overlapped with a virus on its whole path, as the AI won't find a good opportunity to slice it.

# [Addition] worked on integartion AI to cut the slices // 
# The challenge were many but the most difficult part was to integrate the gameAI with normal 
# part. Learnt threading and used it to improve the conversion of data from get_snapshot to 
# numpy array and use it for AI. The cutting can still be improved but happy to integrate these additional
# features

import time
from datetime import datetime
import cv2
import numpy as np
import win32api, win32con
import math

# initialize global variables
delayBetweenSlices = 0.19  # for sleep(delayBetweenSlices)
drawBombsMode = True
screenHeight = win32api.GetSystemMetrics(1)
screenWidth = win32api.GetSystemMetrics(0)

# Main class for AI 
class AiCutter():
    def __init__(self):
        # game screen dim to match the canvas
        self.gameScreen = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
        self.today = datetime.now()
        self.timeString = self.today.strftime('%b_%d_%Y__%H_%M_%S')
        self.width = 1920
        self.height = 1027
        #bombs
        self.bombs = [ ]
        self.possibleSwipes = [ ]
        self.bombMinDistance = 58
        self.bomdDown = 120
        # color ranges for object detections BGR
        self.objectBoundaries = [([0, 200, 200], [0, 255, 255], 120, True),  # virus
                                 ([0, 40, 10], [30, 170, 50], 100, True),    # virus
                                 ([10, 50, 220], [40, 250, 255], 80, True),  # virus
                                 ([30, 30, 20], [60, 70, 60], 60, False),    # bomb
                            ]
        self.bomgHeightCond = self.height * 1 / 2
        self.swipeThread = None
        self.cacheCoord = {}
        self.cacheDistance = 55 
        self.cacheTime = 1

#conversion of data from pixels to numpy
    def aiVirusCut(self, img):        
        screen = np.array(img)
        self.gameScreen['width'] = screen.shape[0]
        self.gameScreen['height'] = screen.shape[1]
        screen = np.flip(screen[:, :, :3], 2)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        img = screen.copy()

        mask = None
        tmpMask = None

        possibleSwipes = []
        self.prevBombs = self.bombs
        bombs = []
        for boundary in self.objectBoundaries:
            lower, upper, minPoints, isvirus = boundary
            tmpMask = cv2.inRange(img, np.array(lower), np.array(upper))
            contours, hierarchy = cv2.findContours(tmpMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if (mask is None):
                mask = tmpMask
            else:
                mask = cv2.bitwise_or(mask, tmpMask)
            for c in contours:
                if (len(c) < minPoints):
                    # contour is too small
                    continue
                centerX, centerY, __1, __2 = map(int, cv2.mean(c))
                sumX, sumY = 0, 0
                rows = 70
                cols = 70
                cnt = 0
                # get center of current object
                for i in range(rows):
                    for j in range(cols):
                        x = int(centerX + i - rows // 2)
                        y = int(centerY + j - cols // 2)
                        if x < 0 or x >= self.width or y < 0 or y >= self.height:
                            continue
                        val = tmpMask[y, x]
                        if val:
                            sumX += x
                            sumY += y
                            cnt += 1
                if cnt == 0:
                    continue
                sumX = int(sumX / cnt)
                sumY = int(sumY / cnt)

                if isvirus == True:
                    # mark all swipable viruses
                    isValid = True
                    for swipePoint in possibleSwipes:
                        x, y = swipePoint
                        dist = self.distPoints(x, y, sumX, sumY)
                        if dist < 15:
                            isValid = False
                            break
                    yBarrier = int(self.height * 4 / 5)
                    if (sumY > yBarrier):
                        break
                    if isValid:
                        possibleSwipes.append((sumX, sumY))
                else:
                    bombs.append((sumX, sumY))

        possibleSwipes.sort(key=lambda tup: self.ordervirussBy(tup), )
        if self.canSwipe():
            for elem in possibleSwipes:
                centerX, centerY = elem
                if (self.shouldSwipe(centerX, centerY)):
                    break

# still nothing swiped? probably because every area was
# already cached, so we remove the cache and retry !
        if self.canSwipe():
            cacheCoord = {}
            for elem in possibleSwipes:
                centerX, centerY = elem
                if (self.shouldSwipe(centerX, centerY)):
                    break

#check for margins
    def sanitizeMargins(self, rx, ry):
        margin = 10
        if (rx > self.width - margin):
            rx = self.width - margin
        if (rx < margin):
            rx = margin
        if ry > self.height - margin:
            ry = self.height - margin
        if ry < margin:
            ry = margin
        return (rx, ry)

#Move mouse
    def moveMouse(self, x, y):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE,
                             int(x / screenWidth * 65535.0), int(y / screenHeight * 65535.0))

#Translate game screen coordinated to canvas screen
    def realCoord(self, x, y):
        rx = int(x)
        ry = int(y)
        rx, ry = self.sanitizeMargins(int(x), int(y))
        rx += self.gameScreen['left']
        ry += self.gameScreen['top']
        return rx, ry

    def gameCoord(self, x, y):
        rx = int(x) - self.gameScreen['left']
        ry = int(y) - self.gameScreen['top']
        return self.sanitizeMargins(rx, ry)

    def distPoints(self, x1, y1, x2, y2):
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

#cutting function 
    def swipe(self, x1,y1, _x2, _y2):
        x1, y1 = self.realCoord(x1,y1)
        x2, y2 = self.realCoord(_x2, _y2)
        # one line swipe is made of multiple cursor moves
        # if we instantly move the cursor too much, the game might not register the swipe
        points = 251
        self.moveMouse(x1, y1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(x1), int(y1), 0, 0)
        for i in range(points + 1):
            x = (x1 * (points - i) + x2 * i) / points
            y = (y1 * (points - i) + y2 * i) / points
            self.moveMouse(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(x2), int(y2), 0, 0)
        print("btn up: ", (x2, y2))
        self.moveMouse(x2, y2)
        time.sleep(delayBetweenSlices)

    def canSwipe(self):
        return True

# always slice the virus closer to the edge
    def ordervirussBy(self, tup):
        x, y = tup
        toFilter = [self.height - y, x]
        if x > self.width * 4 / 5:
            toFilter.append(self.width - x)
        return min(toFilter)

# returns true if the line determined by [(x1, y1), (x2, y2)] doesn't slice a bomb or a bomb's path
# retained calculation formulas from original parts to make it work 
    def lineIsSafe(self, x1S, y1S, x2S, y2S):
        global bombMinDistance
        for bomb in self.bombs:
            xBomb, yBomb = bomb
            minBombDistance = 999999999
            xPrev, yPrev = 0, 0
            # from the previous frame, find which bomb is closest to our current bomb, to predict the bomb's path
            # (closest bomb from the previous frame is probably the same bomb)
            for prevBomb in self.prevBombs:
                dist = self.distPoints(prevBomb[0], prevBomb[1], xBomb, yBomb)
                if minBombDistance > dist:
                    xPrev, yPrev = prevBomb
                    dist = minBombDistance
            if xPrev == 0 and yPrev == 0:
                # no close bomb found (maybe the bomb just entered the scene?)
                continue
            # where do we expect the bomb to be, considering its previous position from the previous frame?
            predicts = [(xBomb + (xBomb - xPrev) * 3, yBomb + (yBomb - yPrev) * 3)]
            if (yBomb < self.bomgHeightCond):
                predicts.append((xBomb + (xBomb - xPrev) * 3, yBomb + self.bomdDown))
                predicts.append((xBomb, yBomb + self.bomdDown))

            # check if our swiping line interferes with the bomb's path
            for predict in predicts:
                points = 10  # points to check among the swiped line
                for i in range(points + 1):
                    xInterm = (xBomb * (points - i) + predict[0] * i) / points
                    yInterm = (yBomb * (points - i) + predict[1] * i) / points

                    points2 = 10  # points to check among the bomb's path
                    for i in range(points2 + 1):
                        xPoint = (x1S * (points2 - i) + x2S * i) / points2
                        yPoint = (y1S * (points2 - i) + y2S * i) / points2
                        dist = self.distPoints(xInterm, yInterm, xPoint, yPoint)
                        if (dist < bombMinDistance):
                            return False

            # check if our swiping lane interferes with the bomb's position
            points = 10
            for i in range(points + 1):
                xPoint = (x1S * (points - i) + x2S * i) / points
                yPoint = (y1S * (points - i) + y2S * i) / points
                dist = self.distPoints(xBomb, yBomb, xPoint, yPoint)
                if (dist < bombMinDistance):
                    return False
        return True


    def shouldSwipe(self, x1,y1):
        # self.swipeThread, img
        x1, y1 = self.realCoord(x1,y1)
        res = True
        for key in list(self.cacheCoord):
            x2, y2 = key
            # remove cached swipes which are too old
            if (self.cacheCoord[key] < time.time() - self.cacheTime):
                del self.cacheCoord[key]
                continue
            dist = self.distPoints(x1, y1, x2, y2)
            # is our current position too close to a cached area?
            if dist < self.cacheDistance:
                res = False
        if res == False:
            return False

        # try different angles to swipe on virus
        # magic numers to test and get correct slicing (can still be improved by more testing)
        swipeTries2 = [
                            (x1-100,y1 + 120, x1+120,y1 - 100),
                            (x1-200,y1 + 180, x1+210,y1 - 250),
                            (x1 + 120,y1 + 80, x1 + 12,y1 - 150),
                            (x1 - 120,y1 + 80, x1 - 12,y1 - 150),
                            (x1 + 150,y1 + 50, x1 + 15,y1 - 130),
                            (x1 - 150,y1 + 50, x1 - 15,y1 - 130),
                        ]

        for curTry in swipeTries2:
            x1S, y1S, x2S, y2S = curTry
            # swipe in a separate thread to efficiently make it work without lagging
            if self.lineIsSafe(x1S, y1S, x2S, y2S):
                self.swipe(x1S, y1S, x2S, y2S)
                points = 10
                # donot slice in same areas
                for i in range(points + 1):
                    xPoint = (x1S * (points - i) + x2S * i) / points
                    yPoint = (y1S * (points - i) + y2S * i) / points
                    self.cacheCoord[self.realCoord(xPoint, yPoint)] = time.time()
                return True
        return False


