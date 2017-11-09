import reflectance_sensors
from time import sleep
import Motob

sens = reflectance_sensors.ReflectanceSensors()
motor = Motob.Motob()

for i in range(5):
    for j in range(10):
        print(sens.update())
        motor.forward(0.2)
        sleep(1)
    for k in range(10):
        print(sens.update())
        motor.backward(0.2)
        sleep(1)
    sleep(5)
