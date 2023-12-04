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

FALSE_KEY={
    
    "w_key":"final-project-team-hagil/assets/keyboard/w key(wrong).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(wrong).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(wrong).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(wrong).png",
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
    "sunset":"final-project-team-hagil/assets/taskbar/sunset.png",

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
   
    RUNNING=True
    screen.blit(background, (background_x, 0))
    right_ans=0
    wrong_ans=0
    
    
    while RUNNING:
        
        
        OG_key()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
            
        taskbar_group.draw(screen)

        
        
        obstacle_sequence =random.randrange(3,11)
        x_coord=evaluate_xdistance(obstacle_sequence)
        y_coord=530
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
                    Testing=False
                    RUNNING = False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        screen.blit(create_key(Al_KEY["w_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-100))
                        key.append("w_key")
                        
                        print("up")
                    elif event.key==pygame.K_s:
                        key.append("s_key")
                        
                        screen.blit(create_key(Al_KEY["s_key"]),(SCREEN_HEIGHT-1000,SCREEN_WIDTH-55))
                    elif event.key==pygame.K_a:
                        screen.blit(create_key(Al_KEY["a_key"]),(SCREEN_HEIGHT-1050,SCREEN_WIDTH-55))
                        key.append("a_key")
                    elif event.key==pygame.K_d:
                        screen.blit(create_key(Al_KEY["d_key"]),(SCREEN_HEIGHT-950,SCREEN_WIDTH-55))
                        key.append("d_key")             
                    elif event.key==pygame.K_SPACE:
                        key.append("submit")
                        screen.blit(create_key(Al_KEY["space_key"]),(SCREEN_HEIGHT-200,SCREEN_WIDTH-100))
                    obstacle_group.empty()
                    if  key[-1]=="submit" and answer==[]:
                        key=[]  
                        Testing=False
                    elif answer==[]:                            
                        pygame.time.wait(10)
                        if key[-1]=="submit":
                            key=[]
                            Testing=False
                        else:
                            key=[]
                            Testing=False 
                    elif key[-1]==answer[0]:        
                        obstacle.update(Al_KEY[answer[0]],coordinate[z],y_coord)
                        right_ans+=1
                        obstacle_group.add(obstacle)
                        obstacle_group.draw(screen)
                        z+=1
                        answer.pop(0)
                        obstacle_group.empty()
                        pygame.display.flip()
                    elif key[-1]!=answer[0]:        
                        obstacle.update(FALSE_KEY[answer[0]],coordinate[z],y_coord)
                        wrong_ans+=1
                        obstacle_group.add(obstacle)
                        obstacle_group.draw(screen)
                        z+=1
                        answer.pop(0)
                        obstacle_group.empty()
                        pygame.display.flip()
    print(right_ans,wrong_ans)     
                        
mainloop()
 

