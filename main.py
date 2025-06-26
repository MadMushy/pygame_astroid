import pygame                    # Import Pygame
import sys
from constants import *          # Pull from constants.txt
from player import Player        # Pull from player.py
from asteroid import Asteroid    # Pull from asteroid.py
from asteroidfield import AsteroidField
from circleshape import *

def main():
    # Initialize pygame
    pygame.init()
    
    # Set screen size using constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set up a clock for controlling FPS
    clock = pygame.time.Clock()

    # Time DELTA, useful for animiations / movements
    dt = 0
    
    # Create two groups for Player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create group for astroids
    asteroids = pygame.sprite.Group()

    # Set static containers for Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set static container for Asteroid Field class
    AsteroidField.containers = updatable

    # Create a new AsteroidField object
    asteroid_field = AsteroidField()

    # Place all of Player into two containers
    Player.containers = (updatable, drawable)
    
    # Create infinate while loop for game logic
    running = True

    # Calling the Player method and setting X and Y
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the exit button
                running = False           # Stops game
        
        # Update
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        # Fill in screen with black
        screen.fill((0, 0, 0))

        # Iterate over all items in drawable container and draw them to the screen
        for item in drawable:
            item.draw(screen)

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
