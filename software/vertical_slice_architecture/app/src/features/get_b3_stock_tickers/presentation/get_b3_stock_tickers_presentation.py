from typing import Any

from app.src.features.cross.infra.adapters.requests_http_client_adapter import RequestsHTTPClientAdapter
from app.src.features.get_b3_stock_tickers.use_case.get_b3_stock_tickers_use_case import (
    GetB3StockTickersUseCase
)
from app.src.features.get_b3_stock_tickers.infra.adapters.fundamentus_b3_stock_tickers_adapter import (
    FundamentusB3StockTickersAdapter
)
from app.src.features.get_b3_stock_tickers.infra.repositories.dynamodb_b3_stock_tickers_repository import (
    DynamoDBB3StockTickersRepository
)
from app.src.features.get_b3_stock_tickers.infra.mappers.http_response_mapper import HTTPResponseMapper


# Initializing mappers, adapters and repositories
http_client_adapter = RequestsHTTPClientAdapter()
b3_stock_tickers_parser_adapter = FundamentusB3StockTickersAdapter()
b3_stock_tickers_repository = DynamoDBB3StockTickersRepository()

# Initializing use case
use_case = GetB3StockTickersUseCase(
    http_client_adapter=http_client_adapter,
    b3_stock_tickers_parser_adapter=b3_stock_tickers_parser_adapter,
    b3_stock_tickers_repository=b3_stock_tickers_repository
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

    output_dto = use_case.execute()

    return HTTPResponseMapper.map(output_dto)
