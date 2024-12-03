import pygame as pg
import sys, time

class Scene():
    def __init__(self, surface):
        self.state = "menu"
        self.window = surface

    def menu(self):
        pg.draw.rect( self.window, (123,63,134), (100,100,100,100) )
    
    def selector(self):
        if self.state == "menu":
            self.menu()
        elif self.state == "gameplay":
            self.game()
        elif self.state == "pause":
            self.pause()
