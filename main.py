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

blink_colour = GREEN

# Write your program here.
def blink():
  global blink_colour
  while True:
    ev3.light.on(Color.blink_colour)
    wait(200)
    ev3.light.off()
    wait(200)

def attack():
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)
    headMotor.run_time(1000,800,Stop.COAST, wait=False)
    #ev3.light.on(Color.RED)
    global blink_colour
    blink_colour = RED
    headMotor.run_time(-1000,800,Stop.COAST,wait=False)
    wait(1000)
    hide()
    wait(1000)

def slither():
    #ev3.light.on(Color.YELLOW)
    global blink_colour
    blink_colour = GREEN
        # slither around
    pushMotor.run_time(1000,1000)

def hide():
    pushMotor.run_time(-800,2000, wait=False)

def main_procedure():
    while True:
    try:
        if obstacleSensor.distance() < 30:
            attack()
        # else
        slither()
    except:
        print "Error!"

# start:
headMotor.run_time(-300,1000)
_thread.start_new_thread(blink())
_thread.start_new_thread(main_procedure())
