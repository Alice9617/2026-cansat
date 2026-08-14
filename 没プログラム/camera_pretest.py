from picamera2 import Picamera2,Preview
import time
from datetime import datetime
def camera(width:int,height:int,cnt:int):
    picam2=Picamera2()
    config=picam2.create_still_configuration(main={"size":(width,height)})
    picam2.configure(config) 
    picam2.start()
    time.sleep(2)
    filename= f"{cnt}_{datetime.now().strftime('%Y%m%d_%H%M%S%f')[:-4]}.jpg"
    picam2.capture_file(filename)
    picam2.stop()
    picam2.close()
    return filename
camera(640,480,1)
print(camera(640,480,1))
    
