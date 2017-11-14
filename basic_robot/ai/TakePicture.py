__author__ = 'torsten'

from basic_robot.ai.Behaviors import Behavior
from basic_robot.sensobs.irproximity_sensor import IRProximitySensor
from basic_robot.ai.BBCON import BBCON


class TakePicture(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, ir_sensob: IRProximitySensor):
        super(bbcon, priority)
        self.ir_sensob = ir_sensob


    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def sense_and_act(self):
        pass
