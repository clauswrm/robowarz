class Sensob:
    def __init__(self, sensor):
        self.sensor = sensor
        self.value = None

    def update(self):
        self.sensor.update()

    def get_value(self):
        return self.value
