from BBCON import BBCON

from go_forward import Go_Forward
from Halt import Halt
from Turn_around import Turn_Around
from Adjust import Adjust
from Motob import Motob
from zumo_button import ZumoButton
from reflectob import Reflectob
from camob import Camob
from Proximity_Sensob import Proximity_Sensob
#from time import sleep



def main():
    """
    Creates a BBCON with motob.
    Initializes the behaviors with sensobs
    Adds the behaviors to the BBCON
    Runs the BBCON indefinetly
    """
    bbcon = BBCON(motob=Motob())
    reflectance = Reflectob()
    camera = Camob()
    proximity = Proximity_Sensob()

    bbcon.add_behavior(Go_Forward(bbcon=bbcon, priority=1))
    bbcon.add_behavior(Adjust(bbcon=bbcon, priority=2, reflectob=reflectance))
    bbcon.add_behavior(Halt(bbcon=bbcon, priority=3, prox_sensob=proximity))
    bbcon.add_behavior(Turn_Around(bbcon=bbcon, priority=4, camera=camera))

    ZumoButton().wait_for_press()
    sleep(2)
    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()
