#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
KopfMotor = Motor(Port.D)
SlitherMotor = Motor(Port.A)
SchubMotor = Motor(Port.B)
obstacleSensor = InfraredSensor(Port.S4)


# Write your program here.

KopfMotor.run_time(-300,1000)
while True:
    if obstacleSensor.distance() < 30:
        ev3.light.on(Color.RED)
        ev3.speaker.play_file(SoundFile.SNAKE_HISS)
        KopfMotor.run_time(1000,800,Stop.COAST)
        KopfMotor.run_time(-1000,800,Stop.COAST)
        ev3.light.off()
        wait(1)
    ev3.light.on(Color.YELLOW)
    wait(1000)
