#!/usr/bin/env python
#guide.py


from constants import *
from utils import *
import math
import gear



class SpiroGuide:
    """
    Pure logic for spirograph simulation, gear management, and speed control.
    No drawing or UI code.
    """
    def __init__(self, width, height, padding, radius, speed, center=(0, 0)):
        from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_PADDING, DEFAULT_RADIUS, DEFAULT_CENTERX, DEFAULT_CENTERY
        width = width if width is not None else DEFAULT_WIDTH
        height = height if height is not None else DEFAULT_HEIGHT
        padding = padding if padding is not None else DEFAULT_PADDING
        radius = radius if radius is not None else DEFAULT_RADIUS
        center = center if center != (0, 0) else (DEFAULT_CENTERX, DEFAULT_CENTERY)
        self.radius = radius - padding
        self.center = center
        self.gears = []
        self.speed = speed
        # Simulation speed control (slider logic, no UI)
        self.slider_min = 2  # FPS should not drop below ~2
        self.slider_max = 1000
        self._set_slider_pos_from_speed()
    def _set_slider_pos_from_speed(self):
        # Logic placeholder: set slider position from speed (no UI)
        rel = (self.speed - self.slider_min) / (self.slider_max - self.slider_min)
        self.slider_pos = rel

    def set_speed_from_slider(self, rel):
        # Set the speed based on slider position (0.0 to 1.0)
        rel = max(0, min(1, rel))
        self.speed = int(self.slider_min + rel * (self.slider_max - self.slider_min))
        self._set_slider_pos_from_speed()

    def clear(self):
        """Clear all gears."""
        self.gears = []

    def remove_gear(self):
        """Remove the most recently added gear."""
        if len(self.gears) > 0:
            self.gears.pop(-1)

    # UI methods removed

    def add_gear(self, gear_radius, hole_count):
        """Add a new gear with the specified radius and number of holes."""
        if hole_count not in range(1, 11):
            hole_count = 2
        if gear_radius not in range(1, int(self.radius * 0.9)):
            gear_radius = int(self.radius * 0.2)
        gear_center = (self.center[0] - (self.radius - gear_radius), self.center[1])
        gear_center = rotate_point_in_circle(center=self.center, point=gear_center, angle_velocity=randint(0, 360))
        new_gear = gear.SpiroGear(self, radius=gear_radius, center=gear_center)
        new_gear.add_random_holes(hole_count)
        self.gears.append(new_gear)


    # All UI, drawing, and event handling removed. Only pure logic remains.
    def update(self):
        """Update the state of all gears (advance simulation by one step)."""
        segments = []
        for gear in self.gears:
            segments.extend(gear.rotate())
        return segments

    def speed_change(self, value):
        """Change the speed of the guide's update loop (logic only)."""
        if value == 'up':
            self.speed += 10
        elif value == 'down':
            self.speed -= 10
        self.speed = max(self.slider_min, min(self.slider_max, self.speed))
