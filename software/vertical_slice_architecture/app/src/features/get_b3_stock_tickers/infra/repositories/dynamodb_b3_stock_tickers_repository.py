from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    UTCDateTimeAttribute,
    UnicodeSetAttribute
)


class B3StockTickerModel(Model):
    """
    PynamoDB model for B3 stock tickers.
    """
    class Meta:
        table_name = 'b3_stock_tickers'
        region = 'us-west-2'  # Change to your AWS region

    code = UnicodeAttribute(hash_key=True)
    company_name = UnicodeAttribute()
    web_site = UnicodeAttribute()
    request_config = UnicodeSetAttribute()
    datetime_extracted = UTCDateTimeAttribute(range_key=True)
