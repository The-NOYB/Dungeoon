import pygame,math,sys,time,json,random
import pygame.gfxdraw

#with open("data/map.json","r") as file:
#        data = json.load(file)
#        world = data["theworld"]["world"]
#        events = data["theworld"]["events"]
#        start = data["theworld"]["spawn"]


world = [ [ 1 for x in range(15) ] for y in range(15)]
print(world)

def mapblit(valx,valy,dx=0,dy=0):
    midx = 720
    midy = 405

    for y,row in enumerate(world):
        for x, col in enumerate(row):
           window.blit(block,(midx + (x-1)*valx - y*valx+ dx, midy - (15 - y)*valy + x * valy + dy))

#frost_wand = pygame.image.load("frost wand.png")


class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,di=None):
        pygame.sprite.Sprite.__init__(self)
        self.dir = di
        self.x,self.y = x,y
        self.dx,self.dy = 0,0

        self.rect = pygame.FRect(0,0,360,220) # this one is dummy
        self.actrect = pygame.FRect((0,0),(21,21))

        self.rect.center = (self.x,self.y)
        self.actrect.center = (self.x,self.y)

        self.image = pygame.Surface((360,220))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
#        pygame.gfxdraw.filled_polygon(self.image,[(180,0),(0,110),(180,220),(360,110)],(150,150,150))
        pygame.gfxdraw.filled_ellipse(self.image,180,110,120,110,(255,255,255))
        self.image.set_alpha(50)

    def update(self,hdx=0,hdy=0):

        dx,dy = 0,0

        if self.dir == "right":
            dx += 1.5 * dt
            dy += .9 * dt 
        elif self.dir == "up":
            dx += 1.5 * dt
            dy -= .9 * dt
        elif self.dir == "left":
            dx -= 1.5 * dt
            dy -= .9 * dt
        elif self.dir == "down":
            dx -= 1.5 * dt
            dy += .9 * dt

        self.x += dx
        self.y += dy
#        self.rect.center = (self.x,self.y)
        self.dx,self.dy = dx,dy

pygame.init()
fontt = pygame.font.Font(None,size=48)
window = pygame.display.set_mode((1440,810))

pygame.display.set_caption("The Snexplorer")
clock = pygame.time.Clock()

block = pygame.transform.scale(pygame.image.load("newblock.png"),(120,104))
#block = pygame.image.load("sprites/newblock.png")
block = block.convert_alpha()

time1,time2,dt = 0,0,0.16

player = Square(720,405)
snakebod = pygame.sprite.Group()
snakebod.add(player)


while True:
    time2 = time.time()
    dt = 60 * (time2 - time1)
    time1 = time.time()

    window.fill((123,69,30))

    dx,dy=player.dx,player.dy
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quitting 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.dir = "up"
            elif event.key == pygame.K_a:
                player.dir = "left"
            elif event.key == pygame.K_s:
                player.dir = "down"
            elif event.key == pygame.K_d:
                player.dir = "right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player.dir == "up":
                player.dir = None
            elif event.key == pygame.K_a and player.dir == "left":
                player.dir = None
            elif event.key == pygame.K_s and player.dir == "down":
                player.dir = None
            elif event.key == pygame.K_d and player.dir == "right":
                player.dir = None
            
    fps = dt**-1*60
    fps = "%.2f" % fps
    window.blit(fontt.render(fps,True,(0,0,0)),(0,0))

    mapblit(60,36,720-player.x,405-player.y)

#    for i in range(1,5):
#        pygame.gfxdraw.pie(window,720,405,100,(i-1)*(90),i*(90),(255,255,255))

#    pygame.gfxdraw.filled_polygon(window,[(719-3*60,404),(719,404-3*36),(719+3*60,404),(719,404+3*36)],(150,100,100))
#    pygame.gfxdraw.filled_circle(window,720,405,75,(150,100,100))

#    window.blit(frost_wand,(player.x,player.y))
    snakebod.update()
    snakebod.draw(window)
    pygame.gfxdraw.rectangle(window,player.actrect,(150,100,100))
    pygame.gfxdraw.rectangle(window,player.rect,(150,100,100))
    pygame.display.update()
    clock.tick(60)
