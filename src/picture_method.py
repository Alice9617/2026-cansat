import cv2
from datetime import datetime 
import os
from Pmethod import Mask
imgpath=r"C:\Users\kuranosuke\Desktop\folders\Programs\physics\cansat2026\img,data\IMG_2499.jpeg"
process=Mask(imgpath)
result=process.mask()
process.return_mask(result)
