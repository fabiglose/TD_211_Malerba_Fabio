#!/usr/bin/python3
#   -*- coding: utf-8 -*-
# Date: Monday 31 May 2021 11h12:01 CEST
# Author: Fabio Malerba
# Last updated by: Fabio Malerba
# Last updated time: Monday 31 May 2021 23:20:20 CEST
# Description: Solarium Scénario 2

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=2)
degré = 0

# On s'occupe du premier servo


def Position_initiale():
    """Il s'agit de mettre les deux servo en position initiale"""
# For the lateral servo
    # First servo (left to right)
    # create a PWMOut object on Pin A1.

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.

my_servo = servo.Servo(pwm)
kit.servo[1].angle = degré
time.sleep(0.5)

# For the horizontal servo
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo2 = servo.Servo(pwm)
kit.servo[1].angle = degré
time.sleep(0.5)

kit.servo[2].angle = degré
time.sleep(0.5)


def Rotation():
    """Apres avoir mis les servos en position initiale,
cette fonction va les faire tourner en arc de cercle"""

    for angle in range(0, 180):
        position = float(degré + 1)
# For the horizontal servo
        kit.servo[1].angle = position
        time.sleep(0.5)
# For the inclined servo
        kit.servo[2].angle = position
        time.sleep(0.5)

    if position == 180:
        for angle in range(0, 180):
            position = float(degré+ 1)

# For the horizontal servo
            kit.servo[1].angle = position
            time.sleep(0.5)
# For the inclined servo
            kit.servo[2].angle = position
            time.sleep(1)
    elif position != 180:

        # Si la position du servo ne correspond pas à celle du
        # capteur alors on fait revenir les servo à
        # leur position initiale
        kit.servo[1].angle = 0
        kit.servo[2].angle = 0
