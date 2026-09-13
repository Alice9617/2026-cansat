import RPi.GPIO as GPIO
import time

right_pwm=14
left_pwm=15
gear_right=16
gear_left=17
GPIO.setmode(GPIO.BCM)
GPIO.setup([14,15,16,17],GPIO.OUT)
GPIO.setwarnings(False)

def pwm_setup(own):                      
    own.right = GPIO.PWM(own.right_pwm,)                   
    own.left = GPIO.PWM(own.left_pwm,)
    own.right.start(0)                                    
    own.left.start(0)

GPIO.cleanup([14,15,16,17])

def move(dir:str,own) -> None:
    GPIO.output(own.right_pwm,GPIO.LOW)
    GPIO.output(own.left_pwm,GPIO.LOW)
    if dir==("forward"):
        GPIO.output(gear_right,GPIO.HIGH)
        GPIO.output(gear_left,GPIO.HIGH)
        GPIO.PWM.ChangeDutyCycle(50)
    elif dir==("right"):
        GPIO.output(gear_right,GPIO.HIGH)
        GPIO.output(gear_left,GPIO.LOW)
        GPIO.PWM.ChangeDutyCycle(50)
    elif dir==("left"):
        GPIO.output(gear_right,GPIO.LOW)
        GPIO.output(gear_left,GPIO.HIGH)
        GPIO.PWM.ChangeDutyCycle(50)
    else:
        GPIO.output(gear_right,GPIO.LOW)
        GPIO.output(gear_left,GPIO.LOW)
        GPIO.PWM.ChangeDutyCycle(50)

