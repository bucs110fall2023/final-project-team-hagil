import pygame


pygame.init()


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)

def background():
    background = pygame.image.load("final-project-team-hagil/assets/gui.jpg")
    background_width = background.get_width()
    background_x = 0

    RUNNING = True

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        # Scroll the background
        background_x -= 1
        if background_x <= -background_width:
            background_x = 0

        # Render the background
        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + background_width, 0))

        pygame.display.update()

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

space_key = pygame.image.load("final-project-team-hagil/assets/space key.png")
space_key_after = pygame.image.load("final-project-team-hagil/assets/space key(after).png")




pygame.display.update()
pygame.time.wait(10)

RUNNING = True

background = pygame.image.load("final-project-team-hagil/assets/redsky.png")
background_width = background.get_width()
background_x = 0

while RUNNING:      
    background_x -= 1
    if background_x <= -background_width:
        background_x = 0

    screen.blit(background, (background_x, 0))
    
    screen.blit(background, (background_x + background_width, 0))
    
    screen.blit(w_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))

    screen.blit(a_key, ((SCREEN_HEIGHT-1050), (SCREEN_WIDTH-55)))

    screen.blit(s_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-55)))

    screen.blit(d_key, ((SCREEN_HEIGHT-950), (SCREEN_WIDTH-55)))

    screen.blit(space_key, ((SCREEN_HEIGHT-200), (SCREEN_WIDTH-100)))
    
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
                
                pygame.display.update()
                
                pygame.time.wait(10)

        # Render the background

    

    
    pygame.display.update()
    
    pygame.time.wait(5)

#hello