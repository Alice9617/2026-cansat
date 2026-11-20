import os
os.makedirs("log",exist_ok=True)

#1:基本的なログの出力
import logging
logging.basicConfig(encoding='utf-8',level=logging.INFO)

logging.critical('crit')
logging.error('error')
logging.warning('warn')
logging.info(f"info:{'tutorial'}")
logging.debug('debug')
#出力結果
#CRITICAL:root:crit
#ERROR:root:error
#WARNING:root:warn
#INFO:root:tutorial

#2:formatter(フォーマッター)
FORMATTER = '%(asctime)s - (%(filename)s) - [%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMATTER)

logging.critical('crit')
logging.error('error')
logging.warning('warn')
logging.info(f"info:{'tutorial'}")
logging.debug('debug')

#formatterでは属性を指定することでログにある程度の説明を持たせることができる。
#%(asctime)s:ファイルの年月日時
#%(filename)s:ファイルの名前をログに表示
#%(levelname)s:ログのレベル（重要度）を表示
#%(message)s:レベルに指定されたメッセージを表示

#3:他モジュールのログ設定をimportする場合
import logging
import sub
 #create formatter(ログの出力形式)
FORMATTER = '%(asctime)s - (%(filename)s) - [%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMATTER)
 #create logger
logger = logging.getLogger(__name__)
logger.info('mainのロガー出力(info)')
 #invoke sub module
sub.sub_log_func()

#4:ハンドラー
#ログの出力先を制御する設定/ドキュメントの定義を行う
#ログメッセージの深刻度に基づいてハンドラーの指定された出力先に振り分ける機能

 #4.2:StreamHandler
  #ロガーを作成
logger = logging.getLogger("example_logger")
logger.setLevel(logging.DEBUG)
  #Stream_handlerを作成
stream_handler = logging.StreamHandler()      #デフォルトはsys.stderr
  #ログフォーマットを設定
formatter = logging.Formatter("%(asctime)s-%(name)s-%(message)s")
stream_handler.setFormatter(formatter)
  #ロガーにハンドラーを追加
logger.addHandler(stream_handler)
  #ログを出力
logger.debug("this is a debug messeage")
logger.info("this is an info message")
logger.warning("this is a warning message")

#5:FileHandler
FORMATTER = "%(asctime)s-(%(filename)s)-[%(levelname)s]-%(message)s"
 #カスタムロガーでレベル設定を行っているので、そちらが優先されて直接影響しないため不要
 #logging.basicConfig(level=logging.INFO)

 #create logger
 #ロガーの共通設定になるレベルは最も低レベルのDEBUGを定義している
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

 #DEBUGレベルのログを'log/debug_handler.log'へ出力する。
handler = logging.FileHandler(
    'log/debug_handler.log',mode='w'
)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter(FORMATTER))
logger.addHandler(handler)

# WARNINGレベルのログを'log/warn_handler.log'へ出力する。
warn_handler = logging.FileHandler(
  'log/warn_handler.log',mode='w'
  )
warn_handler.setLevel(logging.WARNING)
warn_handler.setFormatter(logging.Formatter(FORMATTER))
logger.addHandler(warn_handler)

logger.debug('ロガーで取得したデバッグログです。!!!!!!!!!!!!!')
logger.info('通常の挙動です。')
logger.warning('警告です。')
logger.error('ファイルが見つかりません。')
logger.critical('緊急事態です。')

#6:フィルター
logger = logging.getLogger("example_logger")
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)

#ログフィルターの内容をカスタムで定義
class LogFilter(logging.Filter):
  def filter(self,ignore):
    word = ignore.getMessage()
    return 'password' not in word
  
#ログフィルターを設定
logger.addFilter(LogFilter())

#ログ出力
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("password = 'xxxx'")