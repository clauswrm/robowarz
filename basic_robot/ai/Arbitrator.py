from basic_robot.ai.BBCON import BBCON
from basic_robot.ai.Behaviors import Behavior
from random import random


class Arbitrator:
    """
    Decides which behavior wins and thus gets its motor recommendations transferred
    to the BBCONs motobs.
    """

    def __init__(self, bbcon: BBCON, stochastic: bool = False):
        self.bbcon = bbcon
        self.stochastic = stochastic

    def choose_action(self) -> Behavior:
        """
        Chooses the behavior according to the 'stochastic'-flag: if False, the behavior
        with highest weight will simply be chosen. Else it will return the output from
        the stochastic_choose_action method.
        """
        if self.stochastic:
            return self.stochastic_choose_action()

        highest_weight, chosen_behavior = -1, None

        for active_behavior in self.bbcon.active_behaviors:
            if active_behavior.weight > highest_weight:
                chosen_behavior = active_behavior
                highest_weight = chosen_behavior.weight
        return chosen_behavior

    def stochastic_choose_action(self) -> Behavior:
        """
        Chooses the behavior stochasticly, with each behavior having a certain probability
        of being chosen, given by the formula:

        P(behavior) = (behavior_weight/sum_of_behavior_weights)
        """
        def generate_stoch_range(behaviors: list) -> list:
            """
            Helper method that takes a list of behaviors, and turns it into a list of
            values between 0 and 1 where the probability of behavior 'i' is defined as:

            P(behavior) = list[i] - list[i-1]
            """
            sum_weights = 0
            new_cummulative_weigths = [0 * len(behaviors)]
            for i, behavior in enumerate(behaviors):
                sum_weights += behavior
                new_cummulative_weigths = behavior.weight
                for j in range(i):
                    new_cummulative_weigths[i] += behavior
            for k in range(len(new_cummulative_weigths)):
                new_cummulative_weigths[k] /= sum_weights

            return new_cummulative_weigths

        stochastic_weights = generate_stoch_range(self.bbcon.active_behaviors)
        r = random()
        for i, weight in enumerate(stochastic_weights):
            if r < weight:
                return self.bbcon.active_behaviors[i]
