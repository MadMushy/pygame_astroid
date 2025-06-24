import pygame                    # Import Pygame
from constants import *          # Pull from constants.txt
from player import Player

def main():
    # Initialize pygame
    pygame.init()
    
    # Set screen size using constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set up a clock for controlling FPS
    clock = pygame.time.Clock()

    # Time DELTA, useful for animiations / movements
    dt = 0

    # Create infinate while loop for game logic
    running = True

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the exit button
                running = False           # Stops game

        # Fill in screen with black
        screen.fill((0, 0, 0))
        
        player.draw(screen)

        # Update contents of entire discplay
        pygame.display.flip()

        dt = clock.tick(60) / 1000       # Limit FPS to 60
        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Ensures that the main function will only be called only when the file is run directly
# Considered the pythonic was to structure executable program in python
if __name__ == "__main__":
    main()
