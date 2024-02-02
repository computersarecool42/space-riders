class Settings:
    """The Settings class store all settings for the game."""
    def __init__(self):
        """Initialize settings."""

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        # Ship
        self.ship_speed = 1.5

        # Bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        