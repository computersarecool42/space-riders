import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    # sr_game - get the current instance of Space Riders
    def __init__(self, sr_game):
        # Inherit properly from Sprite
        super().__init__()

        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings
        self.color = sr_game.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midtop = sr_game.ship_rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.bullet_rect.y)

        # Create the bullet's surface.
        self.bullet_image = pygame.Surface([self.settings.bullet_width, self.settings.bullet_height])
        self.bullet_image.fill(self.color)

        # Movement flag
        self.fire = False

    def update(self):
        """Update the bullet position."""
        print(f"Bu: {self.fire}")
        if self.fire and self.bullet_rect.top > self.screen_rect.top:
            self.y -= self.settings.bullet_speed

        self.bullet_rect.y = self.y

    def blitme(self):
        """Draw the bullet at its current location."""
        self.screen.blit(self.bullet_image, self.bullet_rect)



