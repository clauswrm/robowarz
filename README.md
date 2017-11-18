# Robowarz
__Creating the best behavior-based robot for graph traversal__

## About
To learn _Behavior-Based Robotics_ (BBR), a simple but powerful,
general strategy for robot control, we built a robot that will
follow a graph lined on a flat surface until it finds its goal.

The robot consists mainly of a Raspberry Pi 2 and a Zumo chassis.
The behavior is based on input form sensors such as camera,
reflectance, ultrasound and proximity sensors.

This was an assignment for the subject _TDT4113 CS Programming
Project_ at Norwegian University of Science and Technology
([NTNU]).

## Implementation
The robot consistes of four different behaviors:

* `Go_forward`
* `Ajust`
* `Stop`
* `Turn_around`

The weight of each behavior depends on output from the sensors
described in the paragraph above. One behavior then gets its motor
recommendation sendt forward to the motors based on the arbitrators
decision.

This happend each time the `BBCON.run_one_timestep()` is excecuted,
wich is **10 times/sec** in our case.

![A typical example of behavior-based robotic control][bbrc]
_A similar BBR model we based our work on._

[NTNU]: https://www.ntnu.edu/ "NTNU homepage"
[bbrc]: https://raw.githubusercontent.com/clauswrm/robowarz/master/bbr.png
"A typical example of behavior-based robotic control"
