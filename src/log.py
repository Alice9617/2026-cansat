import logging

#ログの書式
FORMATTER='%(asctime)s-(%(filename)s)-[%(levelname)s]-%(message)s'

#ログの基本設定
logging.basicConfig(
    lebel=logging.DEBUG,
    format=FORMATTER,
    datefmt='%Y-%m-%d %H:%M%S'
)

#メインプログラムのロガー
logger=logging.getLogger(__name__)

#サブシステムのインポート
import camera 
import gps
import main
import motor_prot
import image
import start

def main_program():
    logger.info('System start')

    camera.camera_log_func()
    gps.gps_log_func()
    main.main_log_func()
    motor_prot.moter_log_func()
    image.opencv_log_func()
    start.start_log_func()

    logger.info('System End')

if __name__=='__main__':
    main_program()
    