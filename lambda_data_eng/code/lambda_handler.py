import datetime
from api import MercadoBitcoinApi
from writter import S3Writter
import logging

logger = logging.getLogger("lambda")
logging.basicConfig(level = logging.INFO, force=True)


def handler(event, context):
    coin = "BTC"
    date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    logger.info("Hey")
    api = MercadoBitcoinApi(coin=coin)
    data = api.get_data(date=date)

    writer = S3Writter(coin=coin)
    writer.write(data)

