import pygame,sys,time
import common
from screen import Screen
from player import Player

class Game():
    def __init__(self) -> None:
        # non imp
        self.state = "menu"
        self.fps = 60

        # imp
        self.clock = pygame.time.Clock()
        self.screen = Screen()
        self.player = Player()

    # the loop running the game
    def game_loop(self) -> None:

        while True:
            self.deltime()
            self.selector()
            self.clock.tick(self.fps)
        
    def menu(self) -> None:
        self.events()
        self.screen.menu() # execute the menu screen
                    
    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        
    # calculating the deltatime
    def deltime (self) -> None:
        common.time2 = time.time()
        common.dt = 60 * (common.time2 - common.time1)
        common.time1 = time.time()


    def selector(self) -> None: 
        if self.state == "menu":
            self.menu()
