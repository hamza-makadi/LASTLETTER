import pygame ,sys ,string
from button import Button

class Player:
    def __init__(self,x,y,active):
        self.x = x
        self.y = y
        self.active = active
        self.images = player_images = [
                                        pygame.image.load("assets/img/icons/Face1.png"),
                                        pygame.image.load("assets/img/icons/Face2.png"),
                                        pygame.image.load("assets/img/icons/Face3.png"),
                                        pygame.image.load("assets/img/icons/Face4.png"),
                                        pygame.image.load("assets/img/icons/Face5.png"),
                                        pygame.image.load("assets/img/icons/Face6.png"),
                                        pygame.image.load("assets/img/icons/Face7.png"),
                                        pygame.image.load("assets/img/icons/Face8.png")    
                                    ]
        self.not_player = pygame.image.load("assets/img/Empty1.png")
        self.image_index = 0  # Default image index
        self.font = pygame.font.Font(None, 24)
        self.input_rect = pygame.Rect(x-25, y+150, 200, 30)  # Position and size of text input box
        self.input_text = ""  # Text entered by the player
        self.active_input = False

        self.next_image = Button(x+130, y+60,image_path="assets/img/Arrow_r.png")
        self.previous_image = Button(x-0, y+60,image_path="assets/img/Arrow_l.png")

    def draw(self, screen):
        if self.active:
            # Draw player image
            player_image = self.images[self.image_index]
            screen.blit(player_image, (self.x, self.y))

            # Draw text input box
            if self.active_input :
                pygame.draw.rect(screen, (171,216,209), self.input_rect, 2)
            else:
                pygame.draw.rect(screen, (102,130,126), self.input_rect, 2)

            ## Draw text itself
            self.draw_placeholder(screen)
            text_surface = self.font.render(self.input_text, True, (255, 255, 255))
            screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 7))
        else:
            screen.blit(self.not_player, (self.x, self.y))
            pygame.draw.rect(screen, (102,130,126), self.input_rect, 2)
        
        self.next_image.draw(screen)
        self.previous_image.draw(screen)

    def draw_placeholder(self,screen):
        if self.input_text=="":
            place_holder = self.font.render("Type your name", True, (155, 155, 155))
            screen.blit(place_holder, (self.input_rect.x + 5, self.input_rect.y + 7))

    def change_player_image(self,event):  
        if self.next_image.is_clicked(event.pos):
            self.select_next_image()
        elif self.previous_image.is_clicked(event.pos):
            self.select_previous_image()

    def select_next_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)

    def select_previous_image(self):
        self.image_index = (self.image_index - 1) % len(self.images)

    def get_player_name(self):
        return self.input_text

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.input_rect.collidepoint(event.pos):
                self.active_input = not self.active_input

            else:
                self.active_input = False
        elif event.type == pygame.KEYDOWN:
            if self.active_input and self.active:   
                if event.key == pygame.K_RETURN:
                    self.active_input = False  # Deactivate the text input box when Enter is pressed
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.unicode in string.ascii_letters:  # Check if the typed character is a letter
                    self.input_text += event.unicode