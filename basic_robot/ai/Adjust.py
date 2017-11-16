from basic_robot.ai.Behaviors import Behavior


class Adjust(Behavior):
    def __init__(self, bbcon, priority, reflectob):
        super().__init__(bbcon, priority)
        self.motor_recommendations = ['adjust', 0]
        self.reflectob = reflectob
        self.error = 0

    def sense_and_act(self):
        self.error = self.reflectob.get_value()
        self.motor_recommendations[1] = self.error

        self.match_degree = 1 if (abs(self.error) > 0.1) else 0
