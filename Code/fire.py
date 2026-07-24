_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "3.0"
_filename_ = "fire.py"
_description_ = "This file is responsible for the fire"

from settings import *

class Fire(pygame.sprite.Sprite):

    shared_image = None #Share images for all
    shared_frame_counter = 0  
    shared_frame_delay = 15 
    fire_images = [] #Main images
    shared_mask = None #Mask for collisions

    def __init__(self, x, y):
        """Initiates fire class"""
        super().__init__()
        if not Fire.fire_images:
            fire_1 = pygame.image.load('images/fire/fire_1.png').convert_alpha()
            fire_1 = pygame.transform.scale_by(fire_1, 5)
            fire_2 = pygame.image.load('images/fire/fire_2.png').convert_alpha()
            fire_2 = pygame.transform.scale_by(fire_2, 5)
            fire_3 = pygame.image.load('images/fire/fire_3.png').convert_alpha()
            fire_3 = pygame.transform.scale_by(fire_3, 5)
            fire_4 = pygame.image.load('images/fire/fire_4.png').convert_alpha()
            fire_4 = pygame.transform.scale_by(fire_4, 5)
            fire_5 = pygame.image.load('images/fire/fire_5.png').convert_alpha()
            fire_5 = pygame.transform.scale_by(fire_5, 5)
            fire_6 = pygame.image.load('images/fire/fire_6.png').convert_alpha()
            fire_6 = pygame.transform.scale_by(fire_6, 5)
            fire_7 = pygame.image.load('images/fire/fire_7.png').convert_alpha()
            fire_7 = pygame.transform.scale_by(fire_7, 5)

            Fire.fire_images = [fire_1, fire_2, fire_3, fire_4, fire_5, fire_6, fire_7]
        
        #first image (none yet)
        if Fire.shared_image is None:  
            Fire.shared_image = Fire.fire_images[0]
            Fire.shared_mask = pygame.mask.from_surface(Fire.shared_image)

        self.image = Fire.shared_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = Fire.shared_mask

    @classmethod
    def update_shared_animation(cls):
        """Updates fire animation randomly for ALL fires with delay"""
        if not cls.fire_images:
            return
        cls.shared_frame_counter += 1
        if cls.shared_frame_counter >= cls.shared_frame_delay:
            cls.shared_frame_counter = 0
            cls.shared_image = random.choice(cls.fire_images)
            cls.shared_mask = pygame.mask.from_surface(cls.shared_image)

    def animation(self):
        """Changing the fire image but keeping the same bottom"""
        previous_midbottom = self.rect.midbottom 
        self.image = Fire.shared_image  
        self.rect = self.image.get_rect(midbottom=previous_midbottom)
        self.mask = Fire.shared_mask

    def update(self):
        """Updating everything at once"""
        self.animation()
        