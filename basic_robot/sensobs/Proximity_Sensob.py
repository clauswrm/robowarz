from basic_robot.sensobs.Irproximity_sensor import IRProximitySensor
from basic_robot.sensobs.Sensob import Sensob

class Proximity_Sensob(Sensob):

    def __init__(self, ir_sensor: IRProximitySensor = IRProximitySensor()):
        super().__init__(ir_sensor)
        self.ir_sensor = ir_sensor

    def update(self):
        self.value = (self.ir_sensor.update() == [True, True])
        return self.value
