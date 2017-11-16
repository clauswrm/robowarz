from basic_robot.sensobs.irproximity_sensor import IRProximitySensor
from basic_robot.sensobs.ultrasonic import Ultrasonic

class Proximity_Sensob:

    def __init__(self, ir_sensor: IRProximitySensor):
        self.ir_sensor = IRProximitySensor()
        self.value = None

    def update(self):
        self.value = (self.ir_sensor.update() == [True, True])
        return self.value

    def get_value(self):
        return self.value