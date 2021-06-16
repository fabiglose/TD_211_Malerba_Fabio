//!/usr/bin/C++
//   -*- coding: utf-8 -*-
// Date: Thuesday 1 June 2021 08h02:01 CEST
// Author: Fabio Malerba
// Last updated by: Fabio Malerba
// Last updated time: Thuesday 1 June 2021 8:20:10 CEST
// Description: Controle manuel des servomoteurs



/*
 Controlling a servo position using a potentiometer (variable resistor).
*/

#include <Servo.h>

Servo myservo;   // create servo object to control a servo
Servo myservo2;

int potpin = 4;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
int potpin2 = 5;
int valu;   
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(10);

}

void loop() {
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(15);                           // waits for the servo to get there
  valu = analogRead(potpin2);
  valu = map(valu, 0, 1023, 0, 180);
  myservo2.write(valu);
  delay(15); 
}
