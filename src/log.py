import camera
import gps
import main
import moter
import opencv
import start

import logging
logging.basicConfig(encoding='UTF-8',level=logging.INFO)

logging.critical('important error')
logging.error('error')
logging.warning('unpredictin error')
logging.info('carm')

FORMATTER='%(asctime)s - (%(filename)s) -[%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMATTER)
logging.basicConfig(level=logging.CRITICAL,format=FORMATTER)
logging.basicConfig(level=logging.ERROR,format=FORMATTER)
logging.basicConfig(level=logging.WARNING,format=FORMATTER)

logger=logging.getLogger(__name__)
logger.info('mains logger input(5levels)')
camera.camera_log_func()
gps.gps_log_func()
main.main_log_func()
moter.moter_log_func()
opencv.opencv_log_func()
start.start_log_func()