from motors import Motors
from time import sleep
from zumo_button import ZumoButton

class Motob:
    def __init__(self):
        self.m = Motors()
        self.speed = 0.5


    def turn_right(self,degrees):
        #TODO: regne på forhold mellom speed og dur
        #TODO: finne ut hvilken fart som gir mest presis styring
        #NOTE: Operasjonen varer i "amount" sekunder.

        #Denne formelen er basert på speed = 0.5:
        dur = degrees/100*self.speed

        self.m.right(speed = self.speed,dur=dur)

    def turn_left(self,degrees):
        #Denne formelen er basert på speed = 0.5. Left turning virker noe kjappere enn right turning.
        #Derav kortere turn duration
        dur = degrees/110*self.speed
        self.m.left(speed = self.speed,dur = dur)

    def forward(self,dur= None):
        self.m.forward(speed = self.speed,dur = dur)

    def backward(self,dur= None):
        self.m.backward(speed = self.speed,dur = dur)

    def stop(self):
        self.m.stop()

    def rightSquare(self,dist):
        for i in range(0,4):
            self.forward(dist)
            sleep(0.25)
            self.turn_right(90)
            sleep(0.25)
    def leftSquare(self,dist):
        for i in range(0,4):
            self.forward(dist)
            sleep(0.25)
            self.turn_left(90)
            sleep(0.25)


    def backAndForth(self,dist):
        self.forward(dist)
        sleep(0.25)
        self.turn_right(180)
        sleep(0.25)
        self.forward(dist)
        sleep(0.25)
        self.turn_left(180)
        sleep(0.25)


if __name__ == '__main__':

    m = Motob()
    while True:
        ZumoButton().wait_for_press()
        sleep(1)
        m.rightSquare(1)
        sleep(1)
        m.leftSquare(1)

