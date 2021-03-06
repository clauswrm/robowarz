from basic_robot.actuation.Motors import Motors
from time import sleep
from basic_robot.sensobs.Zumo_button import ZumoButton


class Motob:
    """
    Connects the high level instructions with the lower level
    motors-class that actually makes the Zumo-robot drive.
    """
    def __init__(self, motors=Motors()):
        self.motors = motors
        self.value = None  # A holder of the most recent motor recommendation sent to the motob.
        self.speed = 0.5

        self.execute_setting = {
            "stop": self.stop,
            "forward": self.forward,
            "adjust": self.adjust,
            "turn": self.turn_around
        }

    def update(self, recommendations):
        """ Receive a new motor recommendation, load it into the value slot, and operationalize it """

        if len(recommendations) == 2:

            self.execute_setting[recommendations[0]](recommendations[1])
        else:
            self.execute_setting[recommendations[0]]()

    def turn_right(self, degrees):
        # Denne formelen er basert på speed = 0.5:
        dur = degrees / 100 * self.speed

        self.motors.right(speed=self.speed, dur=dur)

    def turn_left(self, degrees=None):
        # Denne formelen er basert på speed = 0.5. Left turning virker noe kjappere enn right turning.
        # Derav kortere turn duration
        dur = degrees / 110 * self.speed
        self.motors.left(speed=self.speed, dur=dur)

    def turn_around(self):
        self.backward(0.6)
        self.turn_right(270)

    def forward(self, dur=None):
        self.motors.forward(speed=self.speed, dur=dur)

    def backward(self, dur=None):
        self.motors.backward(speed=self.speed, dur=dur)

    def stop(self):
        self.motors.stop()

    def adjust(self, error):
        if error > 0.1:
            self.turn_right(error * 35)
        elif error < -0.1:
            self.turn_left(-error * 35)

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
