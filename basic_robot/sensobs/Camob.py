from basic_robot.sensobs.Camera import Camera
from basic_robot.sensobs.Sensob import Sensob
from time import sleep


class Camob(Sensob):
    """ High level class to interface with the Zumo robots camera """

    def __init__(self, bbcon):
        super().__init__(None)
        self.bbcon = bbcon
        self.c = Camera()
        self.c.update()

    def update(self):
        if not self.bbcon.moving:
            self.c.update()

    def take_pic(self):
        self.c.update().show()

    def get_pixel(self, x, y):
        return self.c.value.getpixel((x, y))

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
        print(return_list)
        return return_list

    def print_color_avg(self):
        '''printer ut gjennomsnittsfargen, brukes til å avgjøre div thresholds'''
        while True:
            print(self.get_avg_col())
            self.c.update()
            sleep(1)

    def match_degree(self):
        # dette er bare en lett idé, godt mulig dette vil kreve en mye mer kompleks algoritme
        # [101,50,30]
        # [
        if self.get_avg_col()[2] > 120:
            return 1
        return 0

    def match_degree_old(self):
        """Denne metoden skal kalkulerer til hvilken grad bildet observert passer med målet.
        Nøyaktig hvilket tall som blir brukt er svært tentativt."""
        # dette er bare en lett idé, godt mulig dette vil kreve en mye mer kompleks algoritme
        base_value = [50, 255, 50]
        # base_value = [255, 50, 50]
        if base_value[0] > 200 or base_value[2] > 200:
            return 0

        color_list = self.get_avg_col()
        a = color_list[0] / base_value[0]
        b = color_list[1] / base_value[1]
        c = color_list[2] / base_value[2]
        z = (a + b + c) / 3
        return z

        # her er z da 'match'-graden som en prosent, den ser bare på hvor mye rødt det er,
        # og bryr seg ikke om hva annet et som er i bildet, sort vil f.eks regnes som rødt.


if __name__ == '__main__':
    def main():
        cam = Camob(None)
        while True:
            print(cam.match_degree())
            cam.c.update()
            sleep(1)


    main()
