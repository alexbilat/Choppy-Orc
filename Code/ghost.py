_author_ = "Alex Bilat"
_date_ = "2025/01/14"
_version_ = "2.0"
_filename_ = "ghost.py"
_description_ = "This file is responsible for the ghosts"

from settings import *

class Ghost(pygame.sprite.Sprite):
    shared_image = None #share images for all
    shared_frame_counter = 0  
    shared_frame_delay = 15 
    ghost_images = []
    shared_mask = None #mask for collisions
    shared_animation_index = 0
    delay = random.randint(1, 20)

    def __init__(self, x, y, go_down, player_class, stick, axe):
        """Initiates ghost class"""
        super().__init__()
        if not Ghost.ghost_images:
            Ghost.load_images()
        
        self.image = Ghost.shared_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = Ghost.shared_mask
        self.x = x
        self.y = y
        self.base_y = y
        self.living = True
        self.death_animation_index = 0     

        #Movement variables
        self.go_down = go_down
        self.start_x = x
        self.start_y = y
        self.speed = 2 
        self.travel_distance = 0
        self.acceleration = 0.1
        self.max_speed = 3
        self.current_speed = 0
        self.time = 0

        #Classes
        self.player = player_class
        self.stick = stick
        self.axe = axe

    @classmethod
    def load_images(cls):
        """Loads the images so that every instance of the class can use it"""
        ghost_1 = pygame.image.load('images/ghost/ghost_1.png').convert_alpha()
        ghost_1 = pygame.transform.scale_by(ghost_1, 5)
        ghost_2 = pygame.image.load('images/ghost/ghost_2.png').convert_alpha()
        ghost_2 = pygame.transform.scale_by(ghost_2, 5)
        ghost_3 = pygame.image.load('images/ghost/ghost_3.png').convert_alpha()
        ghost_3 = pygame.transform.scale_by(ghost_3, 5)

        cls.ghost_images = [ghost_1, ghost_2, ghost_3]
        cls.shared_image = ghost_1
        cls.shared_mask = pygame.mask.from_surface(cls.shared_image)

    @classmethod
    def update_shared_animation(cls):
        """
        Updates the shared animation for ALL ghost instances with a delay.
        Random ghost blinking
        """

        if not cls.ghost_images:
            return
        cls.shared_frame_counter += 1
        if cls.shared_animation_index % 3 == 0:
            frame_delay = cls.shared_frame_delay * cls.delay  #Stay longer on frame 1
        else:
            frame_delay = cls.shared_frame_delay  #Normal delay for frames 2 and 3

        if cls.shared_frame_counter >= frame_delay:
            cls.shared_animation_index += 1
            cls.shared_image = cls.ghost_images[cls.shared_animation_index % 3]
            cls.shared_mask = pygame.mask.from_surface(cls.shared_image)
            cls.shared_frame_counter = 0
            if cls.shared_animation_index % 3 == 0:
                cls.delay = random.randint(1, 20)  
            
    def animation(self):
        """Keep the center of the rect and show the new image"""
        self.death_animation_index = 0
        self.image = Ghost.ghost_images[Ghost.shared_animation_index % 3]
        self.mask = Ghost.shared_mask

    def movement(self):
        """Oscilate the ghost up and down"""
        if self.player.alive:
            self.time += 0.03 
            offset = self.go_down * math.sin(self.time)
            self.rect.y = self.base_y + offset

    def reset(self):
        """Reset the ghost to original position"""
        self.rect.center = (self.x, self.base_y) 
        self.current_speed = 0
        self.living = True
        self.time = 0

    def check_for_fade(self):
        """Fade the ghost and remove collisions when the axe is on stick"""
        if self.stick.sprite.stuck:
            self.living = False
            self.image.set_alpha(153)
        else:
            self.living = True
            self.image.set_alpha(255)
        
    
    def update(self):
        """Update everything at once"""
        self.check_for_fade()
        self.movement()
        self.animation()
