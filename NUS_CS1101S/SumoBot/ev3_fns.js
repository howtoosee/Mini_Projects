// Source language The language for this mission is Source §3 (including the list, streams and arrays library), 
// plus the following functions from ev3. 
// You may use the listing below as reference when you are working on this mission:



//Motors:

ev3_motorA() //returns the motor connected to the port A.
ev3_motorB() //returns the motor connected to the port B.
ev3_motorC() //returns the motor connected to the port C.
ev3_motorD() //returns the motor connected to the port D.

ev3_runForDistance(motor, rotations, speed)
//causes the motor (which you get from the previous functions) to rotate at the specified speed for a specific number of rotations; if you pass a negative number of rotations, the motor will rotate backward. The speed is measured in tacho counts per second.

ev3_runForTime(motor, time, speed)
//causes the motor (which you get from the previous functions) to rotate at the specified speed for a specific duration (in milliseconds). The speed is measured in tacho counts per second.

ev3_stop(motor)
//cause the motor (which you get from the previous functions) to stop rotating.


// Note: ev3_runForDistance and ev3_runForTime work by sending instructions to the motors. 
// They will return almost immediately, without waiting for the motor to actually run for the specified time or distance. 
// If you wish to wait, use ev3_pause, documented below.



//Color sensor

ev3_colorSensor() 
//returns the connected color sensor.

ev3_colorSensorRed(colorSensor) 
//returns the red value read from the colorSensor which is a number within the range of 0 to 1020.

ev3_colorSensorGreen(colorSensor) 
//returns the green value read from the colorSensor which is a number within the range of 0 to 1020.

ev3_colorSensorBlue(colorSensor) 
//returns the blue value read from the colorSensor which is a number within the range of 0 to 1020.

ev3_reflectedLightIntensity(colorSensor) 
//return the percentage of the reflected light intensity.



//Touch sensor

ev3_touchSensor1() 
//returns the touch sensor connected to the port 1.

ev3_touchSensor2() 
//returns the touch sensor connected to the port 2.

ev3_touchSensorPressed(touchSensor) 
//returns a value based on the amount of pressure detected by the touch sensor.



//Ultrasonic sensor

ev3_ultrasonicSensor() 
//returns the connected ultrasonic sensor.

ev3_ultrasonicSensorDistance(ultrasonicSensor) 
//returns the distance between the sensor and an object in centimeters (cm).



//Gyro sensor

ev3_gyroSensor() 
//returns the connected gyro sensor.

ev3_gyroSensorRate(gyroSensor) 
//Returns the value of the gyro sensor.



//Miscellaneous

ev3_pause(time)
//Pauses the program for a specified amount of time in milliseconds.

ev3_runUntil(terminatingCondition, task) 
//repeatedly executes task() terminatingCondition() is satisfied; note that both of the two arguments are functions.