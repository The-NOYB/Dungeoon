import pygame,math,sys,time
from common import *
from game import Game

pygame.init()

if __name__ == '__main__':
    app = Game()
    app.game_loop()
