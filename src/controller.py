import pygame
import random
from src.taskbar import Taskbar
from src.obstacle import Obstacle
from src.group import Group
from src.button import Button
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
    self.state=()
    self.taskbar_group=Group()# image size should be < 686x52px 
    self.Ending=True
    self.aim=0
    self.main_aim=0
    self.aim2=0
    RUNNING=True
    #thread.start()
    self.state="gameloop"
    self.newkey=["w_key","s_key","a_key","d_key"]    
    self.ICONS={
        "#3":"assets/others icons/#3.png",
        "#2":"assets/others icons/#2.png",
        "#1":"assets/others icons/#1.png",
        "go":"assets/others icons/go.png",
    }
    self.SONG={
    "Careless":"assets/musics/careless.wav",
    "Cross me":"assets/musics/Cross me.wav",
    "I don't care":"assets/musics/I don't care.wav",
    "Shake it off":"assets/musics/Shake it off.wav",
    "You belong with me":"assets/musics/You belong with me.wav",
    "greater than one":"assets/musics/greater than one.wav",
    }
    self.OG_KEY={
    "w_key":"assets/keyboard/w key.png",
    "s_key":"assets/keyboard/s key.png",
    "a_key":"assets/keyboard/a key.png",
    "d_key":"assets/keyboard/d key.png",
    "space_key":"assets/keyboard/space key.png"
}
    self.Al_KEY={
    "w_key":"assets/keyboard/w key(after).png",
    "s_key":"assets/keyboard/s key(after).png",
    "a_key":"assets/keyboard/a key(after).png",
    "d_key":"assets/keyboard/d key(after).png",
    "space_key":"assets/keyboard/space key(after).png"
    
}
    self.FALSE_KEY={
    "w_key":"assets/keyboard/w key(wrong).png",
    "s_key":"assets/keyboard/s key(wrong).png",
    "a_key":"assets/keyboard/a key(wrong).png",
    "d_key":"assets/keyboard/d key(wrong).png"
}    
    self.BG={
    "dreamy":"assets/background/dreamy.png",
    "mountain":"assets/background/mountain.png",
    "nightsky":"assets/background/nightsky.png",
    "redsky":"assets/background/redsky.png",
    "sunset":"assets/background/sunset.png"
}
    self.TASKBAR={
    "mountain":"assets/taskbar/mountain.png",
    "nightsky":"assets/taskbar/nightsky.png",
    "redsky":"assets/taskbar/redsky+dreamy.png",
    "dreamy":"assets/taskbar/redsky+dreamy.png",
    "sunset":"assets/taskbar/sunset.png",
}   
    self.SCREEN_WIDTH = 720
    self.SCREEN_HEIGHT = 1080
    self.SCREEN_SIZE = (self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
    self.RUNNING=True
    self.Testing=True
    self.working=True
  def OG_key(self):
    self.screen.blit(pygame.image.load(self.OG_KEY["w_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-100))
    self.screen.blit(pygame.image.load(self.OG_KEY["s_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["a_key"]),(self.SCREEN_HEIGHT-1050,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["d_key"]),(self.SCREEN_HEIGHT-950,self.SCREEN_WIDTH-55))
    self.screen.blit(pygame.image.load(self.OG_KEY["space_key"]),(self.SCREEN_HEIGHT-150,self.SCREEN_WIDTH-100))
  def mainloop(self):
        pygame.init()
        self.screen=pygame.display.set_mode([self.SCREEN_HEIGHT,self.SCREEN_WIDTH])
        self.start_img=pygame.image.load("assets/others icons/start.png").convert_alpha()
        self.start_button=Button(415,500,self.start_img,0.2)
        self.state="mainscreen"
        while self.working:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    self.working=False
            if self.state=="mainscreen":
                self.start_screen()
            elif self.state=="gameloop":
                self.gameloop()
            elif self.state=="gameoverloop":
                self.gameoverloop()
    #select state loop
  
  ### below are some sample loop states ###

  #def menuloop(self):
    
      #event loop

      #update data

      #redraw
  
  def start_screen(self):
    self.run = True
    while self.run:
        self.main_screen = pygame.image.load("assets/main_screen.jpg")
        self.screen.blit(self.main_screen, (0, 0))
        self.start_button.draw(self.screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.run=False
                self.state="gameloop"
            elif event.type == pygame.QUIT:
                self.run = False
                self.working=False
                
    
  def gameloop(self):
    self.aim=0
    self.main_aim=0
    self.aim2=0
    self.obstacle_group.empty()
    self.RUNNING=True
    self.Testing=True
    self.start=True    
    self.font=pygame.font.Font("assets/Caveat.ttf",49) 
    self.random_song=choose_random(self.SONG)   
    self.music = pygame.mixer.music.load(self.SONG[self.random_song])
    self.song_time=song_length(self.SONG[self.random_song])
    if self.song_time>100:
        if self.song_time>=240:
            self.aim=450
        elif self.song_time>=180:
            self.aim=350
        elif self.song_time>=120:
            self.aim=250
        else:
            self.aim=200
    self.main_aim=self.aim
    pygame.mixer.music.set_volume(0.2)
    self.random_value=choose_random(self.BG)
    self.background=pygame.image.load(self.BG[self.random_value])
    self.screen.blit(self.background,(0,0))
    self.taskbar=Taskbar(self.TASKBAR[self.random_value],540,360)
    self.taskbar_group.add(self.taskbar)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                    self.working=False
    while self.start:
        for k in self.ICONS:
            self.icon=pygame.image.load(self.ICONS[k])
            self.screen.blit(self.icon,(self.SCREEN_HEIGHT/2-20,self.SCREEN_WIDTH-650))
            pygame.display.flip()
            pygame.time.wait(1000)
            self.screen.blit(self.background,(0,0))
        self.start=False
    self.start_time=time.time()
    pygame.mixer.music.play(-1)
    while self.RUNNING:
        self.current_time=time.time()
        self.elapsed_time=evaluate_time(self.start_time,self.current_time)
        self.OG_key()
        if self.elapsed_time>self.song_time-5:
            self.RUNNING=False
            pygame.mixer_music.stop()
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
        
            
        self.taskbar_group.draw(self.screen)
        
        pygame.display.flip()  
        self.obstacle_sequence =random.randrange(3,11)
        self.x_coord=evaluate_xdistance(self.obstacle_sequence)
        self.y_coord=340
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
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.working=False
        while self.Testing:
            
            self.OG_key()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Testing=False
                    self.RUNNING = False
                    self.working=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        self.screen.blit(pygame.image.load(self.Al_KEY["w_key"]),(self.SCREEN_HEIGHT-1000,self.SCREEN_WIDTH-100))
                        self.key.append("w_key")
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
                        elif self.key[-1]=="w_key" or self.key[-1]=="a_key" or self.key[-1]=="s_key" or self.key[-1]=="d_key":
                            self.obstacle.update(self.FALSE_KEY[self.answer[0]],self.coordinate[self.z],self.y_coord)
                            self.wrong_ans+=1
                            self.obstacle_group.add(self.obstacle)
                            self.obstacle_group.draw(self.screen)
                            self.z+=1
                            self.answer.pop(0)
                            self.obstacle_group.empty()
                        else:
                            self.key.append("error")
                    pygame.display.flip()
                    if self.key[-1]=="submit":
                        self.aim=self.aim-self.right_ans
                        self.aim2=self.aim2+self.wrong_ans
                        self.Testing=False
                    elif  self.answer==[]:
                        self.aim=self.aim-self.right_ans
                        self.aim2=self.aim2+self.wrong_ans
                        self.Testing=False
                    if self.aim2>20:
                        self.RUNNING=False
                        pygame.mixer_music.stop()  
                    elif self.aim<=0:
                        self.aim=0
                        self.aim2=0  
            self.solving_time=time.time()     
            self.current_time=time.time()
            elapsed_time=evaluate_time(self.start_time,self.current_time)           
            if evaluate_time(self.create_time,self.solving_time)>2:
                self.aim=self.aim-self.right_ans
                self.aim2=self.aim2+self.wrong_ans
                if self.aim2>20:
                    self.RUNNINaG=False
                    pygame.time.wait(20) 
                self.Testing=False
                self.obstacle_group.empty()
            elif elapsed_time>self.song_time-5:
                self.RUNNING=False
                pygame.mixer_music.stop()
                pygame.display.flip()
            pygame.display.flip()     
    self.state="gameoverloop"
  def gameoverloop(self):
        print(self.main_aim-self.aim)
        self.Ending=True
        self.home=Obstacle("assets/home.png",0,0)
        self.reset=Obstacle("assets/reset.png",980,0)
        self.obstacle_group.empty()
        self.font=pygame.font.Font("assets/San serif.otf",45)
        self.end_msg= "Target: "+ str(self.main_aim)
        self.end_msg2= "Finised combos: " + str(self.main_aim-self.aim)
        self.end_msg3=" Misses combo: " + str(self.aim2)
        self.text=self.font.render(self.end_msg,True,"cadetblue")
        self.text2=self.font.render(self.end_msg2, True, "cadetblue")
        self.text3=self.font.render(self.end_msg3, True, "cadetblue")
        if self.aim<=0 and self.aim2<20:
            self.announcement=pygame.image.load("assets/you win.png")
        elif self.aim2>=20 or self.aim >0:
            self.announcement=pygame.image.load("assets/you lose.png")
        else:
            self.announcement=pygame.image.load("assets/you lose.png")
        while self.Ending:
            self.screen.fill("plum1")
            self.screen.blit(pygame.image.load("assets/game_over (1).png"),(self.SCREEN_HEIGHT-750,0))
            self.home_rect=pygame.Rect(0,0,100,90)
            self.reset_rect=pygame.Rect(980,0,100,100)
            self.screen.blit(self.text,(self.SCREEN_HEIGHT-670,self.SCREEN_WIDTH/2-150))
            self.screen.blit(self.text2,(self.SCREEN_HEIGHT-740,self.SCREEN_WIDTH/2-100))
            self.screen.blit(self.text3,(self.SCREEN_HEIGHT-720,self.SCREEN_WIDTH/2-50))
            self.screen.blit(self.announcement,(self.SCREEN_HEIGHT-850,self.SCREEN_WIDTH/2))
            self.obstacle_group.add(self.home)
            self.obstacle_group.draw(self.screen)
            self.obstacle_group.add(self.reset)
            self.obstacle_group.draw(self.screen)
            pygame.display.flip()
            pygame.time.wait(300)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.Ending=False
                    self.working=False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.home_rect.collidepoint(event.pos):
                        if event.button==1:
                            self.Ending=False
                            self.state="mainscreen"
                    elif self.reset_rect.collidepoint(event.pos):
                        if event.button==1:    
                            self.Ending=False
                            self.state="gameloop"
control=Controller()
control.mainloop()