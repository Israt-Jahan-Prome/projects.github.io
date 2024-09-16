# projects.github.io

Arduino-Based Automated Farming System:
The system uses a water tank to store water from a source (e.g., a river) and a water pump to
supply the farm. Two sensors have been used here: an Ultrasonic Sensor to measure the water level inside the water
tank and a Soil Moisture Sensor to measure soil moisture content. The
LCD displays the water level and moisture content in percentages taken from the sensors and the status of the water tank and water pump, whether on or off. The system operates 
based on four main conditions:
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
A four-wheeled robot built in Webots: robot simulator with a camera and two distance sensors in the front. The robot can detect objects in front of it with the help of a camera and sensors and changes its path accordingly by taking turns. Some of the objects, such as cylinders, cones, round shapes, etc., are made from scratch.  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PID controlled line follower: 
A four-wheeled robot built in Webots: robot simulator which follows a path or line. The line or track is designed in Autodesk Tinkercad and has multiple turns. The robot has three infrared sensors at its front, which are used to detect the line on the floor. PID is also implemented to calculate the error, that is, how much the robot deviates from the line, and it adjusts the position of the robot to bring it back on the track.
