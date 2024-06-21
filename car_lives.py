import pygame
from pygame.sprite import Sprite

class CarLife(Sprite):
    """A class to manage the main car of the player."""

    def __init__(self, tr_game) -> None:
        super().__init__()
        """Initialize the main car and set its starting position."""
        self.main_window = tr_game.main_window
        self.main_window_rect = tr_game.main_window.get_rect()
        self.settings = tr_game.settings

        #Load the main car image and get its rect.
        self.image = pygame.image.load('images/car_life.png')
        self.rect = self.image.get_rect()


        #Store a float for the main car's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

