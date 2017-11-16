from Behaviors import Behavior
from BBCON import BBCON


class Go_Forward(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, reflectance_sensob):
        super().__init__(bbcon, priority)

        self.match_degree = 1