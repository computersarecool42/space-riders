import pygame
import sys
from ship import Ship
from bullet import Bullet
from settings import Settings


class SpaceRiders:
    """The SpaceRiders class is managing game assets and behaviours."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        pygame.display.set_caption("Space Riders")

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Fullscreen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Set the dimensions to the full size of the screen
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # The self argument here refers to the current instance of SpaceRiders.
        # This is the parameter that gives Ship access to the game’s resources, such as the screen object.
        self.ship = Ship(self)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.ship.bullet.blitme()

        # Make visible the most recent drawn screen
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self.__check_events_keyup(event)

    def _check_events_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            print("True!")
            self.ship.bullet.fire = True
        elif event.key == pygame.K_q:
            sys.exit()

    def __check_events_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.ship.bullet.fire = False

    def run_game(self):
        """Start the main loop."""
        while True:
            # Listen keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.ship.bullet.update()
            self._update_screen()


if __name__ == '__main__':
    # Create an instance and run the game
    sp = SpaceRiders()
    sp.run_game()
