_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "5.0"
_filename_ = "bat.py"
_description_ = "This file is responsible for the bat"

from settings import *

class Bat(pygame.sprite.Sprite):
    shared_image = None #share images for all
    shared_frame_counter = 0  
    shared_frame_delay = 15 
    bat_images = [] #main images
    flipped_images = [] 
    shared_mask = None #mask for collisions
    shared_animation_index = 0

    def __init__(self, x, y, go_left, go_right, speed, player_class, axe, sound):
        """Initiates bat class"""
        super().__init__()
        if not Bat.bat_images:
            bat_1 = pygame.image.load('images/bat/bat_1.png').convert_alpha()
            bat_1 = pygame.transform.scale_by(bat_1, 5)
            bat_2 = pygame.image.load('images/bat/bat_2.png').convert_alpha()
            bat_2 = pygame.transform.scale_by(bat_2, 5)
            bat_3 = pygame.image.load('images/bat/bat_3.png').convert_alpha()
            bat_3 = pygame.transform.scale_by(bat_3, 5) 
            bat_4 = pygame.image.load('images/bat/bat_1.png').convert_alpha()
            bat_4 = pygame.transform.scale_by(bat_4, 5)            
                      
            Bat.bat_images = [bat_3, bat_1, bat_2, bat_4]
        
        if not Bat.flipped_images:
            Bat.flipped_images = [pygame.transform.flip(image, True, False) for image in Bat.bat_images]

        dead_1 = pygame.image.load('images/bat/bat_dead_1.png').convert_alpha()
        dead_1 = pygame.transform.scale_by(dead_1, 5)
        dead_2 = pygame.image.load('images/bat/bat_dead_2.png').convert_alpha()
        dead_2 = pygame.transform.scale_by(dead_2, 5)
        dead_3 = pygame.image.load('images/bat/bat_dead_3.png').convert_alpha()
        dead_3 = pygame.transform.scale_by(dead_3, 5)
        dead_4= pygame.image.load('images/bat/bat_dead_4.png').convert_alpha()
        dead_4 = pygame.transform.scale_by(dead_4, 5)

        self.dead_images = (dead_1, dead_2, dead_3, dead_4)
        self.flipped_dead_images = [pygame.transform.flip(image, True, False) for image in self.dead_images]

        #first image (none yet)
        if Bat.shared_image is None:  
            Bat.shared_image = Bat.bat_images[0]
            Bat.shared_mask = pygame.mask.from_surface(Bat.shared_image)

        self.player = player_class
        self.sound = sound
        self.axe = axe
        self.image = Bat.shared_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = Bat.shared_mask
        self.x = x
        self.y = y
        self.living = True
        self.death_animation_index = 0     

        #Movement variables
        self.go_left = go_left
        self.go_right = go_right
        self.start_x = x
        self.direction = 1  
        self.range = go_right 
        self.travel_distance = 0
        self.acceleration = 0.1
        self.max_speed = 3
        self.current_speed = 0
        self.time = 0
        self.speed = speed

        #Sound
        self.enemy_dead = pygame.mixer.Sound('audio/enemy_dead.ogg')
        self.sound_played = False

    @classmethod
    def update_shared_animation(cls):
        """Updates bat animation for ALL bats with delay"""
        if not cls.bat_images:
            return
        cls.shared_frame_counter += 2.5
        if cls.shared_frame_counter >= cls.shared_frame_delay:
            cls.shared_animation_index += 1
            cls.shared_image = cls.bat_images[cls.shared_animation_index % 4]
            cls.shared_mask = pygame.mask.from_surface(cls.shared_image)
            cls.shared_frame_counter = 0
            
    def animation(self):
        """Making the bat's wings move based on direction"""
        if self.living:
            self.death_animation_index = 0
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
            if self.direction == 1:
                self.image = Bat.shared_image
            else:
                self.image = Bat.flipped_images[Bat.shared_animation_index % 4]
        else:
            if self.death_animation_index < len(self.dead_images):
                if self.direction == 1:
                    self.image = self.dead_images[self.death_animation_index]
                else:
                    self.image = self.flipped_dead_images[self.death_animation_index]
                self.death_animation_index += 1 
            else:
                self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
                    
        self.mask = Bat.shared_mask

    def movement(self):
        """Bat oscilating left and right"""
        if self.player.alive:
            self.time += self.speed

            #Find movement range (from -go_left to +go_right)
            total_range = (self.go_left + self.go_right) / 2
            offset = total_range * math.sin(self.time)
            
            #Update position
            self.rect.x = self.start_x + offset
            
            #Update direction for animation
            if math.cos(self.time) > 0:
                self.direction = 1
            else:
                self.direction = -1

    def dead(self):
        """Making the bat die when colliding with the axe"""
        if not self.living or self.sound_played:
            return
            
        axe_sprite = self.axe.sprite  
        if axe_sprite.is_thrown or axe_sprite.recalling:
            if pygame.sprite.collide_mask(self, axe_sprite):
                self.living = False
                if self.sound.sprite.sfx_enabled:    
                    self.enemy_dead.play()
                self.sound_played = True

    def reset(self):
        """Reseting the bat when it's alive again"""
        self.rect.center = (self.x, self.y)
        self.living = True
        self.current_speed = 0
        self.direction = 1
        self.rect.x = self.start_x
        self.time = 0
        self.sound_played = False
    
    def update(self):
        """Updating everything at once"""
        self.animation()
        self.movement()
        self.dead()
