import pygame


pygame.init()


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

pygame.display.update()


RUNNING = True
PRESSED = True


while RUNNING:
    for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(w_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
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
                    screen.blit(space_key_after,(((SCREEN_HEIGHT-500), SCREEN_WIDTH-100)))

            elif event.type==pygame.KEYUP:

                if event.key==pygame.K_w:
                    print("Up released")
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

#hello