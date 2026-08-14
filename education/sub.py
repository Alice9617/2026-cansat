import logging
 #create logger
logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def sub_log_func():
    logger.info('サブファイルのロギング設定です')
    logging.error('サブファイルのロギング設定のエラーです')
    