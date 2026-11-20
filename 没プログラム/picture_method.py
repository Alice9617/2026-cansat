import cv2
from datetime import datetime 
import os
from 没プログラム.Pmethod import Mask
imgpath=r"C:\Users\kuranosuke\Desktop\folders\Programs\physics\Cansat2026\img,data\IMG_2499.jpeg"
process=Mask(imgpath)
result=process.mask()
process.return_mask(result)
