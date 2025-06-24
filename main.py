import pygame                    # Import Pygame
from constants import *          # Pull from constants.txt

def main():
    # Initialize pygame
    pygame.init()
    
    # Set screen size using constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create infinate while loop for game logic
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the exit button
                running = False           # Stops game

        # Fill in screen with black
        screen.fill((0, 0, 0))
        
        # Update contents of entire discplay
        pygame.display.flip()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
