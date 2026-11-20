import logging

#loggerの取得
logger =logging.getLogger(__name__)

#ログの設定
#logging.basicConfig(level=logging.debug)
logging.basicConfig(level=logging.WARNING)

#ログの出力
logger.debug("DEBUG")
logger.info("INFO")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")

#上記のlogging.basicConfig内のlebelというものは、どのレベルまでのログを出力するかを決めれる

#上記の内容におけるログレベルの変更を行ってみよう。(level=logging.入れたいログレベル)で作成できる
#[#]を消して結果を確認するとよい。必ずどちらか片方をコメントアウトすること

