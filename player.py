from circleshape import *  # Import all classes and functions from the circleshape module
from constants import *    # Import all constants (like PLAYER_RADIUS, PLAYER_TURN_SPEED) from the constants module
from shot import Shot

# Define a Player class that inherits from CircleShape
class Player(CircleShape):

    def __init__(self, x, y):
        # Initialize the parent class (CircleShape) with x, y, and a predefined PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        # Store the player's position as a 2D vector
        self.position = pygame.Vector2(x, y)
        
        # Initialize the player's velocity to zero
        self.velocity = pygame.Vector2(0, 0)
        
        # Set the initial rotation angle (in degrees) to 0
        self.rotation = 0
        
        # Initalize a shot timer set to zero
        self.shoot_timer = 0
        
    # Method to generate the triangle shape representing the player
    def triangle(self):
        # Calculate the forward direction vector based on the current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Calculate a rightward vector perpendicular to forward (used for triangle base)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Calculate the top point of the triangle (nose of the player)
        a = self.position + forward * self.radius
        
        # Calculate the bottom-left point of the triangle
        b = self.position - forward * self.radius - right
        
        # Calculate the bottom-right point of the triangle
        c = self.position - forward * self.radius + right
        
        # Return the three triangle points as a list
        return [a, b, c]

    # Method to draw the player on the screen
    def draw(self, screen):
        # Draw a white triangle (with outline width 2) using the points from self.triangle()
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # Method to rotate the player
    def rotate(self, dt):
        # Update the rotation angle based on time delta and turn speed constant
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to update the player each frame
    def update(self, dt):
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()
        
        # shot timer goes down at the rate of time delta
        self.shoot_timer -= dt

        # If the 'A' key is pressed, rotate the player left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # If the 'D' key is pressed, rotate the player right
        if keys[pygame.K_d]:
            self.rotate(dt)
        # If the 'W' key is pressed move forward
        if keys[pygame.K_w]:
            self.move(dt)
        # If the S key is pressef move backwards
        if keys[pygame.K_s]:
            self.move(-dt)
        # If the space bar is pressed run the shoot function
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        # if the shot timer is above zero return before preforming a shot
        if self.shoot_timer > 0:
            return
        # Set the timer to .3 before preforming a shot.
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        # Calls the Shot class and set starting position at the player location
        shot = Shot(self.position.x, self.position.y)
        # Sets the shot to start at tip of player and move off in same diecion 
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED

    def move(self, dt):
        # Calculate the forward direction vector based on current rotation 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Update the position by moving in forward direction
        # Scaled by player speed and time delta
        self.position += forward * PLAYER_SPEED * dt
