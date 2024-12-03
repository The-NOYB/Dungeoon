import pygame,sys,time

class Item():
    def __init__(self, name, quantity, description, timer, effect):
        self.NAME = name
        self.QUANTITY = quantity
        self.DESCRIPTION = description
        self.TIMER = timer
        self.AFTERUSE = effect

    def B(self):
        pass
    
    def C(self):
        pass
