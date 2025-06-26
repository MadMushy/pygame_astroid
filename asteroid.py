import pygame
import random
from circleshape import *
from constants import *

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

    def split(self):
        
        # Kill current asteroid
        self.kill()

        # If radius is below or at the min radius just return was a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        if self.radius > ASTEROID_MIN_RADIUS:
            
            new_angle = random.uniform(20, 50)
            
            angle_one = self.velocity.rotate(new_angle)
            angle_two = self.velocity.rotate(-new_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = angle_one * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = angle_two * 1.2
