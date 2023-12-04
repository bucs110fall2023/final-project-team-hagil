import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Background(pygame.sprite.Sprite):
    def __init__(self,img):
        self.image= pygame.Surface((800, 600))
        self.image=pygame.image.load(img)

class Foreground(pygame.sprite.Sprite):
    def __init__(self,img):
        self.image= pygame.Surface((800, 600))
        self.image=pygame.image.load(img)
class Player(pygame.sprite.Sprite):
    def __init__(self,img):
        self.image= pygame.Surface((800, 600))
        self.image=pygame.image.load(img)
# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Create a clock object
clock = pygame.time.Clock()

# Create a sprite group for the background
background_group = pygame.sprite.Group()

# Create a sprite group for the foreground
foreground_group = pygame.sprite.Group()

# Create a sprite group for the player
player_group = pygame.sprite.Group()

# Create a background sprite
background = Background("final-project-team-hagil/assets/keyboard/s key.png")
background.image = pygame.Surface((800, 600))
background_group.add(background)

# Create a foreground sprite
foreground = Foreground("final-project-team-hagil/assets/keyboard/d key.png")

foreground_group.add(foreground)

# Create a player sprite
player = Player("final-project-team-hagil/assets/keyboard/a key.png")
player.image = pygame.Surface((10, 10))
player_group.add(player)

# The main game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the sprites
    player_group.update()

    # Draw the sprites
    screen.fill(BLACK)
    background_group.draw(screen)
    foreground_group.draw(screen)
    player_group.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Limit the framerate
    clock.tick(60)