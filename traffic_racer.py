import sys

import pygame

from settings import Settings
from main_car import MainCar

class TrafficRacer:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
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

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            self.main_car.update()
            
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

    def _update_screen(self):
        """Update the screen surfaces and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.main_window.fill(self.settings.bg_color)
        #Redraw the main_car during each pass through the loop.
        self.main_car.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()


#Start the game when this main file is selected/run
if  __name__ == '__main__':
    #Make a game instance, and run the game
    tr = TrafficRacer()
    tr.run_game()
