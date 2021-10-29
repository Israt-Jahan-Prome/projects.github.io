"""PID_LFR controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

time_step = 32
max_speed = 4

#Motor
#For front wheels
right_motor_front = robot.getDevice('wheel_f_r')
right_motor_front.setPosition(float('inf'))
right_motor_front.setVelocity(0.0)

left_motor_front = robot.getDevice('wheel_f_l')
left_motor_front.setPosition(float('inf'))
left_motor_front.setVelocity(0.0)


#For back wheels
right_motor_back= robot.getDevice('wheel_b_r')
right_motor_back.setPosition(float('inf'))
right_motor_back.setVelocity(0.0)

left_motor_back = robot.getDevice('wheel_b_l')
left_motor_back.setPosition(float('inf'))
left_motor_back.setVelocity(0.0)


#Ir sensor
right_ir = robot.getDevice('ir_right')
right_ir.enable(time_step)
mid_ir = robot.getDevice('ir_mid')
mid_ir.enable(time_step)
left_ir = robot.getDevice('ir_left')
left_ir.enable(time_step) 

#PID
last_error = intg = diff = prop = waitCounter = 0
kp = 0.005
ki = 0
kd = 0.15

def pid(error):
 global last_error, intg, diff, prop, kp, ki, kd
 prop = error
 intg = error + intg
 diff = error - lasi_error
 balance = (kp*prop) + (ki*intg) + (kd*diff)
 last_error = error
 return balance

def setSpeed(base_speed, balance):
 wheels[0].setVelocity(base_speed + balance)
 wheels[1].setVelocity(base_speed - balance)
 wheels[2].setVelocity(base_speed + balance)
 wheels[3].setVelocity(base_speed - balance)



#simulation

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
   right_ir_val = right_ir.getValue()
   mid_ir_val = mid_ir.getValue()
   left_ir_val = left_ir.getValue()
  

   print("left: {} mid : {} right: {}" .format(left_ir_val,mid_ir_val,right_ir_val))

   left_speed_f =  max_speed   
   right_speed_f =  max_speed     
   left_speed_b =  max_speed   
   right_speed_b =  max_speed
   
  
# Process sensor data here.
   if left_ir_val<600 and right_ir_val<600 and mid_ir_val>=600:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val<600 and right_ir_val>=600 and mid_ir_val>=600:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(0)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(0)
    
   if left_ir_val>=600 and right_ir_val<600 and mid_ir_val>=600:
    left_motor_front.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(0)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val>=600 and right_ir_val<600 and mid_ir_val<600:
    left_motor_front.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(0)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val<600 and right_ir_val>=600 and mid_ir_val<600:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(0)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(0)
    
   if left_ir_val<600 and right_ir_val<600 and mid_ir_val<600:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(right_speed_b)

    if left_ir_val[4] != 1000:
     setSpeed(0, -3)
    
    else:
     error = (left_ir_val[5] - 100) 
     rectify = pid(error)
     setSpeed(5, rectify)
    
    if right_ir_val[4] != 1000:
     setSpeed(0, -3)
    
    else:
     error = (right_ir_val[5] - 100) 
     rectify = pid(error)
     setSpeed(5, rectify)
     
     if mid_ir_val[4] != 1000:
      setSpeed(0, -3)
    
     else:
      error = (mid_ir_val[5] - 100) 
      rectify = pid(error)
      setSpeed(5, rectify)

  # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
