from basic_robot.ai.Behaviors import Behavior
from basic_robot.ai.BBCON import BBCON
from basic_robot.sensobs.reflectob import Reflectob


class Adjust(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, reflectob: Reflectob):
        super().__init__(bbcon, priority)
        self.motor_recommendations = ['adjust', 0]
        self.reflectob = reflectob

    def sense_and_act(self):
        self.error = self.reflectob.get_value()
        self.motor_recommendations[1] = self.error
        self.match_degree = abs(self.error)
