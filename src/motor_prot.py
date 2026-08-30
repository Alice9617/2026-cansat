"""
oshirukko
"""
import RPi.GPIO as GPIO
import time

L_DIR = 5
R_DIR = 13

PWM_L = 12
PWM_R = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(L_DIR, GPIO.OUT)
GPIO.setup(R_DIR, GPIO.OUT)
GPIO.setup(PWM_L, GPIO.OUT)
GPIO.setup(PWM_R, GPIO.OUT)

pwm_l = GPIO.PWM(PWM_L, 1000)
pwm_r = GPIO.PWM(PWM_R, 1000)

pwm_l.start(0)
pwm_r.start(0)

def move(duty: int, direction: str) -> None:
 duty = int(duty)

 if direction == "forward":
     GPIO.output(L_DIR, 1)
     GPIO.output(R_DIR, 1)
     pwm_l.ChangeDutyCycle(duty)
     pwm_r.ChangeDutyCycle(duty)
 elif direction ==  "left":
     GPIO.output(L_DIR, 1)
     GPIO.output(R_DIR, 1)
     pwm_l.ChangeDutyCycle(duty * 0.3)
     pwm_r.ChangeDutyCycle(duty)
 elif direction == "right":
     GPIO.output(L_DIR, 1)
     GPIO.output(R_DIR, 1)
     pwm_l.ChangeDutyCycle(duty)
     pwm_r.ChangeDutyCycle(duty * 0.3)
 else:
     pwm_l.ChangeDutyCycle(0)
     pwm_r.ChangeDutyCycle(0)

if __name__ == "__main__":
    try:
        while True:
            duty, direction = input("duty,dir = ").split(",")
            move(duty, direction.strip())

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
