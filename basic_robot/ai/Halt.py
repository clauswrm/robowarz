from basic_robot.ai.Behaviors import Behavior
from basic_robot.sensobs.Proximity_Sensob import Proximity_Sensob
from basic_robot.ai.BBCON import BBCON


class Halt(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, prox_sensob: Proximity_Sensob):
        super().__init__(bbcon, priority)
        self.prox_sensob = prox_sensob

    def consider_activation(self):
        if self.bbcon.moving:
            self.active_flag = True

    def sense_and_act(self):
        if self.prox_sensob.get_value():
            pass
            # TODO: Calculate weight for when in a garage
