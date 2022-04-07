from src.person import Person
import src.config as config

class Queen(Person):
    def __init__(self):
        super().__init__(config.queen_initial_x, config.queen_initial_y, 1, 2, 'queen', config.queen_damage, config.queen_health, config.queen_movement_speed, config.queen_attack_range)
        self._attack_distance = config.queen_attack_distance
        self._facing_direction = 'w'