from camera import Camera
from ultrasonic import Ultrasonic
from motors import Motors
from PIL import Image
from imager2 import Imager
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
