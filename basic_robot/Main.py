from camera import Camera
from PIL import Image
cam = Camera()

while True:
    img = Image.open("image.png")
    print(img.getPixel((100,100)))
    