__author__ = 'torsten'

from basic_robot.ai.Behaviors import Behavior
from basic_robot.sensobs.Proximity_Sensob import Proximity_Sensob
from basic_robot.ai.BBCON import BBCON


class TakePicture(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, prox_sensob: Proximity_Sensob):
        super(bbcon, priority)
        self.prox_sensob = prox_sensob


    def consider_activation(self):
        #TODO: When Henrik finish develop sensob for reflectance, use sensob to check if end of tape and if IR sensors are detecting garage
        self.active_flag = True

    def consider_deactivation(self):
        if not self.prox_sensob.check_proximity_both_sides():
            self.active_flag = False


    def sense_and_act(self):
        if self.prox_sensob.get_distance_from_adjacent_object() < 15:
            self.motor_recommendations.append("stop")
            self.motor_recommendations.append("take and analyze picture")
            self.motor_recommendations.append("if picture is green, stop and finish")
            self.motor_recommendations.append("else, drive back and turn around")