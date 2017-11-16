from basic_robot.ai.BBCON import BBCON
from basic_robot.ai.go_forward import Go_Forward
from basic_robot.ai.Halt import Halt
from basic_robot.ai.Turn_around import Turn_Around
from basic_robot.ai.Adjust import Adjust
from basic_robot.actuation.Motob import Motob
from basic_robot.sensobs.zumo_button import ZumoButton
from basic_robot.sensobs.reflectob import Reflectob
from basic_robot.sensobs.camob import Camob
from basic_robot.sensobs.Proximity_Sensob import Proximity_Sensob
from time import sleep


def main():
    """
    Creates a BBCON with motob.
    Initializes the behaviors with sensobs
    Adds the behaviors to the BBCON
    Runs the BBCON indefinetly
    """
    bbcon = BBCON(motob=Motob())
    bbcon.motob.stop()

    reflectance = Reflectob()
    #camera = Camob()
    proximity = Proximity_Sensob()

    bbcon.add_sensob(reflectance)
    #bbcon.add_sensob(camera)
    bbcon.add_sensob(proximity)

    forward = Go_Forward(bbcon=bbcon, priority=1)
    adjust = Adjust(bbcon=bbcon, priority=2, reflectob=reflectance)
    halt = Halt(bbcon=bbcon, priority=3, prox_sensob=proximity)
    #turn = Turn_Around(bbcon=bbcon, priority=4, camera=camera)

    bbcon.add_behavior(forward)
    bbcon.add_behavior(adjust)
    bbcon.add_behavior(halt)
    #bbcon.add_behavior(turn)

    bbcon.activate_behavior(forward)
    bbcon.activate_behavior(adjust)
    bbcon.activate_behavior(halt)

    ZumoButton().wait_for_press()
    sleep(2)
    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()
