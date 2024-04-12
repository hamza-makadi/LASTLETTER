import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, font_size=30, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        self.handle_hover()

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_hover(self):
        if self.is_hovered():
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set a pointer cursor when hovered
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Set the default arrow cursor when not hovered

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
