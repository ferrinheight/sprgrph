import pygame

class UIButton:
    def __init__(self, text, x, y, width, height, callback, font_size, font_color, outline_color, fill_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font(None, font_size)
        self.font_color = font_color
        self.outline_color = outline_color
        self.fill_color = fill_color
        self.rendered = None
        self._render()

    def _render(self):
        self.rendered = pygame.Surface((self.rect.width, self.rect.height))
        self.rendered.fill(self.outline_color)
        pygame.draw.rect(self.rendered, self.fill_color, (2, 2, self.rect.width-4, self.rect.height-4))
        text_surf = self.font.render(self.text, True, self.font_color)
        tw, th = text_surf.get_size()
        self.rendered.blit(text_surf, (self.rect.width//2 - tw//2, self.rect.height//2 - th//2))

    def draw(self, surface):
        surface.blit(self.rendered, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()
