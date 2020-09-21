'''
Created on Nov 18, 2019

A simple snake game clone,
but image yourself as a caterpillar.

@author: 16368
'''

import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

class GameCons:
    '''Class to set some default game constants'''
    
    BORDER_WIDTH = 300
    BORDER_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27
    
class GameBoard(Canvas):
    '''Class to set up the game state and game logic'''
    
    def __init__(self):
        
        super().__init__(width=GameCons.BORDER_WIDTH, height=GameCons.BORDER_HEIGHT,
                       bg="black", highlightthickness=0)
        
        self.startGame()
        self.pack()
        
    def startGame(self):
        '''initializes the game'''
        
        self.inTheGame = True
        self.defaultDots = 3
        self.score = 0
        
        # Variables used to move the caterpillar object
        self.moveX = GameCons.DOT_SIZE
        self.moveY = 0
        
        # Default first apple starting coords
        self.appleX = 100
        self.appleY = 190
        
        self.loadImages()
        
        self.createGameObjects()
        self.locatingApple()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(GameCons.DELAY, self.onTimer)
        
    def loadImages(self):
        '''loads the games graphics from the disk'''
        
        try:
            self.imageDot = Image.open("dot.png")
            self.dotRendered = ImageTk.PhotoImage(self.imageDot)
            self.imageHead = Image.open("head.png")
            self.headRendered = ImageTk.PhotoImage(self.imageHead)
            self.imageApple = Image.open("apple.png")
            self.appleRendered = ImageTk.PhotoImage(self.imageApple)
            
        except IOError as error:
            
            print(error)
            sys.exit(1)
            
    def createGameObjects(self):
        '''Creates the game objects on the Canvas'''
        
        self.create_text(30, 10, text="Score: {0}".format(self.score),
                               tag='score', fill='white')
        self.create_image(self.appleX, self.appleY, image=self.appleRendered,
                               anchor=NW, tag='apple')
        self.create_image(50, 50, image=self.headRendered, anchor=NW, tag='head')
        self.create_image(30, 50, image=self.dotRendered, anchor=NW, tag='dot')
        self.create_image(40, 50, image=self.dotRendered, anchor=NW, tag='dot')
        
    def checkForAppleCollision(self):
        '''Check if the head of the caterpillar collided with the apple'''
        
        apple = self.find_withtag('apple')
        head = self.find_withtag('head')
        
        x1, y1, x2, y2 = self.bbox(head)
        overlapping = self.find_overlapping(x1, y1, x2, y2)
        
        for overlap in overlapping:
            
            if apple[0] == overlap:
                
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dotRendered, anchor=NW, tags='dot')
                self.locatingApple()
    
    def moveCaterpillar(self):
        '''Moves the caterpillar object'''
        
        body = self.find_withtag('dot')
        head = self.find_withtag('head')
        
        player = body + head
        
        i = 0
        while i < len(player) - 1:
            
            coords1 = self.coords([player[i]])
            coords2 = self.coords([player[i+1]])
            self.move(player[i], coords2[0] - coords1[0], coords2[1] - coords1[1])
            i += 1
            
        self.move(head, self.moveX, self.moveY)
        
    def checkForCollisions(self):
        '''Checks for any kind of collision'''
        
        bodyLinks = self.find_withtag('dot')
        head = self.find_withtag('head')
        
        x1, y1, x2, y2 = self.bbox(head)
        overlapping= self.find_overlapping(x1, y1, x2, y2)
        
        for body in bodyLinks:
            for overlap in overlapping:
                if overlap == body:
                    self.inTheGame = False
                    
        if x1 < 0:
            self.inTheGame = False
        
        if x1 > GameCons.BORDER_WIDTH - GameCons.DOT_SIZE:
            self.inTheGame = False
            
        if y1 < 0:
            self.inTheGame = False
            
        if y1 > GameCons.BORDER_HEIGHT - GameCons.DOT_SIZE:
            self.inTheGame = False
            
    def locatingApple(self):
        '''Places the apple object somewhere on the Canvas'''
        
        apple = self.find_withtag('apple')
        self.delete(apple[0])
        
        r = random.randint(0, GameCons.MAX_RAND_POS)
        self.appleX = r * GameCons.DOT_SIZE
        r = random.randint(0, GameCons.MAX_RAND_POS)
        self.appleY = r * GameCons.DOT_SIZE
        
        self.create_image(self.appleX, self.appleY, anchor=NW,
                          image=self.appleRendered, tag='apple')
    
    def onKeyPressed(self, e):
        '''Controls direction variables with cursor keys'''
        
        key = e.keysym
        
        LEFT_CURSOR_KEY = 'Left'
        if key == LEFT_CURSOR_KEY and self.moveX <=0:
            
            self.moveX = -GameCons.DOT_SIZE
            self.moveY = 0
        
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:

            self.moveX = GameCons.DOT_SIZE
            self.moveY = 0

        RIGHT_CURSOR_KEY = "Up"
        if key == RIGHT_CURSOR_KEY and self.moveY <= 0:

            self.moveX = 0
            self.moveY = -GameCons.DOT_SIZE

        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.moveY >= 0:

            self.moveX = 0
            self.moveY = GameCons.DOT_SIZE
            
    def onTimer(self):
        '''Creates a game cycle each timer event'''
        
        self.drawScore()
        self.checkForCollisions()
        
        if self.inTheGame:
            self.checkForAppleCollision()
            self.moveCaterpillar()
            self.after(GameCons.DELAY, self.onTimer)
        else:
            self.gameOver()
            
    def drawScore(self):
        '''Draws the score'''
        
        score = self.find_withtag('score')
        self.itemconfigure(score, text="Score: {0}".format(self.score))
        
    def gameOver(self):
        '''Deletes all objects and draws a game over message'''
        
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                         text="Game Over with a Score of {0}".format(self.score), fill='white')
        
class Caterpillar(Frame):
    '''Class to start the game instance'''
    
    def __init__(self):
        super().__init__()
        
        self.master.title('Caterpillar')
        self.board = GameBoard()
        self.pack()
        
def main():
    
    root = Tk()
    game = Caterpillar()
    root.mainloop()
    
if __name__ == '__main__':
    main()