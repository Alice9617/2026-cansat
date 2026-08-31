from camera import camera
from Pmethod import Mask
from picture_method import imgpath,process,result
from gps import get_position

def main():
    imge_file=camera()
    latitude,longitude=get_position()
    result=process(Mask(imgpath))

if __name__=="__main__":
    main()
