import serial
ser =serial.Serial(
    port='COM3',     #ポート番号(port)
    baudrate=9600,   #通信速度(baudrate)初期設定は9600
    timeout=1        #待ち時間(timeout) 基本的には1秒でok
)
while True:
    line = ser.readline().decode('utf-8', errors='ignore')
    if line:
        print(line.strip())