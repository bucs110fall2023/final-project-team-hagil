from typing import Any
import pygame 
import random

pygame.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)
RUNNING=True
clock=pygame.time.Clock()
pygame.display.flip()
screen.fill("white")
answer=[]
count=0


OG_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key.png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key.png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key.png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key.png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key.png",
}
Al_KEY={
    
    "w_key":"final-project-team-hagil/assets/keyboard/w key(after).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(after).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(after).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(after).png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key(after).png",
}


def evaluate_xdistance(obstacle_sequence):
    if obstacle_sequence==10 or obstacle_sequence==6:
        x=310
    elif obstacle_sequence==7 or obstacle_sequence==8 or obstacle_sequence==9:
        x=300
    elif obstacle_sequence==3 or obstacle_sequence==4 or obstacle_sequence==5:
        x=420-(obstacle_sequence-3)*50
    return x
def evaluate_ydistance(obstacle_sequence):
    if obstacle_sequence==10 or obstacle_sequence==6:
        if obstacle_sequence==10:
            y=50
        else:
            y=90
    elif obstacle_sequence==7 or obstacle_sequence==8 or obstacle_sequence==9:
        y=80-(obstacle_sequence-7)*10
    elif obstacle_sequence==3 or obstacle_sequence==4 or obstacle_sequence==5:
        y=110
    return y
class Taskbar(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.surface=pygame.Surface([600,600])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
    def update(self) :
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    self.image=pygame.image.load("final-project-team-hagil/assets/keyboard/w key.png")
class Group(pygame.sprite.Group):
    def update(self):
        for Object in self.sprites():
            Object.update()

taskbar=Taskbar("final-project-team-hagil/assets/taskbar/sunset.png",540,570)
taskbar_group=Group()
obstacle_group=Group()
taskbar_group.add(taskbar)
taskbar_group.draw(screen)


key=[]
order={}
while True:
    obstacle_sequence =random.randrange(3,11)
    x_coord=evaluate_xdistance(obstacle_sequence)
    y_coord=550
    distance=evaluate_ydistance(obstacle_sequence)
    answer=[]
    coordinate=[]
    final=[]
    for i in range(obstacle_sequence):
        newkey=["w_key","s_key","a_key","d_key"]
        generatekey=(random.choice(newkey))
        answer.append(generatekey)
        
        obstacle=Obstacle(OG_KEY[generatekey],x_coord,y_coord)
        location=(x_coord,y_coord)
        coordinate.append(location)
        
        
        obstacle_group.add(obstacle)
        
        

        pygame.time.wait(100)
        pygame.display.update()
        x_coord+=distance
        obstacle_group.draw(screen)
        pygame.display.update()
    #for k in answer:
        #order[k]= 
        
    print(answer)
    for i in range(obstacle_sequence):
        order[answer[i]]=coordinate[i]
        final.append(order[answer[i]])
    print (final)  
    pygame.time.wait(1000)
    obstacle_group.empty()
    
    
    # image size should be < 686x52px 
    taskbar_group.draw(screen)
            
    
    pygame.time.wait(100)

    pygame.display.flip()

            