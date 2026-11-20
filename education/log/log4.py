#今回はログの司令塔であるhandler（c4-621ではない）の実装を行う
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#ファイルへの出力設定
handler=logging.FileHandler(
    "system.log",
    encoding="utf-8"
)

#表示形式の設定
formatter=logging.Formatter(
    '%(asctime)s-%(filename)s-[%(levelname)s]-%(message)s'
)

handler.setFormatter(formatter)

#LoggerにHandlerを登録
logger.addHandler(handler)

logger.info('Systems start')
logger.warning("GPS Signal Weak")
logger.error("Camera Error")