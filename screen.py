import pygame,sys,time
import common

class Screen():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode( (common.WIDTH, common.HEIGHT) )
        self.font = pygame.font.Font( None, size=48 )
        pygame.display.set_caption("Dungeoon")

    def load(self) -> None:
        pygame.display.update()
        pass
    
    def menu(self) -> None:
        self.window.fill( (100,100,100) )
        self.show_fps()
        pygame.display.update()
        

    def pause(self) -> None:
        pygame.display.update()
        pass

    def run(self) -> None:
        pygame.display.update()
        pass

    def show_fps(self) -> None:
        fps = common.dt**-1*60
        fps = "%.2f" % fps

        self.window.blit( self.font.render( fps, True, (0,0,0) ), (0,0) )
