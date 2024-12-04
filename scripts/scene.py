import pygame as pg
import sys, time
from .map import Map

class Scene():
    def __init__(self, surface, surface_length):
        self.state = "menu"
        self.window = surface
        self.window_dimensions = surface_length
        self.font = pg.font.Font( None, 48 )
        self.map = None

    def menu(self):
        self.window.blit( self.font.render( "Dungeoon", True, (0,0,0)), ( 200,200) )
        keys = pg.key.get_pressed()

        # handling key input
        if keys[ pg.K_RETURN ]:
            self.map = Map(self.window_dimensions)
            self.state = "gameplay"

    def game(self):
        self.map.blit_map( self.window )
        
    def pause(self):
        pass

    def map(self):
        pass
    
    def selector(self):
        if self.state == "menu":
            self.menu()
        elif self.state == "gameplay":
            self.game()
        elif self.state == "pause":
            self.pause()
