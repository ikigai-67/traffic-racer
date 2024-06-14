class GameStats:
    """Track statistics for Traffic Racer."""

    def __init__(self, sg_game):
        """Initialize statistics."""
        self.settings = sg_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.main_car_left = self.settings.main_car_limit