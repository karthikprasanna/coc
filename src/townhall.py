from src.building import Building
import src.config as config

class Townhall(Building):
    def __init__(self):
        super().__init__(config.townhall_x, config.townhall_y, 3, 4, 'townhall')