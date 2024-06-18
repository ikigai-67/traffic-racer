from random import randint

import pygame
from pygame.sprite import Sprite #must use image and rect for attributes


class IncomingVehicle(Sprite):
    """A class to represent an incoming vehicle."""

    def __init__(self, tr_game):
        super().__init__()
        """Initialize the incoming vehicle and its starting position."""
        self.main_window = tr_game.main_window
        self.settings = tr_game.settings

        #Load the images of the incoming vehicles and get its rect.
        self.incoming_vehicles_list = [
            'BuickerB_180.png',
            'GalardB_180.png',
            'JeepB_180.png',
            'RamB_180.png',
            'SuperB_180.png'
                ]

        random_vehicle = 'images/'
        random_vehicle += self.incoming_vehicles_list[randint(1,4)]
        self.image = pygame.image.load(random_vehicle)
        self.rect = self.image.get_rect()

        # #Start each new incoming vehicle near the top left of the screen.
        # self.rect.x = self.rect.width * 0.5
        # self.rect.y = self.rect.top #self.rect.bottom = self.rect.top

        #Start each new incoming vehicle near the top left of the screen.
        self.rect.bottom = self.main_window.get_rect().top
        #self.rect.y = self.main_window_rect.top #self.rect.bottom = self.rect.top
        incoming_vehicle_right_max = self.settings.screen_width - (self.rect.width//2)
        self.rect.right = randint(0, incoming_vehicle_right_max)
        self.rect.left = randint(0, incoming_vehicle_right_max)


        #Store the incoming vehicles exact position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move incoming vehicles down the screen."""
        #update the exact position of the incoming vehicle.
        self.y += self.settings.incoming_vehicle_speed
        #Update the rect position
        self.rect.y = self.y

