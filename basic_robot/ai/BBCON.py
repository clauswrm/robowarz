from basic_robot.ai import Arbitrator
from time import sleep

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator()

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """
        1) Updates all sensobs
        2) Updates all behaviors
        3) Invoke arbitrator
        4) Update motobs
        5) Wait
        6) Reset sensobs
        """

        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.update()
        self.arbitrator.choose_action()
        for motob in self.motobs:
            motob.update()
        sleep(0.2)
        for sensob in self.sensobs:
            sensob.reset()
