from basic_robot.ai.Behaviors import Behavior


class Turn_Around(Behavior):
    def __init__(self, bbcon, priority, camera):
        super().__init__(bbcon, priority)
        self.camera = camera
        self.motor_recommendations = ['turn']
        self.active_flag = False

    def consider_activation(self):
        if not self.bbcon.moving:
            self.active_flag = True
            self.bbcon.activate_behavior(self)
            self.bbcon.add_sensob(self.camera)

    def consider_deactivation(self):
        if self.bbcon.moving:
            self.active_flag = False
            self.bbcon.deactivate_behavior(self)

    def sense_and_act(self):
        self.match_degree = self.camera.match_degree()
