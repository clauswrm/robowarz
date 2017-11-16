from Behaviors import Behavior
from BBCON import BBCON
from reflectob import Reflectob()
class Adjust(Behavior):


    def __init__(self, bbcon: BBCON, priority: int):
        super(self,bbcon,priority)
        self.motor_recommendations['adjust',0]
        self.reflectob = Reflectob()


    def sense_and_act(self):
        self.error = self.reflectob.get_value()
        self.motor_recommendations[1]=self.error
        self.match_degree = abs(self.error)

