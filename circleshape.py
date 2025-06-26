import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Method for checking collisions between player and asteroid
    def check_collision(self, rock):
        
        # Call distance_to pygame function came up with rock name.
        distance = self.position.distance_to(rock.position)
        if distance < (self.radius + rock.radius):
            return True
        else:
            return False

