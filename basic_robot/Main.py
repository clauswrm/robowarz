from ai.BBCON import BBCON
from actuation.Motob import Motob
from actuation.motors import Motors
from sensobs.zumo_button import ZumoButton
from time import sleep

def main():
    bbcon = BBCON(motors=Motob())
    bbcon.add_behavior()

    ZumoButton().wait_for_press()
    sleep(2)
    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()