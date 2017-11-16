class Sensob:
    def __init__(self, sensor):
        self.sensor = sensor

    def update(self):
        self.sensor.update()