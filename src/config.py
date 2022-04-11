import src.colors as colors
import src.shapes as shapes
import math

COLORS = colors.COLORS

SHAPES = shapes.SHAPES

clock = False

level = 1

can_attack= False
can_defend = False

game_over = False
game_result = " "*10

session_ID = 0.0

screen_height = 40
screen_width =  150

debug_string = ""

king_damage = 15
king_health = 100
king_movement_speed = 1
king_attack_range = 1

queen_damage = 14
queen_health = 100
queen_movement_speed = king_movement_speed
queen_attack_range = 2
queen_attack_distance = 8

barbarian_damage = 10
barbarian_health = 100
barbarian_movement_speed = 1
barbarian_attack_range = 1

archer_damage = barbarian_damage // 2
archer_health = barbarian_health // 2
archer_movement_speed = barbarian_movement_speed * 2
archer_attack_range = 25

balloon_damage = barbarian_damage * 2
balloon_health = barbarian_health 
balloon_movement_speed = barbarian_movement_speed 
balloon_attack_range = 1

troop_max_health = 100

king_initial_x = math.floor(screen_width * 15/16)
king_initial_y = math.floor(screen_height * 1/16)

queen_initial_x = math.floor(screen_width * 15/16)
queen_initial_y = math.floor(screen_height * 1/16)

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
cannon1_range = 20

cannon2_x = math.floor((screen_width - 1)*1 / 4)
cannon2_y = math.floor((screen_height - 1)*3 / 4)
cannon2_damage = 10
cannon2_range = 20

cannon3_x = math.floor((screen_width - 1)*1 / 4) + 2
cannon3_y = math.floor((screen_height - 1)*1 / 4)
cannon3_damage = 10
cannon3_range = 20

cannon4_x = math.floor((screen_width - 1)*1 / 4) + 2
cannon4_y = math.floor((screen_height - 1)*3 / 4) 
cannon4_damage = 10
cannon4_range = 20

tower1_x = math.floor((screen_width - 1)*1 / 4)
tower1_y = math.floor((screen_height - 1)*2 / 4)
tower1_damage = cannon1_damage
tower1_range = cannon1_range

tower2_x = math.floor((screen_width - 1)*1 / 4)
tower2_y = math.floor((screen_height - 1)*2 / 4) + 1
tower2_damage = cannon2_damage
tower2_range = cannon2_range

tower3_x = math.floor((screen_width - 1)*3 / 4)
tower3_y = math.floor((screen_height - 1)*2 / 4) 
tower3_damage = cannon3_damage
tower3_range = cannon3_range

tower4_x = math.floor((screen_width - 1)*3 / 4)
tower4_y = math.floor((screen_height - 1)*2 / 4) + 1
tower4_damage = cannon4_damage
tower4_range = cannon4_range

wall_d_x = math.floor((screen_width - 1)*1 / 4)
wall_d_y = math.floor((screen_height - 1)*3 / 4)

wall_c_x = math.floor((screen_width - 1)*3 / 4)
wall_c_y = math.floor((screen_height - 1)*3 / 4)

wall_b_x = math.floor((screen_width - 1)*3 / 4)
wall_b_y = math.floor((screen_height - 1)*1 / 4)

wall_a_x = math.floor((screen_width - 1)*1 / 4)
wall_a_y = math.floor((screen_height - 1)*1 / 4)

spawning_point = {
    'l' : [ math.floor((screen_width)*7 / 8),  math.floor((screen_height)*1 / 2)],
    'o' : [ math.floor((screen_width)*1 / 2),  math.floor((screen_height)*3 / 4)],
    'k' : [ math.floor((screen_width)*1 / 4),  math.floor((screen_height)*1 / 2)],

    'g' : [ math.floor((screen_width)*7 / 8),  math.floor((screen_height)*1 / 2)],
    't' : [ math.floor((screen_width)*1 / 2),  math.floor((screen_height)*3 / 4)],
    'f' : [ math.floor((screen_width)*1 / 4),  math.floor((screen_height)*1 / 2)],

    'j' : [ math.floor((screen_width)*7 / 8),  math.floor((screen_height)*1 / 2)],
    'u' : [ math.floor((screen_width)*1 / 2),  math.floor((screen_height)*3 / 4)],
    'h' : [ math.floor((screen_width)*1 / 4),  math.floor((screen_height)*1 / 2)],
}

bottombar_x = screen_width // 8
bottombar_y = screen_height // 16

bottombar_h = 1
bottombar_w = 25

# FRAME REFRESHING
FPS = 20
FRAME_TIME = 1/FPS


