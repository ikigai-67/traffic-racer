import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, tr_game, msg):
        """Initialize button attributes."""
        self.screen = tr_game.main_window
        self.screen_rect = self.screen.get_rect()

        #Dimension and properties of the button.
        self.width, self.height = 100, 25
        self.button_color = (230, 230, 230)
        self.text_color = (70, 70, 70)
        self.font = pygame.font.SysFont(None, 24)

        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Prepare the button message.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into an image and center it to the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw a blank button and then draw the image."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)