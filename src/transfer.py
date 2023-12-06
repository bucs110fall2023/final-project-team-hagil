import pygame 
import random
import time
import threading
import sys


# Initialize Pygame
pygame.init()

# Set size of Screen Size
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill("white")
pygame.display.flip()

# Set Music
music = pygame.mixer.music.load("final-project-team-hagil/assets/musics/careless.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)




font=pygame.font.Font(None,49)

OG_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key.png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key.png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key.png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key.png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key.png"
}
AL_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key(after).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(after).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(after).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(after).png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key(after).png"
    
}
FALSE_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key(wrong).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(wrong).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(wrong).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(wrong).png"
}    
BG={
    "dreamy":"final-project-team-hagil/assets/background/dreamy.png",
    "mountain":"final-project-team-hagil/assets/background/mountain.png",
    "nightsky":"final-project-team-hagil/assets/background/nightsky.png",
    "redsky":"final-project-team-hagil/assets/background/redsky.png",
    "sunset":"final-project-team-hagil/assets/background/sunset.png"
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
        self.rect.x=pos_x
        self.rect.y=pos_y
    def update(self,img,new_x_pos,new_y_pos) :
        self.image=pygame.image.load(img)
        self.rect.x=new_x_pos
        self.rect.y=new_y_pos

class Keyboard(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.image=pygame.Surface([700,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
                         
class Group(pygame.sprite.Group):
    def update(self):
        for Object in self.sprites():
            Object.update()
        


def evaluate_time(current_time,start_time,obstacle_group):
    if current_time-start_time>1000:
        obstacle_group.empty()
        Testing=False
                  
                    
def choose_random(list_name):
    selection=[]
    chosen_value=()
    for k in list_name :
        selection.append(k)
    chosen_value=random.choice(selection)
    return chosen_value

def evaluate_xdistance(obstacle_sequence):
    if obstacle_sequence==10 or obstacle_sequence==6:
        x=300
    elif obstacle_sequence==7 or obstacle_sequence==8 or obstacle_sequence==9:
        x=290
    elif obstacle_sequence==3 or obstacle_sequence==4 or obstacle_sequence==5:
        x=400-(obstacle_sequence-3)*50
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
    screen.blit(create_key(OG_KEY["space_key"]),(SCREEN_HEIGHT-150,SCREEN_WIDTH-100))

def create_key(lib):
    use_key=pygame.image.load(lib)
    return use_key



def mainloop():
    background_x=0
    taskbar_group=pygame.sprite.Group()# image size should be < 686x52px 
    random_value=choose_random(BG)
    background = pygame.image.load(BG[random_value])
    taskbar=Taskbar(TASKBAR[random_value],540,360)
    taskbar_group.add(taskbar)
    obstacle_group=pygame.sprite.Group()

    screen.blit(background, (background_x, 0))
    
    RUNNING = True
    
    aim=600
    aim2=0
    while RUNNING:
    
        right_ans=0
        wrong_ans=0
        pygame.display.update()
        screen.fill("white")
        if aim <=0:
            RUNNING=False
        msg2="You miss "+ str(aim2)
        msg= "Your aim is "+ str(aim)
        text2=font.render(msg2,True,"red")
        text=font.render(msg,True,"blue")
        screen.blit(background,(0,0))
        screen.blit(text,(SCREEN_HEIGHT/4,0))
        screen.blit(text2,(SCREEN_HEIGHT/4,100))
        
        OG_key()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    #stop_thread.is_set()
                    RUNNING = False
                    sys.exit()
            
        taskbar_group.draw(screen)
        
        pygame.display.flip()
        obstacle_sequence =random.randrange(3,11)
        x_coord=evaluate_xdistance(obstacle_sequence)
        y_coord=340
        distance=evaluate_ydistance(obstacle_sequence)
        answer=[]
        coordinate=[]
        key=["state"]
        z=0
 
                
        print(key)      
        pygame.display.update()
        for i in range(obstacle_sequence):
            newkey=["w_key","s_key","a_key","d_key"]
            generatekey=(random.choice(newkey))
            answer.append(generatekey)
                
            obstacle=Obstacle(OG_KEY[generatekey],x_coord,y_coord)
            coordinate.append(x_coord)
                
            obstacle_group.add(obstacle)
                
                

            pygame.time.wait(50)
            pygame.display.update()
            x_coord+=distance
            obstacle_group.draw(screen)
            
        pygame.display.update()
        print(answer)
        print(answer[0])
        print(coordinate[0])
        Testing=True

    
        while Testing:
            
            OG_key()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    #stop_thread.is_set()
                    RUNNING = False
                    Testing=False
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        screen.blit(create_key(AL_KEY["w_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-100))
                        key.append("w_key")
                        
                        print("up")
                    elif event.key==pygame.K_s:
                        key.append("s_key")
                    
                        screen.blit(create_key(AL_KEY["s_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-55))
                    elif event.key==pygame.K_a:
                        screen.blit(create_key(AL_KEY["a_key"]),(SCREEN_HEIGHT-1050,SCREEN_WIDTH-55))
                        key.append("a_key")
                    elif event.key==pygame.K_d:
                        screen.blit(create_key(AL_KEY["d_key"]),(SCREEN_HEIGHT-950,SCREEN_WIDTH-55))
                        key.append("d_key")             
                    elif event.key==pygame.K_SPACE:
                        key.append("submit")
                        screen.blit(create_key(AL_KEY["space_key"]),(SCREEN_HEIGHT-150,SCREEN_WIDTH-100))
                    pygame.display.flip()
                    obstacle_group.empty()
                    if key[-1]==answer[0]:        
                        obstacle.update(AL_KEY[answer[0]],coordinate[z],y_coord)
                        right_ans+=1
                        obstacle_group.add(obstacle)
                        obstacle_group.draw(screen)
                        z+=1
                        answer.pop(0)
                        obstacle_group.empty()
                    elif key[-1]!=answer[0]: 
                        if key[-1]=="submit":
                            Testing=False
                        else:       
                            obstacle.update(FALSE_KEY[answer[0]],coordinate[z],y_coord)
                            wrong_ans+=1
                            obstacle_group.add(obstacle)
                            obstacle_group.draw(screen)
                            z+=1
                            answer.pop(0)
                            obstacle_group.empty()
                        pygame.display.flip()
                    if key[-1]=="submit":
                        aim=aim-right_ans
                        aim2=aim2+wrong_ans
                        if aim2>10:
                            RUNNING=False
                    elif  answer==[]:
                        aim=aim-right_ans
                        aim2=aim2+wrong_ans
                        if aim2>10:
                            RUNNING=False
                        pygame.time.wait(20) 
                        Testing=False

                    

                pygame.display.flip()
            pygame.display.flip()
       
    screen.fill("yellow")
    pygame.display.flip()
    pygame.time.wait(1000)                    
mainloop()
 

