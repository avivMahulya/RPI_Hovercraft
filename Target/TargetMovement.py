
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

class MotorControl:
    MOTOR1_ESC=4  #Connect the ESC in this GPIO pin 
    max_value = 2000
    min_value = 700
    motor1_speed = 0
    pi = None
    def initialize_motors(self):
        motor1_speed = 0
        self.MOTOR1_ESC = 4
        self.pi = pigpio.pi(); #set the raspberry GPIO_CONF
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, 1500)  # reset the ESC


    def forward(self):
        self.motor1_speed += 100
        if self.motor1_speed > 2000:
            self.motor1_speed = 2000
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, self.motor1_speed)  # update motor1 speed
        print("Hover move forward")
        

    def backward(self):
        self.motor1_speed -= 100
        if self.motor1_speed < 900:
            self.motor1_speed = 900
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, self.motor1_speed)  # update motor1 speed
        print("Hover speed decrease")

    def left(self):
        print("Hover move left")

    def right(self):
        print("Hover move right")

    def stop(self):
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, 0)
        print("Hover stop")
        
    def arm(self): #This is the arming procedure of an ESC   
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, 0)
        time.sleep(1)
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, self.max_value)
        time.sleep(1)
        self.pi.set_servo_pulsewidth(self.MOTOR1_ESC, self.min_value)
        time.sleep(1)


