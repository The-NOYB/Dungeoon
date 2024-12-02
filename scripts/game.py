import pygame as pg
import sys, time
from .scene import Scene

class Game():
    def __init__(self):
        pg.init()

        self.running = True
        self.clock = pg.time.Clock()

        # screen and window related stuff
        self.screen_width, self.screen_height = 1280,720
        self.screen_dimensions = ( self.screen_width, self.screen_height )
#        self.font = pg.font.Font( False, 48)
        self.dummy_screen = pg.Surface( self.screen_dimensions )
        self.window = pg.display.set_mode( self.screen_dimensions )

        # other modules
        self.scene = Scene(self.window)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.window.fill( (123,63,134) )
            
            self.events() 
            self.scene.selector()

            pg.display.update()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.exit()
            if event.type == pg.KEYDOWN:
                pass
