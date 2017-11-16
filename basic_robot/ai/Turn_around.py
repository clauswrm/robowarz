from basic_robot.ai.Behaviors import Behavior
from basic_robot.ai.BBCON import BBCON
from basic_robot.sensobs.camob import Camobs


class Turn_Around(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, camera: Camobs):
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
