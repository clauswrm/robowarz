from ai.BBCON import BBCON
from sensobs.Sensob import Sensob


class Behavior:
    """
    Default behavior that analyzes a subset of the BBCONs sensory information
    as a basis for determining a motor request.
    """

    def __init__(self, bbcon: BBCON, priority: int, *sensobs: Sensob):
        self.bbcon = bbcon
        self.sensobs = [sensob for sensob in sensobs]
        self.motor_recommendations = []
        self.active_flag = False
        self.halt_request = None
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    def consider_activation(self):
        """ If the behavior is deactivated, it tests whether it should deactivate. """
        pass

    def consider_deactivation(self):
        """ If the behavior is activated, it tests whether it should activate. """
        pass

    def sense_and_act(self):
        """ The core computations performed by the behavior that use sensob
        readings to produce motor recommendations( and halt requests). """
        pass

    def update(self):
        """
        1) Update the activity status
        2) Call sense_and_act
        3) Update behaviors weight
        """
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        self.sense_and_act()
        self.weight = self.priority * self.match_degree
