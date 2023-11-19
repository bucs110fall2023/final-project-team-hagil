import pygame


pygame.init()


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)


redsky = pygame.image.load("assets/redsky.png").convert()
redsky_width = redsky.get_width()
redsky_x = 0

sunset = pygame.image.load("assets/sunset.png").convert()
sunset_width = sunset.get_width()
sunsetl_x = 0

mountain = pygame.image.load("assets/mountain.png").convert()
mountain_width = mountain.get_width()
mountain_x = 0

nightsky = pygame.image.load("assets/nightsky.png").convert()
nightsky_width = nightsky.get_width()
nightsky_x = 0


clock = pygame.time.Clock()
FPS = 60


tiles = SCREEN_WIDTH / redsky_width


w_key = pygame.image.load("assets/w key.png")
w_key_after = pygame.image.load("assets/w key(after).png")

s_key = pygame.image.load("assets/s key.png")
s_key_after = pygame.image.load("assets/s key(after).png")

a_key = pygame.image.load("assets/a key.png")
a_key_after = pygame.image.load("assets/a key(after).png")

d_key = pygame.image.load("assets/d key.png")
d_key_after = pygame.image.load("assets/d key(after).png")

space_key = pygame.image.load("assets/space key.png")
space_key_after = pygame.image.load("assets/space key(after).png")


screen.blit(w_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))

screen.blit(a_key, ((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))

screen.blit(s_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-55)))

screen.blit(d_key, ((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))

screen.blit(space_key, ((SCREEN_HEIGHT-200), (SCREEN_WIDTH-100)))


pygame.display.update()
pygame.time.wait(10)


RUNNING = True
PRESSED = True


while RUNNING:

    clock.tick(FPS)

    screen.blit(redsky, (redsky_x, 0))

    for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                RUNNING=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(w_key_after,((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.blit(s_key_after,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-55))
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.blit(a_key_after,((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.blit(d_key_after,((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    screen.blit(space_key_after,(((SCREEN_HEIGHT-200), SCREEN_WIDTH-100)))

            elif event.type==pygame.KEYUP:

                if event.key==pygame.K_w:
                    print("Up released")
                    screen.blit(w_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-100))
                elif event.key==pygame.K_s:
                    print("Down")
                    screen.blit(s_key,((SCREEN_HEIGHT-1000), SCREEN_WIDTH-55))
                elif event.key==pygame.K_a:
                    print("Left")
                    screen.blit(a_key,((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_d:
                    print("Right")
                    screen.blit(d_key,((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))
                elif event.key==pygame.K_SPACE:
                    print("Space")
                    screen.blit(space_key,(((SCREEN_HEIGHT-200), SCREEN_WIDTH-100)))
            pygame.time.wait(30)
            pygame.display.update()

