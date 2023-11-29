import pygame 

pygame.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)
RUNNING=True
screen.fill("white")
pygame.display.flip()

class playerTask(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
        
taskbar=playerTask("final-project-team-hagil/assets/test.png",540,400)
taskbar_group=pygame.sprite.Group(taskbar)# image size should be < 686x52px
taskbar_group.draw(screen)
pygame.display.flip()
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            