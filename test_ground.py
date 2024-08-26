import pygame
import time
# here is a youtube link https://www.youtube.com/watch?v=mcWJjfccVrw&list=WL
# Initialize pygame
pygame.init()

# Set the screen size and create a new surface
screen_width, screen_height = 1900, 1600
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Set the screen background color to black
screen.fill((0, 0, 0))

# Create a blue surface
blue_surface = pygame.Surface((screen_width, screen_height))
blue_surface.fill((0, 0, 255))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flash the screen
    screen.blit(blue_surface, (0, 0))
    pygame.display.flip()
    time.sleep(1 / 8)  # Adjust the sleep time for frequency (1/8 for 8 Hz)
    screen.fill((0, 0, 0))
    pygame.display.flip()

# Quit pygame
pygame.quit()
