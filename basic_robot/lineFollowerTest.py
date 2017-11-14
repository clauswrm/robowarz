from actuation.Motob import Motob
from sensobs.reflectance_sensors import ReflectanceSensors
from sensobs.zumo_button import ZumoButton
from time import sleep,time
from math import sqrt

d = 100
m = Motob()
m.stop()
#TODO: Uten å bruke motorer, få den til å printe ut antall grader den vil svinge i hver retning ut i fra senorverdier

def calculate_error(sens_values):
    #returnerer en verdi som sier noe om hvor "feil" vi ligger på linja. En positiv verdi indikerer at vi er for langt
    #til høyre. En negativ verdi indikerer at vi er for langt til venstre.
    outValue = 0
    outValue += sens_values[0]
    outValue += 0.6 * sens_values[1]
    outValue -= 0.6 * sens_values[4]
    outValue -= sens_values[5]
    return outValue

def check_for_junction(sens_values):
    #TODO: Etabler en eller annen funksjon av sensorerdiene


sens = ReflectanceSensors()
value = []

while True:
    ZumoButton().wait_for_press()

    m.forward()

    running = True

    try:
        while running:
            x =
            value = sens.update()
            print("Value: "+str(value))
            error = calculate_error(value)
            print(str(time())+" : "+str(error))
            sleep(0.1)
            m.stop()
            if error > 0.5:
                m.turn_right(error*20)
                pass
            elif error <-0.05:
                m.turn_left(-error*20)
                pass
            m.forward()
    except:
        m.stop()


