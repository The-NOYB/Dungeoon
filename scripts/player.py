import pygame as pg
import  sys, time

class Player():
    def __init__(self):
        self.health = 100
        self.vel = 32
        self.inventory = []
        self.direction = None
        self.x, self.y = [ 100, 100 ]

    def update(self, key_input):
        # key input here
        if not ( key_input[pg.K_w] or key_input[pg.K_a] or key_input[pg.K_s] or key_input[pg.K_d] ): 
            self.direction = None
        elif key_input[pg.K_w] and not ( key_input[pg.K_s] ):
            self.direction = "UP"
        elif key_input[pg.K_a] and not ( key_input[pg.K_d] ):
            self.direction = "LEFT"
        elif key_input[pg.K_s] and not ( key_input[pg.K_w] ):
            self.direction = "DOWN"
        elif key_input[pg.K_d] and not ( key_input[pg.K_a] ):
            self.direction = "RIGHT"
        
        # properties here
        if self.direction == "RIGHT":
            self.x += 3
            self.y -= 3
        elif self.direction == "LEFT":
            self.x -= 3
            self.y += 3
        elif self.direction == "DOWN":
            self.x += 3
            self.y += 3
        elif self.direction == "UP":
            self.x -= 3
            self.y -= 3

        print( f"{self.direction = }, {self.x = }, {self.y = }")
    
    def C(self):
        pass
