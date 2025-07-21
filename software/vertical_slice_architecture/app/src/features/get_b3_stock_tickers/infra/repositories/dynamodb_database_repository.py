import os

import boto3
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    MapAttribute
)

from app.src.features.cross.utils.decorators import timing_decorator
from app.src.features.cross.utils.log_utils import (
    setup_logger,
    log_loop_status
)
from app.src.features.get_b3_stock_tickers.domain.interfaces.database_repository_interface import (
    IDatabaseRepository
)
from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


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


class DynamoDBDatabaseRepository(IDatabaseRepository):
    """
    Implementation of the B3 stock tickers repository using DynamoDB.
    """
    def __init__(self):
        self.logger = setup_logger(__name__)


    @timing_decorator
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

                    batch.save(model)

                    # Logging the status of the loop
                    log_loop_status(
                        logger=self.logger,
                        loop_idx=idx,
                        total_elements=len(b3_stock_tickers),
                        log_pace=200,
                        log_msg="Put <loop_idx> items to repository."
                    )

        except Exception as e:
            self.logger.exception(f"Error saving batch of B3 stock tickers: {e}")
            raise
