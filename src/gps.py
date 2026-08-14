import RPi.GPIO as GPIO
import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    timeout=1)
while True:
    line = ser.readline().decode('utf-8', errors='ignore')
    if line:
        print(line.strip())

