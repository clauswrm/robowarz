__author__ = 'torsten'

from basic_robot.sensobs.irproximity_sensor import IRProximitySensor
from basic_robot.sensobs.ultrasonic import Ultrasonic

class Proximity_Sensob:

    def __init__(self, ir_sensor: IRProximitySensor, ultra_sensor: Ultrasonic):
        self.ir_sensor = IRProximitySensor()
        self.ultra_sensor = Ultrasonic()

    def update_sensors(self):
        self.ir_sensor.update()
        self.ultra_sensor.update()

    def check_proximity_both_sides(self):
        return self.ir_sensor.get_value() == [True, True]

    def get_distance_from_adjacent_object(self):
        return self.ultra_sensor.get_value()

