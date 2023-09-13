class Settings:
    """A class to store all the setting for Alien Invastion."""
    
    def __init__(self):
        """Init the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 20
        