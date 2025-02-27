import pygame
from pygame.locals import *
import random
import pygwidgets


# Fruit class
class Fruit():

    def __init__(self, window, windowWidth, windowHeight, fruitType, points=15):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        # self.image = pygwidgets.Image(window, (0, 0), 'images/apple.png')
        self.fruitType = fruitType     # It stores the fruit type (e.g., 'apple', 'banana', 'pear', etc)
        self.points = points

        # It builds the file name of the matching fruit file on the fly.
        imagePath = f'images/{self.fruitType}.png'
        self.image = pygwidgets.Image(window, (0, 0), imagePath)

        # A rect is made up of [x, y, width, height]
        startingRect = self.image.getRect()
        self.width = startingRect[2]  # width
        self.height = startingRect[3]  # height

        # Choose a random speed in the y direction
        self.ySpeed = random.randrange(5, 9)
        self.maxX = self.windowWidth - self.width
        self.reset()

    def reset(self):
        # Pick a random starting position
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(-450, -self.height)
        self.image.setLoc((self.x, self.y))

    def update(self):
        # check for going off screen, move to above the windows
        if self.y > self.windowHeight:
            self.reset()

        # move location
        self.y = self.y + self.ySpeed
        self.image.setLoc((self.x, self.y))


    def getRect(self):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return myRect

    def draw(self):
        self.image.draw()

    def getPoints(self):
        # Return the point value of the fruit
        return self.points
