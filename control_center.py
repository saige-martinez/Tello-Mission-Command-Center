import sys

import pygame

from settings import Settings
from drone import Drone


class ControlCenter:
    """Overall class to manage control center assets and behavior."""

    def __init__(self):
        """"Initialize the control center and create control center resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Drone Mission Control Center')

        self.drone = Drone(self)

    def run_control_center(self):
        """Start main loop for the control center."""
        while True:
            self._check_events()
            self.drone.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            self.drone.takeoff = True
        elif event.key == pygame.K_e:
            self.drone.land = True
        elif event.key == pygame.K_UP:
            self.drone.move_forward = True
        elif event.key == pygame.K_DOWN:
            self.drone.move_backward = True
        elif event.key == pygame.K_RIGHT:
            self.drone.move_right = True
        elif event.key == pygame.K_LEFT:
            self.drone.move_left = True
        elif event.key == pygame.K_w:
            self.drone.move_up = True
        elif event.key == pygame.K_s:
            self.drone.move_down = True
        elif event.key == pygame.K_d:
            self.drone.rotate_right = True
        elif event.key == pygame.K_a:
            self.drone.rotate_left = True
        elif event.key == pygame.K_SPACE:
            self.drone.take_photo = True
        elif event.key == pygame.K_ESCAPE:
            self.drone.land = True
            sys.exit()

    def _check_key_up_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_q:
            self.drone.takeoff = False
        elif event.key == pygame.K_e:
            self.drone.land = False
        elif event.key == pygame.K_UP:
            self.drone.move_forward = False
        elif event.key == pygame.K_DOWN:
            self.drone.move_backward = False
        elif event.key == pygame.K_RIGHT:
            self.drone.move_right = False
        elif event.key == pygame.K_LEFT:
            self.drone.move_left = False
        elif event.key == pygame.K_w:
            self.drone.move_up = False
        elif event.key == pygame.K_s:
            self.drone.move_down = False
        elif event.key == pygame.K_d:
            self.drone.rotate_right = False
        elif event.key == pygame.K_SPACE:
            self.drone.take_photo = False
        elif event.key == pygame.K_a:
            self.drone.rotate_left = False

    def _update_screen(self):
        """Update and display new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a control center instance and run the control center.
    cc = ControlCenter()
    cc.run_control_center()
