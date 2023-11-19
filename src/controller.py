import pygame

pygame.init()
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
pygame.display.update()
while RUNNING:
    screen.fill("blue")
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    new_surface.blit(w_key_after,((HEIGHT-1000),WIDTH-100))
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.fill("red")
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.fill("yellow")
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.fill("green")
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    new_surface.blit(space_key_after,(((HEIGHT-500),WIDTH-130)))
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    print("Up released")
                    new_surface.blit(w_key,((HEIGHT-1000),WIDTH-100))    
                elif event.key==pygame.K_SPACE:
                    new_surface.blit(space_key,(((HEIGHT-500),WIDTH-130)))
            pygame.time.wait(30)
            pygame.display.update()