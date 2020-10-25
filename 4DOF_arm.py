import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle, servo, freq):
    #calculate angle values to servo pwm values
    pwm=GPIO.PWM(servo, freq)
    pwm.start(0)
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    pwm.stop()

def move_arm(base, ac1, ac2, ac3):
    #take servo values and move arm
    rotate_base(base)
    rotate_ac1(ac1)
    rotate_ac2(ac2)
    rotate_ac3(ac3)
    
def rotate_base(angle):
    base = 22
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(base, GPIO.OUT)
    SetAngle(angle, base, 50)
    GPIO.cleanup()

def rotate_ac1(angle):
    ac1 = 24
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ac1, GPIO.OUT)
    SetAngle(angle, ac1, 50)
    GPIO.cleanup()
    
def rotate_ac2(angle):
    ac2 = 26
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ac2, GPIO.OUT)
    SetAngle(angle, ac2, 50)
    GPIO.cleanup()

def rotate_ac3(angle):
    ac3 = 32
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ac3, GPIO.OUT)
    SetAngle(angle, ac3, 50)
    GPIO.cleanup()

def current_position(base, ac1, ac2, ac3):
    #save the current position value of servo
    f = open("current_position.txt", "w")
    f.write("{}\n{}\n{}\n{}".format(base, ac1, ac2, ac3))
    f.close()

def last_position():
    #make sure that the servos are in the last position
    f = open("current_position.txt", "r")
    base = int(f.readline())
    ac1 = int(f.readline())
    ac2 = int(f.readline())
    ac3 = int(f.readline())
    move_arm(base, ac1, ac2, ac3)
     
#servo values    
arm_base = 50
arm_ac1 = 130
arm_ac2 = 90
arm_ac3 = 150

#read the last positions from txt file
#make sure the servos are at the last position
last_position()

#move the arm 
move_arm(arm_base, arm_ac1, arm_ac2, arm_ac3)

#write the current postion on txt file
current_position(arm_base, arm_ac1, arm_ac2, arm_ac3)







