class Behavior:
    """
    Default behavior that analyzes a subset of the BBCONs sensory information
    as a basis for determining a motor request.
    """

    def __init__(self, bbcon, priority):
        self.bbcon = bbcon
        self.motor_recommendations = []
        self.active_flag = True
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
        readings to produce motor recommendations (and halt requests). """
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

        if self.active_flag:
            self.sense_and_act()
            self.weight = self.priority * self.match_degree

    def __str__(self):
        return self.__class__.__name__