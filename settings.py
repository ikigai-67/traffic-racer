class Settings:
    """A class to store all settings for Traffic Racer."""
    
    def __init__(self) -> None:
        """Initialize the game settings."""
        #Main window/screen settings/properties.
        self.screen_width = 400
        self.screen_height = 550
        self.bg_color = (70, 70, 70)

        #Main_car settings
        self.main_car_limit = 3

        #How quickly the game speeds up.
        self.speedup_scale = 1.001

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.main_car_speed = 1.7
        #Incoming vehicles settings
        self.incoming_vehicle_speed = 1.5
        self.incoming_vehicle_frequency = 0.015

        #Scoring settings.
        self.incoming_vehicle_points = 10

    def increase_speed(self):
        """Increase speed settings."""
        self.main_car_speed *= self.speedup_scale
        self.incoming_vehicle_speed *= self.speedup_scale