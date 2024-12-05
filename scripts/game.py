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
        self.font = pg.font.Font( '../../../Downloads/celtic_bit/celtic-bit.ttf', 48 )
        self.font1 = pg.font.Font( None, 48 )
        self.screen_dimensions = ( self.screen_width, self.screen_height )
#        self.dummy_screen = pg.Surface( self.screen_dimensions )
        self.window = pg.display.set_mode( self.screen_dimensions )

        # other modules
        self.scene = Scene(self.window, self.screen_dimensions, self.font)

    def run(self):
        # main loop for the App
        while self.running:
            self.clock.tick(60)
            self.window.fill( (103,23,104) )
            
            self.events() 
            self.scene.selector()

            fps = "%.2f" % self.clock.get_fps()
            self.window.blit( self.font1.render( fps, True, (0,0,0) ), (0, 0) )
            pg.display.update()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
