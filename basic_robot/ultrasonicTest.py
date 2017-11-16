from time import sleep

from camera import Camera
from motors import Motors
from sensobs.ultrasonic import Ultrasonic

cam = Camera()
ultra = Ultrasonic()
m = Motors()
m.stop()

while True:
    ultra.reset()
    ultra.update()
    print("Dist: " + str(ultra.get_value()))
    sleep(1)
