from camera import Camera
from imager2 import getpixel
from time import sleep


class camob:
    def __init__(self):
        self.c = Camera()

    def get_pixel(self, x, y):
        return self.c.image.getpixel((x, y))

    '''iterer over alle pixlene i listen og legger sammen verdiene, deler deretter på antall pixler'''
    ''' returnerer deretter gjenomsnittet av alle verdiene'''
    def get_avg_col(self):
        im = self.c.sensor_get_value

        return_list = [0, 0, 0]
        for i in range(self.c.img_height):
            for j in range(self.c.img_width):
                for k in range(0, 3):
                    return_list[k] += im.getpixel(j, i)[k]
        for l in range(0, 3):
            return_list[l] = return_list[l] // (self.c.img_height * self.c.img_width)
        return return_list

    def print_color_avg(self):
        '''printer ut gjennomsnittsfargen, brukes til å avgjøre div thresholds'''
        while True:
            print(self.get_avg_col())
            self.c.update
            sleep(1)



    def find_red_circle(self):
        '''Skal finne den røde sirkelen, skriver resten av koden etter jeg har testet noen numeriske verdier'''
        if True:
            pass
