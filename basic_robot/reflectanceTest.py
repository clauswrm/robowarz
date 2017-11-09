import reflectance_sensors
from time import sleep
from Motob import Motob
from zumo_button import ZumoButton

sens = reflectance_sensors.ReflectanceSensors()
m = Motob()

while True:
    ZumoButton().wait_for_press()

    m.forward()

    running = True
    while running:
        arr = sens.update()
        print(arr)
        for x in arr:
            if x < 0.1:
                running = False

    m.stop()


