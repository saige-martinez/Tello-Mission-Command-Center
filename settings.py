class Settings:
    """A class to store all settings for Control Center."""

    def __init__(self):
        """Initialize control center settings."""
        # Screen settings.
        self.screen_width = 320
        self.screen_height = 240
        self.bg_color = (230, 230, 230)

        # Drone settings.
        self.drone_speed = 50
        self.camera_width = 1280
        self.camera_height = 960
