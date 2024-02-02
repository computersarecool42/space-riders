import pygame
from bullet import Bullet


class Ship:
    def __init__(self, sr_game):
        """Initialize the ship and set its starting position."""
        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        # self.rect.center = self.screen_rect.center
        # self.ship_rect.midbottom = self.screen_rect.midbottom
        self.ship_rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.ship_rect.x)
        self.y = float(self.ship_rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.bullet = Bullet(self)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.ship_rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x.
        self.ship_rect.x = self.x
        self.ship_rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.ship_rect)
