import pygame

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the first surface
surface1 = pygame.Surface((400, 400))
surface1.fill((255, 0, 0))  # Fills the surface with red color

# Create the second surface
surface2 = pygame.Surface((200, 200))
surface2.fill((0, 255, 0))  # Fills the surface with green color

# Blit the second surface onto the first surface
surface1.blit(surface2, (25, 25))

# Blit the combined surface onto the screen surface
screen.blit(surface1, (100, 100))

# Update the display to show the changes
pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()