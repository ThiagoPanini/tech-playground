import os

import boto3
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    MapAttribute
)

from app.src.features.cross.utils.logger import setup_logger
from app.src.features.get_b3_stock_tickers.domain.interfaces.b3_stock_tickers_repository_interface import (
    IB3StockTickersRepository
)
from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


logger = setup_logger(__name__)


class B3StockTickerModel(Model):
    """
    PynamoDB model for B3 stock tickers.
    """
    class Meta:
        table_name = os.getenv("DYNAMODB_B3_STOCK_TICKERS_TABLE_NAME")
        region = boto3.session.Session().region_name

    code = UnicodeAttribute(hash_key=True)
    company_name = UnicodeAttribute()
    web_site = UnicodeAttribute()
    request_config = MapAttribute()
    date_extracted = UnicodeAttribute(range_key=True)

    def __init__(self, *args, **kwargs):
        self.Meta.table_name = os.getenv("DYNAMODB_B3_STOCK_TICKERS_TABLE_NAME")
        super().__init__(*args, **kwargs)


class DynamoDBB3StockTickersRepository(IB3StockTickersRepository):
    """
    Implementation of the B3 stock tickers repository using DynamoDB.
    """

    def __log_loop_status(self, loop_idx: int, total_elements: int, log_pace: int = 50) -> None:
        """
        Logs the progress of a loop processing stock tickers at specified intervals.

        At every `log_pace` iterations, this method logs the number of tickers processed,
        the number remaining, and the percentage of completion.

        Args:
            loop_idx (int): The current index of the loop iteration.
            total_elements (int): The total number of elements to process.
            log_pace (int): The interval at which to log progress. Default is 50.
        """

        if loop_idx > 0 and loop_idx % log_pace == 0:
            num_elements_left = total_elements - loop_idx
            pct_elements_left = round(100 * (1 - (num_elements_left / total_elements)), 2)
            logger.info(f"Processed {loop_idx} tickers. "
                        f"Remaining: {num_elements_left} tickers ({pct_elements_left}% completed)")


    def batch_write_items(self, b3_stock_tickers: list[B3StockTicker]) -> None:
        """
        Saves a batch of B3 stock tickers to the repository.

        Args:
            b3_stock_tickers (list[B3StockTicker]): The list of B3 stock tickers to save.
        """
        try:
            with B3StockTickerModel.batch_write() as batch:
                for idx, ticker in enumerate(b3_stock_tickers):
                    model = B3StockTickerModel(
                        code=ticker.code,
                        company_name=ticker.company_name,
                        web_site=ticker.web_site.value,
                        request_config=ticker.request_config.to_dict(),
                        date_extracted=ticker.date_extracted
                    )

                    self.__log_loop_status(
                        loop_idx=idx,
                        total_elements=len(b3_stock_tickers),
                        log_pace=100
                    )
                    batch.save(model)

        except Exception as e:
            logger.exception(f"Error saving batch of B3 stock tickers: {e}")
            raise
