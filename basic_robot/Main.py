from ai.BBCON import BBCON
from actuation.Motob import Motob
from sensobs.zumo_button import ZumoButton
from time import sleep

def main():
    """
    Creates a BBCON with motob.
    Initializes the behaviors with sensobs
    Adds the behaviors to the BBCON
    Runs the BBCON indefinetly
    """
    bbcon = BBCON(motob=Motob())
    bbcon.add_behavior()

    ZumoButton().wait_for_press()
    sleep(2)
    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()