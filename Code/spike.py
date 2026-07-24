_author_ = "Alex Bilat"
_date_ = "2025/01/12"
_version_ = "4.0"
_filename_ = "spike.py"
_description_ = "Creates spike obstacles"

from settings import *

class Spike(pygame.sprite.Sprite):

    shared_image = None  #Share images for all
    shared_frame_counter = 0
    shared_frame_delay = 15
    spike_images = []  #Main images
    shared_mask = None  #Mask for collisions

    def __init__(self, x, y):
        """Init spikes"""
        super().__init__()
        if not Spike.spike_images:
            Spike.load_images()
        self.image = Spike.shared_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = Spike.shared_mask

    @classmethod
    def load_images(cls):
        """Load all the images for all instances once"""
        spike_1 = pygame.image.load('images/spikes/spike_1.png').convert_alpha()
        spike_1 = pygame.transform.scale_by(spike_1, 5)
        spike_2 = pygame.image.load('images/spikes/spike_2.png').convert_alpha()
        spike_2 = pygame.transform.scale_by(spike_2, 5)
        spike_3 = pygame.image.load('images/spikes/spike_3.png').convert_alpha()
        spike_3 = pygame.transform.scale_by(spike_3, 5)
        spike_4 = pygame.image.load('images/spikes/spike_4.png').convert_alpha()
        spike_4 = pygame.transform.scale_by(spike_4, 5)
        cls.spike_images = [spike_1, spike_2, spike_3, spike_4]
        cls.shared_image = random.choice(cls.spike_images)
        cls.shared_mask = pygame.mask.from_surface(cls.shared_image)

    @classmethod
    def update_shared_animation(cls):
        """Random spike animation for ALL spikes with delay"""
        if not cls.spike_images:
            return
        cls.shared_frame_counter += 1
        if cls.shared_frame_counter >= cls.shared_frame_delay:
            cls.shared_frame_counter = 0
            cls.shared_image = random.choice(cls.spike_images)
            cls.shared_mask = pygame.mask.from_surface(cls.shared_image)

    def animation(self):
        """Apply the image"""
        self.image = Spike.shared_image  
        self.mask = Spike.shared_mask

    def update(self):
        """Update everything at once"""
        self.animation()
        