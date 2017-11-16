from basic_robot.sensobs.irproximity_sensor import IRProximitySensor
from basic_robot.sensobs.Sensob import Sensob
from basic_robot.sensobs.ultrasonic import Ultrasonic

class Proximity_Sensob(Sensob):

    def __init__(self, ir_sensor: IRProximitySensor):
        super().__init__(ir_sensor)
        self.ir_sensor = IRProximitySensor()

    def update(self):
        self.value = (self.ir_sensor.update() == [True, True])
        return self.value
