import pygame
import random
from taskbar import Taskbar
from obstacle import Obstacle
from group import Group

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


class Controller:
  
  def __init__(self):
    
    self.obstacle_group=Group()

    self.taskbar_group=Group()# image size should be < 686x52px 
    
    
    RUNNING=True
    
    #thread.start()
    self.total_win=[]
    self.total_lose=[]
    self.state="gameloop"
    self.newkey=["w_key","s_key","a_key","d_key"]
            
    self.OG_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key.png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key.png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key.png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key.png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key.png"
}
    self.Al_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key(after).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(after).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(after).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(after).png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key(after).png"
    
}
    self.FALSE_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key(wrong).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(wrong).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(wrong).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(wrong).png"
}    
    self.BG={
    "dreamy":"final-project-team-hagil/assets/background/dreamy.png",
    "mountain":"final-project-team-hagil/assets/background/mountain.png",
    "nightsky":"final-project-team-hagil/assets/background/nightsky.png",
    "redsky":"final-project-team-hagil/assets/background/redsky.png",
    "sunset":"final-project-team-hagil/assets/background/sunset.png"
}
    self.TASKBAR={
    "mountain":"final-project-team-hagil/assets/taskbar/mountain.png",
    "nightsky":"final-project-team-hagil/assets/taskbar/nightsky.png",
    "redsky":"final-project-team-hagil/assets/taskbar/redsky+dreamy.png",
    "dreamy":"final-project-team-hagil/assets/taskbar/redsky+dreamy.png",
    "sunset":"final-project-team-hagil/assets/taskbar/sunset.png",
}   
    
    
    self.SCREEN_WIDTH = 720
    self.SCREEN_HEIGHT = 1080
    self.SCREEN_SIZE = (self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
    self.RUNNING=True
    self.Testing=True
  def OG_key(self):
      
    
    self.screen.blit(pygame.image.load(self.OG_KEY["w_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-100))
    self.screen.blit(pygame.image.load(self.OG_KEY["s_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["a_key"]),(self.SCREEN_HEIGHT-1050,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["d_key"]),(self.SCREEN_HEIGHT-950,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["space_key"]),(self.SCREEN_HEIGHT-150,self.SCREEN_WIDTH-100))
  def mainloop(self):
        pygame.init()
        self.screen=pygame.display.set_mode([self.SCREEN_HEIGHT,self.SCREEN_WIDTH])
        self.screen.fill("white")

        pygame.display.flip()
        pygame.time.wait(60)
        self.gameloop()
    #select state loop
  
  ### below are some sample loop states ###

  #def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    self.random_value=choose_random(self.BG)
    self.taskbar=Taskbar(self.TASKBAR[self.random_value],540,665)
    self.taskbar_group.add(self.taskbar)     
    
    while self.RUNNING:
        self.OG_key()
    
        self.right_ans=0
        self.wrong_ans=0
        pygame.display.update()
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                    
            
        self.taskbar_group.draw(self.screen)
        
        pygame.display.flip()  
        self.obstacle_sequence =random.randrange(3,11)
        self.x_coord=evaluate_xdistance(self.obstacle_sequence)
        self.y_coord=640
        self.distance=evaluate_ydistance(self.obstacle_sequence)
        self.answer=[]
        self.coordinate=[]
        self.key=["state"]
        self.z=0
        pygame.display.update()
        for i in range(self.obstacle_sequence):
            generatekey=(random.choice(self.newkey))
            self.answer.append(generatekey)
                
            self.obstacle=Obstacle(self.OG_KEY[generatekey],self.x_coord,self.y_coord)
            self.coordinate.append(self.x_coord)
                
            self.obstacle_group.add(self.obstacle)
                
                

            pygame.time.wait(50)
            pygame.display.update()
            self.x_coord+=self.distance
            self.obstacle_group.draw(self.screen)
        self.obstacle_group.empty()    
        pygame.display.update()
        
        self.Testing=True
    
        while self.Testing:
            
            self.OG_key()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    #stop_thread.is_set()
                    self.RUNNING = False
                    self.Testing=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        self.screen.blit(pygame.image.load(self.Al_KEY["w_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-100))
                        self.key.append("w_key")
                        print("up")
                    elif event.key==pygame.K_s:
                        self.key.append("s_key")
                        self.screen.blit(pygame.image.load(self.Al_KEY["s_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-55))
                    elif event.key==pygame.K_a:
                        self.screen.blit(pygame.image.load(self.Al_KEY["a_key"]),(self.SCREEN_HEIGHT-1050,self.SCREEN_WIDTH-55))
                        self.key.append("a_key")
                    elif event.key==pygame.K_d:
                        self.screen.blit(pygame.image.load(self.Al_KEY["d_key"]),(self.SCREEN_HEIGHT-950,self.SCREEN_WIDTH-55))
                        self.key.append("d_key")             
                    elif event.key==pygame.K_SPACE:
                        self.key.append("submit")
                        self.screen.blit(pygame.image.load(self.Al_KEY["space_key"]),(self.SCREEN_HEIGHT-150,self.SCREEN_WIDTH-100))
                    pygame.display.flip()
                    self.obstacle_group.empty()
                    
                
                    if self.key[-1]==self.answer[0]:        
                        self.obstacle.update(self.Al_KEY[self.answer[0]],self.coordinate[self.z],self.y_coord)
                        self.right_ans+=1
                        self.obstacle_group.add(self.obstacle)
                        self.obstacle_group.draw(self.screen)
                        self.z+=1
                        self.answer.pop(0)
                        self.obstacle_group.empty()
                    elif self.key[-1]!=self.answer[0]:        
                        self.obstacle.update(self.FALSE_KEY[self.answer[0]],self.coordinate[self.z],self.y_coord)
                        self.wrong_ans+=1
                        self.obstacle_group.add(self.obstacle)
                        self.obstacle_group.draw(self.screen)
                        self.z+=1
                        self.answer.pop(0)
                        self.obstacle_group.empty()
                    pygame.display.flip()
                    if self.key[-1]=="submit":
                        self.total_win.append(self.right_ans)
                        self.total_lose.append(self.wrong_ans)
                        self.Testing=False
                    elif  self.answer==[]:
                        pygame.time.wait(20) 
                        self.total_win.append(self.right_ans)
                        self.total_lose.append(self.wrong_ans)
                        self.key=[]  
                        self.Testing=False                    
                  
                    
                    

                pygame.display.flip()
            pygame.display.flip()
    print(self.total_lose,self.total_win)     
    
        
 
    
  #def gameoverloop(self):
      #event loop

      #update data

      #redraw
control=Controller()
control.mainloop()