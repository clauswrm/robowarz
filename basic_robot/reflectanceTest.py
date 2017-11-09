import reflectance_sensors
from time import sleep
import Motob
sens = reflectance_sensors.ReflectanceSensors()
for i in range(10):
    print(sens.update())
    Motob.forward(0.2)
    sleep(1)