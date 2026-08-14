import RPi.GPIO as GPIO
import time
import subprocess
import main
import logging
parachute_HIGH=20
parachute_LOW=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(parachute_HIGH,GPIO.OUT)
GPIO.setup(parachute_LOW,GPIO.OUT)

def parachute(state):
    state=GPIO.input(20)
    while(state==GPIO.LOW or state==None):
        if state==GPIO.HIGH:
            time.sleep(15)
            while(True):
                subprocess.run("python3",main)
        elif state==GPIO.LOW:
            logging.info("restart process...")
        else:
            continue

import logging
logger=logging.getLogger(__name__)
logger.setlevel(logging.INFO)

def start_log_func():
    logging.info("camera logging settings error")
    logging.error("camera files settings error")
    



