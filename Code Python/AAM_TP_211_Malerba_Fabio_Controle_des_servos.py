#!/usr/bin/python3
#   -*- coding: utf-8 -*-
# Date: Saturday 29 May 2021 09h02:01 CEST
# Author: Fabio Malerba
# Last updated by: Fabio Malerba
# Last updated time: Monday 31 May 2021 17:20:20 CEST
# Description: Solarium Scénario 1

'''Ce programme utilise les 2 servomoteurs
pour faire décrire un arc de cercle au panneau solaire.'''

import time
import board
import pwmio
from adafruit_motor import servo

# First servo (left to right)
# create a PWMOut object on Pin A1.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 1):  # 0 - 180 degrees, 1 degree at a time.
        my_servo.angle = angle
        time.sleep(0.5)
    for angle in range(180, 0, -1):  # 180 - 0 degrees, 1 degree at a time.
        my_servo.angle = angle
        time.sleep(0.5)

# Second servo (up to down)
# create a PWMOut object on Pin A4.
pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo2 = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 1):  # 0 - 180 degrees, 1 degree at a time.
        my_servo2.angle = angle
        time.sleep(0.5)
    for angle in range(180, 0, -1):  # 180 - 0 degrees, 1 degree at a time.
        my_servo2.angle = angle
        time.sleep(0.5)

