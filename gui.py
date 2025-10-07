#!/usr/bin/env python

"""
gui.py - Pygame-based GUI frontend for use with the core Spirograph logic.
Handles all drawing, event handling, and user interaction.
Imports pure spirograph simulation logic from gear.py and guide.py(soon to be new single script!).
"""


import pygame
from guide import SpiroGuide
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_PADDING, DEFAULT_RADIUS, DEFAULT_CENTERX, DEFAULT_CENTERY, WHITE, BLUE, GREY, RED, GREEN, BLACK, DARK_GREY
from gui_buttons import UIButton

def run_gui():
    pygame.init()
    surface = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    spiro = SpiroGuide(DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_PADDING, DEFAULT_RADIUS, 60, (DEFAULT_CENTERX, DEFAULT_CENTERY))
    spiro.add_gear(0, 2)
    # UI Buttons
    show_gear_config = False
    gear_radius_pct = 0.2
    gear_holes = 2
    def open_gear_config():
        nonlocal show_gear_config, gear_radius_pct, gear_holes
        show_gear_config = True
        gear_radius_pct = 0.2
        gear_holes = 2
    # Background color options: use only those from constants.py
    bg_colors = [BLACK, WHITE, DARK_GREY, BLUE, GREY, RED, GREEN]
    bg_color_idx = 0
    def change_bg_color():
        nonlocal bg_color_idx
        bg_color_idx = (bg_color_idx + 1) % len(bg_colors)
        draw_surface.fill(bg_colors[bg_color_idx])
    def save_drawing():
        import datetime
        filename = f"spirograph_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pygame.image.save(draw_surface, filename)
        print(f"Saved drawing to {filename}")
    def clear_lines():
        draw_surface.fill(bg_colors[bg_color_idx])
    buttons = [
        UIButton('Add Gear', 700, 10, 80, 30, open_gear_config, 16, WHITE, BLUE, GREY),
        UIButton('Remove Gear', 700, 50, 80, 30, spiro.remove_gear, 16, WHITE, BLUE, GREY),
        UIButton('Clear', 700, 90, 80, 30, clear_lines, 16, WHITE, BLUE, GREY),
        UIButton('Save', 10, DEFAULT_HEIGHT-40, 80, 30, save_drawing, 16, WHITE, (40,120,40), (20,60,20)),
        UIButton('BG Color', DEFAULT_WIDTH-110, DEFAULT_HEIGHT-40, 100, 30, change_bg_color, 16, WHITE, (40,40,120), (20,20,60)),
    ]
    slider_rect = pygame.Rect(5, 40, 200, 20)
    slider_dragging = False
    def set_speed_from_slider(x):
        rel = (x - slider_rect.x) / slider_rect.width
        rel = max(0, min(1, rel))
        spiro.set_speed_from_slider(rel)
    draw_surface = pygame.Surface((DEFAULT_WIDTH, DEFAULT_HEIGHT))
    draw_surface.fill(bg_colors[bg_color_idx])
    # Gear config widget UI state
    gear_slider_dragging = False
    hole_slider_dragging = False
    def add_gear_from_config():
        nonlocal show_gear_config
        show_gear_config = False
        radius = int(spiro.radius * gear_radius_pct)
        spiro.add_gear(radius, gear_holes)
    def cancel_gear_config():
        nonlocal show_gear_config
        show_gear_config = False
    confirm_button = UIButton('Confirm', 340, 260, 80, 32, add_gear_from_config, 16, WHITE, (80,120,80), (40,120,40))
    cancel_button = UIButton('Cancel', 430, 260, 80, 32, cancel_gear_config, 16, WHITE, (120,80,80), (120,40,40))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif show_gear_config:
                widget_rect = pygame.Rect(250, 120, 300, 180)
                slider_x = widget_rect.x+100
                slider_y = widget_rect.y+60
                slider_w = 160
                slider_area = pygame.Rect(slider_x, slider_y-8, slider_w, 24)
                holes_slider_x = widget_rect.x+100
                holes_slider_y = widget_rect.y+110
                holes_slider_w = 160
                holes_slider_area = pygame.Rect(holes_slider_x, holes_slider_y-8, holes_slider_w, 24)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        show_gear_config = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slider_area.collidepoint(event.pos):
                        gear_slider_dragging = True
                        rel = (event.pos[0] - slider_x) / (slider_w-12)
                        gear_radius_pct = max(0.05, min(0.75, rel * 0.7 + 0.05))
                    elif holes_slider_area.collidepoint(event.pos):
                        hole_slider_dragging = True
                        rel = (event.pos[0] - holes_slider_x) / (holes_slider_w-12)
                        gear_holes = int(round(max(1, min(10, rel * 9 + 1))))
                    elif confirm_button.rect.collidepoint(event.pos):
                        confirm_button.handle_event(event)
                    elif cancel_button.rect.collidepoint(event.pos):
                        cancel_button.handle_event(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    gear_slider_dragging = False
                    hole_slider_dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    if gear_slider_dragging:
                        rel = (event.pos[0] - slider_x) / (slider_w-12)
                        gear_radius_pct = max(0.05, min(0.75, rel * 0.7 + 0.05))
                    if hole_slider_dragging:
                        rel = (event.pos[0] - holes_slider_x) / (holes_slider_w-12)
                        gear_holes = int(round(max(1, min(10, rel * 9 + 1))))
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
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
        # Update simulation and draw new segments
        if not show_gear_config:
            segments = spiro.update()
            for prev, curr, color in segments:
                if prev is not None and curr is not None:
                    pygame.draw.line(draw_surface, color, prev, curr, 1)
        # Draw everything
        surface.blit(draw_surface, (0, 0))
        # Draw overlay (gears/guides) only for display, not for saving
        for gear in spiro.gears:
            pygame.draw.circle(surface, (200, 200, 200), gear.center, gear.radius, 1)
            for hole in gear.holes:
                pygame.draw.circle(surface, (50, 255, 75), hole.center, 4, 2)
        pygame.draw.circle(surface, (255, 255, 255), spiro.center, spiro.radius, 2)
        font = pygame.font.Font(None, 36)
        fps_info = font.render(f'FPS: {int(spiro.speed)}', True, (255, 255, 255))
        surface.blit(fps_info, (5, 5))
        pygame.draw.rect(surface, (180, 180, 180), slider_rect, border_radius=10)
        slider_handle_x = int(slider_rect.x + spiro.slider_pos * slider_rect.width)
        handle_rect = pygame.Rect(slider_handle_x - 7, slider_rect.y - 4, 14, slider_rect.height + 8)
        pygame.draw.rect(surface, (100, 100, 255), handle_rect, border_radius=7)
        small_font = pygame.font.Font(None, 22)
        min_label = small_font.render('Slow', True, (200, 200, 200))
        max_label = small_font.render('Fast', True, (200, 200, 200))
        surface.blit(min_label, (slider_rect.x, slider_rect.y + slider_rect.height + 2))
        surface.blit(max_label, (slider_rect.x + slider_rect.width - max_label.get_width(), slider_rect.y + slider_rect.height + 2))
        for button in buttons:
            button.draw(surface)
        if show_gear_config:
            widget_rect = pygame.Rect(250, 120, 300, 180)
            pygame.draw.rect(surface, (40, 40, 40), widget_rect, border_radius=12)
            pygame.draw.rect(surface, (180, 180, 180), widget_rect, 2, border_radius=12)
            label_font = pygame.font.Font(None, 28)
            surface.blit(label_font.render('Add Gear', True, (255,255,255)), (widget_rect.x+90, widget_rect.y+10))
            # Radius slider
            surface.blit(label_font.render('Radius:', True, (200,200,200)), (widget_rect.x+20, widget_rect.y+50))
            slider_x = widget_rect.x+100
            slider_y = widget_rect.y+60
            slider_w = 160
            pygame.draw.rect(surface, (120,120,120), (slider_x, slider_y, slider_w, 8), border_radius=4)
            handle_x = int(slider_x + (gear_radius_pct-0.05)/0.7 * (slider_w-12))
            pygame.draw.rect(surface, (100,200,255), (handle_x, slider_y-4, 12, 16), border_radius=6)
            r_val = int(spiro.radius * gear_radius_pct)
            surface.blit(label_font.render(f'{r_val}', True, (255,255,255)), (slider_x+slider_w+10, slider_y-8))
            # Holes slider
            surface.blit(label_font.render('Holes:', True, (200,200,200)), (widget_rect.x+20, widget_rect.y+100))
            holes_slider_x = widget_rect.x+100
            holes_slider_y = widget_rect.y+110
            holes_slider_w = 160
            pygame.draw.rect(surface, (120,120,120), (holes_slider_x, holes_slider_y, holes_slider_w, 8), border_radius=4)
            holes_handle_x = int(holes_slider_x + ((gear_holes-1)/9) * (holes_slider_w-12))
            pygame.draw.rect(surface, (255,200,100), (holes_handle_x, holes_slider_y-4, 12, 16), border_radius=6)
            surface.blit(label_font.render(f'{gear_holes}', True, (255,255,255)), (holes_slider_x+holes_slider_w+10, holes_slider_y-8))
            confirm_button.draw(surface)
            cancel_button.draw(surface)
        pygame.display.flip()
        clock.tick(spiro.speed)
    pygame.quit()

if __name__ == "__main__":
    run_gui()
