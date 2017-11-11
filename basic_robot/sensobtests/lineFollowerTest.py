from Motob import Motob
import reflectance_sensors
from zumo_button import ZumoButton
from time import sleep

d = 100
m = Motob()

#TODO: Uten å bruke motorer, få den til å printe ut antall grader den vil svinge i hver retning ut i fra senorverdier

def calculate_error(sens_values):
    outValue = 0
    outValue += sens_values[0]
    outValue += 0.6 * sens_values[1]
    outValue -= 0.6 * sens_values[3]
    outValue -= sens_values[4]
    return outValue


sens = reflectance_sensors.ReflectanceSensors()
value = []

while True:
    ZumoButton().wait_for_press()

    m.forward()

    running = True
    while running:
        value = sens.update()
        error = calculate_error(value)
        if -0.1 < error < 0.1:
            pass
        elif error > 0:
            m.turn_left(error * 20)
        else:
            m.turn_right(-error * 20)
        print(error)
    m.stop()


