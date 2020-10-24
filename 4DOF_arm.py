import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle, servo, freq):
    pwm=GPIO.PWM(servo, freq)
    pwm.start(0)
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    pwm.stop()
    GPIO.cleanup()
    
def rotate_base(angle):    
    SetAngle(angle, base, 50)

def rotate_ac1(angle):
    SetAngle(angle, ac1, 50)
    
def rotate_ac2(angle):
    SetAngle(angle, ac2, 50)

def rotate_ac3(angle):
    SetAngle(angle, ac3, 50)
    
base = 22
ac1 = 24
ac2 = 26
ac3 = 32


GPIO.setmode(GPIO.BOARD)
GPIO.setup(base, GPIO.OUT)
GPIO.setup(ac1, GPIO.OUT)
GPIO.setup(ac2, GPIO.OUT)
GPIO.setup(ac3, GPIO.OUT)

rotate_base(110)
#rotate_ac1(140)
#rotate_ac2(90)
#rotate_ac3(130)




