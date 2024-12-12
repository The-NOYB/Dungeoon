import pygame as pg
import sys, time
from .map import Map
from .player import Player

class Scene():

    def __init__(self, surface, surface_length, font):
        self.state = "menu"
        self.window = surface
        self.window_dimensions = surface_length
        self.font = font
        self.map = None
        self.group = pg.sprite.Group()

    def menu(self):
        self.window.blit( self.font.render( "Dungeoon", True, (0,0,0) ), ( 200,200) )
        key_input = pg.key.get_pressed()

        # handling key input
        if key_input[ pg.K_RETURN ]:
            self.map = Map(self.window_dimensions)
            self.player = Player()
            self.group.add( self.player )
            self.state = "gameplay"

    def game(self):
        # getting the key input
        key_input = pg.key.get_pressed()

        # bliting map -> player
        self.map.blit_map( self.window )
        self.player.update( key_input )
        self.group.draw( self.window )
        
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
