from camera import Camera
# from imager2 import getpixel
from time import sleep
from PIL import Image


class Camob:
    def __init__(self):
        self.c = Camera()
        self.c.update()

    def take_pic(self):
        self.c.update.show()

    def get_pixel(self, x, y):
        return self.c.image.getpixel((x, y))

    '''iterer over alle pixlene i listen og legger sammen verdiene, deler deretter på antall pixler'''
    ''' returnerer deretter gjenomsnittet av alle verdiene'''

    def get_avg_col(self):
        img = self.c.value

        return_list = [0, 0, 0]
        for i in range(self.c.img_height):
            for j in range(self.c.img_width):
                for k in range(0, 3):
                    return_list[k] += img.getpixel((j, i))[k]
        for l in range(0, 3):
            return_list[l] = return_list[l] // (self.c.img_height * self.c.img_width)
        return return_list

    def print_color_avg(self):
        '''printer ut gjennomsnittsfargen, brukes til å avgjøre div thresholds'''
        while True:
            print(self.get_avg_col())
            self.c.update()
            sleep(1)

    def find_red_circle(self):
        '''Skal finne den røde sirkelen, skriver resten av koden etter jeg har testet noen numeriske verdier'''
        if True:
            pass

    def match_degree(self):
        '''Denne metoden skal kalkulerer til hvilken grad bildet observert passer med målet.
        Nøyaktig hvilket tall som blir brukt er svært tentativt.'''
        # dette er bare en lett idé, godt mulig dette vil kreve en mye mer kompleks algoritme
        base_value = [50, 255, 50]
        #base_value = [255, 50, 50]
        if base_value[0] > 200 or base_value[2] > 200:
            return 0

        color_list = self.get_avg_col()
        a = color_list[0] / base_value[0]
        b = color_list[1] / base_value[1]
        c = color_list[2] / base_value[2]
        z = (a + b + c) / 3
        print(z)
        return z

    def match_degree_basic(self):
        # dette er bare en lett idé, godt mulig dette vil kreve en mye mer kompleks algoritme
        base_value = 255
        color_list = self.get_avg_col()
        z = color_list[0] / base_value
        #her er z da 'match'-graden som en prosent, den ser bare på hvor mye rødt det er,
        #og bryr seg ikke om hva annet et som er i bildet, sort vil f.eks regnes som rødt.
        return z

# rød er f eks
# [222, 76, 30]
'''
im = Image.open('image.jpg'e).convert('RGB')
print(im.getpixel((1, 1)))

return_list = [0, 0, 0]
for i in range(0, 96):
    for j in range(0, 128):
        for k in range(0, 3):
            return_list[k] += im.getpixel((j, i))[k]
for l in range(0, 3):
    return_list[l] = return_list[l] // (96*128)
print(return_list)
'''


def main():
    cam = Camob()
    while True:
        print(cam.match_degree_basic())
        cam.c.update()
        sleep(1)


main()
