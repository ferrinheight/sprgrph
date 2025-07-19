#!/usr/bin/env python
#gear.py


from utils import *
import math

class Hole:
    """
    Represents a hole in a gear where the drawing utensil can be inserted.
    Pure logic only; no drawing code.
    """
    def __init__(self, parent, offset_radius=None, offset_angle=None, color=None):
        self.parent = parent
        self.offset_radius = offset_radius
        self.offset_angle = offset_angle
        self.color = color if color is not None else random_color()
        self.center = None
        self.prev_center = None
        self.update_absolute_position()

    def rotate(self, local_angle_delta):
        self.offset_angle += local_angle_delta
        return self.update_absolute_position()

    def update_absolute_position(self):
        cx, cy = self.parent.center
        x = cx + self.offset_radius * math.cos(self.offset_angle)
        y = cy + self.offset_radius * math.sin(self.offset_angle)
        prev = self.center
        self.prev_center = prev if prev is not None else (x, y)
        self.center = (x, y)
        return self.prev_center, self.center

class SpiroGear:
    """
    Represents a spirograph gear that can contain multiple holes.
    Pure logic only; no drawing code.
    """
    def __init__(self, parent, radius=10, center=(0, 0), holes=None):
        self.parent = parent
        from constants import DEFAULT_RADIUS
        self.radius = radius if radius is not None else DEFAULT_RADIUS
        self.center = center
        self.direction = 1
        self.holes = holes if holes is not None else []

    def add_random_holes(self, count=1):
        for _ in range(count):
            r = randint(int(0.2 * self.radius), int(0.9 * self.radius))
            theta = math.radians(randint(0, 359))
            self.holes.append(Hole(self, offset_radius=r, offset_angle=theta))

    def add_holes(self, holes=None):
        if holes is None:
            return
        self.holes.extend(holes)

    def rotate(self):
        angle_velocity = calculate_angular_velocity(point=self.center, center=self.parent.center, direction=self.direction)
        old_center = self.center
        self.center = rotate_point_in_circle(center=self.parent.center, point=self.center, angle_velocity=angle_velocity)
        guide_radius = self.parent.radius
        gear_radius = self.radius
        local_angle_delta = -angle_velocity * (guide_radius / gear_radius)
        # Return a list of (prev, curr, color) for each hole
        segments = []
        for hole in self.holes:
            prev, curr = hole.rotate(local_angle_delta)
            segments.append((prev, curr, hole.color))
        return segments


