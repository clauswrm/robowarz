from basic_robot.ai.Behaviors import Behavior
from basic_robot.ai.BBCON import BBCON
from basic_robot.sensobs.camob import Camobs


class TurnAround(Behavior):
    def __init__(self, bbcon: BBCON, priority: int, camera: Camobs):
        super().__init__(bbcon, priority)
        self.camera = camera

    def consider_activation(self):
        if not self.bbcon.moving:
            self.active_flag = True

    def consider_deactivation(self):
        if self.bbcon.moving:
            self.active_flag = False

    def sense_and_act(self):
        if self.camera.match_degree():
            pass
            # TODO: Calculate weight for when in a garage and seeing red/green stuff
