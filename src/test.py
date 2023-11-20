import pygame 

pygame.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
screen = pygame.display.set_mode(SCREEN_SIZE)

background = pygame.image.load("final-project-team-hagil/assets/gui.jpg")
background_width = background.get_width()
background_x = 0
w_key = pygame.image.load("final-project-team-hagil/assets/w key.png")
w_key_after = pygame.image.load("final-project-team-hagil/assets/w key(after).png")
pressed=True
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("Up")
                    screen.blit(w_key_after,((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))
                    pygame.display.update()
                    pygame.time.wait(50)

    # Scroll the background
    background_x -= 1
    if background_x <= -background_width:
        background_x = 0

    # Render the background
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background_width, 0))
    screen.blit(w_key, ((SCREEN_HEIGHT-1000), (SCREEN_WIDTH-100)))

    pygame.display.update()
    pygame.time.wait(50)