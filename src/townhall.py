from src.object import Object
import src.config as config

class Townhall(Object):
    def __init__(self):
        super().__init__(config.townhall_x, config.townhall_y, 3, 4, 'townhall')