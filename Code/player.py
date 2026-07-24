_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "20.1"
_filename_ = "player.py"
_description_ = "This file is responsible for the player"

from settings import *
from bat import *

class Player(pygame.sprite.Sprite):
    def __init__(self, fire, axe, chest, spike, bat, ghost, sound):
        """Initializing the player class"""
        super().__init__()

        #Classes
        self.ghost = ghost
        self.spike = spike
        self.fire = fire
        self.chest = chest
        self.bat = bat
        self.axe = axe
        self.sound = sound

        #Start variables
        self.gravity = 2.5
        self.max_gravity = 20
        self.alive = True
        self.death_timer = 0
        self.direction = 'right'
        self.moving = False
        self.falling = False
        self.jump_up = False
        self.walking_speed = 7
        self.dx = 0
        self.on_floor = True

        #Player stand right
        self.player_stand_1 = pygame.image.load('images/player/player_stand_1.png').convert_alpha()
        self.player_stand_1 = pygame.transform.scale_by( self.player_stand_1, 5)
        self.player_stand_2 = pygame.image.load('images/player/player_stand_2.png').convert_alpha()
        self.player_stand_2 = pygame.transform.scale_by( self.player_stand_2, 5)
        self.player_stand_3 = pygame.image.load('images/player/player_stand_3.png').convert_alpha()
        self.player_stand_3 = pygame.transform.scale_by( self.player_stand_3, 5)
        self.player_stand = [self.player_stand_1, self.player_stand_2, self.player_stand_3]

        #Player stand left
        self.player_stand_1_flipped = pygame.transform.flip(self.player_stand_1, True, False)
        self.player_stand_2_flipped = pygame.transform.flip(self.player_stand_2, True, False)
        self.player_stand_3_flipped = pygame.transform.flip(self.player_stand_3, True, False)
        self.player_stand_flipped = [self.player_stand_1_flipped, self.player_stand_2_flipped, self.player_stand_3_flipped]

        #Player jump right
        self.player_jump = pygame.image.load('images/player/player_jump.png').convert_alpha()
        self.player_jump = pygame.transform.scale_by(self.player_jump, 5)
        #Player jump left
        self.player_jump_flipped = pygame.transform.flip(self.player_jump, True, False)

        #Player walk right
        self.player_walk_1 = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
        self.player_walk_1 = pygame.transform.scale_by(self.player_walk_1, 5)
        self.player_walk_2 = pygame.image.load('images/player/player_walk_2.png').convert_alpha()
        self.player_walk_2 = pygame.transform.scale_by(self.player_walk_2, 5)
        self.player_walk_3 = pygame.image.load('images/player/player_walk_3.png').convert_alpha()
        self.player_walk_3 = pygame.transform.scale_by(self.player_walk_3, 5)
        self.player_walk = [self.player_walk_1, self.player_walk_2, self.player_walk_3]

        #Player walk left
        self.player_walk_1_flipped = pygame.transform.flip(self.player_walk_1, True, False)
        self.player_walk_2_flipped = pygame.transform.flip(self.player_walk_2, True, False)
        self.player_walk_3_flipped = pygame.transform.flip(self.player_walk_3, True, False)
        self.player_walk_flipped = [self.player_walk_1_flipped, self.player_walk_2_flipped, self.player_walk_3_flipped]
        
        #Main stand animation
        self.player_animation_index = 0
        self.image = self.player_stand[self.player_animation_index]
        self.rect = self.image.get_rect(midbottom=(250, 833))

        #Player burn right
        self.player_burn_1 = pygame.image.load('images/player/player_burn_1.png').convert_alpha()
        self.player_burn_2 = pygame.image.load('images/player/player_burn_2.png').convert_alpha()
        self.player_burn_3 = pygame.image.load('images/player/player_burn_3.png').convert_alpha()
        self.player_burn_4 = pygame.image.load('images/player/player_burn_4.png').convert_alpha()
        self.player_burn_5 = pygame.image.load('images/player/player_burn_5.png').convert_alpha()
        self.player_burn_6 = pygame.image.load('images/player/player_burn_6.png').convert_alpha()
        self.player_burn_7 = pygame.image.load('images/player/player_burn_7.png').convert_alpha()
        self.player_burn_8 = pygame.image.load('images/player/player_burn_8.png').convert_alpha()
        self.burn = [self.player_burn_1, self.player_burn_2, self.player_burn_3, self.player_burn_4, self.player_burn_5, self.player_burn_6, self.player_burn_7, self.player_burn_8]
        for i in range(len(self.burn)):
            self.burn[i] = pygame.transform.scale_by(self.burn[i], 5)

        self.burn_flipped = [pygame.transform.flip(image, True, False) for image in self.burn]
        self.frame_count = 0
        self.frame_max = 30
        self.fading = False

        #Sound
        self.jump_sound = pygame.mixer.Sound('audio/jump.ogg')
        self.jump_sound.set_volume(0.1)
        self.death_sound = pygame.mixer.Sound('audio/player_die.ogg')
        self.death_sound.set_volume(0.1)

    def apply_gravity(self, blocks):
        """
        Applies gravity to the player and handles vertical collisions
        Main logic:
            - Increases the player's gravity by 0.5 each call
            - Moves the player down by the current gravity value
            - Check and adjust for vertical collisions with blocks and rebound_blocks
            - Sets the player's variables based on collisions
        """

        self.gravity += 0.5 #Apply gravity
        if self.gravity > self.max_gravity:
            self.gravity = self.max_gravity
        
        self.rect.y += self.gravity
        
        #Vertical Collisions
        collisions = pygame.sprite.spritecollide(self, blocks.blocks, False) or pygame.sprite.spritecollide(self, blocks.rebound_blocks, False)
        if collisions:
            for block in collisions:
                if self.gravity > 0:  #Moving down
                    if self.rect.bottom >= block.rect.top:
                        self.rect.bottom = block.rect.top
                        self.gravity = 0
                        self.on_floor = True
                        self.falling = False
                        break
                    
                elif self.gravity < 0:  #Moving up
                    if self.rect.top < block.rect.bottom:
                        self.rect.top = block.rect.bottom + 1
                        self.gravity = 0
                        self.on_floor = False
                        self.falling = True
                        break
        else:
            if self.gravity > 0.5:
                self.falling = True   

        if self.falling: 
            collisions = pygame.sprite.spritecollide(self, blocks.blocks, False) or pygame.sprite.spritecollide(self, blocks.rebound_blocks, False)
            for block in collisions:
                if self.rect.top < block.rect.bottom:
                    self.rect.top = block.rect.bottom + 1
                    self.gravity = 0
                    self.on_floor = False
                    self.falling = True
                    break 

    def movement(self, blocks):
        """
        Handles the player's movement and horizontal collisions
        Movement:
            - Moves the player to the right when 'D' or 'Right Arrow' key is pressed
            - Moves the player to the left when 'A' or 'Left Arrow' key is pressed
            - Makes the player jump when 'W' or 'Up Arrow' key is pressed
        Collision Detection:
            - Check for horizontal collisions with all blocks (blocks, rebound_blocks)
        """

        self.dx = 0
        if self.alive: 
            keys = pygame.key.get_pressed()
            #Go right
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.dx = self.walking_speed 
                self.moving = True
                self.direction = 'right'
            
            #Go left
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:  
                self.dx = -self.walking_speed
                self.moving = True
                self.direction = 'left'
            else:
                self.moving = False

            #Jump!
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_floor and not self.falling:
                if self.sound.sprite.sfx_enabled:
                    self.jump_sound.play()
                self.gravity = -11.5 
                self.on_floor = False
                self.falling = False
                self.jump_up = True
    
            if self.jump_up:
                if self.gravity > 0:
                    self.jump_up = False
                    self.falling = True

            self.rect.x += self.dx

        #Horizontal collisions
        collisions = pygame.sprite.spritecollide(self, blocks.blocks, False) or pygame.sprite.spritecollide(self, blocks.rebound_blocks, False)
        for block in collisions:
            if self.dx > 0:  #Moving right 
                self.rect.right = block.rect.left
            elif self.dx < 0:  #Moving left
                self.rect.left = block.rect.right

    def animation(self):
        """
        Handles the player's animation (with directions)
        Main logic:
            If the player is on the floor:
                - If the player is moving, shows walking animation
                - If the player is not moving, shows standing animation
            If the player is not on the floor:
                - Set the image to the jumping 
        """

        if self.on_floor:
            if self.moving:
                #Walking animation
                self.player_animation_index += 0.15
                if self.player_animation_index >= len(self.player_walk):
                    self.player_animation_index = 0
                if self.direction == 'right':
                    self.image = self.player_walk[int(self.player_animation_index)]
                else:
                    self.image = self.player_walk_flipped[int(self.player_animation_index)]
            else:
                #Standing animation
                self.player_animation_index += 0.12 
                if self.player_animation_index >= len(self.player_stand):
                    self.player_animation_index = 0
                if self.direction == 'right':
                    self.image = self.player_stand[int(self.player_animation_index)]
                else:
                    self.image = self.player_stand_flipped[int(self.player_animation_index)]

            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        else:
            #Jumping animation
            if self.direction == 'right':
                self.image = self.player_jump
            if self.direction == 'left':
                self.image = self.player_jump_flipped

    def fire_collisions(self):
        """Death when coliding with fire"""
        collisions = pygame.sprite.spritecollide(self, self.fire, False, pygame.sprite.collide_mask)
        if collisions:
            if self.sound.sprite.sfx_enabled:
                self.death_sound.play()
            self.alive = False
            self.player_animation_index = 0
            self.gravity = 0

    def spike_collisions(self):
        """Death when coliding with spikes"""
        collisions = pygame.sprite.spritecollide(self, self.spike, False, pygame.sprite.collide_mask)
        if collisions:
            if self.sound.sprite.sfx_enabled:
                self.death_sound.play()
            self.alive = False
            self.player_animation_index = 0
            self.gravity = 0

    def bat_collisions(self):
        """Death when coliding with bats"""
        for bat in self.bat.sprites():  
            if bat.living:
                if pygame.sprite.collide_mask(self, bat):
                    if self.sound.sprite.sfx_enabled:
                        self.death_sound.play()
                    self.alive = False
                    self.player_animation_index = 0
                    self.gravity = 0

    def ghost_collisions(self):
        """Death when coliding with ghosts"""
        for ghost in self.ghost.sprites():  
            if ghost.living:
                if pygame.sprite.collide_mask(self, ghost):
                    if self.sound.sprite.sfx_enabled:
                        self.death_sound.play()
                    self.alive = False
                    self.player_animation_index = 0
                    self.gravity = 0
                    
    def out_of_map(self):
        """Death if ever outside of map (last resort glitch fix)"""
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH:
            self.alive = False
            if self.sound.sprite.sfx_enabled:
                self.death_sound.play()

        if self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.alive = False
            if self.sound.sprite.sfx_enabled:
                self.death_sound.play()

    def dead(self, screen, state):
        """Playing dying animation + reset (fade all elements with screen fade)"""
        fade_surface = None
        if not self.alive:
            if self.player_animation_index < len(self.burn):
                #Death animation
                if self.direction == 'right':
                    self.image = self.burn[int(self.player_animation_index)]
                else:
                    self.image = self.burn_flipped[int(self.player_animation_index)]
                self.player_animation_index += 0.15
            else:

                #Fading phase
                self.frame_count += 1   
                half_way = self.frame_max // 2
                if self.frame_count <= half_way:  #Fade in
                    fade_alpha = int((self.frame_count / (self.frame_max / 2)) * 255)
                    if self.frame_count == 1:
                        for ghost in self.ghost:
                            ghost.reset()
                            ghost.time = 0
                        for chest in self.chest:
                            chest.reset()
                        for bat in self.bat:
                            bat.reset()
                            bat.time = 0
                        if self.axe.stick.sprite:
                            self.axe.stick.sprite.stuck = False
                        self.axe.teleport_to_player()
                           
                else: #Fade out
                    fade_alpha = 255 - int(((self.frame_count - self.frame_max // 2) / (self.frame_max / 2)) * 255)
                    if state == 'level_5':
                        self.rect.midbottom = (375, 840)
                    elif state == 'level_3':
                        self.rect.midbottom = (230, 833) 
                    elif state == 'level_10':
                        self.rect.midbottom = (400, 670)
                    elif state == 'level_11':
                        self.rect.midbottom = (200, 880)
                    elif state == 'level_13':
                        self.rect.midbottom = (200, 833)
                    elif state == 'level_14':
                        self.rect.midbottom = (200, 880)
                    elif state == 'level_15':
                        self.rect.midbottom = (500, 250)  
                    else:
                       self.rect.midbottom = (250, 833) 

                fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                fade_surface.fill((33, 38, 63))
                fade_surface.set_alpha(fade_alpha)
                self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
                
                if self.frame_count > half_way:
                    player_alpha = int(((self.frame_count - half_way) / (self.frame_max / 2)) * 255)
                    self.image = self.player_stand[0]
                    self.image.set_alpha(player_alpha)                

                self.fading = True

                if self.frame_count >= self.frame_max: #Respawn
                    self.player_animation_index = 0
                    self.alive = True
                    self.frame_count = 0
                    self.direction = 'right'
                    self.death_timer = 0
                    self.gravity = 0
                    self.fading = False
                                    
        if fade_surface:
            screen.blit(fade_surface, (0, 0))
        return fade_surface
            
    def update(self, blocks, screen, state):
        """Update everything at once"""
        if self.alive:
            self.fire_collisions()
            self.spike_collisions()
            self.bat_collisions()
            self.ghost_collisions()
            self.movement(blocks)
            self.apply_gravity(blocks)
            self.animation()
            self.out_of_map()
        fade_surface = self.dead(screen, state)
        return fade_surface
