_author_ = "Alex Bilat"
_date_ = "2025/01/16"
_version_ = "23.3"
_filename_ = "main.py"
_description_ = "Main executable to run the game"

from settings import *
from start_screen import *
from blocks import *    
from player import *
from axe import *
from fire import *
from chest import *
from spike import *
from bat import *
from stick import *
from settings import *
from ghost import *
from restart import *
from score import *
from username import *
from music import *
from sound_effects import *

#Initiate        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Choppy orc')
font = pygame.font.Font('font/font.ttf')
pygame.mixer.init()

#Classes
start_screen = Start_screen()
blocks = Blocks()
clock = pygame.time.Clock()
fire = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()
axe = pygame.sprite.GroupSingle()
chest = pygame.sprite.Group()
spike = pygame.sprite.Group()
bat = pygame.sprite.Group()
stick = pygame.sprite.GroupSingle()
ghost = pygame.sprite.Group()
restart = pygame.sprite.GroupSingle()
score = pygame.sprite.GroupSingle()
music = pygame.sprite.GroupSingle()
sound_effects = pygame.sprite.GroupSingle()
score.add(Score())
username = pygame.sprite.GroupSingle(Username())



#Fire positions:
spacing = 41
level_1_fire_x = 635
level_1_fire_y = 850
level_2_fire_x = 897 
level_2_fire_y = 694
level_3_fire_x = 610
level_3_fire_y = 606
level_4_fire_x = 570
level_4_fire_y = 858
level_5_fire_x = 568
level_5_fire_y = 858
level_6_fire_x = 1030
level_6_fire_y = 605
level_7_fire_x = 570
level_7_fire_y = 857
level_8_fire_x = 653
level_8_fire_y = 857
level_9_fire_x = 443
level_10_fire_x = 105
level_10_fire_y = 731
level_11_fire_x_1 = 360
level_11_fire_y_1 = 647
level_11_fire_x_2 = 700
level_11_fire_y_2 = 480
level_12_fire_x = 570
level_12_fire_y = level_8_fire_y
level_12_fire_x_2 = 1160
level_13_fire_x = 740
level_13_fire_y = 857
level_14_fire_x_1 = 280
level_14_fire_y_1 = 480
level_14_fire_x_2 = 1200
level_14_fire_y_2 = 395
level_15_fire_x_1 = 735
level_15_fire_x_2 = 985
level_15_fire_y = 227
level_fire_positions = {
    'start': [],
    'level_1': [(level_1_fire_x, level_1_fire_y), (level_1_fire_x + spacing, level_1_fire_y), (level_1_fire_x + (2 * spacing), level_1_fire_y), (level_1_fire_x + (3 * spacing), level_1_fire_y), (level_1_fire_x + (4 * spacing), level_1_fire_y)],
    'level_2': [(level_2_fire_x , level_2_fire_y), (level_2_fire_x  + spacing, level_2_fire_y), (level_2_fire_x  + (2 * spacing), level_2_fire_y), (level_2_fire_x  + (3 * spacing), level_2_fire_y), (level_2_fire_x  + (4 * spacing), level_2_fire_y)],
    'level_3': [(level_3_fire_x, level_3_fire_y), (level_3_fire_x + spacing, level_3_fire_y), (level_3_fire_x + (2 * spacing), level_3_fire_y), (level_3_fire_x + (3 * spacing), level_3_fire_y), (level_3_fire_x + (4 * spacing), level_3_fire_y), (level_3_fire_x + (5 * spacing), level_3_fire_y), (level_3_fire_x + (6 * spacing), level_3_fire_y)],
    'level_4': [(level_4_fire_x, level_4_fire_y), (level_4_fire_x + spacing, level_4_fire_y), (level_4_fire_x + (2 * spacing), level_4_fire_y), (level_4_fire_x + (3 * spacing), level_4_fire_y), (level_4_fire_x + (4 * spacing), level_4_fire_y), (level_4_fire_x + (5 * spacing), level_4_fire_y), (level_4_fire_x + (6 * spacing), level_4_fire_y), (level_4_fire_x + (7 * spacing), level_4_fire_y), (level_4_fire_x + (8 * spacing), level_4_fire_y), (level_4_fire_x + (9 * spacing), level_4_fire_y), (level_4_fire_x + (10 * spacing), level_4_fire_y)],
    'level_5': [(level_5_fire_x, level_4_fire_y), (level_5_fire_x + spacing, level_4_fire_y), (level_5_fire_x + (2 * spacing), level_4_fire_y), (level_5_fire_x + (3 * spacing), level_4_fire_y), (level_5_fire_x + (4 * spacing), level_4_fire_y), (level_5_fire_x + (5 * spacing), level_4_fire_y), (level_5_fire_x + (6 * spacing), level_4_fire_y), (level_5_fire_x + (7 * spacing), level_4_fire_y), (level_5_fire_x + (8 * spacing), level_4_fire_y), (level_5_fire_x + (9 * spacing), level_4_fire_y), (level_5_fire_x + (10 * spacing), level_4_fire_y), (level_5_fire_x + (11 * spacing), level_4_fire_y),
                 (1070, level_3_fire_y), (1070 + spacing, level_3_fire_y), (1070 + (2 * spacing), level_3_fire_y)],
    'level_6': [(level_6_fire_x, level_6_fire_y), (level_6_fire_x + spacing, level_6_fire_y)],
    'level_7': [(level_7_fire_x, level_7_fire_y), (level_7_fire_x + spacing, level_7_fire_y), (level_7_fire_x + (2 * spacing), level_7_fire_y), (level_7_fire_x + (3 * spacing), level_7_fire_y), (level_7_fire_x + (4 * spacing), level_7_fire_y), (level_7_fire_x + (5 * spacing), level_7_fire_y), (level_7_fire_x + (6 * spacing), level_7_fire_y), (level_7_fire_x + (7 * spacing), level_7_fire_y), (level_7_fire_x + (8 * spacing), level_7_fire_y), (level_7_fire_x + (9 * spacing), level_7_fire_y), (level_7_fire_x + (10 * spacing), level_7_fire_y)],
    'level_8': [(level_8_fire_x, level_8_fire_y), (level_8_fire_x + spacing, level_8_fire_y), (level_8_fire_x + (2 * spacing), level_8_fire_y), (level_8_fire_x + (3 * spacing), level_8_fire_y), (level_8_fire_x + (4 * spacing), level_8_fire_y)],
    'level_9': [(level_9_fire_x, level_8_fire_y), (level_9_fire_x + spacing, level_8_fire_y), (level_9_fire_x + (2 * spacing), level_8_fire_y), (level_9_fire_x + (3 * spacing), level_8_fire_y), (level_9_fire_x + (4 * spacing), level_8_fire_y)],
    'level_10': [(level_10_fire_x, level_10_fire_y), (level_10_fire_x + spacing, level_10_fire_y), (level_10_fire_x + (2 * spacing), level_10_fire_y), (level_10_fire_x + (3 * spacing), level_10_fire_y), (level_10_fire_x + (4 * spacing), level_10_fire_y)], 
    'level_11': [(level_11_fire_x_1, level_11_fire_y_1), (level_11_fire_x_1 + spacing, level_11_fire_y_1), (level_11_fire_x_1 + (2 * spacing), level_11_fire_y_1), (level_11_fire_x_1 + (3 * spacing), level_11_fire_y_1), (level_11_fire_x_1 + (4 * spacing), level_11_fire_y_1), (level_11_fire_x_1 + (5 * spacing), level_11_fire_y_1), (level_11_fire_x_1 + (6 * spacing), level_11_fire_y_1), (level_11_fire_x_1 + (7 * spacing), level_11_fire_y_1),
                 (level_11_fire_x_2, level_11_fire_y_2), (level_11_fire_x_2 + spacing, level_11_fire_y_2), (level_11_fire_x_2 + (2 * spacing), level_11_fire_y_2), (level_11_fire_x_2 + (3 * spacing), level_11_fire_y_2), (level_11_fire_x_2 + (4 * spacing), level_11_fire_y_2), (level_11_fire_x_2 + (5 * spacing), level_11_fire_y_2), (level_11_fire_x_2 + (6 * spacing), level_11_fire_y_2), (level_11_fire_x_2 + (7 * spacing), level_11_fire_y_2),
                 (360, 856), (360 + spacing, 856)],
    'level_12': [(level_12_fire_x, level_12_fire_y), (level_12_fire_x + spacing, level_12_fire_y), (level_12_fire_x + (2 * spacing), level_12_fire_y), (level_12_fire_x + (3 * spacing), level_12_fire_y), (level_12_fire_x + (4 * spacing), level_12_fire_y), (level_12_fire_x + (5 * spacing), level_12_fire_y), (level_12_fire_x + (6 * spacing), level_12_fire_y), (level_12_fire_x + (7 * spacing), level_12_fire_y), (level_12_fire_x + (8 * spacing), level_12_fire_y), (level_12_fire_x + (9 * spacing), level_12_fire_y), 
                 (level_12_fire_x_2, level_12_fire_y), (level_12_fire_x_2 + spacing, level_12_fire_y), (level_12_fire_x_2 + (2 * spacing), level_12_fire_y), (level_12_fire_x_2 + (3 * spacing), level_12_fire_y), (level_12_fire_x_2 + (4 * spacing), level_12_fire_y), (level_12_fire_x_2 + (5 * spacing), level_12_fire_y), (level_12_fire_x_2 + (6 * spacing), level_12_fire_y)],
    'level_13': [(level_13_fire_x, level_13_fire_y), (level_13_fire_x + spacing, level_13_fire_y), (level_13_fire_x + (2 * spacing), level_13_fire_y), (level_13_fire_x + (3 * spacing), level_13_fire_y), (level_13_fire_x + (4 * spacing), level_13_fire_y), (level_13_fire_x + (5 * spacing), level_13_fire_y), (level_13_fire_x + (6 * spacing), level_13_fire_y), (level_13_fire_x + (7 * spacing), level_13_fire_y)], 
    'level_14': [(level_14_fire_x_1, level_14_fire_y_1), (level_14_fire_x_1 + spacing, level_14_fire_y_1), (level_14_fire_x_1 + (2 * spacing), level_14_fire_y_1), (level_14_fire_x_1 + (3 * spacing), level_14_fire_y_1), (level_14_fire_x_1 + (4 * spacing), level_14_fire_y_1), (level_14_fire_x_1 + (5 * spacing), level_14_fire_y_1), (level_14_fire_x_1 + (6 * spacing), level_14_fire_y_1),
                (level_14_fire_x_2, level_14_fire_y_2), (level_14_fire_x_2 + spacing, level_14_fire_y_2), (level_14_fire_x_2 + (2 * spacing), level_14_fire_y_2), (level_14_fire_x_2 + (3 * spacing), level_14_fire_y_2), (level_14_fire_x_2 + (4 * spacing), level_14_fire_y_2),
                (690, 353), (690 + spacing, 353)],
    'level_15': [(level_15_fire_x_1, level_15_fire_y), (level_15_fire_x_1 + spacing, level_15_fire_y), (level_15_fire_x_1 + (2 * spacing), level_15_fire_y), (level_15_fire_x_1 + (3 * spacing), level_15_fire_y),
                (level_15_fire_x_2, level_15_fire_y), (level_15_fire_x_2 + spacing, level_15_fire_y), (level_15_fire_x_2 + (2 * spacing), level_15_fire_y), (level_15_fire_x_2 + (3 * spacing), level_15_fire_y)],
    'end': []
}

#Chest positions
level_chest_positions = {
    'start': [],
    'level_1': [(530, 415), (1350, 497)],
    'level_2': [(1350, 352)],
    'level_3': [(1450, 798)],
    'level_4': [(1450, 798), (435, 293)],
    'level_5': [(1450, 588)],
    'level_6': [(1450, 378), (380, 419)],
    'level_7': [(1400, 588), (1440, 797)],
    'level_8': [(1400, 503)],
    'level_9': [(570, 462), (1470, 545)],
    'level_10': [(1009, 545), (1427, 797)], 
    'level_11': [(500, 840)],
    'level_12': [(450, 335), (1500, 420)],
    'level_13': [(1520, 797)], 
    'level_14': [(870, 546)],
    'level_15': [(1000, 587)],
    'end': []
}

#Spike positions
level_4_spike_y = 125
level_5_spike_y = 168
level_5_spike_x = 720
level_6_spike_x = 260
level_6_spike_y = 546
level_9_spike_x = 850
level_9_spike_y = 125
level_7_x = 520
level_7_y = 126
level_13_spike_x_1 = 555
level_13_spike_y_1 = 85
level_13_spike_x_2 = 530
level_13_spike_y_2 = 589
level_14_spike_x_1 = 690
level_14_spike_y_1 = 126
level_14_spike_x_2 = 750
level_14_spike_y_2 = 673
level_spike_positions = {
    'start': [],
    'level_1': [],
    'level_2': [],
    'level_3': [],
    'level_4': [(340, 420), (300, 420), (600, level_4_spike_y), (600 + spacing, level_4_spike_y), (600 + (2 * spacing), level_4_spike_y), (600 + (3 * spacing), level_4_spike_y), (600 + (4 * spacing), level_4_spike_y), (600 + (5 * spacing), level_4_spike_y), (600 + (6 * spacing), level_4_spike_y), (600 + (7 * spacing), level_4_spike_y), (600 + (8 * spacing), level_4_spike_y)],
    'level_5': [(level_5_spike_x, level_5_spike_y), (level_5_spike_x + spacing, level_5_spike_y), (level_5_spike_x + (2 * spacing), level_5_spike_y), (level_5_spike_x + (3 * spacing), level_5_spike_y), (level_5_spike_x + (4 * spacing), level_5_spike_y), (level_5_spike_x + (5 * spacing), level_5_spike_y), (level_5_spike_x + (6 * spacing), level_5_spike_y), (level_5_spike_x + (7 * spacing), level_5_spike_y)],
    'level_6': [(level_6_spike_x, level_6_spike_y), (level_6_spike_x + spacing, level_6_spike_y), (level_6_spike_x + (2 * spacing), level_6_spike_y), (level_6_spike_x + (3 * spacing), level_6_spike_y)],
    'level_7': [(level_7_x, level_7_y),(level_7_x + spacing, level_7_y), (level_7_x + (2 * spacing), level_7_y) , (level_7_x + (3 * spacing), level_7_y), (level_7_x + (4 * spacing), level_7_y), (900, level_7_y), (900 + spacing, level_7_y)],
    'level_8': [],
    'level_9': [(level_9_spike_x, level_9_spike_y), (level_9_spike_x + spacing, level_9_spike_y), (level_9_spike_x + (2 * spacing), level_9_spike_y), (level_9_spike_x + (3 * spacing), level_9_spike_y), (level_9_spike_x + (4 * spacing), level_9_spike_y), (level_9_spike_x + (5 * spacing), level_9_spike_y), (level_9_spike_x + (6 * spacing), level_9_spike_y), (level_9_spike_x + (7 * spacing), level_9_spike_y), (level_9_spike_x + (8 * spacing), level_9_spike_y), (level_9_spike_x + (9 * spacing), level_9_spike_y), (level_9_spike_x + (10 * spacing), level_9_spike_y)],
    'level_10': [],
    'level_11': [],
    'level_12': [(303, 547), (303 + spacing, 547)],
    'level_13': [(level_13_spike_x_1, level_13_spike_y_1), (level_13_spike_x_1 + spacing, level_13_spike_y_1), (level_13_spike_x_1 + (2 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (3 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (4 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (5 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (6 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (7 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (8 * spacing), level_13_spike_y_1), (level_13_spike_x_1 + (9 * spacing), level_13_spike_y_1),
                 (level_13_spike_x_2, level_13_spike_y_2), (level_13_spike_x_2 + spacing, level_13_spike_y_2), (level_13_spike_x_2 + (2 * spacing), level_13_spike_y_2), (level_13_spike_x_2 + (3 * spacing), level_13_spike_y_2)], 
    'level_14': [(90, 203), (90 + spacing, 203),
                 (260, 589),(260 + spacing, 589),
                 (level_14_spike_x_1, level_14_spike_y_1), (level_14_spike_x_1 + spacing, level_14_spike_y_1), (level_14_spike_x_1 + (2 * spacing), level_14_spike_y_1), (level_14_spike_x_1 + (3 * spacing), level_14_spike_y_1),
                 (level_14_spike_x_2, level_14_spike_y_2), (level_14_spike_x_2 + spacing, level_14_spike_y_2), (level_14_spike_x_2 + (2 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (3 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (4 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (5 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (6 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (7 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (8 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (9 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (10 * spacing), level_14_spike_y_2), (level_14_spike_x_2 + (11 * spacing), level_14_spike_y_2), 
                 (1520, 589), (1520 + spacing, 589)],
    'level_15': [], 
    'end': []
}

#Bat positions
level_bat_positions = {
    'start': [],
    'level_1': [],
    'level_2': [],
    'level_3': [],
    'level_4': [],
    'level_5': [],
    'level_6': [(760, 400, 160, 160, 0.02), (900, 775, 100, 100, 0.02)],
    'level_7': [(560, 230, 50, 50, 0.03), (1200, 560, 50, 50, 0.03)],
    'level_8': [],
    'level_9': [(1300, 800, 150, 150, 0.02)],
    'level_10': [(1370, 370, 25, 25, 0.03), (1370, 550, 25, 25, 0.03)], 
    'level_11': [(780, 825, 200, 200, 0.02), (1405, 600, 15, 15, 0.03)],
    'level_12': [],
    'level_13': [(800, 450, 150, 150, 0.02), (1200, 650, 75, 75, 0.03)], 
    'level_14': [(1040, 450, 25, 25, 0.03), (1200, 800, 75, 75, 0.02)],
    'level_15': [(590, 300, 15, 15, 0.03)], 
    'end': []
}

#Ghost stick positions 
level_ghost_stick_positions = {
    'start': [],
    'level_1': [],
    'level_2': [],
    'level_3': [],
    'level_4': [],
    'level_5': [],
    'level_6': [],
    'level_7': [],
    'level_8': [(695, 370)],
    'level_9': [(861, 750)],
    'level_10': [(1406, 162)], 
    'level_11': [(1533, 160)],
    'level_12': [(147, 160)],
    'level_13': [(1535, 162)], 
    'level_14': [(945, 202)],
    'level_15': [(149, 162)], 
    'end': []
}

level_ghost_positions = {
    'start': [],
    'level_1': [],
    'level_2': [],
    'level_3': [],
    'level_4': [],
    'level_5': [],
    'level_6': [],
    'level_7': [],
    'level_8': [(500, 685, 25)],
    'level_9': [(640, 690, 25)],
    'level_10': [(450, 150, 20), (1300, 720, 25)], 
    'level_11': [(1150, 650, 25)],
    'level_12': [(580, 230, 25), (1150, 200, 25)],
    'level_13': [(1360, 300, 25), (460, 500, 25), (700, 670, 25)], 
    'level_14': [(610, 620, 25), (970, 483, 20)],
    'level_15': [(380, 700, 25), (800, 525, 18), (1300, 300, 25)], 
    'end': []

}

#Restart button positions
level_restart_positions = {
    'start': [],
    'level_1': [(1550, 50)],
    'level_2': [(1550, 50)],
    'level_3': [(1550, 50)],
    'level_4': [(1550, 50)],
    'level_5': [(1550, 50)],
    'level_6': [(1550, 50)],
    'level_7': [(1550, 50)],
    'level_8': [(1550, 50)],
    'level_9': [(1550, 50)],
    'level_10': [(1550, 50)], 
    'level_11': [(1550, 50)],
    'level_12': [(1550, 50)],
    'level_13': [(1550, 50)], 
    'level_14': [(1550, 50)],
    'level_15': [(1550, 50)], 
    'end': []
}

level_music_positions = {
    'start': [(750, 625)],
    'level_1': [(1375, 50)],
    'level_2': [(1375, 50)],
    'level_3': [(1375, 50)],
    'level_4': [(1375, 50)],
    'level_5': [(1375, 50)],
    'level_6': [(1375, 50)],
    'level_7': [(1375, 50)],
    'level_8': [(1375, 50)],
    'level_9': [(1375, 50)],
    'level_10': [(1375, 50)], 
    'level_11': [(1375, 50)],
    'level_12': [(1375, 50)],
    'level_13': [(1375, 50)], 
    'level_14': [(1375, 50)],
    'level_15': [(1375, 50)], 
    'end': []
}

level_sfx_positions = {
    'start': [(900, 625)],
    'level_1': [(1240, 50)],
    'level_2': [(1240, 50)],
    'level_3': [(1240, 50)],
    'level_4': [(1240, 50)],
    'level_5': [(1240, 50)],
    'level_6': [(1240, 50)],
    'level_7': [(1240, 50)],
    'level_8': [(1240, 50)],
    'level_9': [(1240, 50)],
    'level_10': [(1240, 50)], 
    'level_11': [(1240, 50)],
    'level_12': [(1240, 50)],
    'level_13': [(1240, 50)], 
    'level_14': [(1240, 50)],
    'level_15': [(1240, 50)], 
    'end': []
}

transitioning = False
def load_level(state):
    """
    Loads the level by initing each class and placing each game element (based on the dictionaries at the top of the code)
    This function:
    - Clears all the elements (fire, chest, spike, bat, stick, ghost)
    - Adds  elements based on the state (again, with the dictionaries at the top)
    - Inits the blocks for each level
    - Resets the player variables 
        - Also set the position of each player based on the level
    - Resets the axe's variables
    """
    
    fire.empty()
    chest.empty()
    spike.empty()
    bat.empty()
    stick.empty()
    ghost.empty()
    
    for pos in level_fire_positions[state]:
        fire.add(Fire(*pos))  #Give fire coords

    for pos in level_chest_positions[state]:
        chest.add(Chest(*pos, player_class, sound_effects))  #Give chest coords
    
    for pos in level_spike_positions[state]:
        spike.add(Spike(*pos))  #Give spike coords

    for pos in level_bat_positions[state]:
        bat.add(Bat(*pos, player_class, axe, sound_effects))  #Give bat coords + bat movement left/right
    
    for pos in level_ghost_stick_positions[state]: #Give ghost stick coords
        stick.add(Ghost_stick(*pos, axe))

    for pos in level_ghost_positions[state]: #Give ghost coords
        ghost.add(Ghost(*pos, player_class, stick, axe))
    
    for pos in level_restart_positions[state]: #Give restart button coords
        restart.add(Restart(*pos, player_class))
    
    for pos in level_music_positions[state]: #Give music buttons coords
        music.add(Music(*pos))
    
    for pos in level_sfx_positions[state]: #Give SFX button coords
        sound_effects.add(Sound_Effects(*pos))

    if state == 'start':
        player.sprite.alive = True
        player.sprite.frame_count = 0

    if state == 'level_1':
        score.sprite.start_counting()
        blocks.level_1()
    elif state == 'level_2':
        blocks.level_2()
    elif state == 'level_3':
        blocks.level_3()
    elif state == 'level_4':
        blocks.level_4()
    elif state == 'level_5':
        blocks.level_5()
    elif state == 'level_6':
        blocks.level_6()
    elif state == 'level_7':
        blocks.level_7()
    elif state == 'level_8':
        blocks.level_8()
    elif state == 'level_9':
        blocks.level_9()  
    elif state == 'level_10':
        blocks.level_10()
    elif state == 'level_11':
        blocks.level_11()
    elif state == 'level_12':
        blocks.level_12()
    elif state == 'level_13':
        blocks.level_13()  
    elif state == 'level_14':
        blocks.level_14()      
    elif state == 'level_15':
        blocks.level_15() 
   
    
    #Reset player position
    player.sprite.player_animation_index = 0
    player.sprite.alive = True
    player.sprite.frame_count = 0
    player.sprite.direction = 'right'
    player.sprite.death_timer = 0
    player.sprite.fading = False
    player.sprite.gravity = 2.5
    if state == 'level_5':
        player.sprite.rect.midbottom = (375, 840)
    elif state == 'level_3':
        player.sprite.rect.midbottom = (230, 833) 
    elif state == 'level_10':
        player.sprite.rect.midbottom = (400, 670) 
    elif state == 'level_11':
        player.sprite.rect.midbottom = (200, 880) 
    elif state == 'level_13':
        player.sprite.rect.midbottom = (200, 833)
    elif state == 'level_14':
        player.sprite.rect.midbottom = (200, 880)
    elif state == 'level_15':
        player.sprite.rect.midbottom = (500, 250)     
    else:
        player.sprite.rect.midbottom = (250, 840)

    axe.sprite.is_thrown = False
    axe.sprite.throw_direction = 'right'
    axe.sprite.on_wall = False
    axe.sprite.player_speed = 17
    axe.sprite.stuck = 'right'
    axe.sprite.block = None
    axe.sprite.y = None
    axe.sprite.has_moved = False
    axe.sprite.recalling = False
    axe.sprite.velocity_x = 0
    axe.sprite.velocity_y = 0
    axe.sprite.acceleration = 5
    axe.sprite.max_speed = 50

def transition(screen, new_state, duration = 60):
    """
    Does the transition between levels with a fade 
    """

    player.sprite.dx = 0
    player.sprite.moving = False

    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    fade_surface.fill((33, 38, 63))
    clock = pygame.time.Clock()

    #Fade out
    for alpha in range(0, 256, int(255 / duration)):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(120)

    global state
    state = new_state
    load_level(state)
    draw_level(state)
    
#Init player and axe
player_class = Player(fire, axe, chest, spike, bat, ghost, sound_effects)
axe_instance = Axe(player_class, stick, sound_effects)
player_class.axe = axe_instance

#Add player and axe to groups
player.add(player_class, fire)
axe.add(axe_instance)  

#Background
background_surf = pygame.image.load('images/background.png').convert()
background_surf = pygame.transform.scale(background_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_rect = background_surf.get_rect(topleft=(0, 0))

state = 'start'
level_1_completed = False
level_2_completed = False
level_3_completed = False
level_4_completed = False
level_5_completed = False
level_6_completed = False
level_7_completed = False
level_8_completed = False
level_9_completed = False
level_10_completed = False
level_11_completed = False
level_12_completed = False
level_13_completed = False
level_14_completed = False
level_15_completed = False

load_level(state)

def draw_level(state):
    """
    Draws the current level on the scree
    This function:
        - Fills the screen (background)
        - Draws all game elements (blocks, sound effects buttons, music buttons, score, restart button, 
          spikes, fire, bats, ghost stick, ghosts, chests, player, and axe)
        - Updates each class/game element
        - Checks if all chests are open to change the level
    """
    
    screen.fill('#2a2f42')
    blocks.draw(screen)

    #SFX buttons
    sound_effects.update(mouse_pos, events)
    sound_effects.draw(screen)

    #music buttons
    music.update(mouse_pos, events)
    music.draw(screen)

    #Score
    score.update()
    score.draw(screen)

    #Restart button
    restart.update(mouse_pos, events)
    restart.draw(screen)

    #Draw spike
    Spike.update_shared_animation()
    spike.update()
    spike.draw(screen)
    
    #Draw fire
    Fire.update_shared_animation()
    fire.update()
    fire.draw(screen)

    #Draw bat
    Bat.update_shared_animation()
    bat.update()
    bat.draw(screen)

    #Draw ghost stick
    stick.update()
    stick.draw(screen)

    #Draw ghost
    Ghost.update_shared_animation()
    ghost.update()
    ghost.draw(screen)

    #Draw chest
    chest.update()
    chest.draw(screen)
    if Chest.all_chests_open(chest):
        globals()[f"{state}_completed"] = True

    #Draw player
    fade_surface = player.sprite.update(blocks, screen, state)
    player.draw(screen)
    if fade_surface:
        screen.blit(fade_surface, (0, 0))

    #Draw axe
    axe.update(player.sprite.rect, player.sprite.direction, blocks, events)
    axe.draw(screen)

def end_screen(events): 
    """
    Generates the end screen +  elements (background, title image, score display, and username input).
    """  
    screen.blit(background_surf, (0, 0))

    start_surf = pygame.image.load('images/buttons/title.png').convert()
    start_surf = pygame.transform.scale(start_surf, (650, 100))
    start_rect = start_surf.get_rect(center=((SCREEN_WIDTH / 2), 150))
    screen.blit(start_surf, start_rect)

    score_number = score.sprite.score

    if not username.sprite.saved:
        score_number = score.sprite.stop_counting()
    score.update()
    score.draw(screen)

    new_state = username.sprite.handle_event(events, score_number)
    if new_state == 'start':
        global state
        state = new_state
        username.sprite.saved = False  
        username.sprite.text = ""      
        load_level('start')           
        return

    username.sprite.update()
    username.sprite.draw(screen)

    username.sprite.update()
    username.sprite.draw(screen)
           
while True:
    """Main coding loop"""
    mouse_pos = pygame.mouse.get_pos()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if state == 'start':
        state = start_screen.update(screen, mouse_pos, event)
        music.update(mouse_pos, events)
        music.draw(screen)
        sound_effects.update(mouse_pos, events)
        sound_effects.draw(screen)
        if state == 'level_1':
            transition(screen, 'level_1')

    if state == 'end':
        end_screen(events)

    if state in ['level_1', 'level_2', 'level_3', 'level_4', 'level_5', 'level_6', 'level_7', 'level_8', 'level_9', 'level_10','level_11', 'level_12', 'level_13', 'level_14', 'level_15']:
        draw_level(state)

    if level_1_completed:
        transition(screen, 'level_2')
        level_1_completed = False
    if level_2_completed:
        transition(screen, 'level_3')
        level_2_completed = False
    if level_3_completed:
        transition(screen, 'level_4')
        level_3_completed = False
    if level_4_completed:
        transition(screen, 'level_5')
        level_4_completed = False
    if level_5_completed:
        transition(screen, 'level_6')
        level_5_completed = False
    if level_6_completed:
        transition(screen, 'level_7')
        level_6_completed = False
    if level_7_completed:
        transition(screen, 'level_8')
        level_7_completed = False
    if level_8_completed:
        transition(screen, 'level_9')
        level_8_completed = False
    if level_9_completed:
        transition(screen, 'level_10')
        level_9_completed = False
    if level_10_completed:
        transition(screen, 'level_11')
        level_10_completed = False
    if level_11_completed:
        transition(screen, 'level_12')
        level_11_completed = False
    if level_12_completed:
        transition(screen, 'level_13')
        level_12_completed = False
    if level_13_completed:
        transition(screen, 'level_14')
        level_13_completed = False
    if level_14_completed:
        transition(screen, 'level_15')
        level_14_completed = False
    if level_15_completed:
        if state != 'end':  
            state = 'end'
            level_15_completed = False
            score.sprite.stop_counting() 
                                           
    pygame.display.update()
    clock.tick(60)
