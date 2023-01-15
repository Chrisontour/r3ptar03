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
import random

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

def play_sound():
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)


def attack(speed):
    global blink_colour
    blink_colour = Color.RED
    _thread.start_new_thread(play_sound, ())
    pushMotor.brake()
    headMotor.run_time(speed,400,Stop.COAST)
    headMotor.run_time(-2*speed,1000)
    hide()
   
def slither(speed):
    global blink_colour
    blink_colour = Color.GREEN
    pushMotor.run(speed)
    slitherMotor.run_time(random.randint(-500,500),200)

def hide():
    global blink_colour
    blink_colour = Color.YELLOW
    slitherMotor.run(360)
    pushMotor.run(-800)
    wait(1500)
    slitherMotor.brake()
    pushMotor.brake()
    slitherMotor.run(-360)
    wait(1000)

def main_procedure():
    while True:
        while obstacleSensor.distance() > 40:
            slither(600)     
        attack(1000)

# start:
_thread.start_new_thread(blink, (55,))
wait(1500)
headMotor.run_time(-300,1000)
main_procedure()
