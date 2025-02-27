#  Balloon Manager

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from Balloon import *
from MegaBalloon import *

#
#  BalloonMgr manages a list of Balloon objects
#
class BalloonMgr():

    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def start(self):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0

        # create 2 MegaBalloons
        for balloonNum in range(2):
            oBalloon = MegaBalloon(self.window, self.maxWidth, self.maxHeight, balloonNum)
            self.balloonList.append(oBalloon)

        # create 13 other balloons of random types
        for balloonNum in range(2, N_BALLOONS):
            randomBalloonClass = random.choice((BalloonSmall, BalloonMedium, BalloonLarge))
            oBalloon = randomBalloonClass(self.window, self.maxWidth, self.maxHeight, balloonNum)
            self.balloonList.append(oBalloon)


        # for balloonNum in range(0, N_BALLOONS):
        #   randomBalloonClass = random.choice((BalloonSmall,
        #                                                BalloonMedium, BalloonLarge, MegaBalloon))
        #   oBalloon = randomBalloonClass(self.window, self.maxWidth,
        #                                               self.maxHeight, balloonNum)
        #   self.balloonList.append(oBalloon)


    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # go 'reversed' so top-most balloon gets popped
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0: # remove this balloon
                        self.balloonList.remove(oBalloon)  
                        self.nPopped = self.nPopped + 1
                        self.score = self.score + nPoints
                    return  # no need to check others

    def getScore(self):
        return self.score

    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                # balloon went off the top, remove it
                self.balloonList.remove(oBalloon)
                self.nMissed = self.nMissed + 1

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()
