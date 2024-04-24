#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:38:58 2024

@author: abbymalone
"""
import pygame, simpleGE, random

class Panda(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("panda.png")
        self.setSize(100, 100)
        self.position = (100, 100)       
    
    def process(self):
        self.addForce(.1, 270)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.dy = 0
            self.addForce(5, 90)    
    def reset(self):
        self.x = random.randint(0, self.scene.background.get_width())
        self.y = 20
        self.dy = random.randint(5, 15)
         
    def checkBounds(self):                     
        if self.bottom > self.scene.background.get_height():
            self.reset()
            
class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (80, 200))
        self.setImage("bamboo.png")
        self.position = (600, 0)    
        self.dx = -3
        
    def checkBounds(self):
        #only check for leave left
        if self.x < 0:
            self.scene.reset()
            
    def process(self):
        if self.collidesWith(self.scene.Panda):
            self.scene.reset() 
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.Panda = Panda(self)
        self.setImage("forest.jpg")
        self.upperBarrier = Barrier(self)
        self.lowerBarrier = Barrier(self)
        self.gap = 400
        self.reset()
        self.sprites = [self.Panda, self.upperBarrier, self.lowerBarrier]
        
    def reset(self):        
        self.topPosition = random.randint(0, 200)
        self.bottomPosition = self.topPosition + self.gap
        self.upperBarrier.position = (640, self.topPosition)
        self.lowerBarrier.position = (640, self.bottomPosition)
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
        
        