import pygame
import random
from taskbar import Taskbar
from obstacle import Obstacle
from group import Group
from mutagen.wave import WAVE
import time
def song_length(song_path):
    audio =WAVE(song_path)
    length=audio.info.length
    return length         
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
def evaluate_time(start_time,current_time):
    return current_time-start_time

class Controller:
  
  def __init__(self):
    
    self.obstacle_group=Group()

    self.taskbar_group=Group()# image size should be < 686x52px 
    
    
    self.aim=500
    self.main_aim=self.aim
    self.aim2=0
    RUNNING=True
    
    #thread.start()
    self.total_win=[]
    self.total_lose=[]
    self.state="gameloop"
    self.newkey=["w_key","s_key","a_key","d_key"]    
    self.ICONS={
        "#3":"final-project-team-hagil/assets/others icons/#3.png",
        "#2":"final-project-team-hagil/assets/others icons/#2.png",
        "#1":"final-project-team-hagil/assets/others icons/#1.png",
        "go":"final-project-team-hagil/assets/others icons/go.png",
    }
    self.SONG={
    "Careless":"final-project-team-hagil/assets/musics/careless.wav",
    "Cross me":"final-project-team-hagil/assets/musics/Cross me.wav",
    "I don't care":"final-project-team-hagil/assets/musics/I don't care.wav",
    }
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
    self.start=True    
    self.font=pygame.font.Font("final-project-team-hagil/assets/Caveat.ttf",49)    
    self.music = pygame.mixer.music.load(self.SONG["I don't care"])
    pygame.mixer.music.set_volume(0.2)
    self.random_value=choose_random(self.BG)
    self.background=pygame.image.load(self.BG[self.random_value])
    self.screen.blit(self.background,(0,0))
    self.taskbar=Taskbar(self.TASKBAR[self.random_value],540,665)
    self.taskbar_group.add(self.taskbar)
    while self.start:
        for k in self.ICONS:
            self.icon=pygame.image.load(self.ICONS[k])
            self.screen.blit(self.icon,(self.SCREEN_HEIGHT/2-20,self.SCREEN_WIDTH-650))
            pygame.display.flip()
            pygame.time.wait(1000)
            self.screen.blit(self.background,(0,0))
        self.start=False
    self.start_time=time.time()
    self.song_time=song_length(self.SONG["I don't care"])
    pygame.mixer.music.play(-1)
    while self.RUNNING:
        self.current_time=time.time()
        self.elapsed_time=evaluate_time(self.start_time,self.current_time)
        self.OG_key()
        if self.elapsed_time>self.song_time-5:
            self.RUNNING=False
        self.right_ans=0
        self.wrong_ans=0
        pygame.display.update()             
        self.msg2=str(self.aim2) + " misses"
        self.msg= str(int(self.aim))+" combos left"
        self.text2=self.font.render(self.msg2,True,"red")
        self.text=self.font.render(self.msg,True,"white")
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.text,(0,0))
        self.screen.blit(self.text2,(0,50))
        self.OG_key()
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
        self.create_time=time.time() 
        
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
                        if self.key[-1]=="submit":
                            self.Testing=False     
                        else:
                            self.obstacle.update(self.FALSE_KEY[self.answer[0]],self.coordinate[self.z],self.y_coord)
                            self.wrong_ans+=1
                            self.obstacle_group.add(self.obstacle)
                            self.obstacle_group.draw(self.screen)
                            self.z+=1
                            self.answer.pop(0)
                            self.obstacle_group.empty()
                    pygame.display.flip()
                    if self.key[-1]=="submit":
                        self.aim=self.aim-self.right_ans
                        self.aim2=self.aim2+self.wrong_ans
                        if self.aim2>10:
                            self.RUNNING=False
                        self.Testing=False
                    elif  self.answer==[]:
                        self.aim=self.aim-self.right_ans
                        self.aim2=self.aim2+self.wrong_ans
                        if self.aim2>10:
                            self.RUNNING=False
                        pygame.time.wait(20)
                        self.Testing=False    
            self.solving_time=time.time()                
            if evaluate_time(self.create_time,self.solving_time)>3:
                self.aim=self.aim-self.right_ans
                self.aim2=self.aim2+self.wrong_ans
                if self.aim2>10:
                    self.key=[]
                    self.RUNNINaG=False
                    pygame.time.wait(20) 
                self.Testing=False
                self.obstacle_group.empty()
            self.current_time=time.time()
            elapsed_time=evaluate_time(self.start_time,self.current_time)
            if elapsed_time>self.song_time-5:
                self.RUNNING=False
                pygame.display.flip()
            pygame.display.flip()
    print(self.main_aim-self.aim)     
    
        
 
    
  #def gameoverloop(self):
      #event loop

      #update data

      #redraw
control=Controller()
control.mainloop()