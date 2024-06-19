import sys
from time import sleep
from random import random

import pygame

from random import randint

from settings import Settings
from game_stats import GameStats
from button import Button
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
        
        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.main_car = MainCar(self)
        self.incoming_vehicles = pygame.sprite.Group()

        #Start game in an inactive state
        self.game_active = False
        #Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self._create_incoming_vehicle()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        #Move the main_car to the right.
        if event.key == pygame.K_p and not self.game_active:
            self._start_game()
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

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks the Play button."""
        Button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if Button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """Start the game and reset the game's statistics and assets."""
        self.stats.reset_stats()
        self.game_active = True

        self.incoming_vehicles.empty()
        
        self._create_incoming_vehicle()
        self.main_car.center_main_car()

        pygame.mouse.set_visible(False)

    def _create_incoming_vehicle(self):
        """Create an incoming vehicle if conditions are right."""
        if random() < self.settings.incoming_vehicle_frequency:
            new_incoming_vehicle = IncomingVehicle(self)
            self.incoming_vehicles.add(new_incoming_vehicle)

    def _update_incoming_vehicles(self):
        """Update incoming vehicles and their coordinates."""
        self.incoming_vehicles.update()
        for vehicle in self.incoming_vehicles.copy():
            if vehicle.rect.top > vehicle.main_window.get_rect().bottom:
                self.incoming_vehicles.remove(vehicle)
        #Look for car collisions.
        if pygame.sprite.spritecollideany(self.main_car, self.incoming_vehicles):
            self._main_car_hit()


    def _main_car_hit(self):
        """Respond to the main car being hit by incoming vehicle."""
        if self.stats.main_car_left >= 0:
            #Decrement main_car_left.
            self.stats.main_car_left -= 2

            #Get rid of any remaining incoming vehicles.
            self.incoming_vehicles.empty()

            #Create a new oncoming_traffic and recenter the main car.
            self._create_incoming_vehicle()
            self.main_car.center_main_car()

            #Pause
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update the screen surfaces and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.main_window.fill(self.settings.bg_color)
        #Redraw the main_car during each pass through the loop.
        self.main_car.blitme()
        self.incoming_vehicles.draw(self.main_window)

        #Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        


#Start the game when this main file is selected/run
if  __name__ == '__main__':
    #Make a game instance, and run the game
    tr = TrafficRacer()
    tr.run_game()
