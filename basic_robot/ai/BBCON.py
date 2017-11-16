from basic_robot.ai.Arbitrator import Arbitrator
from time import sleep


class BBCON:
    """
    BBCON (Behavior-Based Controller)

    At each timestep, the robot should call its BBCON to determine its next move.
    Has controll over all behaviors, sensobs and motobs and updates them accordingly
    by running the run_one_timestep method.

    Should only require one instance (per robot).
    """

    def __init__(self, motob):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motob = motob
        self.arbitrator = Arbitrator(bbcon=self)
        self.moving = True

    def add_behavior(self, behavior):
        """ Append a newly-created behavior onto the behaviors list """
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        """ Append a newly-created sensob onto the sensobs list """
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        """ Add an existing behavior onto the active_behaviors list """
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        """ Remove an existing behavior from the active_behaviors list """
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """
        1) Updates all sensobs
        2) Updates all behaviors
        3) Invoke arbitrator
        4) Update motobs
        5) Wait
        """

        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.update()
        chosen_behavior = self.arbitrator.choose_action()
        print(chosen_behavior.motor_recommendations)

        if chosen_behavior.motor_recommendations[0] == 'stop':
            self.moving = False
        else:
            self.moving = True

        self.motob.update(chosen_behavior.motor_recommendations)
        #sleep(0.1)
