from camera import Camera
from ultrasonic import Ultrasonic
from PIL import Image
from imager2 import Imager
import PIL
from time import sleep
cam = Camera()
ultra = Ultrasonic()
while True:

    print(ultra.sensor_get_value())
    sleep(1)
