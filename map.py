import pygame,sys,time
from common import *


class Map():

    def __init__(self):
        self.level = [ [ 1 for x in range(15) ] for y in range(15)]
        self.path = "data/maps/"

    def mapblit(screen,valx,valy,dx=0,dy=0):
    
        map_del.x -= dx
        map_del.y -= dy
    
        for y,row in enumerate(world):
            for x, col in enumerate(row):
                screen.blit(block,(midx + (x-1)*valx - y*valx+ map_del.x, midy - (15 - y)*valy + x * valy + map_del.y))

    def loadmap(self):
        pass
    
    def C(self):
        pass

something = A()

