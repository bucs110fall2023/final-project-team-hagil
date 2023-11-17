import pygame

pygame.init()
WIDTH=720
HEIGHT=1080
screen_size=(HEIGHT,WIDTH)
screen=pygame.display.set_mode(screen_size)
RUNNING=True
pressed=True
screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)
w_key=pygame.image.load("final-project-team-hagil/assets/w key.png")
w_key_after=pygame.image.load("final-project-team-hagil/assets/w key(after).png")
screen.blit(w_key,((HEIGHT-1000),WIDTH-100))
pygame.display.update()
while RUNNING:
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(w_key_after,((HEIGHT-1000),WIDTH-100))
                    pygame.time.wait(50)
                    pygame.display.update()
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.fill("red")
                    pygame.display.update()
                    pygame.time.wait(50)
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.fill("yellow")
                    pygame.display.update()
                    pygame.time.wait(50)
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.fill("green")
                    pygame.display.update()
                    pygame.time.wait(50)
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    print("Up released")
                    screen.blit(w_key,((HEIGHT-1000),WIDTH-100))
                    pygame.display.update()    