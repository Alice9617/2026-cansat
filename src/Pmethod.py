import cv2
from datetime import datetime
import os

class Mask:
    def __init__(self,imgpath):
        print(imgpath)
        self.imgpath=imgpath
        self.img=cv2.imread(imgpath)
        self.hsv=cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        if self.img is None:
            raise FileNotFoundError("Img cant recomended")

    def color_range(self):
        red1_low=(0,100,100)
        red1_high=(10,255,255)
        red2_low=(170,100,100)
        red2_high=(180,255,255)
        return red1_low,red1_high,red2_low,red2_high

    def mask(self):
        red1_low,red1_high,red2_low,red2_high=self.color_range()
        mask1= cv2.inRange(self.hsv,red1_low,red1_high)
        mask2=cv2.inRange(self.hsv,red2_low,red2_high)
        mask=cv2.bitwise_or(mask1,mask2)
        masked=cv2.bitwise_and(self.img,self.img,mask=mask)
        return masked

    def return_mask(self,masked):
        filepath=r"C:\Users\kuranosuke\Desktop\folders\Programs\physics\cansat2026\img,data"
        filename=datetime.now().strftime("results_%Y%m%d_%H%M%S_%f.jpg")
        savepath=os.path.join(filepath,filename)
        cv2.imwrite(savepath,masked)
