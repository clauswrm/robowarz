from motors import Motors
from time import sleep
from sensobs.zumo_button import ZumoButton


class Motob:
    def __init__(self, motors=Motors()):
        self.motors = motors
        self.value = None  # A holder of the most recent motor recommendation sent to the motob.
        self.speed = 0.5

        self.execute_setting = {
            "stop": self.stop,
            "forward": self.forward,
            "adjust": self.adjust,
            "turn":self.turn_right

        }

    def update(self, recommendations):
        """ Receive a new motor recommendation, load it into the value slot, and operationalize it """

        if len(recommendations)==2:

            self.execute_setting[recommendations[0]](recommendations[1])
        else:
            self.execute_setting[recommendations[0]]()

    def turn_right(self, degrees):
        # TODO: regne på forhold mellom speed og dur
        # TODO: finne ut hvilken fart som gir mest presis styring
        # NOTE: Operasjonen varer i "amount" sekunder.

        # Denne formelen er basert på speed = 0.5:
        if degrees != None:
            dur = degrees / 100 * self.speed

        self.motors.right(speed=self.speed, dur=dur)

    def turn_left(self, degrees=None):
        # Denne formelen er basert på speed = 0.5. Left turning virker noe kjappere enn right turning.
        # Derav ko rtere turn duration
        if degrees != None:
            dur = degrees / 110 * self.speed
        self.motors.left(speed=self.speed, dur=dur)

    def forward(self, dur=None):
        self.motors.forward(speed=self.speed, dur=dur)

    def backward(self, dur=None):
        self.motors.backward(speed=self.speed, dur=dur)

    def stop(self):
        self.motors.stop()

    def make_adjustment(self,error):

        if error > 0.1:
            m.turn_right(error * 20)
        elif error < -0.1:
            m.turn_left(-error * 20)
        m.forward()

    def rightSquare(self, dist):
        for i in range(0, 4):
            self.forward(dist)
            sleep(0.25)
            self.turn_right(90)
            sleep(0.25)

    def leftSquare(self, dist):
        for i in range(0, 4):
            self.forward(dist)
            sleep(0.25)
            self.turn_left(90)
            sleep(0.25)

    def backAndForth(self, dist):
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
        m.turn_right(90)
