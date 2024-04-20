import pygame

class Button:
    def __init__(self, x, y, image_path=None, width=None, height=None, text="", font_size=30, text_color=(255, 255, 255)):
        if image_path:
            self.image_path = image_path
            self.image = pygame.image.load(self.image_path)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            
            # Adjust the button size if width and height are provided
            if width and height:
                self.image = pygame.transform.scale(self.image, (width, height))
                self.rect.size = (width, height)
        else:
            self.rect = pygame.Rect(x, y, width, height)
            self.image = None

        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color

    def draw(self, surface):

        if self.image:
            self.image = pygame.image.load(self.image_path)
            surface.blit(self.image, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
        #####-----debugging purposes----#####
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
