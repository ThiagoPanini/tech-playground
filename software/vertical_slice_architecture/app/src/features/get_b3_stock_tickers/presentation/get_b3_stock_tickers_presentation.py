from typing import Any

from app.src.features.cross.infra.adapters.requests_http_client_adapter import RequestsHTTPClientAdapter
from app.src.features.get_b3_stock_tickers.usecases.get_b3_stock_tickers_usecase import (
    GetB3StockTickersUseCase
)
from app.src.features.get_b3_stock_tickers.infra.adapters.fundamentus_b3_stock_tickers_adapter import (
    FundamentusB3StockTickersAdapter
)


# Initializing mappers, adapters and repositories
http_client_adapter = RequestsHTTPClientAdapter()
b3_stock_tickers_parser_adapter = FundamentusB3StockTickersAdapter()


# Initializing use case
use_case = GetB3StockTickersUseCase(
    http_client_adapter=http_client_adapter,
    b3_stock_tickers_parser_adapter=b3_stock_tickers_parser_adapter
)


# Defining a handler function for executing the use case in AWS Lambda
def handler(event: dict[str, Any], context: Any) -> Any:
    """
    AWS Lambda handler function to execute the GetB3StockTickersUseCase.

    Args:
        event (dict[str, Any]): The event data passed to the Lambda function.
        context (Any): The context object provided by AWS Lambda.

    Returns:
        Any: The result of the use case execution, typically a list of stock tickers.
    """

    return use_case.execute()
