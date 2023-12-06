import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Set the display dimensions (optional)
pygame.display.set_mode((400, 300))

# Load a music file
pygame.mixer.music.load("final-project-team-hagil/assets/musics/careless.mp3")

# Set the end event
music_end_event = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(music_end_event)

# Start playing the music
pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == music_end_event:
            print("Music has ended.")
            running = False

    # You can add other game logic or processing here

    # Optionally, you can add a small delay to reduce CPU usage
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
sys.exit()
