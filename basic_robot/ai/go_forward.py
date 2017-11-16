from basic_robot.ai.Behaviors import Behavior


class Go_Forward(Behavior):
    def __init__(self, bbcon, priority):
        super().__init__(bbcon, priority)

        self.match_degree = 1