import reflectance_sensors
from time import sleep

sens = reflectance_sensors.ReflectanceSensors()

for i in range(10):
    print(sens.update())
    sleep(1)
