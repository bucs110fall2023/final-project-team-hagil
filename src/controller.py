import pygame


pygame.init()
<<<<<<< HEAD
WIDTH=720
HEIGHT=1080
screen_size=(HEIGHT,WIDTH)
screen_s=(600,600)
screen=pygame.display.set_mode(screen_size)
new_surface=pygame.display.set_mode(screen_s)
RUNNING=True
pressed=True
screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)
w_key=pygame.image.load("final-project-team-hagil/assets/w key.png")
w_key_after=pygame.image.load("final-project-team-hagil/assets/w key(after).png")
space_key=pygame.image.load("final-project-team-hagil/assets/space key.png")
space_key_after=pygame.image.load("final-project-team-hagil/assets/space key(after).png")
new_surface.blit(w_key,((HEIGHT-1000),WIDTH-100))
new_surface.blit(space_key,((HEIGHT-500),WIDTH-130))
=======


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)


w_key = pygame.image.load("final-project-team-hagil/assets/w key.png")
w_key_after = pygame.image.load("final-project-team-hagil/assets/w key(after).png")

s_key = pygame.image.load("final-project-team-hagil/assets/s key.png")
s_key_after = pygame.image.load("final-project-team-hagil/assets/s key(after).png")

a_key = pygame.image.load("final-project-team-hagil/assets/a key.png")
a_key_after = pygame.image.load("final-project-team-hagil/assets/a key(after).png")

d_key = pygame.image.load("final-project-team-hagil/assets/d key.png")
d_key_after = pygame.image.load("final-project-team-hagil/assets/d key(after).png")

space_key = w_key = pygame.image.load("final-project-team-hagil/assets/space key.png")
space_key_after = pygame.image.load("final-project-team-hagil/assets/space key(after).png")


screen.blit(w_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))
screen.blit(space_key, ((SCREEN_HEIGHT-500), (SCREEN_WIDTH-100)))

>>>>>>> 653429ec103a01a2789843f3c3bba2581d8b29d5
pygame.display.update()


RUNNING = True
PRESSED = True


while RUNNING:
    screen.fill("blue")
    pygame.display.flip()
    for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
<<<<<<< HEAD
                    new_surface.blit(w_key_after,((HEIGHT-1000),WIDTH-100))
=======
                    screen.blit(w_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
>>>>>>> 653429ec103a01a2789843f3c3bba2581d8b29d5
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.blit(s_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    screen.fill("red")
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.blit(a_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    screen.fill("yellow")
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.blit(d_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    screen.fill("green")
                elif event.key==pygame.K_SPACE:
                    print("Space")
<<<<<<< HEAD
                    new_surface.blit(space_key_after,(((HEIGHT-500),WIDTH-130)))
=======
                    screen.blit(space_key_after,(((SCREEN_HEIGHT-500), SCREEN_WIDTH-100)))

>>>>>>> 653429ec103a01a2789843f3c3bba2581d8b29d5
            elif event.type==pygame.KEYUP:

                if event.key==pygame.K_w:
                    print("Up released")
<<<<<<< HEAD
                    new_surface.blit(w_key,((HEIGHT-1000),WIDTH-100))    
                elif event.key==pygame.K_SPACE:
                    new_surface.blit(space_key,(((HEIGHT-500),WIDTH-130)))
            pygame.time.wait(30)
            pygame.display.update()
=======
                    screen.blit(w_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    pygame.display.update()
                elif event.key==pygame.K_s:
                    print("Up released")
                    screen.blit(s_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    pygame.display.update()
                elif event.key==pygame.K_a:
                    print("Up released")
                    screen.blit(a_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    pygame.display.update()
                elif event.key==pygame.K_d:
                    print("Up released")
                    screen.blit(d_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                    pygame.display.update()  
                elif event.key==pygame.K_SPACE:
                    screen.blit(space_key,(((SCREEN_HEIGHT-500), SCREEN_WIDTH-100)))

            pygame.time.wait(50)
            pygame.display.update()
>>>>>>> 653429ec103a01a2789843f3c3bba2581d8b29d5
