_author_ = "Alex Bilat"
_date_ = "2025/01/11"
_version_ = "16.0"
_filename_ = "blocks.py"
_description_ = "This file is responsible for the level generation"

from settings import *

class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        """Intialize blocks class"""
        super().__init__()
        self.blocks = pygame.sprite.Group()
        self.rebound_blocks = pygame.sprite.Group()

    def clear_blocks(self):
        """Resets blocks"""
        self.blocks.empty()
        self.rebound_blocks.empty()

    def level_1(self):
        """"Getting the layout of level 1"""
        self.clear_blocks() 

        #roof
        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_1/top.png').convert()      
        roof.rect = roof.image.get_rect(topleft = (0,0))
        self.blocks.add(roof)

        level_1 = pygame.sprite.Sprite()
        level_1.image = pygame.image.load('images/level_1/level_1.png').convert()      
        level_1.rect = level_1.image.get_rect(topleft = (0,0))
        self.blocks.add(level_1)
       
        #topleft section
        topleft = pygame.sprite.Sprite()
        topleft.image = pygame.image.load('images/level_1/topleft.png').convert()
        topleft.rect = topleft.image.get_rect(topleft = (0, 119))
        self.blocks.add(topleft)

        #leftsection
        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_1/left.png').convert()
        left.rect = left.image.get_rect(topleft = (0,287))
        self.blocks.add(left)

        #left bottom
        leftbottom = pygame.sprite.Sprite()
        leftbottom.image = pygame.image.load('images/level_1/bottomleft.png').convert()
        leftbottom.rect = leftbottom.image.get_rect(topleft = (0, 833))
        self.blocks.add(leftbottom)

        #bottom 
        bottom = pygame.sprite.Sprite()
        bottom.image= pygame.image.load('images/level_1/bottom.png').convert()
        bottom.rect = bottom.image.get_rect(topleft = (615, 875))
        self.blocks.add(bottom)

        #bottom right ish
        bottomright_ish = pygame.sprite.Sprite()
        bottomright_ish.image = pygame.image.load('images/level_1/bottomright_ish.png').convert()
        bottomright_ish.rect = bottomright_ish.image.get_rect(topleft = (824, 833))
        self.blocks.add(bottomright_ish)

        #bottom right
        bottomright = pygame.sprite.Sprite()
        bottomright.image = pygame.image.load('images/level_1/bottomright.png').convert()
        bottomright.rect = bottomright.image.get_rect(topleft = (1034, 539))
        self.blocks.add(bottomright)

        #right
        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_1/right.png').convert()
        right.rect = right.image.get_rect(topleft = (1580, 215))
        self.blocks.add(right)

        #topright
        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_1/topright.png').convert()
        topright.rect = topright.image.get_rect(topleft = (1327, 119))
        self.blocks.add(topright)

        #middle block
        middle = pygame.sprite.Sprite()
        middle.image = pygame.image.load('images/level_1/middle_block.png').convert()
        middle.rect = middle.image.get_rect(topleft = (355, 457))
        self.blocks.add(middle)

    def level_2(self):
        """"Getting the layout of level 2"""
        self.clear_blocks() 

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_2/floor.png').convert()
        floor.rect = floor.image.get_rect(topleft = (81, SCREEN_HEIGHT - 105))
        self.blocks.add(floor)


        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_2/left.png').convert()
        left.rect = left.image.get_rect(bottomleft = (0, SCREEN_HEIGHT + 9))
        self.blocks.add(left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_2/roof.png').convert()
        roof.rect = roof.image.get_rect(bottomleft = (0, 150))
        self.blocks.add(roof)

        mid = pygame.sprite.Sprite()
        mid.image = pygame.image.load('images/level_2/mid.png').convert()
        x,y = floor.rect.bottomright
        mid.rect = mid.image.get_rect(bottomleft = (x, y + 11))
        self.blocks.add(mid)

        mid_2 = pygame.sprite.Sprite()
        mid_2.image = pygame.image.load('images/level_2/mid_2.png').convert()
        x = mid.rect.right
        mid_2.rect = mid.image.get_rect(topleft = (x, 718))
        self.blocks.add(mid_2)

        mid_3 = pygame.sprite.Sprite()
        mid_3.image = pygame.image.load('images/level_2/mid_3.png').convert()
        mid_3.rect = mid_3.image.get_rect(topleft = (1081, 394))
        self.blocks.add(mid_3)

        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_2/right.png').convert()
        right.rect = right.image.get_rect(topleft = (1486, 30))
        self.blocks.add(right)

        level_2 = pygame.sprite.Sprite()
        level_2.image = pygame.image.load('images/level_2/level_2.png').convert()      
        level_2.rect = level_2.image.get_rect(topleft = (0,0))
        self.blocks.add(level_2)
        
    def level_3(self):
        """"Getting the layout of level 3"""
        self.clear_blocks() 

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_3/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_3/left.png').convert()
        left.rect = left.image.get_rect(topleft = (0, 0))
        self.blocks.add(left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_3/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0,0))
        self.blocks.add(roof)

        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_3/right.png').convert()
        right.rect = right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(right)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_3/topright.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(topright)

        midleft = pygame.sprite.Sprite()
        midleft.image = pygame.image.load('images/level_3/midleft.png').convert()
        midleft.rect = midleft.image.get_rect(bottomleft = (293, SCREEN_HEIGHT))
        self.blocks.add(midleft)

        midright = pygame.sprite.Sprite()
        midright.image = pygame.image.load('images/level_3/midright.png').convert()
        midright.rect = midright.image.get_rect(bottomleft = (1008, SCREEN_HEIGHT))
        self.blocks.add(midright)

        mid = pygame.sprite.Sprite()
        mid.image = pygame.image.load('images/level_3/mid.png').convert()
        mid.rect = mid.image.get_rect(bottomleft = (588, 714))
        self.blocks.add(mid)

    def level_4(self):
        """"Getting the layout of level 4"""
        self.clear_blocks() 

        leftfloor = pygame.sprite.Sprite()
        leftfloor.image = pygame.image.load('images/level_4/leftfloor.png').convert()
        leftfloor.rect = leftfloor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(leftfloor)

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_4/left.png').convert()
        left.rect = left.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_4/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0,0))
        self.blocks.add(roof)

        mid = pygame.sprite.Sprite()
        mid.image = pygame.image.load('images/level_4/mid.png').convert()
        mid.rect = mid.image.get_rect(bottomleft = (leftfloor.rect.bottomright))
        self.blocks.add(mid)

        midleft = pygame.sprite.Sprite()
        midleft.image = pygame.image.load('images/level_4/midleft.png').convert()
        midleft.rect = midleft.image.get_rect(topright = (mid.rect.topleft))
        self.blocks.add(midleft)

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_4/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (mid.rect.bottomright))
        self.blocks.add(floor)

        rightfloor = pygame.sprite.Sprite()
        rightfloor.image = pygame.image.load('images/level_4/rightfloor.png').convert()
        rightfloor.rect = rightfloor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(rightfloor)

        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_4/right.png').convert()
        right.rect = right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(right)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_4/topright.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(topright)

    def level_5(self):
        """"Getting the layout of level 5"""
        self.clear_blocks() 

        leftfloor = pygame.sprite.Sprite()
        leftfloor.image = pygame.image.load('images/level_5/leftfloor.png').convert()
        leftfloor.rect = leftfloor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(leftfloor)

        midleft_1 = pygame.sprite.Sprite()
        midleft_1.image = pygame.image.load('images/level_5/midleft_1.png').convert()
        midleft_1.rect = midleft_1.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(midleft_1)

        midleft_2 = pygame.sprite.Sprite()
        midleft_2.image = pygame.image.load('images/level_5/midleft_2.png').convert()
        midleft_2.rect = midleft_2.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(midleft_2)

        midleft_3 = pygame.sprite.Sprite()
        midleft_3.image = pygame.image.load('images/level_5/midleft_3.png').convert()
        midleft_3.rect = midleft_3.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(midleft_3)

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_5/left.png').convert()
        left.rect = left.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left)

        topleft = pygame.sprite.Sprite()
        topleft.image = pygame.image.load('images/level_5/topleft.png').convert()
        topleft.rect = topleft.image.get_rect(topleft = (0, 0))
        self.blocks.add(topleft)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_5/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0,0))
        self.blocks.add(roof)

        topmid = pygame.sprite.Sprite()
        topmid.image = pygame.image.load('images/level_5/topmid.png').convert()
        topmid.rect = topmid.image.get_rect(topright = (1050, 0))
        self.blocks.add(topmid)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_4/topright.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(topright)

        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_5/right.png').convert()
        right.rect = right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(right)

        bottomright = pygame.sprite.Sprite()
        bottomright.image = pygame.image.load('images/level_5/bottomright.png').convert()
        bottomright.rect = bottomright.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottomright)

        bottom = pygame.sprite.Sprite()
        bottom.image = pygame.image.load('images/level_5/bottom.png').convert()
        bottom.rect = bottom.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom)

        floating = pygame.sprite.Sprite()
        floating.image = pygame.image.load('images/level_5/floating.png').convert()
        floating.rect = floating.image.get_rect(topright = (630, 504))
        self.blocks.add(floating)   

    def level_6(self):
        """"Getting the layout of level 6"""
        self.clear_blocks()

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_6/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)   

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_6/left.png').convert()
        left.rect = left.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_6/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0,0))
        self.blocks.add(roof)

        right_wall = pygame.sprite.Sprite()
        right_wall.image = pygame.image.load('images/level_6/right_wall.png').convert()
        right_wall.rect = right_wall.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rebound_blocks.add(right_wall)

        midright = pygame.sprite.Sprite()
        midright.image = pygame.image.load('images/level_6/midright.png').convert()
        midright.rect = midright.image.get_rect(bottomright = (right_wall.rect.topright))
        self.blocks.add(midright)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_6/topright.png').convert()
        topright.rect = topright.image.get_rect(bottomright = (midright.rect.topright))
        self.blocks.add(topright)

        float_left = pygame.sprite.Sprite()
        float_left.image = pygame.image.load('images/level_6/float_left.png').convert()
        float_left.rect = float_left.image.get_rect(bottomleft = (252, 546))
        self.blocks.add(float_left)

        mid = pygame.sprite.Sprite()
        mid.image = pygame.image.load('images/level_6/mid.png').convert()
        mid.rect = mid.image.get_rect(topleft = (float_left.rect.topright))
        self.blocks.add(mid)

        float_right = pygame.sprite.Sprite()
        float_right.image = pygame.image.load('images/level_6/float_right.png').convert()
        float_right.rect = float_right.image.get_rect(bottomleft = (mid.rect.bottomright))
        self.blocks.add(float_right)

    def level_7(self):
        """"Getting the layout of level 7"""
        self.clear_blocks()

        bottomleft = pygame.sprite.Sprite()
        bottomleft.image = pygame.image.load('images/level_7/bottomleft.png').convert()
        bottomleft.rect = bottomleft.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(bottomleft)

        left_rebound = pygame.sprite.Sprite()
        left_rebound.image = pygame.image.load('images/level_7/left_rebound.png').convert()
        left_rebound.rect = left_rebound.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(left_rebound)

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_7/left.png').convert()
        left.rect = left.image.get_rect(topleft = (0, 0))
        self.blocks.add(left)

        top_left = pygame.sprite.Sprite()
        top_left.image = pygame.image.load('images/level_7/top_left.png').convert()
        top_left.rect = top_left.image.get_rect(topleft = (0,0))
        self.blocks.add(top_left)

        top_rebound = pygame.sprite.Sprite()
        top_rebound.image = pygame.image.load('images/level_7/top_rebound.png').convert()
        top_rebound.rect = top_rebound.image.get_rect(topleft = (top_left.rect.topright))
        self.rebound_blocks.add(top_rebound)

        top_right = pygame.sprite.Sprite()
        top_right.image = pygame.image.load('images/level_7/top_right.png').convert()
        top_right.rect = top_right.image.get_rect(topright = (SCREEN_WIDTH,0))
        self.blocks.add(top_right)

        upper_right_wall = pygame.sprite.Sprite()
        upper_right_wall.image = pygame.image.load('images/level_7/upper_right_wall.png').convert()
        upper_right_wall.rect = upper_right_wall.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(upper_right_wall)

        floating_right = pygame.sprite.Sprite()
        floating_right.image = pygame.image.load('images/level_7/floating_right.png').convert()
        floating_right.rect = floating_right.image.get_rect(bottomright = (upper_right_wall.rect.bottomleft))
        self.blocks.add(floating_right)

        bottom_right = pygame.sprite.Sprite()
        bottom_right.image = pygame.image.load('images/level_7/bottom_right.png').convert()
        bottom_right.rect = bottom_right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right)

        bottom_right_floor = pygame.sprite.Sprite()
        bottom_right_floor.image = pygame.image.load('images/level_7/bottom_right_floor.png').convert()
        bottom_right_floor.rect = bottom_right_floor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right_floor)

        bottom_right_rebound = pygame.sprite.Sprite()
        bottom_right_rebound.image = pygame.image.load('images/level_7/bottom_right_rebound.png').convert()
        bottom_right_rebound.rect = bottom_right_rebound.image.get_rect(bottomright = (bottom_right_floor.rect.bottomleft))
        self.rebound_blocks.add(bottom_right_rebound)

        bottom_right_left_wall = pygame.sprite.Sprite()
        bottom_right_left_wall.image = pygame.image.load('images/level_7/bottom_right_left_wall.png').convert()
        bottom_right_left_wall.rect = bottom_right_left_wall.image.get_rect(bottomright = (bottom_right_rebound.rect.bottomleft))
        self.blocks.add(bottom_right_left_wall)

        rightside_top = pygame.sprite.Sprite()
        rightside_top.image = pygame.image.load('images/level_7/rightside_top.png').convert()
        rightside_top.rect = rightside_top.image.get_rect(bottomleft = (bottom_right_left_wall.rect.topleft))
        self.blocks.add(rightside_top)

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_7/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        lower_middle = pygame.sprite.Sprite()
        lower_middle.image = pygame.image.load('images/level_7/lower_middle.png').convert()
        lower_middle.rect = lower_middle.image.get_rect(bottomleft = (bottomleft.rect.bottomright))
        self.blocks.add(lower_middle)

        upper_middle = pygame.sprite.Sprite()
        upper_middle.image = pygame.image.load('images/level_7/upper_middle_rebound.png').convert()
        upper_middle.rect = upper_middle.image.get_rect(bottomleft = (lower_middle.rect.topleft))
        self.rebound_blocks.add(upper_middle)

    def level_8(self):
        """"Getting the layout of level 8"""
        self.clear_blocks()

        bottomleft = pygame.sprite.Sprite()
        bottomleft.image = pygame.image.load('images/level_8/bottom_left.png').convert()
        bottomleft.rect = bottomleft.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(bottomleft)

        left_wall = pygame.sprite.Sprite()
        left_wall.image = pygame.image.load('images/level_8/left_wall.png').convert()
        left_wall.rect = left_wall.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_wall)

        top_left = pygame.sprite.Sprite()
        top_left.image = pygame.image.load('images/level_8/top_left.png').convert()
        top_left.rect = top_left.image.get_rect(topleft = (0, 0))
        self.blocks.add(top_left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_8/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0, 0))
        self.blocks.add(roof)

        top_right = pygame.sprite.Sprite()
        top_right.image = pygame.image.load('images/level_8/top_right.png').convert()
        top_right.rect = top_right.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(top_right)

        right_wall = pygame.sprite.Sprite()
        right_wall.image = pygame.image.load('images/level_8/right_wall.png').convert()
        right_wall.rect = right_wall.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(right_wall)

        bottom_right = pygame.sprite.Sprite()
        bottom_right.image = pygame.image.load('images/level_8/bottom_right.png').convert()
        bottom_right.rect = bottom_right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right)

        bottom_right_floor = pygame.sprite.Sprite()
        bottom_right_floor.image = pygame.image.load('images/level_8/bottom_right_floor.png').convert()
        bottom_right_floor.rect = bottom_right_floor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right_floor)  

        low_floor = pygame.sprite.Sprite()
        low_floor.image = pygame.image.load('images/level_8/low_floor.png').convert()
        low_floor.rect = low_floor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(low_floor)

        middle_down = pygame.sprite.Sprite()
        middle_down.image = pygame.image.load('images/level_8/middle_down.png').convert()
        middle_down.rect = middle_down.image.get_rect(topleft = (top_right.rect.bottomleft))
        self.blocks.add(middle_down)  

        middle_left = pygame.sprite.Sprite()
        middle_left.image = pygame.image.load('images/level_8/middle_left.png').convert()
        middle_left.rect = middle_left.image.get_rect(bottomright = (middle_down.rect.bottomleft))
        self.blocks.add(middle_left) 
    
    def level_9(self):
        """"Getting the layout of level 9"""
        self.clear_blocks()

        bottomleft = pygame.sprite.Sprite()
        bottomleft.image = pygame.image.load('images/level_9/bottomleft.png').convert()
        bottomleft.rect = bottomleft.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(bottomleft)

        left_wall = pygame.sprite.Sprite()
        left_wall.image = pygame.image.load('images/level_9/left_wall.png').convert()
        left_wall.rect = left_wall.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_wall)

        left_roof = pygame.sprite.Sprite()
        left_roof.image = pygame.image.load('images/level_9/left_roof.png').convert()
        left_roof.rect = left_roof.image.get_rect(topleft = (0, 0))
        self.blocks.add(left_roof)

        middle_down = pygame.sprite.Sprite()
        middle_down.image = pygame.image.load('images/level_9/middle_down.png').convert()
        middle_down.rect = middle_down.image.get_rect(topright = (left_roof.rect.bottomright))
        self.blocks.add(middle_down)

        right_roof = pygame.sprite.Sprite()
        right_roof.image = pygame.image.load('images/level_9/right_roof.png').convert()
        right_roof.rect = right_roof.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(right_roof)

        right_wall = pygame.sprite.Sprite()
        right_wall.image = pygame.image.load('images/level_9/right_wall.png').convert()
        right_wall.rect = right_wall.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(right_wall)

        right_floor = pygame.sprite.Sprite()
        right_floor.image = pygame.image.load('images/level_9/right_floor.png').convert()
        right_floor.rect = right_floor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(right_floor)

        middle_floor = pygame.sprite.Sprite()
        middle_floor.image = pygame.image.load('images/level_9/middle_floor.png').convert()
        middle_floor.rect = middle_floor.image.get_rect(bottomright = (right_floor.rect.bottomleft))
        self.blocks.add(middle_floor)

        middle_rebound = pygame.sprite.Sprite()
        middle_rebound.image = pygame.image.load('images/level_9/middle_rebound.png').convert()
        middle_rebound.rect = middle_rebound.image.get_rect(bottomright = (672, 630))
        self.rebound_blocks.add(middle_rebound)

        middle_right = pygame.sprite.Sprite()
        middle_right.image = pygame.image.load('images/level_9/middle_right.png').convert()
        middle_right.rect = middle_right.image.get_rect(bottomleft = (middle_down.rect.bottomright))
        self.blocks.add(middle_right)     

    def level_10(self):
        """"Getting the layout of level 10"""
        self.clear_blocks()

        bottomleft = pygame.sprite.Sprite()
        bottomleft.image = pygame.image.load('images/level_10/bottomleft.png').convert()
        bottomleft.rect = bottomleft.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(bottomleft)

        spawn_block = pygame.sprite.Sprite()
        spawn_block.image = pygame.image.load('images/level_10/spawn_block.png').convert()
        spawn_block.rect = spawn_block.image.get_rect(bottomleft = (bottomleft.rect.bottomright))
        self.blocks.add(spawn_block)

        left_wall = pygame.sprite.Sprite()
        left_wall.image = pygame.image.load('images/level_10/left_wall.png').convert()
        left_wall.rect = left_wall.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_wall)

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_10/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_10/roof.png').convert()
        roof.rect = roof.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(roof)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_10/top_right.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(topright)

        bottom_right = pygame.sprite.Sprite()
        bottom_right.image = pygame.image.load('images/level_10/bottomright.png').convert()
        bottom_right.rect = bottom_right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right)

        topright_rebound = pygame.sprite.Sprite()
        topright_rebound.image = pygame.image.load('images/level_10/topright_rebound.png').convert()
        topright_rebound.rect = topright_rebound.image.get_rect(topright = (topright.rect.bottomright))
        self.rebound_blocks.add(topright_rebound)

        topright_not_rebound = pygame.sprite.Sprite()
        topright_not_rebound.image = pygame.image.load('images/level_10/topright_not_rebound.png').convert()
        topright_not_rebound.rect = topright_not_rebound.image.get_rect(topright = (topright_rebound.rect.bottomright))
        self.blocks.add(topright_not_rebound)

        right_rebound = pygame.sprite.Sprite()
        right_rebound.image = pygame.image.load('images/level_10/right_rebound.png').convert()
        right_rebound.rect = right_rebound.image.get_rect(topright = (topright_not_rebound.rect.bottomright))
        self.rebound_blocks.add(right_rebound)

        mainleft_rebound = pygame.sprite.Sprite()
        mainleft_rebound.image = pygame.image.load('images/level_10/mainleft_rebound.png').convert()
        mainleft_rebound.rect = mainleft_rebound.image.get_rect(topleft = (topright_rebound.rect.topleft))
        self.rebound_blocks.add(mainleft_rebound)

        mainbottom_rebound = pygame.sprite.Sprite()
        mainbottom_rebound.image = pygame.image.load('images/level_10/mainbottom_rebound.png').convert()
        mainbottom_rebound.rect = mainbottom_rebound.image.get_rect(bottomleft = (mainleft_rebound.rect.bottomleft))
        self.rebound_blocks.add(mainbottom_rebound)

        maintop = pygame.sprite.Sprite()
        maintop.image = pygame.image.load('images/level_10/maintop.png').convert()
        maintop.rect = maintop.image.get_rect(bottomright = (mainbottom_rebound.rect.topright))
        self.blocks.add(maintop)

        mainleft = pygame.sprite.Sprite()
        mainleft.image = pygame.image.load('images/level_10/mainleft.png').convert()
        mainleft.rect = mainleft.image.get_rect(bottomleft = (maintop.rect.topleft))
        self.blocks.add(mainleft)

        floating = pygame.sprite.Sprite()
        floating.image = pygame.image.load('images/level_10/floating.png').convert()
        floating.rect = floating.image.get_rect(bottomright = (420, 420))
        self.rebound_blocks.add(floating)

    def level_11(self):
        """"Getting the layout of level 11"""
        self.clear_blocks()

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_11/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        left_wall_rebound = pygame.sprite.Sprite()
        left_wall_rebound.image = pygame.image.load('images/level_11/left_wall_rebound.png').convert()
        left_wall_rebound.rect = left_wall_rebound.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(left_wall_rebound)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_11/roof.png').convert()
        roof.rect = roof.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.rebound_blocks.add(roof)

        right_wall_rebound = pygame.sprite.Sprite()
        right_wall_rebound.image = pygame.image.load('images/level_11/right_wall_rebound.png').convert()
        right_wall_rebound.rect = right_wall_rebound.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.rebound_blocks.add(right_wall_rebound)

        bottomright_rebound = pygame.sprite.Sprite()
        bottomright_rebound.image = pygame.image.load('images/level_11/bottomright_rebound.png').convert()
        bottomright_rebound.rect = bottomright_rebound.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rebound_blocks.add(bottomright_rebound)

        floating_right = pygame.sprite.Sprite()
        floating_right.image = pygame.image.load('images/level_11/floating_right.png').convert()
        floating_right.rect = floating_right.image.get_rect(bottomright = (1386, 713))
        self.rebound_blocks.add(floating_right)

        floating_middle = pygame.sprite.Sprite()
        floating_middle.image = pygame.image.load('images/level_11/floating_middle.png').convert()
        floating_middle.rect = floating_middle.image.get_rect(bottomright = (1092, 756))
        self.blocks.add(floating_middle)

        floating_left = pygame.sprite.Sprite()
        floating_left.image = pygame.image.load('images/level_11/floating_left.png').convert()
        floating_left.rect = floating_left.image.get_rect(bottomright = (floating_middle.rect.bottomleft))
        self.blocks.add(floating_left)
        

    def level_12(self):
        """"Getting the layout of level 12"""
        self.clear_blocks()

        left_floor = pygame.sprite.Sprite()
        left_floor.image = pygame.image.load('images/level_12/left_floor.png').convert()
        left_floor.rect = left_floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_floor)

        left_wall_rebound = pygame.sprite.Sprite()
        left_wall_rebound.image = pygame.image.load('images/level_12/left_wall_rebound.png').convert()
        left_wall_rebound.rect = left_wall_rebound.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(left_wall_rebound)

        left_floating_rebound = pygame.sprite.Sprite()
        left_floating_rebound.image = pygame.image.load('images/level_12/left_floating_rebound.png').convert()
        left_floating_rebound.rect = left_floating_rebound.image.get_rect(bottomright = (211, 337))
        self.rebound_blocks.add(left_floating_rebound)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_12/roof.png').convert()
        roof.rect = roof.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.rebound_blocks.add(roof)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_12/topright.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(topright)

        right_wall = pygame.sprite.Sprite()
        right_wall.image = pygame.image.load('images/level_12/right_wall.png').convert()
        right_wall.rect = right_wall.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(right_wall)

        bottom_right = pygame.sprite.Sprite()
        bottom_right.image = pygame.image.load('images/level_12/bottomright.png').convert()
        bottom_right.rect = bottom_right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right)

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_12/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        left_non_rebound = pygame.sprite.Sprite()
        left_non_rebound.image = pygame.image.load('images/level_12/left_non_rebound.png').convert()
        left_non_rebound.rect = left_non_rebound.image.get_rect(bottomleft = (left_floor.rect.bottomright))
        self.blocks.add(left_non_rebound)

        left_float = pygame.sprite.Sprite()
        left_float.image = pygame.image.load('images/level_12/left_float.png').convert()
        left_float.rect = left_float.image.get_rect(bottomright = (378, 546))
        self.blocks.add(left_float)

        left_rebound = pygame.sprite.Sprite()
        left_rebound.image = pygame.image.load('images/level_12/left_rebound.png').convert()
        left_rebound.rect = left_rebound.image.get_rect(topleft = (left_non_rebound.rect.topright))
        self.rebound_blocks.add(left_rebound)

        right_non_rebound = pygame.sprite.Sprite()
        right_non_rebound.image = pygame.image.load('images/level_12/right_non_rebound.png').convert()
        right_non_rebound.rect = right_non_rebound.image.get_rect(bottomright = (1092, 945))
        self.blocks.add(right_non_rebound)

        right_rebound = pygame.sprite.Sprite()
        right_rebound.image = pygame.image.load('images/level_12/right_rebound.png').convert()
        right_rebound.rect = right_rebound.image.get_rect(topleft = (right_non_rebound.rect.topright))
        self.rebound_blocks.add(right_rebound)
   
    def level_13(self):
        """"Getting the layout of level 13"""
        self.clear_blocks()

        left_floor = pygame.sprite.Sprite()
        left_floor.image = pygame.image.load('images/level_13/bottomleft_floor.png').convert()
        left_floor.rect = left_floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_floor)

        left_wall = pygame.sprite.Sprite()
        left_wall.image = pygame.image.load('images/level_13/left_wall.png').convert()
        left_wall.rect = left_wall.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left_wall)

        left_roof = pygame.sprite.Sprite()
        left_roof.image = pygame.image.load('images/level_13/left_roof.png').convert()
        left_roof.rect = left_roof.image.get_rect(topleft = (0, 0))
        self.blocks.add(left_roof)

        middle_roof = pygame.sprite.Sprite()
        middle_roof.image = pygame.image.load('images/level_13/middle_roof.png').convert()
        middle_roof.rect = middle_roof.image.get_rect(topleft = (0, 0))
        self.blocks.add(middle_roof)

        right_roof = pygame.sprite.Sprite()
        right_roof.image = pygame.image.load('images/level_13/right_roof.png').convert()
        right_roof.rect = right_roof.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.blocks.add(right_roof)

        right_wall = pygame.sprite.Sprite()
        right_wall.image = pygame.image.load('images/level_13/right_wall_rebound.png').convert()
        right_wall.rect = right_wall.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.rebound_blocks.add(right_wall)

        right_rebound = pygame.sprite.Sprite()
        right_rebound.image = pygame.image.load('images/level_13/right_rebound.png').convert()
        right_rebound.rect = right_rebound.image.get_rect(bottomright = (1596, 378))
        self.rebound_blocks.add(right_rebound)

        middle_platform = pygame.sprite.Sprite()
        middle_platform.image = pygame.image.load('images/level_13/middle_platform.png').convert()
        middle_platform.rect = middle_platform.image.get_rect(bottomright = (1596, 588))
        self.blocks.add(middle_platform)

        bottom_right = pygame.sprite.Sprite()
        bottom_right.image = pygame.image.load('images/level_13/bottomright.png').convert()
        bottom_right.rect = bottom_right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottom_right)

        bottomright_left = pygame.sprite.Sprite()
        bottomright_left.image = pygame.image.load('images/level_13/bottomright_left.png').convert()
        bottomright_left.rect = bottomright_left.image.get_rect(bottomright = (bottom_right.rect.bottomleft))
        self.blocks.add(bottomright_left)

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_13/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(floor)

        floor_left = pygame.sprite.Sprite()
        floor_left.image = pygame.image.load('images/level_13/floor_left.png').convert()
        floor_left.rect = floor_left.image.get_rect(bottomright = (715, 945))
        self.blocks.add(floor_left)

        left_rebound = pygame.sprite.Sprite()
        left_rebound.image = pygame.image.load('images/level_13/left_rebound.png').convert()
        left_rebound.rect = left_rebound.image.get_rect(bottomright = (floor_left.rect.bottomleft))
        self.rebound_blocks.add(left_rebound)

        left_non_rebound = pygame.sprite.Sprite()
        left_non_rebound.image = pygame.image.load('images/level_13/left_non_rebound.png').convert()
        left_non_rebound.rect = left_non_rebound.image.get_rect(bottomright = (left_rebound.rect.bottomleft))
        self.blocks.add(left_non_rebound)

        top_floating = pygame.sprite.Sprite()
        top_floating.image = pygame.image.load('images/level_13/top_floating.png').convert()
        top_floating.rect = top_floating.image.get_rect(bottomleft = (left_non_rebound.rect.topleft))
        self.blocks.add(top_floating)

    def level_14(self):
        """"Getting the layout of level 14"""
        self.clear_blocks()

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_14/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(floor)

        left_wall_rebound = pygame.sprite.Sprite()
        left_wall_rebound.image = pygame.image.load('images/level_14/left_wall_rebound.png').convert()
        left_wall_rebound.rect = left_wall_rebound.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(left_wall_rebound)

        topleft = pygame.sprite.Sprite()
        topleft.image = pygame.image.load('images/level_14/topleft.png').convert()
        topleft.rect = topleft.image.get_rect(topleft = (0, 0))
        self.rebound_blocks.add(topleft)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_14/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0, 0))
        self.rebound_blocks.add(roof)

        topright = pygame.sprite.Sprite()
        topright.image = pygame.image.load('images/level_14/topright.png').convert()
        topright.rect = topright.image.get_rect(topright = (SCREEN_WIDTH, 0))
        self.rebound_blocks.add(topright)

        midright = pygame.sprite.Sprite()
        midright.image = pygame.image.load('images/level_14/midright.png').convert()
        midright.rect = midright.image.get_rect(topright = (topright.rect.bottomright))
        self.blocks.add(midright)

        bottomright = pygame.sprite.Sprite()
        bottomright.image = pygame.image.load('images/level_14/bottomright.png').convert()
        bottomright.rect = bottomright.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.blocks.add(bottomright)

        left_mid = pygame.sprite.Sprite()
        left_mid.image = pygame.image.load('images/level_14/left_mid.png').convert()
        left_mid.rect = left_mid.image.get_rect(bottomright = (547, 945))
        self.blocks.add(left_mid)

        left_left = pygame.sprite.Sprite()
        left_left.image = pygame.image.load('images/level_14/left_left.png').convert()
        left_left.rect = left_left.image.get_rect(topright = (left_mid.rect.topleft))
        self.blocks.add(left_left)

        float_right = pygame.sprite.Sprite()
        float_right.image = pygame.image.load('images/level_14/float_right.png').convert()
        float_right.rect = float_right.image.get_rect(bottomright = (1386, 673))
        self.rebound_blocks.add(float_right)

        float_bottom = pygame.sprite.Sprite()
        float_bottom.image = pygame.image.load('images/level_14/float_bottom.png').convert()
        float_bottom.rect = float_bottom.image.get_rect(bottomright = (float_right.rect.bottomleft))
        self.rebound_blocks.add(float_bottom)

        float_middle = pygame.sprite.Sprite()
        float_middle.image = pygame.image.load('images/level_14/float_middle.png').convert()
        float_middle.rect = float_middle.image.get_rect(bottomleft = (float_bottom.rect.topleft))
        self.rebound_blocks.add(float_middle)

        float_upper = pygame.sprite.Sprite()
        float_upper.image = pygame.image.load('images/level_14/float_upper.png').convert()
        float_upper.rect = float_upper.image.get_rect(bottomleft = (float_middle.rect.topleft))
        self.rebound_blocks.add(float_upper)

        float_top = pygame.sprite.Sprite()
        float_top.image = pygame.image.load('images/level_14/float_top.png').convert()
        float_top.rect = float_top.image.get_rect(bottomright = (float_upper.rect.topright))
        self.rebound_blocks.add(float_top)

    def level_15(self):
        """"Getting the layout of level 15"""
        self.clear_blocks()

        floor = pygame.sprite.Sprite()
        floor.image = pygame.image.load('images/level_15/floor.png').convert()
        floor.rect = floor.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(floor)

        bottomleft_rebound = pygame.sprite.Sprite()
        bottomleft_rebound.image = pygame.image.load('images/level_15/bottomleft_rebound.png').convert()
        bottomleft_rebound.rect = bottomleft_rebound.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.rebound_blocks.add(bottomleft_rebound)

        midleft = pygame.sprite.Sprite()
        midleft.image = pygame.image.load('images/level_15/midleft.png').convert()
        midleft.rect = midleft.image.get_rect(bottomright = (336, 662))
        self.blocks.add(midleft)

        left_floating = pygame.sprite.Sprite()
        left_floating.image = pygame.image.load('images/level_15/left_floating.png').convert()
        left_floating.rect = left_floating.image.get_rect(bottomright = (midleft.rect.topright))
        self.blocks.add(left_floating)

        left = pygame.sprite.Sprite()
        left.image = pygame.image.load('images/level_15/left.png').convert()
        left.rect = left.image.get_rect(bottomleft = (0, SCREEN_HEIGHT))
        self.blocks.add(left)

        roof = pygame.sprite.Sprite()
        roof.image = pygame.image.load('images/level_15/roof.png').convert()
        roof.rect = roof.image.get_rect(topleft = (0, 0))
        self.blocks.add(roof)

        midfloat_topleft = pygame.sprite.Sprite()
        midfloat_topleft.image = pygame.image.load('images/level_15/midfloat_topleft.png').convert()
        midfloat_topleft.rect = midfloat_topleft.image.get_rect(bottomright = (547, 336))
        self.rebound_blocks.add(midfloat_topleft)

        midfloat_left = pygame.sprite.Sprite()
        midfloat_left.image = pygame.image.load('images/level_15/midfloat_left.png').convert()
        midfloat_left.rect = midfloat_left.image.get_rect(topleft = (midfloat_topleft.rect.bottomleft))
        self.rebound_blocks.add(midfloat_left)

        midfloat_right = pygame.sprite.Sprite()
        midfloat_right.image = pygame.image.load('images/level_15/midfloat_right.png').convert()
        midfloat_right.rect = midfloat_right.image.get_rect(bottomleft = (midfloat_left.rect.bottomright))
        self.rebound_blocks.add(midfloat_right)

        midfloat_floor = pygame.sprite.Sprite()
        midfloat_floor.image = pygame.image.load('images/level_15/midfloat_floor.png').convert()
        midfloat_floor.rect = midfloat_floor.image.get_rect(bottomleft = (midfloat_right.rect.bottomright))
        self.blocks.add(midfloat_floor)

        midfloat_bottomright = pygame.sprite.Sprite()
        midfloat_bottomright.image = pygame.image.load('images/level_15/midfloat_bottomright.png').convert()
        midfloat_bottomright.rect = midfloat_bottomright.image.get_rect(bottomleft = (midfloat_floor.rect.bottomright))
        self.blocks.add(midfloat_bottomright)

        midfloat_topright = pygame.sprite.Sprite()
        midfloat_topright.image = pygame.image.load('images/level_15/midfloat_topright.png').convert()
        midfloat_topright.rect = midfloat_topright.image.get_rect(bottomright = (midfloat_bottomright.rect.topright))
        self.blocks.add(midfloat_topright)

        bottomright = pygame.sprite.Sprite()
        bottomright.image = pygame.image.load('images/level_15/bottomright.png').convert()
        bottomright.rect = bottomright.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rebound_blocks.add(bottomright)

        right = pygame.sprite.Sprite()
        right.image = pygame.image.load('images/level_15/right.png').convert()
        right.rect = right.image.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rebound_blocks.add(right)

        upfloat_down_right = pygame.sprite.Sprite()
        upfloat_down_right.image = pygame.image.load('images/level_15/upfloat_down_right.png').convert()
        upfloat_down_right.rect = upfloat_down_right.image.get_rect(bottomright = (966, 252))
        self.blocks.add(upfloat_down_right)

        upfloat_down_left = pygame.sprite.Sprite()
        upfloat_down_left.image = pygame.image.load('images/level_15/upfloat_down_left.png').convert()
        upfloat_down_left.rect = upfloat_down_left.image.get_rect(bottomright = (upfloat_down_right.rect.bottomleft))
        self.rebound_blocks.add(upfloat_down_left)

        upfloat_middle = pygame.sprite.Sprite()
        upfloat_middle.image = pygame.image.load('images/level_15/upfloat_middle.png').convert()
        upfloat_middle.rect = upfloat_middle.image.get_rect(bottomright = (1260, 336))
        self.blocks.add(upfloat_middle)

        upfloat_left = pygame.sprite.Sprite()
        upfloat_left.image = pygame.image.load('images/level_15/upfloat_left.png').convert()
        upfloat_left.rect = upfloat_left.image.get_rect(topright = (upfloat_middle.rect.topleft))
        self.rebound_blocks.add(upfloat_left)
        
        upfloat_bottomright = pygame.sprite.Sprite()
        upfloat_bottomright.image = pygame.image.load('images/level_15/upfloat_bottomright.png').convert()
        upfloat_bottomright.rect = upfloat_bottomright.image.get_rect(bottomleft = (upfloat_left.rect.bottomright))
        self.blocks.add(upfloat_bottomright)
        
    def draw(self, screen):
        """Draw the blocks on the screen"""
        self.rebound_blocks.draw(screen)
        self.blocks.draw(screen)
       