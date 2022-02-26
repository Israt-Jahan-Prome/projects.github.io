# projects.github.io

Arduino Based Automated Farming Sysyem:
In this project, there is a water tank to store water from a source (e.g. river) and a water pump to
supply water to the farm. Two sensors have been used here: an Ultrasonic Sensor to measure water level inside the water
tank and a Soil Moisture Sensor to measure the moisture content of soil. The
LCD displays the water level and moisture content in percentages taken from the sensors and the status of water tank and water pump either they are on or off. The project is
based on four main conditins:
 If the water inside the water tank is below 50% it means there is shortage of water and the water tank is turned on.
 If the water inside the water tank is above 50% it means there is enough amount of water inside the tank and the water tank is turned off.
 If the moisture content of soil is below 70% it means the soil is dry and the water pump is turned on.
 If the moisture content of soil is above 70% it means the soil is not dry and the water pump is turned off.
If the water level and moisture content is increased or decreased, the changes in status of water tank and water pump can be seen.

Equipments:
Arduino UNO R3, Ultrasonic Sensor (HC SR-04), Soil Moisture Sensor (Designed by
www.TheEngineeringProjects.com), 20x4 Alphanumeric LCD Display (LM044L), Diode,
Transistor, Battery, Capacitor, Inductor, Motor, Resistor, Variable Resistor or Potentiometer.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Object Recognition: 
A four wheeled robot build in Webots: robot simulator with a camera and two distance sensors in the front. The robot can detect objects in front of it with the help of camera and sensors and changes its path accordingly by taking turns. Some of the objects such as cylinder, cone, round shapes etc. are made from scratch.  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PID controlled line follower: 
A four wheeled robot build in Webots: robot simulator which follows a path or line. The line or track is designed in Autodesk Tinkercad and it has multiple turns. The robot has three Infrared sensors in its front which are used to detect the line on the floor. PID is also implemented to calculate the error that is how much the robot gets deviated from the line and it adjusts the position of the robot to bring it back on the track.
