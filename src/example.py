import pygame

# Initialize Pygame
pygame.init()
screen=pygame.display.set_mode([600,600])
# Create a clock object
clock = pygame.time.Clock()

# Set the timer event
pygame.time.set_timer(pygame.USEREVENT,10000)  # 1000 milliseconds = 1 second

# Start the main game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handle the timer event
        if event.type == pygame.USEREVENT:
            print("Timer expired!")

    # Update the game state

    # Render the game screen

    # Flip the display
    pygame.display.flip()

    # Limit the framerate
    clock.tick(60)