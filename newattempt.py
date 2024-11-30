import pygame,math,sys,time,json,random
import pygame.gfxdraw

#with open("data/map.json","r") as file:
#        data = json.load(file)
#        world = data["theworld"]["world"]
#        events = data["theworld"]["events"]
#        start = data["theworld"]["spawn"]


world = [ [ 1 for x in range(15) ] for y in range(15)]

midx = 720
midy = 405

map_del = pygame.math.Vector2(0,0)

def vision_blit(direction,dir_vecs):
    dx1,dy1 = dir_vecs[direction][0]*60, dir_vecs[direction][1]*35*3
    dx2,dy2 = dir_vecs[direction][0]*60*3, dir_vecs[direction][1]*35

    pygame.gfxdraw.filled_trigon(screen,720,405,720+dx1,405+dy1,720+dx2,405+dy2,(255,255,255))
    pygame.gfxdraw.filled_ellipse(screen,720,405,30,30,(255,255,255))
    
def mapblit(screen,valx,valy,dx=0,dy=0):

    map_del.x -= dx
    map_del.y -= dy

    for y,row in enumerate(world):
        for x, col in enumerate(row):
            screen.blit(block,(midx + (x-1)*valx - y*valx+ map_del.x, midy - (15 - y)*valy + x * valy + map_del.y))

frost_wand = pygame.image.load("data/sprites/frost wand.png")

view_rect = pygame.FRect(0,0,660,370)
view_rect.center = [midx,midy]
view_rect_mask = pygame.mask.from_surface(pygame.Surface((660,370)))

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,di=0):
        pygame.sprite.Sprite.__init__(self)
        self.dir = di # up-left-down-right 1-2-3-4
        self.num_dir = di # up-left-down-right 1-2-3-4
        self.change_dir_bool = False
        self.x,self.y = x,y
        self.dx,self.dy = 0,0

        # for vision trigons
        self.dir_vecs = [( 1,-1 ),( -1,-1 ),( -1,1 ),( 1,1 )]



#        self.rect = pygame.FRect(0,0,180,110) # this one is dummy
        self.rect = pygame.FRect((0,0),(21,21))

        self.rect.center = (self.x,self.y)
#        self.actrect.center = (self.x,self.y)

        self.image = frost_wand
#        self.image = pygame.Surface((180,110))
#        self.image.blit(frost_wand,(90-frost_wand.get_width(),55 - frost_wand.get_height()))
#        self.image.fill((0,0,0))
#        self.image.set_colorkey((0,0,0))
#        pygame.gfxdraw.filled_polygon(self.image,[(180,0),(0,110),(180,220),(360,110)],(150,150,150))

    def dirchange(self):
        self.change_dir_bool = False
        if self.num_dir == 3 :
            self.num_dir = 0
        else:
            self.num_dir += 1
        
    def update(self,hdx=0,hdy=0):

        if self.change_dir_bool:
            self.dirchange()

        dx,dy = 0,0

        if self.dir == "right":
            self.num_dir = 3
            dx += 1.5 * dt
            dy += .875 * dt 
        elif self.dir == "up":
            self.num_dir = 0
            dx += 1.5 * dt
            dy -= .875 * dt
        elif self.dir == "left":
            self.num_dir = 1
            dx -= 1.5 * dt
            dy -= .875 * dt
        elif self.dir == "down":
            self.num_dir = 2
            dx -= 1.5 * dt
            dy += .875 * dt

        self.x += dx
        self.y += dy
#        self.rect.center = (self.x,self.y)
        self.dx,self.dy = dx,dy

pygame.init()

sound = pygame.mixer.Sound("data/sfx/jump.wav")
#channel = pygame.mixer.find_channel()
#channel = pygame.mixer.find_channel()#Getting a Free Channel
#left,right = .1, .0
#channel.set_volume(left,right)
#channel.play(sound)

fontt = pygame.font.Font(None,size=48)
window = pygame.display.set_mode((1440,810))
screen = pygame.Surface((1440,810))
screen.set_alpha(150)

pygame.display.set_caption("The Snexplorer")
clock = pygame.time.Clock()

block = pygame.transform.scale(pygame.image.load("data/sprites/newblock.png"),(120,104))
#block = pygame.image.load("sprites/newblock.png")
block = block.convert_alpha()

mask = pygame.mask.from_surface(screen)
mask_outline = mask.outline()

time1,time2,dt = 0,0,0.16

player = Square(720,405)
snakebod = pygame.sprite.Group()
snakebod.add(player)

while True:
    time2 = time.time()
    dt = 60 * (time2 - time1)
    time1 = time.time()

    window.fill((0,0,0))
    screen.fill((0,0,0))

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
            if event.key == pygame.K_SPACE:
                player.change_dir_bool = True
#            if event.key == pygame.K_SPACE and channel.get_volume() == [1,0]:
#                channel.set_volume(0,1)
#            elif event.key == pygame.K_SPACE:
#                channel.set_volume(1,0)
                        
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
    screen.blit(fontt.render(fps,True,(200,200,200)),(0,0))

#    print(channel.get_volume())
    mapblit(window,60,35,dx,dy)

#        scrolling = True
#        # keep on updating the scroll value of the map object
#        mapblit(window,60,35,dx,dy)
#        view_rect.x += dx
#        view_rect.y += dy
#    else:
#        scrolling = False
#        # stop updating the scroll value of the map object, so that player appears moving
#        mapblit(window,60,35,0,0)
#        player.rect.x += dx
#        player.rect.y += dy

#    for i in range(1,5):
#        pygame.gfxdraw.pie(window,720,405,100,(i-1)*(90),i*(90),(255,255,255))

#    pygame.gfxdraw.filled_polygon(window,[(719-3*60,404),(719,404-3*36),(719+3*60,404),(719,404+3*36)],(150,100,100))
#    pygame.gfxdraw.filled_circle(window,720,405,75,(150,100,100))

#    window.blit(frost_wand,(player.x,player.y))
    snakebod.update()
    snakebod.draw(window)

#    pygame.gfxdraw.rectangle(window,player.actrect,(150,100,100))
    pygame.gfxdraw.rectangle(window,player.rect,(150,100,100))
#    pygame.gfxdraw.rectangle(screen,view_rect,(150,100,100))
    pygame.gfxdraw.polygon(screen,mask_outline,(255,255,255))

    vision_blit(player.num_dir,player.dir_vecs)
    screen.set_colorkey((255,255,255))

    window.blit(screen,(0,0))
    pygame.display.update()
    clock.tick(60)
