class main:
    def __init__(self,main,log,gps,camera,moter,opencv,start):
        self.main=main
        self.log=log
        self.gps=gps
        self.camera=camera
        self.moter=moter
        self.cv=opencv
        self.start=start


import logging
logger=logging.getLogger(__name__)
logger.setlevel(logging.INFO)

def main_log_func():
    logging.info("camera logging settings error")
    logging.error("camera filese logging settings error")
    