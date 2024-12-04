import pygame,sys,time

class Map():

    def __init__(self, dimensions) -> None:
        self.level = [ [ 1 for x in range(15) ] for y in range(15)]
        self.block = pygame.transform.scale( pygame.image.load("data/sprites/newblock.png"), (120, 104) )
        self.TILESIZE_x = 60
        self.TILESIZE_y = 35
        self.window_dimensions = dimensions
        self.midx, self.midy = [ x//2 for x in self.window_dimensions ]

    def loadmap( self ) -> None:
        pass
    
    def blit_map(self, screen) -> None:

        for y, row in enumerate( self.level ):
            for x, col in enumerate( row ):
                screen.blit( self.block, (self.midx + (x-1)*self.TILESIZE_x - y*self.TILESIZE_x, self.midy - (15 - y)*self.TILESIZE_y + x * self.TILESIZE_y ) )
