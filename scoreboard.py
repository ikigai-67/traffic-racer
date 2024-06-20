import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, tr_game):
        """Initialize scorekeeping attributes."""
        self.screen = tr_game.main_window
        self.screen_rect =self.screen.get_rect()
        self.settings = tr_game.settings
        self.stats = tr_game.stats

        #Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        #Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
    
    #Display the score at the bottom right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom - 20

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)