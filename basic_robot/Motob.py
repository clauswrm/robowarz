from motors import Motors
from time import sleep
from zumo_button import ZumoButton

class Motob:
    def __init__(self):
        self.m = Motors()
        self.speed = 0.5


    def turn_right(self,amount):
        #TODO: regne på forhold mellom speed og dur
        #TODO: finne ut hvilken fart som gir mest presis styring
        #NOTE: Operasjonen varer i "amount" sekunder.
        self.m.right(speed = self.speed,dur=amount)

    def turn_left(self,amount):
        self.m.left(speed = self.speed,dur = amount)

    def forward(self,dur):
        self.m.forward(speed = self.speed,dur = dur)

    def rightSquare(self,dist):
        for i in range(0,4):
            self.forward(dist)
            sleep(0.25)
            self.turn_right(0.4)
            sleep(0.25)





m = Motob()
while True:
    ZumoButton().wait_for_press()
    sleep(1)
    m.rightSquare(1)
