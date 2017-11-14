from sensobs.camera import Camera
from sensobs.ultrasonic import Ultrasonic
from actuation.motors import Motors
from PIL import Image
import PIL
from time import sleep
cam = Camera()
ultra = Ultrasonic()
m = Motors()
m.stop()

while True:
    ultra.reset()
    ultra.update()
    print("Dist: " + str(ultra.get_value()))
    sleep(1)
