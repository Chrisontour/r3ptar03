#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Create your objects here.
ev3 = EV3Brick()
headMotor = Motor(Port.D)
slitherMotor = Motor(Port.A)
pushMotor = Motor(Port.B)
obstacleSensor = InfraredSensor(Port.S4)

# Write your program here.
headMotor.run_time(-300,1000)
while True:
    if obstacleSensor.distance() < 30:
        ev3.speaker.play_file(SoundFile.SNAKE_HISS)
        headMotor.run_time(1000,800,Stop.COAST)
        ev3.light.on(Color.RED)
        headMotor.run_time(-1000,800,Stop.COAST,wait=True)
        ev3.light.off()
        wait(1)
    # else
    ev3.light.on(Color.YELLOW)
    wait(1000)
    # drive backwards
    # change direction
    # slither around
