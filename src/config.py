from distutils.command import config
import src.colors as colors
import src.shapes as shapes
import math

COLORS = colors.COLORS

SHAPES = shapes.SHAPES

clock = False

game_over = False
game_result = " "*10

session_ID = 0.0

screen_height = 40
screen_width =  150

king_damage = 15
king_health = 100
king_movement_speed = 1
king_attack_range = 1

barbarian_damage = 10
barbarian_health = 100
barbarian_movement_speed = 1
barbarian_attack_range = 1

king_initial_x = math.floor(screen_width * 3/4)
king_initial_y = math.floor(screen_height * 1/4)

townhall_x = math.floor((screen_width - 3) / 2)
townhall_y = math.floor((screen_height - 4) / 2)

hut1_x = math.floor((screen_width - 1)*3 / 4) 
hut1_y = math.floor((screen_height - 1)*3 / 4)

hut2_x = math.floor((screen_width - 1)*3 / 4)
hut2_y = math.floor((screen_height - 1)*3 / 4) + 1

hut3_x = math.floor((screen_width - 1)*3 / 4)
hut3_y = math.floor((screen_height - 1)*3 / 4) + 2

hut4_x = math.floor((screen_width - 1)*3 / 4)
hut4_y = math.floor((screen_height - 1)*3 / 4) + 3

hut5_x = math.floor((screen_width - 1)*3 / 4) 
hut5_y = math.floor((screen_height - 1)*3 / 4) + 4

cannon1_x = math.floor((screen_width - 1)*1 / 4)
cannon1_y = math.floor((screen_height - 1)*1 / 4)
cannon1_damage = 10
cannon1_range = 40

cannon2_x = math.floor((screen_width - 1)*1 / 4)
cannon2_y = math.floor((screen_height - 1)*3 / 4)
cannon2_damage = 10
cannon2_range = 40

wall_d_x = math.floor((screen_width - 1)*1 / 4)
wall_d_y = math.floor((screen_height - 1)*3 / 4)

wall_c_x = math.floor((screen_width - 1)*3 / 4)
wall_c_y = math.floor((screen_height - 1)*3 / 4)

wall_b_x = math.floor((screen_width - 1)*3 / 4)
wall_b_y = math.floor((screen_height - 1)*1 / 4)

wall_a_x = math.floor((screen_width - 1)*1 / 4)
wall_a_y = math.floor((screen_height - 1)*1 / 4)

spawning_point = {
    'l' : [ math.floor((screen_width)*3 / 4),  math.floor((screen_height)*1 / 2)],
    'o' : [ math.floor((screen_width)*1 / 2),  math.floor((screen_height)*3 / 4)],
    'k' : [ math.floor((screen_width)*1 / 4),  math.floor((screen_height)*1 / 2)],
}


# FRAME REFRESHING
FPS = 20
FRAME_TIME = 1/FPS


