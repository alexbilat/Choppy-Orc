_author_ = "Alex Bilat"
_date_ = "2025/01/15"
_version_ = "1.3"
_filename_ = "restart.py"
_description_ = "This file is responsible for the restart button"

from settings import *

class Restart(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        """Init the restart button"""
        super().__init__()
        
        self.button = pygame.image.load('images/buttons/restart.png').convert()
        self.button = pygame.transform.scale_by(self.button, 5)

        self.center_x = x
        self.center_y = y

        self.big_button = pygame.transform.scale_by(self.button, 1.1)

        self.image = self.button
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        self.player = player


    def animation(self, mouse_pos):   
        """Make the button larger is mouse is hovering over it"""
        if self.rect.collidepoint(mouse_pos):
            self.image = self.big_button
            self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        else:
            self.image = self.button
            self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
    
    def colisions(self, events, mouse_pos):
        """Check for clicks to restart level"""
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN: #If clicked, kill the player to restart level
                if self.rect.collidepoint(mouse_pos):
                    if self.player.alive:
                        self.player.alive = False
                        self.player.player_animation_index = 0
                        self.player.gravity = 0
            
    def update(self, mouse_pos, events):
        """Update everything at once"""
        self.colisions(events, mouse_pos)
        self.animation(mouse_pos)