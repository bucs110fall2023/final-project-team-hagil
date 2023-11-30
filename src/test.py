import pygame 
import random

pygame.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)
RUNNING=True
screen.fill("white")
clock=pygame.time.Clock()
pygame.display.flip()

key={
    "w_key":"final-project-team-hagil/assets/keyboard/w key.png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key.png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key.png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key.png",
}

class playerTask(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y ):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
    def update(self):
        self.kill()
obstacle=Obstacle("final-project-team-hagil/assets/keyboard/w key.png",240,400)
obstacle_group=pygame.sprite.Group(obstacle)
taskbar =playerTask("final-project-team-hagil/assets/test.png",540,400)
taskbar_group=pygame.sprite.Group(taskbar)# image size should be < 686x52px 
taskbar_group.draw(screen)

obstacle_sequence=random.randrange(3,11)

if obstacle_sequence==10 or obstacle_sequence==6:
    x=310
    if obstacle_sequence==10:
        y=50
    else:
        y=90
elif obstacle_sequence==7 or obstacle_sequence==8 or obstacle_sequence==9:
    x=300
    y=80-(obstacle_sequence-7)*10
elif obstacle_sequence==3 or obstacle_sequence==4 or obstacle_sequence==5:
    y=110
    x=420-(obstacle_sequence-3)*50
answer=[]
for i in range(obstacle_sequence):
    newkey=["w_key","s_key","a_key","d_key"]
    generatekey=(random.choice(newkey))
    answer.append(generatekey)
    obstacle=Obstacle(key[generatekey],x,400)
    obstacle_group=pygame.sprite.Group(obstacle)
    obstacle_group.draw(screen)
    pygame.time.wait(50)
    pygame.display.update()
    obstacle_group.update()
    pygame.display.update()
    x+=y
print(answer)
pygame.display.update()
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
            