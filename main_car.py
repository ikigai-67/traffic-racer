import pygame

class MainCar:
    """A class to manage the main car of the player."""

    def __init__(self, tr_game) -> None:
        """Initialize the main car and set its starting position."""
        self.main_window = tr_game.main_window
        self.main_window_rect = tr_game.main_window.get_rect()
        self.settings = tr_game.settings

        #Load the main car image and get its rect.
        self.image = pygame.image.load('images/SuperB.png')
        self.image_rect = self.image.get_rect()

        #Start and Place each new main car at the center of the screen.
        #self.attribute.location = self.attribute.location
        self.image_rect.center = self.main_window_rect.center #aligns the center of self.image_rect to the center of self.screen_rect

        #Store a float for the main car's exact horizontal and vertical position.
        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

        #Movement flags, start with a man_car that is not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        Update main car's position based on the movement of flag
          self.moving_right/left
        """
        if (self.moving_right) and (self.image_rect.right) < self.main_window_rect.right:
            self.image_rect.x += self.settings.main_car_speed

        if (self.moving_left) and (self.image_rect.left > 0):
            self.image_rect.x -= self.settings.main_car_speed

        if (self.moving_down) and (self.image_rect.bottom < self.main_window_rect.bottom) :
            self.image_rect.y += self.settings.main_car_speed

        if (self.moving_up) and (self.image_rect.top > 0):
            self.image_rect.y -= self.settings.main_car_speed


    def blitme(self):
        """Draw the main car at its current location."""
        self.main_window.blit(self.image, self.image_rect)