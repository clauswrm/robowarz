from basic_robot.ai.Behaviors import Behavior


class Turn_Around(Behavior):
    def __init__(self, bbcon, priority, camera):
        super().__init__(bbcon, priority)
        self.camera = camera
        self.motor_recommendations = ['turn']

    def consider_activation(self):
        if not self.bbcon.moving:
            self.active_flag = True

    def consider_deactivation(self):
        if self.bbcon.moving:
            self.active_flag = False

    def sense_and_act(self):
        self.match_degree = self.camera.match_degree()
