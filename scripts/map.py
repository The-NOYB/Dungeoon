import pygame,sys,time

class Map():

    def __init__( self ) -> None:
        self.level = [ [ 1 for x in range(15) ] for y in range(15)]
        self.block = "data/sprites/newblock.png"


    def loadmap( self ) -> None:
        pass
    
    def blit_map(self, screen) -> None:
        for y, row in enumerate(world):
            for x, col in enumerate(row):
                screen.blit( self.block, (midx + (x-1)*valx - y*valx+ map_del.x, midy - (15 - y)*valy + x * valy + map_del.y) )
