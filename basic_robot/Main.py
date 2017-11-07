from camera import Camera
from PIL import Image
from imager2 import Imager
import PIL


cam = Camera()

cam.update()

print(cam.get_value.getpixel((50,50)))
