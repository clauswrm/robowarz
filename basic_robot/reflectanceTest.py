import reflectance_sensors
from time import sleep
from Motob import Motob
from zumo_button import ZumoButton

sens = reflectance_sensors.ReflectanceSensors()
m = Motob()

def adjustLine(arr):

    if(arr[0] <0.1 or arr[1] < 0.1):
        m.turn_left(5)

    elif(arr[4]<0.1 or arr[5] <0.1):
        m.turn_right(5)
    m.forward
while True:
    ZumoButton().wait_for_press()
    m.forward()
    while True:
        arr = sens.update()
        adjustLine(arr)
        sleep(0.1)



