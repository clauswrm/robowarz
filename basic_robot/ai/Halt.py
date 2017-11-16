from basic_robot.ai.Behaviors import Behavior


class Halt(Behavior):
    def __init__(self, bbcon, priority, prox_sensob):
        super().__init__(bbcon, priority)
        self.prox_sensob = prox_sensob
        self.motor_recommendations = ['stop']

    def consider_activation(self):
        if self.bbcon.moving:
            self.active_flag = True
            self.bbcon.activate_behavior(self)

    def sense_and_act(self):
        self.match_degree = 1 if self.prox_sensob.get_value() else 0
