_author_ = "Alex Bilat"
_date_ = "2025/01/12"
_version_ = "3.0"
_filename_ = "stick.py"
_description_ = "Creates stick for ghost disabling"

from settings import *

class Ghost_stick(pygame.sprite.Sprite):
    shared_image = None  #Share images for all
    shared_frame_counter = 0
    shared_frame_delay = 15
    stick_images = []  #Main images
    shared_mask = None  #Mask for collisions

    def __init__(self, x, y, axe):
        """Init sticks class"""
        super().__init__()
        if not Ghost_stick.stick_images:
            Ghost_stick.load_images()
            
        self.image = Ghost_stick.shared_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = Ghost_stick.shared_mask
        self.axe = axe
        self.stuck = False

    @classmethod
    def load_images(cls):
        """Load images for all sticks"""
        #Stick image
        stick = pygame.image.load('images/Ghost/ghost_stick.png').convert_alpha()
        stick = pygame.transform.scale_by(stick, 5)
        cls.stick_images = [stick]
        cls.shared_image = stick 
        cls.shared_mask = pygame.mask.from_surface(cls.shared_image)
        
    def animation(self): 
        """Apply the image"""  
        self.image = Ghost_stick.shared_image  
        self.mask = Ghost_stick.shared_mask
    
    def colisions(self):
        """Make the axe stick"""
        axe_sprite = self.axe.sprite  
        if axe_sprite.is_thrown and not axe_sprite.recalling:
            if pygame.sprite.collide_mask(self, axe_sprite):
                self.stuck = True
        if axe_sprite.recalling:
            self.stuck = False
            
    def update(self):
        """Update all at once"""
        self.colisions()
        self.animation()