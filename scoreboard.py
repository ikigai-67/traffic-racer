import pygame.font
from pygame.sprite import Group

from car_lives import CarLife

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, tr_game):
        """Initialize scorekeeping attributes."""
        self.tr_game = tr_game
        self.screen = tr_game.main_window
        self.screen_rect = self.screen.get_rect()
        self.settings = tr_game.settings
        self.stats = tr_game.stats
        

        #Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        #Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_car_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score = round(self.stats.score, -1)
        score = f"{score:,}"
        self.score_image = self.font.render(
            score, True, self.text_color, self.settings.bg_color)
    
        #Display the score at the bottom right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom - 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        #Display the score at the middle bottom of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.score_rect.bottom

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = f"lvl: {str(self.stats.level)}"
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        #Position the level above the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.top - 10

    def prep_car_lives(self):
        """Show how many ships are left."""
        self.car_lives = Group()
        for car_life_number in range(self.stats.main_car_left):
            car_life = CarLife(self.tr_game)
            car_life.rect.x = 10 + car_life_number * car_life.rect.width
            car_life.rect.bottom = self.score_rect.bottom
            self.car_lives.add(car_life)


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.car_lives.draw(self.screen)