import pygame,sys,time

class Map():

    def __init__( self ) -> None:
        self.level = [ [ 1 for x in range(15) ] for y in range(15)]
        self.path = "data/maps/"
        self.block = "data/sprites/newblock.png"


    def loadmap( self ) -> None:
        pass
    
    def C(self) -> None:
        pass
