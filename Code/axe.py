_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "12.1"
_filename_ = "axe.py"
_description_ = "This file is responsible for the axe"

from settings import *

class Axe(pygame.sprite.Sprite):
    def __init__(self, player, stick, sound):
        """Initialize the Axe class"""
        super().__init__()
        self.is_thrown = False
        self.throw_direction = 'right'
        self.on_wall = False
        self.player_speed = 17
        self.stuck = 'right'
        self.block = None
        self.y = None
        self.has_moved = False
        self.player = player
        self.stick = stick

        #recalling initiation stuff
        self.recalling = False
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 100
        self.max_speed = 50
        self.recall_start_time = 0
        self.allow_throw = True

        #Sound
        self.jump_sound = pygame.mixer.Sound('audio/jump.ogg')
        self.jump_sound.set_volume(0.1)
        self.jump_sound_played = False
        self.recall_sound = pygame.mixer.Sound('audio/recall.ogg')
        self.recall_sound.set_volume(0.1)
        self.throw_sound = pygame.mixer.Sound('audio/axethrow.ogg')
        self.throw_sound.set_volume(0.1)
        self.wall_hit = pygame.mixer.Sound('audio/hit.ogg')
        self.wall_hit.set_volume(0.1)
        self.last_jump_y = 0
        self.can_play_jump_sound = True
        self.sound = sound

        #main images
        self.axe_stand = pygame.image.load('images/axe/axe_stand.png').convert_alpha()
        self.axe_stand = pygame.transform.scale_by(self.axe_stand, 5)
        self.axe_stand_flipped = pygame.transform.flip(self.axe_stand, True, False)
        self.image = self.axe_stand 
        self.rect = self.image.get_rect(center=(self.player.rect.center))
        self.prev_rect = self.rect.copy()
        self.hitbox = self.rect.inflate(42, 0)

        #throwing animation images
        self.axe_throw_1 = pygame.image.load('images/axe/axe_1.png').convert_alpha()
        self.axe_throw_1 = pygame.transform.scale_by(self.axe_throw_1, 5)
        self.axe_throw_2 = pygame.image.load('images/axe/axe_2.png').convert_alpha()
        self.axe_throw_2 = pygame.transform.scale_by(self.axe_throw_2, 5)
        self.axe_throw_3 = pygame.image.load('images/axe/axe_3.png').convert_alpha()
        self.axe_throw_3 = pygame.transform.scale_by(self.axe_throw_3, 5)
        self.axe_throw_4 = pygame.image.load('images/axe/axe_4.png').convert_alpha()
        self.axe_throw_4 = pygame.transform.scale_by(self.axe_throw_4, 5)
        self.axe_throw = [self.axe_throw_1, self.axe_throw_2, self.axe_throw_3, self.axe_throw_4]
        self.axe_throw_index = 0

        #throwing animation flipped
        self.axe_throw_1_flipped = pygame.transform.flip(self.axe_throw_1, True, False)
        self.axe_throw_2_flipped = pygame.transform.flip(self.axe_throw_2, True, False)
        self.axe_throw_3_flipped = pygame.transform.flip(self.axe_throw_3, True, False)
        self.axe_throw_4_flipped = pygame.transform.flip(self.axe_throw_4, True, False)
        self.axe_throw_flipped = [self.axe_throw_1_flipped, self.axe_throw_2_flipped, self.axe_throw_3_flipped, self.axe_throw_4_flipped]

        #stuck image
        self.axe_stuck = pygame.image.load('images/axe/axe_stuck.png').convert_alpha()
        self.axe_stuck = pygame.transform.scale_by(self.axe_stuck, 5)
        self.axe_stuck_flipped = pygame.transform.flip(self.axe_stuck, True, False)
        self.axe_stuck_rect = self.axe_stuck.get_rect(center = (self.rect.center))
        self.axe_stuck_rect_flipped = self.axe_stuck_flipped.get_rect(center = (self.rect.center))

    def animation(self, player_rect, player_direction):
        """
        Updates the axe's animation state based on what's happening in game
        Main logic:
            - If the axe is not thrown, not on the wall, and not being recalled (or the player is just walking), it updates the axe's position and image to the standing one
            - If the axe is stuck anywhere, it updates the axe's image to the stuck animation
            - If the axe is thrown or being recalled, it updates the axe's image to the throwing/spinning animation (cycle through the animation list)
            - If the player is fading, it makes the axe invisible and updates its position if it was on the wall (so you don't see the axe when the player is reseting)
        """

        if not self.is_thrown and not self.on_wall and not self.recalling: #Walking around with the axe
            if player_direction == 'right':
                self.image = self.axe_stand
                x, y = player_rect.midbottom
                self.rect.midbottom = (x - 20,y)
            else:
                self.image = self.axe_stand_flipped
                x, y = player_rect.midbottom
                self.rect.midbottom = (x + 20,y)
        
        if self.on_wall: #Stuck animation
            if self.throw_direction == 'right':
                self.image = self.axe_stuck
            else:
                self.image = self.axe_stuck_flipped


        if (self.is_thrown or self.recalling): #Throwing/spinning animation
            self.axe_throw_index += 0.2
            if self.axe_throw_index >= len(self.axe_throw):
                self.axe_throw_index = 0
            if self.throw_direction == 'right':
                self.image = self.axe_throw[int(self.axe_throw_index)]
            else:
                self.image = self.axe_throw_flipped[int(self.axe_throw_index)]

        if self.player.fading: #Make axe invisible during fades
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
            if self.on_wall:
                x, y = player_rect.midbottom
                self.rect.midbottom = (x - 20,y)
                self.on_wall = False

        if self.player.frame_count > (self.player.frame_max//2): #Make the axe fade with the player
            axe_alpha = int(((self.player.frame_count - (self.player.frame_max//2)) / (self.player.frame_max / 2)) * 255)
            x, y = player_rect.midbottom
            self.rect.midbottom = (x - 20,y)
            self.image = self.axe_stand
            self.image.set_alpha(axe_alpha)        

    def movement(self, player_direction, events, player_rect):
        """
        Does the throwing and recallling for the axe
        Main logic:
        - Throw the axe when the space key is pressed
        - Play the throw sound (if sfx enabled)
        - Recall the axe when the space key is pressed
        - Play the recall sound (if sfx enabled)
        - Teleport the axe to the player if it has been in the air for more than 1.5 seconds (fixing orbit glitch)
        - Resets the axe's variables when it reaches the player
        """

        if self.player.alive:
            if not self.player.fading:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not self.is_thrown and not self.on_wall and self.allow_throw:
                                #throw the axe
                                self.is_thrown = True
                                if self.sound.sprite.sfx_enabled:
                                    self.throw_sound.play()
                                self.throw_direction = player_direction

                            elif self.on_wall and not self.is_thrown and not self.recalling:
                                #recall the axe
                                self.recalling = True
                                if self.sound.sprite.sfx_enabled:
                                    self.recall_sound.play()
                                self.allow_throw = False
                                self.recall_start_time = pygame.time.get_ticks()
                                self.velocity_x = 0
                                self.velocity_y = 0

        #THROWING THE AXE
        if self.is_thrown:
            if self.throw_direction == 'right':
                self.rect.x += self.player_speed #Throw right
                self.has_moved = True
            else:
                self.rect.x -= self.player_speed  #Throw left
                self.has_moved = True


        #RECALLING THE AXE
        if self.recalling and not self.is_thrown: 
            player_x, player_y = player_rect.center 
            direction_x = player_x - self.rect.centerx #Find direction to player left or right
            direction_y = player_y - self.rect.centery #Find direction to player up or down
            distance = (direction_x ** 2 + direction_y ** 2) ** 0.5 #Normalize so the axe doesn't move too fast when moving down (pythagorean theorem for hypotenus (or distance to player))
            if distance != 0: #When you're at the player (or don't devide by 0)
                direction_x /= distance #Normalize
                direction_y /= distance #Normalize

            #Apply acceleration
            self.velocity_x += self.acceleration * direction_x 
            self.velocity_y += self.acceleration * direction_y 

            speed = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
            if speed > self.max_speed:
                self.velocity_x = (self.velocity_x / speed) * self.max_speed
                self.velocity_y = (self.velocity_y / speed) * self.max_speed

            #Move the axe
            self.rect.x += int(self.velocity_x) 
            self.rect.y += int(self.velocity_y) 

            elapsed_time = pygame.time.get_ticks() - self.recall_start_time #Teleport to player if in air for 1.5+ seconds (orbit glitch fix)
            if elapsed_time > 1500:  
                self.teleport_to_player()

            #Bigger catch area
            enlarged_player_rect = player_rect.inflate(75, 75)

            #Reset when axe reaches the player
            if self.rect.colliderect(enlarged_player_rect):
                self.recalling = False
                self.on_wall = False
                self.is_thrown = False
                self.velocity_x = 0
                self.velocity_y = 0
                self.rect = self.prev_rect
                self.allow_throw = True
        
    def collisions(self, blocks):
        """
        Handle collisions and making the axe stick to walls 
        Handle rebounds off the yellow walls
        """
        
        if self.is_thrown and self.has_moved:
            fake_collisions = pygame.sprite.spritecollide(self, blocks.rebound_blocks, False, None)
            if fake_collisions:
                for block in fake_collisions: #Recalling collisions
                    if self.throw_direction == 'right': #Collisions on the right
                        if self.prev_rect.right <= block.rect.left:
                            self.on_wall = False  
                            self.recalling = True
                            if self.sound.sprite.sfx_enabled:
                                self.recall_sound.play()
                            self.is_thrown = False
                            self.allow_throw = False
                            self.recall_start_time = pygame.time.get_ticks()
                            return 
                    else: #Collisions on the left
                        if self.prev_rect.left >= block.rect.right: 
                            self.on_wall = False  
                            self.recalling = True
                            if self.sound.sprite.sfx_enabled:
                                self.recall_sound.play()
                            self.is_thrown = False
                            self.allow_throw = False
                            self.recall_start_time = pygame.time.get_ticks()
                            return
                    
        if self.is_thrown and self.has_moved:
            collisions = pygame.sprite.spritecollide(self, blocks.blocks, False,  None ) 
            if collisions: #Normal collisions
                for block in collisions:
                    self.block = block
                    if self.throw_direction == 'right': #Rightside wall collisions   
                        if self.prev_rect.right <= block.rect.left:
                            if self.sound.sprite.sfx_enabled:
                                self.wall_hit.play()
                            self.rect.y += 30
                            self.rect.right = self.block.rect.left
                            self.on_wall = True
                            self.is_thrown = False
                            self.stuck = 'left'
                            
                        else:
                            pass
                        
                    else: #Leftside wall collisions
                        if self.prev_rect.left >= block.rect.right:
                            if self.sound.sprite.sfx_enabled:
                                self.wall_hit.play()
                            self.rect.y += 30
                            self.rect.left = block.rect.right
                            self.on_wall = True
                            self.is_thrown = False
                            self.stuck = 'right'
                        else:
                            pass
            
    def axe_jump(self):
        """Making player bounce up on the axe"""
        if not self.jump_sound_played and self.can_play_jump_sound:
            if self.sound.sprite.sfx_enabled:
                self.jump_sound.play()
            self.jump_sound_played = True
            self.can_play_jump_sound = False
        self.player.gravity = -17
            
    def teleport_to_player(self):
        """Teleports axe back to player"""
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.is_thrown = False
        self.on_wall = False
        self.recalling = False
        self.allow_throw = True
        self.velocity_x = 0
        self.velocity_y = 0
        if self.stick.sprite:
            self.stick.sprite.stuck = False
        x, y = self.player.rect.midbottom
        self.rect.midbottom = (x - 20,y)
    
    def stick_collisions(self):
        """Collisions with the ghost stick to disable ghosts"""
        stick_sprite = self.stick.sprite
        if stick_sprite and stick_sprite.stuck and not self.recalling:
            if self.throw_direction == 'right':
                self.rect.midright = stick_sprite.rect.midleft
            else:
                x, y = stick_sprite.rect.midright
                self.rect.midleft = (x - 20, y)
            self.on_wall = True
            self.is_thrown = False  
            self.recalling = False
    
    def update(self, player_rect, player_direction, blocks, events):
        """Update the axe all at once"""
        self.prev_rect = self.rect.copy()
        self.hitbox.center = self.rect.center
        if self.on_wall:
            if self.rect.colliderect(self.player.rect):
                if self.player.falling:
                    self.axe_jump()
            else:
                self.can_play_jump_sound = True
                self.jump_sound_played = False

        self.movement(player_direction, events, player_rect)
        self.collisions(blocks)
        self.stick_collisions()
        self.animation(player_rect, player_direction)
