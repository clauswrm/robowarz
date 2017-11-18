from basic_robot.sensobs.Camera import Camera
from basic_robot.sensobs.Ultrasonic import Ultrasonic
from basic_robot.actuation.Motors import Motors
from time import sleep

if __name__ == '__main__':

    cam = Camera()
    ultra = Ultrasonic()
    m = Motors()
    m.stop()

    while True:
        ultra.reset()
        ultra.update()
        print("Dist: " + str(ultra.get_value()))
        sleep(1)
