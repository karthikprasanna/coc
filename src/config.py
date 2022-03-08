import src.colors as colors
import src.shapes as shapes
import math

COLORS = colors.COLORS

SHAPES = shapes.SHAPES

screen_height = 40
screen_width =  150

king_damage = 0
king_health = 0
king_movement_speed = 0

barbarian_damage = 0
barbarian_health = 0
barbarian_movement_speed = 0

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
cannon1_damage = 0.5
cannon1_range = 6

cannon2_x = math.floor((screen_width - 1)*1 / 4)
cannon2_y = math.floor((screen_height - 1)*3 / 4)
cannon2_damage = 0.5
cannon2_range = 6

wall_d_x = math.floor((screen_width - 1)*1 / 4)
wall_d_y = math.floor((screen_height - 1)*3 / 4)

wall_c_x = math.floor((screen_width - 1)*3 / 4)
wall_c_y = math.floor((screen_height - 1)*3 / 4)

wall_b_x = math.floor((screen_width - 1)*3 / 4)
wall_b_y = math.floor((screen_height - 1)*1 / 4)

wall_a_x = math.floor((screen_width - 1)*1 / 4)
wall_a_y = math.floor((screen_height - 1)*1 / 4)

# FRAME REFRESHING
FPS = 20
FRAME_TIME = 1/FPS


