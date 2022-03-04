from distutils.command import config
from object import Object
import config

class Townhall(Object):
    def __init__(self):
        super().__init__(config.townhall_x, config.townhall_y, 3, 4, 'townhall')