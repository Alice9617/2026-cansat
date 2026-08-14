from picamera2 import Picamera2
import time
from datetime import datetime

cnt=0

def camera(width, height, cnt):
    picam2 = Picamera2()

    config = picam2.create_still_configuration(
        main={"size": (width, height)}
    )
    picam2.configure(config)
    picam2.start()
    time.sleep(1)
    return picam2
picam2=camera(640,480,0)
while True:
        a = input("Do you want to take a picture?(YES/NO): ").strip().upper()
        if a == "YES":
            cnt += 1
            filename = datetime.now().strftime("camera_%Y%m%d_%H%M%S_%f.png")
            picam2.capture_file(filename)
            print(f"{filename} captured")
        elif a == "NO":
            picam2.stop()
            picam2.close()
            print("camera closed")
            break
        else:
            print("Please type YES or NO")
