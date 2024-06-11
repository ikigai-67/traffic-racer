class Settings:
    """A class to store all settings for Traffic Racer."""
    
    def __init__(self) -> None:
        """Initialize the game settings."""
        #Main window/screen settings/properties.
        self.screen_width = 400
        self.screen_height = 550
        self.bg_color = (70, 70, 70)

        #Main_car settings
        self.main_car_speed = 2


        #Incoming vehicles settings
        self.incoming_vehicle_speed = 2
