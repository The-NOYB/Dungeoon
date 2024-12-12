import pygame as pg
import  sys, time

class Player(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        # position and sprite stuff
        self.x, self.y = [ 100, 100 ]
        self.vel = 32
        self.image = pg.Surface( (50, 50) )
        self.rect = self.image.get_rect()

        # properties
        self.health = 100
        self.inventory = []
        self.direction = None

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
            self.x += 2
            self.y += 1.16
        elif self.direction == "LEFT":
            self.x -= 2
            self.y -= 1.16
        elif self.direction == "DOWN":
            self.x -= 2
            self.y += 1.16
        elif self.direction == "UP":
            self.x += 2
            self.y -= 1.16

        self.rect.x = self.x
        self.rect.y = self.y

        print( f"{self.direction = }, {self.x = }, {self.y = }")
    
    def C(self):
        pass
