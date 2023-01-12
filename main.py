#!/usr/bin/env pybricks-micropython
# This program requires LEGO EV3 MicroPython v2.0 or higher.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import _thread

# Create your objects here.
ev3 = EV3Brick()
headMotor = Motor(Port.D)
slitherMotor = Motor(Port.A)
pushMotor = Motor(Port.B)
obstacleSensor = InfraredSensor(Port.S4)

blink_colour = Color.GREEN

# Write your program here.
def blink(duration):
  global blink_colour
  while True:
    ev3.light.on(blink_colour)
    wait(duration)
    ev3.light.off()
    wait(duration)

def attack(speed):
    global blink_colour
    blink_colour = Color.RED
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)
    headMotor.run_time(speed,800,Stop.COAST)
    headMotor.run_time(-speed,800,Stop.COAST)
    wait(1000)
    hide()
    wait(1000)

def slither(speed):
    global blink_colour
    blink_colour = Color.YELLOW
        # slither around
    pushMotor.run_time(speed,1000)

def hide():
    pushMotor.run_time(-800,2000, wait=False)

def main_procedure():
    while obstacleSensor.distance() < 30:
        attack(1000)
    slither(800)     # else

# start:
headMotor.run_time(-300,1000)
_thread.start_new_thread(blink, (200))
main_procedure()
