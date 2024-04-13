import pygame
from player import Player

class BackgroundImage:
    def __init__(self, screen, image_path, window_width, window_height):
        self.image_path = image_path
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (window_width, window_height))
        self.screen = screen

    
    def display(self):
        self.screen.blit(self.image, (0, 0))
        
        
        