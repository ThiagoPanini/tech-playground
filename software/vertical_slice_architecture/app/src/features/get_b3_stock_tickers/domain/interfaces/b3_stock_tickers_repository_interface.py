from abc import ABC, abstractmethod
from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


class IB3StockTickersRepository(ABC):
    """
    Interface for the B3 stock tickers repository.
    This interface defines methods for putting tickers data into the repository.
    """

    @abstractmethod
    def put_item(self, b3_stock_tickers: B3StockTicker) -> None:
        """
        Saves a B3 stock ticker to the repository.

        Args:
            b3_stock_tickers (B3StockTicker): The B3 stock ticker to save.
        """
