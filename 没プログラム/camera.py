from picamera2 import Picamera2 , Preview
import time
from datetime import datetime


#撮影用プログラム
def camera(width,height,cnt):
    picam2=Picamera2()
#解像度指定
    config=picam2.create_still_configuration(main={"size":(width,height)})
    picam2.configure(config)

#カメラ起動
    picam2.start()
    time.sleep(2)

#ファイル名作成
    filename= f"{cnt}_{datetime.now().strftime('%Y%m%d_%H%M%S%f')[:-4]}.jpg"

#ファイルをフォルダに保存
    picam2.capture_file(filename)

#カメラ停止
    picam2.close()

if __name__=="__main__":
    capture(1080,1920,1)          #高さ1080幅1920の解像度で撮影

import logging
logger=logging.getLogger(__name__)
logger.setlevel(logging.INFO)

def camera_log_func():
    logging.info("cameraファイルのロギング設定です")
    logging.error("cameraファイルのロギング設定のエラーです")
    