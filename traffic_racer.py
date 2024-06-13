import sys

import pygame

from random import randint

from settings import Settings
from main_car import MainCar
from incoming_vehicles import IncomingVehicle

class TrafficRacer:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        #Initialize clock for the framerate.
        self.clock = pygame.time.Clock()

        #Initialize games main window
        self.main_window = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Traffic Racer")

        self.main_car = MainCar(self)
        self.incoming_vehicles = pygame.sprite.Group()

        self._create_oncoming_traffic()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.main_car.update()
            self._update_incoming_vehicles()
            self._update_screen()

            #Set the default framerate.
            self.clock.tick(60)

    def _check_events(self):
        """Watch and respond for keyboard and mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        #Move the main_car to the right.
        if event.key == pygame.K_RIGHT:
            self.main_car.moving_right = True
        #Move main_car to the left.
        if event.key == pygame.K_LEFT:
            self.main_car.moving_left = True
        #Move main_car upward.
        if event.key == pygame.K_UP:
            self.main_car.moving_up = True
        #Move main_car downward.
        if event.key == pygame.K_DOWN:
            self.main_car.moving_down = True
        #Quit the game with just a press of a button.
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        #Stop the movement of the  car.
        if event.key == pygame.K_RIGHT:
            self.main_car.moving_right = False
        if event.key == pygame.K_LEFT:
            self.main_car.moving_left = False
        if event.key == pygame.K_DOWN:
            self.main_car.moving_down = False
        if event.key == pygame.K_UP:
            self.main_car.moving_up = False

    def _create_incoming_vehicle(self, x_position):
        """Create an incoming vehicle and place it in a row"""
        new_incoming_vehicle = IncomingVehicle(self)
        new_incoming_vehicle.x = x_position + randint(-15,15)
        new_incoming_vehicle.rect.x = x_position
        self.incoming_vehicles.add(new_incoming_vehicle)

    def _create_oncoming_traffic(self):
        """Create an oncoming traffic of vehicles."""
        #Create a vehicle for the oncoming traffic and keep adding until there's no room left.
        incoming_vehicle = IncomingVehicle(self)
        incoming_vehicle_width = incoming_vehicle.rect.width

        current_x = incoming_vehicle_width

        while current_x < (self.settings.screen_width - incoming_vehicle_width):
            self._create_incoming_vehicle(current_x)
            current_x += 1.75 * incoming_vehicle_width

    def _update_incoming_vehicles(self):
        """Update incoming vehicles and their coordinates."""
        self.incoming_vehicles.update()
        for vehicle in self.incoming_vehicles.copy():
            if vehicle.rect.top > vehicle.main_window_rect.bottom:
                self.incoming_vehicles.remove(vehicle)
                if len(self.incoming_vehicles) < 1:
                    self._create_oncoming_traffic()

    def _update_screen(self):
        """Update the screen surfaces and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.main_window.fill(self.settings.bg_color)
        #Redraw the main_car during each pass through the loop.
        self.main_car.blitme()
        self.incoming_vehicles.draw(self.main_window)
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        


#Start the game when this main file is selected/run
if  __name__ == '__main__':
    #Make a game instance, and run the game
    tr = TrafficRacer()
    tr.run_game()
