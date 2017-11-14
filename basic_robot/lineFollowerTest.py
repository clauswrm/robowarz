from actuation.Motob import Motob
from sensobs.reflectance_sensors import ReflectanceSensors
from sensobs.zumo_button import ZumoButton
from time import sleep, time
from math import sqrt

d = 100
m = Motob()
m.stop()


# TODO: Uten å bruke motorer, få den til å printe ut antall grader den vil svinge i hver retning ut i fra senorverdier

def calculate_error(sens_values):
    # returnerer en verdi som sier noe om hvor "feil" vi ligger på linja. En positiv verdi indikerer at vi er for langt
    # til høyre. En negativ verdi indikerer at vi er for langt til venstre.
    outValue = 0
    outValue += sens_values[0]
    outValue += 0.6 * sens_values[1]
    outValue -= 0.6 * sens_values[4]
    outValue -= sens_values[5]
    return outValue


def make_adjustment(error):

    if error > 0.1:
        m.turn_right(error * 20)
    elif error < -0.1:
        m.turn_left(-error * 20)
    m.forward()



def check_for_junction(sens_values):
    # TODO: Etabler en eller annen funksjon av sensorverdiene
    # denne kalibreringen fungerer trolig kun oppå bordene
    k = 1.4
    x = sum(sens_values)
    print(sens_values)
    print(x)
    if x < k:
        return True
    return False


sens = ReflectanceSensors()
value = []


while True:
    m.forward()
    running = True
    try:
        while running:

            sleep(0.02)
            value = sens.update()
            error = calculate_error(value)
            m.stop()
            if check_for_junction(value):
                m.turn_right(110)#bør nok oftest være 90 grader
                error = calculate_error(sens.update())
                m.stop()
                sleep(1)

            make_adjustment(error)
    except:
        m.stop()
