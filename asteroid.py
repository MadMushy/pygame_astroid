import pygame
from circleshape import *

# Define a new class Astroid that inherits from Circleshape
class Asteroid(CircleShape):

    # Contructor method to initalize asteroids position and size
    def __init__(self, x, y, radius):
        
        # Call on parent circleshape constructor to get position and radius 
        super().__init__(x, y, radius)

    # Method to draw the astroid on the screen
    def draw(self, screen):
        
        # Draw an astroid (circle) on the screen that is white, uses position and radius from
        # circleshape and has a with of 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Method to update the astroids position
    def update(self, dt):

        # Move the astroid position by its velocity scaled on the time delta.
        self.position += self.velocity*dt


