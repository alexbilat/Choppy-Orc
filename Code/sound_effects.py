_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "1.0"
_filename_ = "sound_effects.py"
_description_ = "Creates SFX mute buttons and handles on/off sfx for all sounds in game"

from settings import *

class Sound_Effects(pygame.sprite.Sprite):
    _instance = None
    sfx_enabled = True 
    
    def __new__(cls, x, y):
        """Make sure that only once instance of the sound_effects ever exists (stop looping the sound)"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, x, y):
        """Init the SFX buttons and turn on/off SFX"""
        if self.initialized:
            self.rect.center = (x, y)
            return
            
        super().__init__()
        self.sfx_on = pygame.image.load('images/buttons/sfx_on.png').convert()
        self.sfx_on = pygame.transform.scale_by(self.sfx_on, 5)
        self.sfx_off = pygame.image.load('images/buttons/sfx_off.png').convert()
        self.sfx_off = pygame.transform.scale_by(self.sfx_off, 5)
        self.rect = self.sfx_on.get_rect(center=(x, y))
        self.image = self.sfx_on
        self.initialized = True

    def update(self, mouse_pos, events):
        """Check for clicks and disabling the sound effects"""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(mouse_pos):
                    Sound_Effects.sfx_enabled = not Sound_Effects.sfx_enabled
                    if Sound_Effects.sfx_enabled:
                        self.image = self.sfx_on
                    else:
                        self.image = self.sfx_off

        