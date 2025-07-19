#!/usr/bin/env python
"""
gui.py - Pygame-based GUI for Spirograph
Handles all drawing, event handling, and user interaction.
Imports pure logic from gear.py and guide.py.
"""


import pygame
from guide import SpiroGuide
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_PADDING, DEFAULT_RADIUS, DEFAULT_CENTERX, DEFAULT_CENTERY, WHITE, BLUE, GREY, RED, GREEN, BLACK
from gui_buttons import UIButton

def run_gui():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    spiro = SpiroGuide(DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_PADDING, DEFAULT_RADIUS, 60, (DEFAULT_CENTERX, DEFAULT_CENTERY))
    spiro.add_gear(0, 2)
    # UI Buttons
    buttons = [
        UIButton('Add gear', 700, 10, 80, 30, lambda: spiro.add_gear(0, 2), 16, WHITE, BLUE, GREY),
        UIButton('Remove gear', 700, 50, 80, 30, spiro.remove_gear, 16, WHITE, BLUE, GREY),
        UIButton('Clear', 700, 90, 80, 30, spiro.clear, 16, WHITE, BLUE, GREY)
    ]
    # Slider UI
    slider_rect = pygame.Rect(5, 40, 200, 20)
    slider_dragging = False
    def set_speed_from_slider(x):
        rel = (x - slider_rect.x) / slider_rect.width
        rel = max(0, min(1, rel))
        spiro.set_speed_from_slider(rel)
    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if slider_rect.collidepoint(event.pos):
                    slider_dragging = True
                    set_speed_from_slider(event.pos[0])
                for button in buttons:
                    button.handle_event(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if slider_dragging:
                    set_speed_from_slider(event.pos[0])
        # Update simulation
        spiro.update()
        # Draw everything
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        # Draw gears and holes
        for gear in spiro.gears:
            pygame.draw.circle(surface, (200, 200, 200), gear.center, gear.radius, 1)
            for hole in gear.holes:
                pygame.draw.circle(surface, (50, 255, 75), hole.center, 4, 2)
                if len(hole.points) > 1:
                    pygame.draw.lines(surface, hole.color, False, hole.points, 1)
        # Draw main guide circle
        pygame.draw.circle(surface, (255, 255, 255), spiro.center, spiro.radius, 2)
        # Draw FPS
        font = pygame.font.Font(None, 36)
        fps_info = font.render(f'FPS: {int(spiro.speed)}', True, (255, 255, 255))
        surface.blit(fps_info, (5, 5))
        # Draw slider
        pygame.draw.rect(surface, (180, 180, 180), slider_rect, border_radius=10)
        slider_handle_x = int(slider_rect.x + spiro.slider_pos * slider_rect.width)
        handle_rect = pygame.Rect(slider_handle_x - 7, slider_rect.y - 4, 14, slider_rect.height + 8)
        pygame.draw.rect(surface, (100, 100, 255), handle_rect, border_radius=7)
        small_font = pygame.font.Font(None, 22)
        min_label = small_font.render('Slow', True, (200, 200, 200))
        max_label = small_font.render('Fast', True, (200, 200, 200))
        surface.blit(min_label, (slider_rect.x, slider_rect.y + slider_rect.height + 2))
        surface.blit(max_label, (slider_rect.x + slider_rect.width - max_label.get_width(), slider_rect.y + slider_rect.height + 2))
        # Draw UI buttons
        for button in buttons:
            button.draw(surface)
        pygame.display.flip()
        clock.tick(spiro.speed)
    pygame.quit()

if __name__ == "__main__":
    run_gui()
