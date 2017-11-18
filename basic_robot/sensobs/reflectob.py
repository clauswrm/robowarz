from basic_robot.sensobs.Sensob import Sensob
from basic_robot.sensobs.Reflectance_sensors import ReflectanceSensors


class Reflectob(Sensob):
    def __init__(self, sensor=ReflectanceSensors()):
        super().__init__(sensor)
        self.error = 0

    def get_value(self):
        return self.error

    def update(self):
        val = self.sensor.update()

        self.error = self.calculate_error(val)

    @staticmethod
    def calculate_error(sens_values):
        outValue = 0
        outValue += sens_values[0]
        outValue += 0.6 * sens_values[1]
        outValue -= 0.6 * sens_values[4]
        outValue -= sens_values[5]
        return outValue
