import pygame


pygame.init()


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)

Surface1=pygame.Surface([1080,720])
ex_box=pygame.Surface([400,600])
pygame.display.update()
def background():
    background = pygame.image.load("assets/gui.jpg")
    background_width = background.get_width()
    background_x = 0

    RUNNING = True

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        # Scroll the background
        background_x -= 1
        if background_x <= -background_width:
            background_x = 0

        # Render the background
        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + background_width, 0))

        pygame.display.update()

def control():
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(w_key_after,((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.blit(s_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-55))
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.blit(a_key_after,((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.blit(d_key_after,((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    screen.blit(space_key_after,(((SCREEN_HEIGHT-200), SCREEN_WIDTH-100)))
                
                pygame.display.update()
                
                pygame.time.wait(10)

    

class controlKey():
    def __init__(self,image,x_coord,y_coord):
        self.image=pygame.image.load("")
        self.image=x_coord
        self.image=y_coord
    def active(self):
        self.new_image=pygame.image.load("")
         
w_key = pygame.image.load("final-project-team-hagil/assets/keyboard/w key.png")
w_key_after = pygame.image.load("final-project-team-hagil/assets/keyboard/w key(after).png")

s_key = pygame.image.load("final-project-team-hagil/assets/keyboard/s key.png")
s_key_after = pygame.image.load("final-project-team-hagil/assets/keyboard/s key(after).png")

a_key = pygame.image.load("final-project-team-hagil/assets/keyboard/a key.png")
a_key_after = pygame.image.load("final-project-team-hagil/assets/keyboard/a key(after).png")

d_key = pygame.image.load("final-project-team-hagil/assets/keyboard/d key.png")
d_key_after = pygame.image.load("final-project-team-hagil/assets/keyboard/d key(after).png")

space_key = pygame.image.load("final-project-team-hagil/assets/keyboard/space key.png")
space_key_after = pygame.image.load("final-project-team-hagil/assets/keyboard/space key(after).png")

class playerTask(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.surface=pygame.Surface([600,600])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
        
        
taskbar =playerTask("final-project-team-hagil/assets/taskbar/sunset.png",540,550)
taskbar_group=pygame.sprite.Group(taskbar)# image size should be < 686x52px



pygame.display.update()
pygame.time.wait(10)

RUNNING = True

background = pygame.image.load("final-project-team-hagil/assets/background/sunset.png")
background_width = background.get_width()
background_x = 0
Playing=True

pygame.display.flip()  
    
while RUNNING:
    
    background_x -= 1
    if background_x <= -background_width:
        background_x = 0

    Surface1.blit(background, (background_x, 0))
    
    Surface1.blit(background, (background_x + background_width, 0))
    
    Surface1.blit(w_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))

    Surface1.blit(a_key, ((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))

    Surface1.blit(s_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-55)))

    Surface1.blit(d_key, ((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))

    Surface1.blit(space_key, ((SCREEN_HEIGHT-200), (SCREEN_WIDTH-100)))    
    
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    Surface1.blit(w_key_after,((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))
                elif event.key==pygame.K_s:
                    print("Down")
                    Surface1.blit(s_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-55))
                elif event.key==pygame.K_a:
                    print("Left")
                    Surface1.blit(a_key_after,((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_d:
                    print("Right")
                    Surface1.blit(d_key_after,((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    Surface1.blit(space_key_after,(((SCREEN_HEIGHT-200), SCREEN_WIDTH-100)))
                
                pygame.display.update()
                
                pygame.time.wait(10)
    
    
    screen.blit(Surface1,(0,0))
    taskbar_group.draw(screen)
    pygame.display.update()
        # Render the background

    

    
    pygame.display.update()
    
    pygame.time.wait(5)

#hello