from djitellopy import tello

import cv2

import time


class Drone:
    """A class to manage the drone."""

    def __init__(self, control_center):
        """Initialize the drone."""
        self.t = tello.Tello()
        self.t.connect()
        self.t.streamon()
        self.settings = control_center.settings

        # Movement flags.
        self.takeoff = self.land = False
        self.move_forward = self.move_backward = False
        self.move_right = self.move_left = False
        self.move_up = self.move_down = False
        self.rotate_right = self.rotate_left = False
        self.take_photo = False

    def update(self):
        """Update the drone."""
        self._position()
        self._camera()

    def _position(self):
        """Update the drone's position based on movement flags."""
        # Store values for drone's position.
        pitch = roll = throttle = yaw = 0

        # Update drone's positional values.
        if self.takeoff:
            self.t.takeoff()
        if self.land:
            self.t.land()
        if self.move_forward:
            pitch = self.settings.drone_speed
        elif self.move_backward:
            pitch = -self.settings.drone_speed
        if self.move_right:
            roll = self.settings.drone_speed
        elif self.move_left:
            roll = -self.settings.drone_speed
        if self.move_up:
            throttle = self.settings.drone_speed
        elif self.move_down:
            throttle = -self.settings.drone_speed
        if self.rotate_right:
            yaw = self.settings.drone_speed
        elif self.rotate_left:
            yaw = -self.settings.drone_speed

        # Update drone's position.
        self.t.send_rc_control(roll, pitch, throttle, yaw)
        time.sleep(0.03)

    def _camera(self):
        """Update the drone's camera and take a photo based on movement flags."""
        # Update drone's camera.
        frame = self.t.get_frame_read().frame
        frame = cv2.resize(frame, (self.settings.camera_width, self.settings.camera_height))
        cv2.imshow('Drone Feed', frame)
        cv2.waitKey(1)

        # Take and save a photo.
        if self.take_photo:
            cv2.imwrite(f'Images/{time.time()}.jpg', frame)
            time.sleep(0.5)
