import pygame

pygame.init()
WIDTH=720
HEIGHT=1080
screen_size=(HEIGHT,WIDTH)
screen=pygame.display.set_mode(screen_size)
RUNNING=True

screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)
while RUNNING:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            RUNNING=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                print("Up")
                screen.fill("blue")
                pygame.display.flip()
                pygame.time.wait(50)
            elif event.key==pygame.K_s:
                print("Down")
                screen.fill("red")
                pygame.display.flip()
                pygame.time.wait(50)
            elif event.key==pygame.K_a:
                print("Left")
                screen.fill("yellow")
                pygame.display.flip()
                pygame.time.wait(50)
            elif event.key==pygame.K_d:
                print("Right")
                screen.fill("green")
                pygame.display.flip()
                pygame.time.wait(50)
                