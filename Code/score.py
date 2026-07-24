_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "4.2"
_filename_ = "score.py"
_description_ = "This file is responsible for the score displaying"

from settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        """Init the score display"""
        super().__init__()
        self.font = pygame.font.Font('font/font.ttf', 50)
        self.score = 0
        self.start_time = None
        self.image = self.font.render(f'{self.score}', False, 'white')
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, 50))
        

    def start_counting(self):
        """Start counting the score"""
        if not self.start_time:
            self.start_time = pygame.time.get_ticks()

    def stop_counting(self):
        """Stop counting the score"""
        self.start_time = None
        self.image = self.font.render(f'Score: {self.score}', False, 'white')
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, 250))
        return self.score

    def update(self):
        """Display the score"""
        if self.start_time:
            current_time = pygame.time.get_ticks()
            self.score = (current_time - self.start_time) // 10 
            self.image = self.font.render(f'{self.score}', False, 'white')
            self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, 50))
        