_author_ = "Alex Bilat"
_date_ = "2024/31/20"
_version_ = "2.0"
_filename_ = "start_screen.py"
_description_ = "Creates start screen"

from settings import *

class Start_screen(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the start screen class"""
        super().__init__()

        #background
        self.background_surf = pygame.image.load('images/background.png').convert()
        self.background_surf = pygame.transform.scale(self.background_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_rect = self.background_surf.get_rect(topleft = (0,0))

        #title
        self.start_surf = pygame.image.load('images/buttons/title.png').convert()
        self.start_surf = pygame.transform.scale_by(self.start_surf, 8)
        self.start_rect = self.start_surf.get_rect(center = ((SCREEN_WIDTH/2),(150)))

        #start button
        self.play_surf = pygame.image.load('images/buttons/start.png').convert_alpha()
        self.play_surf = pygame.transform.scale_by(self.play_surf, 1.6)
        self.play_rect = self.play_surf.get_rect(center = ((SCREEN_WIDTH//2),((SCREEN_HEIGHT//2) - 50)))
        self.play_surf_2 = pygame.transform.scale_by(self.play_surf, 1.1)
        self.play_rect_2 = self.play_surf_2.get_rect(center = ((SCREEN_WIDTH//2),((SCREEN_HEIGHT//2) - 50)))

    def draw(self, screen, mouse_pos):
        """Draw the main screen"""
        #Draw
        screen.blit(self.background_surf, self.background_rect)
        screen.blit(self.start_surf, self.start_rect)
        
        #Zoom animation on start button
        if self.play_rect.collidepoint(mouse_pos):
            screen.blit(self.play_surf_2, self.play_rect_2)
        else:
            screen.blit(self.play_surf, self.play_rect)

    def clicked(self, mouse_pos, event):
        """Check for clicks on start button"""
        #Allow clicks
        if event.type == pygame.MOUSEBUTTONDOWN and self.play_rect.collidepoint(mouse_pos):
            return 'level_1'
        else:
            return 'start'
    
    def update(self, screen, mouse_pos, event):
        """Main update code for start screen"""
        self.draw(screen, mouse_pos)
        return self.clicked(mouse_pos, event)
    