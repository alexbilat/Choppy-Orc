_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "2.0"
_filename_ = "chest.py"
_description_ = "This file is responsible for the chests"

from settings import *

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y, player, sound):
        """Init the bat class"""
        super().__init__()
        self.chest_close = pygame.image.load('images/chests/chest_close.png').convert_alpha()
        self.chest_close = pygame.transform.scale_by(self.chest_close, 5.3)
        self.chest_open = pygame.image.load('images/chests/chest_open.png').convert_alpha()
        self.chest_open = pygame.transform.scale_by(self.chest_open, 5.3)
        self.is_open = False
        self.player = player
        self.sound = sound
        self.image = self.chest_close
        self.rect = self.image.get_rect(center=(x, y))
        self.chest_sound = pygame.mixer.Sound('audio/win.ogg')
        self.chest_sound.set_volume(0.1)
        self.chest_sound.set_volume(0.2)
        self.sound_played = False

    def collisions(self):
        """
        Check for collisions between chest and player.
        Change animation and mark chest open
        """
        
        if self.rect.colliderect(self.player.rect) and not self.is_open:
            self.image = self.chest_open
            if not self.sound_played:
                if self.sound.sprite.sfx_enabled:
                    self.chest_sound.play()
                self.sound_played = True
            self.is_open = True

    def reset(self):
        """Reseting the chest back to close"""
        self.image = self.chest_close
        self.is_open = False
        self.sound_played = False

    def update(self):
        """Updating everything at once"""
        self.collisions()

    @classmethod
    def all_chests_open(cls, chests):
        """Check if all chests are open"""
        return all(chest.is_open for chest in chests)
