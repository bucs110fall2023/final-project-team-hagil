import pygame 
import time
import random

pygame.init()


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
RUNNING=True
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill("white")
pygame.display.flip



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
BG={
    "dreamy":"final-project-team-hagil/assets/background/dreamy.png",
    "mountain":"final-project-team-hagil/assets/background/mountain.png",
    "nightsky":"final-project-team-hagil/assets/background/nightsky.png",
    "redsky":"final-project-team-hagil/assets/background/redsky.png",
    "sunset":"final-project-team-hagil/assets/background/sunset.png",
    
}
TASKBAR={
    "mountain":"final-project-team-hagil/assets/taskbar/mountain.png",
    "nightsky":"final-project-team-hagil/assets/taskbar/nightsky.png",
    "redsky":"final-project-team-hagil/assets/taskbar/redsky+dreamy.png",
    "dreamy":"final-project-team-hagil/assets/taskbar/redsky+dreamy.png",
    "sunset":"final-project-team-hagil/assets/taskbar/sunset.png"

}
class Taskbar(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.surface=pygame.Surface([600,600])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y ):
        super().__init__()
        self.image=pygame.Surface([700,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]

class GameKey(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y ):
        super().__init__()
        self.image=pygame.Surface([50,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
        


        
def choose_random(list_name):
    selection=[]
    chosen_value=()
    for k in list_name :
        selection.append(k)
    chosen_value=random.choice(selection)
    return chosen_value


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



def OG_key():

    screen.blit(create_key(OG_KEY["w_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-100))
    screen.blit(create_key(OG_KEY["s_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-55))
    screen.blit(create_key(OG_KEY["a_key"]),(SCREEN_HEIGHT-1050,SCREEN_WIDTH-55))
    screen.blit(create_key(OG_KEY["d_key"]),(SCREEN_HEIGHT-950,SCREEN_WIDTH-55))
    screen.blit(create_key(OG_KEY["space_key"]),(SCREEN_HEIGHT-200,SCREEN_WIDTH-100))
  


def create_key(lib):
    use_key=pygame.image.load(lib)
    return use_key


def mainloop():
    background_x=0
    
    obstacle_group=pygame.sprite.Group()

    taskbar_group=pygame.sprite.Group()# image size should be < 686x52px 
    random_value=choose_random(BG)
    background = pygame.image.load(BG[random_value])
    taskbar=Taskbar(TASKBAR[random_value],540,550)
    taskbar_group.add(taskbar)
   
    background_width = background.get_width()
    RUNNING=True
    Playing=True
    
    
    
    while RUNNING:
        
        obstacle_sequence=()
        
        background_x -= 1
        if background_x <= -background_width:
            background_x = 0

        screen.blit(background, (background_x, 0))
    
        screen.blit(background, (background_x + background_width, 0))
        
        taskbar_group.draw(screen)

        OG_key()
        Playing= True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(create_key(Al_KEY["w_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-100))
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.blit(create_key(Al_KEY["s_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-55))
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.blit(create_key(Al_KEY["a_key"]),(SCREEN_HEIGHT-1050,SCREEN_WIDTH-55))
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.blit(create_key(Al_KEY["d_key"]),(SCREEN_HEIGHT-950,SCREEN_WIDTH-55))
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    screen.blit(create_key(Al_KEY["space_key"]),(SCREEN_HEIGHT-200,SCREEN_WIDTH-100))
                    
                pygame.display.update()
        pygame.display.update()
        
        while Playing:
            obstacle_sequence =random.randrange(3,11)
            x=evaluate_xdistance(obstacle_sequence)
            y=evaluate_ydistance(obstacle_sequence)
            answer=[]
            for i in range(obstacle_sequence):
                
                newkey=["w_key","s_key","a_key","d_key"]
                generatekey=(random.choice(newkey))
                answer.append(generatekey)
                obstacle=Obstacle(OG_KEY[generatekey],x,550)
                obstacle_group.add(obstacle)

                pygame.time.wait(100)
                pygame.display.update()
                x+=y
                obstacle_group.draw(screen)
                pygame.display.update()
            
            obstacle_group.empty()
            pygame.time.wait(2000)# image size should be < 686x52px 
            taskbar_group.draw(screen)
            Playing=False

mainloop()
 

