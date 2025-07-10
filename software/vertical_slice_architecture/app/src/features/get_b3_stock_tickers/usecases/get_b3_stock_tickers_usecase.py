from dataclasses import dataclass

from app.src.features.cross.utils.logger import setup_logger
from app.src.features.cross.domain.interfaces.http_client_adapter import IHTTPClientAdapter
from app.src.features.cross.domain.entities.http_client_request_config import HTTPClientRequestConfig
from app.src.features.cross.domain.entities.http_client_retry_config import HTTPClientRetryConfig
from app.src.features.get_b3_stock_tickers.domain.interfaces.b3_stock_tickers_parser_adapter_interface import (
    IB3StockTickersParserAdapter
)


logger = setup_logger(__name__)


@dataclass(frozen=True)
class GetB3StockTickersUseCase:
    """
    Use case for fetching B3 stock tickers.
    
    Attributes:
        http_client_adapter (IHTTPClientAdapter): Adapter for making HTTP requests.
    """

    http_client_adapter: IHTTPClientAdapter
    b3_stock_tickers_parser_adapter: IB3StockTickersParserAdapter

    def execute(self) -> list[str]:
        """
        Executes the use case to fetch B3 stock tickers.
        
        Returns:
            A list of stock ticker codes from B3.
        """

        # Building a B3 stock tickers request entity
        request_config = HTTPClientRequestConfig(
            url="https://www.fundamentus.com.br/resultado.php",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
            timeout=10,
            retry_config=HTTPClientRetryConfig(
                num_retries=3,
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504]
            )
        )

        logger.info(f"Fetching B3 stock tickers from {request_config.url}")
        response = self.http_client_adapter.get(request_config=request_config)

        logger.info("Parsing B3 stock tickers from the HTTP response with BeautifulSoup")
        b3_stock_tickers = self.b3_stock_tickers_parser_adapter.parse_b3_stock_tickers(
            http_client_response=response,
            request_config=request_config
        )

        return b3_stock_tickers
