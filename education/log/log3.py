#ここではログを出力するときにどのような情報を出力するかを指定するプログラムを作成する
import logging
FORMATTER='%(asctime)s-%(filename)s-[%(levelname)s]-%(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    format=FORMATTER,
)

logger=logging.getLogger(__name__)
logger.info("System Start")

#FORMATTERという書式を決めるものに書式を入れ,指定している。
#%(asctime)sは現在日時,%(filename)sはファイル名,%(levelname)sはログのレベル名,%(message)sには出力する文章内容がそれぞれ入っている
