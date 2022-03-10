from src.object import Object
import src.config as config

class Bottombar(Object):
    def __init__(self, progress, type):
        super().__init__(config.bottombar_x, config.bottombar_y, config.bottombar_h, config.bottombar_w, type)
        self._progress = progress

    def update_progress(self, new_progress, village = None):
        self._progress = new_progress
        self.change_type(self._type.split('_')[0] + str(self._progress), village)