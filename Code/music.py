_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "5.0"
_filename_ = "music.py"
_description_ = "This file is responsible for the music buttons and main song"

from settings import *

class Music(pygame.sprite.Sprite):
    _instance = None
    
    def __new__(cls, x, y):
        """Make sure that music is only initialized once, otherwise music will play over itself"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, x, y):
        """Init music class"""
        if self.initialized:
            self.rect.center = (x, y)
            return
            
        super().__init__()
        self.music_on = pygame.image.load('images/buttons/music_on.png').convert()
        self.music_on = pygame.transform.scale_by(self.music_on, 5)
        self.music_off = pygame.image.load('images/buttons/music_off.png').convert()
        self.music_off = pygame.transform.scale_by(self.music_off, 5)
        self.rect = self.music_on.get_rect(center=(x, y))
        self.image = self.music_on
        self.music = True
        self.song = pygame.mixer.Sound('audio/music.ogg')
        self.song.set_volume(0.1)
        self.song.play(-1)
        self.initialized = True

    def update(self, mouse_pos, events):
        """
        Update the music state based on mouse clicks
        Keep the loop playing, just remove the volume
        """

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN: #Play/mute the sound based on the clicking the button
                if self.rect.collidepoint(mouse_pos):
                    self.music = not self.music
                    if self.music:
                        self.image = self.music_on
                        self.song.set_volume(0.1)
                    else:
                        self.image = self.music_off
                        self.song.set_volume(0)
        