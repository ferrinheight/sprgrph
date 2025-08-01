#!/usr/bin/env python
#utils.py

import math
from random import randint, random


def random_color():
    return (randint(0, 255), randint(0, 255),randint(0, 255))

def calculate_distance(point1 = (0, 0), point2 = (0, 0)):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def calculate_angular_velocity(point = (0, 0), center = (0, 0), direction = 1):
    r = calculate_distance(point1 = point, point2 = center)
    if r == 0:
        return 0
    angular_velocity = direction * (TANGENTIAL_SPEED / r)
    return angular_velocity

def random_point_in_circle(radius, center = (0, 0)):
    # find random point in a circle
    # https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly/50746409#50746409
    if center == (0, 0):
        return (0, 0)
    r = float(radius) * math.sqrt(random())
    theta = random() * 2 * math.pi
    x = center[0] + r * math.cos(theta)
    y = center[1] + r * math.sin(theta)
    return (x, y)

def rotate_point_in_circle(center = (0, 0), point = (0, 0), angle_velocity = 0):
    if (0, 0) in (center, point) or angle_velocity == 0:
        return (0, 0)
    x = point[0] - center[0]
    y = point[1] - center[1]
    new_x = x * math.cos(angle_velocity) - y * math.sin(angle_velocity)
    new_y = x * math.sin(angle_velocity) + y * math.cos(angle_velocity)
    return (new_x + center[0], new_y + center[1])


from constants import *
import math
from random import randint, random

def random_color():
    """Return a random RGB color tuple."""
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def calculate_distance(point1=(0, 0), point2=(0, 0)):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def calculate_angular_velocity(point=(0, 0), center=(0, 0), direction=1):
    """Calculate the angular velocity for a point rotating around a center."""
    r = calculate_distance(point1=point, point2=center)
    if r == 0:
        return 0
    angular_velocity = direction * (TANGENTIAL_SPEED / r)
    return angular_velocity

def random_point_in_circle(radius, center=(0, 0)):
    """Generate a random point within a circle of given radius and center."""
    if center == (0, 0):
        return (0, 0)
    r = float(radius) * math.sqrt(random())
    theta = random() * 2 * math.pi
    x = center[0] + r * math.cos(theta)
    y = center[1] + r * math.sin(theta)
    return (x, y)

def rotate_point_in_circle(center=(0, 0), point=(0, 0), angle_velocity=0):
    """Rotate a point around a center by a given angle (radians)."""
    if (0, 0) in (center, point) or angle_velocity == 0:
        return (0, 0)
    x = point[0] - center[0]
    y = point[1] - center[1]
    new_x = x * math.cos(angle_velocity) - y * math.sin(angle_velocity)
    new_y = x * math.sin(angle_velocity) + y * math.cos(angle_velocity)
    return (new_x + center[0], new_y + center[1])

