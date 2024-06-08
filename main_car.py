import pygame

class MainCar:
    """A class to manage the main car of the player."""

    def __init__(self, tr_game) -> None:
        """Initialize the main car and set its starting position."""
        self.screen = tr_game.screen
        self.screen_rect = tr_game.screen.get_rect()

        #Load the main car image and get its rect.
        self.image = pygame.image.load('images/SuperB.png')
        self.image_rect = self.image.get_rect()

        #Start and Place each new main car at the center of the screen.
        #self.attribute.location = self.attribute.location
        self.image_rect.center = self.screen_rect.center #aligns the center of self.image_rect to the center of self.screen_rect

    def blitme(self):
        """Draw the main car at its current location."""
        self.screen.blit(self.image, self.image_rect)