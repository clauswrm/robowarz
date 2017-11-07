from camera import Camera
from PIL import Image
from imager2 import Imager
import PIL
from time import sleep
cam = Camera()
while True:

	cam.update()

	print(cam.get_value().getpixel((50,50)))
	sleep(2)
