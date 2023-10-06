#!/usr/bin/env python
#guide.py

from constants import *
from utils import *
import pygame
import math
import gear
from functools import partial
import pygame
from tkinter import simpledialog
import tkinter as tk

class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height, callback, font_size, font_color, outline_color, fill_color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(outline_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, font_color)
        W = self.text_surface.get_width()
        H = self.text_surface.get_height()
        pygame.draw.rect(self.image, fill_color, (x + 2, y + 2, width - 4, height - 4))
        self.image.blit(self.text_surface, [width // 2 - W // 2, height // 2 - H // 2])

    def click(self, args = ()):
        self.callback(*args)

#pygame.init()
class SpiroGuide:
    def __init__(self, width, height, padding, radius, speed, center = (0, 0)):
        self.surface = pygame.display.set_mode((width, height))
        self.graph_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.ui_surface = pygame.Surface((width, height)) #, pygame.SRCALPHA)
        self.ui_visible = False
        self.ui_value = 1
        self.tkroot = tk.Tk()
        self.tkroot.withdraw()
        self.radius = radius - padding
        self.center = center
        self.gears = []
        self.speed = speed
        self.buttons = pygame.sprite.Group()
        self.ui_buttons = pygame.sprite.Group()
        buttons = [
            Button('Add gear', 700, 10, 80, 30, self.ui_show, 16, WHITE, BLUE, GREY),
            Button('Remove gear', 700, 50, 80, 30, self.remove_gear, 16, WHITE, BLUE, GREY),
            Button('Clear', 700, 90, 80, 30, self.clear, 16, WHITE, BLUE, GREY)
        ]
        ui_buttons = [
            Button('X', 470, 100, 30, 30, self.ui_hide, 20, GREY, BLACK, RED),
            Button('+', 400, 120, 50, 50, self.ui_plus, 24, GREEN, BLACK, GREY),
            Button('-', 400, 180, 50, 50, self.ui_minus, 24, BLUE, BLACK, GREY)
        ]
        for button in buttons:
            self.buttons.add(button)
        for button in ui_buttons:
            self.ui_buttons.add(button)

    def clear(self):
        self.gears = []
        self.graph_surface.fill((0, 0, 0, 0))

    def remove_gear(self):
        if len(self.gears) > 0:
            self.gears.pop(-1)

    def ui_show(self):
        self.ui_visible = True

    def ui_hide(self):
        self.ui_visible = False
        self.add_gear(0, self.ui_value)
        self.ui_value = 1

    def ui_plus(self):
        if self.ui_value < 10:
            self.ui_value += 1

    def ui_minus(self):
        if self.ui_value > 1:
            self.ui_value -= 1

    def add_gear(self, gear_radius, hole_count):
        if hole_count not in range(1, 11):
            hole_count = randint(0, 6)
        if gear_radius not in range(1, int(self.radius * 0.9)):
            gear_radius = randint(20, round(self.radius * 0.8))
        gear_center = (self.center[0] - (self.radius - gear_radius), self.center[1])
        gear_center = rotate_point_in_circle(center = self.center, point = gear_center, angle_velocity = randint(0, 360))
        self.gears.append(gear.SpiroGear(self, radius = gear_radius, center = gear_center))
        self.gears[-1].add_random_holes(hole_count)
        print('gear center: {}'.format(self.gears[-1].center))
        print('gear holes: {}'.format(','.join([str(h.center) for h in self.gears[-1].holes])))

    def click(self, pos):
        #x, y = pos
        if self.ui_visible:
            buttons = self.ui_buttons
        else:
            buttons = self.buttons
        for button in buttons:
            if button.rect.collidepoint(*pos):
                button.click()

    def key_press(self, key):
        if key == pygame.K_UP:
            self.speed_change('up')
        if key == pygame.K_DOWN:
            self.speed_change('down')

    def draw(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        if self.ui_visible:
            pygame.draw.rect(self.ui_surface, GREY, (350, 100, 150, 150))
            self.ui_buttons.draw(self.ui_surface)
            self.ui_surface.blit(font.render(str(self.ui_value), True, RED), (350, 150))
            self.surface.blit(self.ui_surface, (0, 0))
        else:
            if len(self.gears) > 0:
                for gear in self.gears:
                    gear.draw(self.surface, self.graph_surface)
            self.surface.blit(self.graph_surface, (0, 0))
            pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)
            self.buttons.draw(self.surface)
            fps_info = font.render(f'FPS: {int(self.speed)}', True, (255, 255, 255))
            self.surface.blit(fps_info, (5, 5))

        pygame.display.flip()

    def update(self):
        # spin(move) gear(s) then draw
        for gear in self.gears:
            gear.rotate()
        self.draw()

    def speed_change(self, value):
        if value == 'up':
            self.speed += 10
        elif value == 'down':
            self.speed -= 10
