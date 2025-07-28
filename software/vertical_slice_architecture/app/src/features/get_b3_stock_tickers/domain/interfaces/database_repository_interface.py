from abc import ABC, abstractmethod
from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


class IDatabaseRepository(ABC):
    """
    Interface for the B3 stock tickers database repository.
    This interface defines methods for putting tickers data into the repository.
    """

    @abstractmethod
    def batch_write_items(self, b3_stock_tickers: list[B3StockTicker]) -> None:
        """
        Saves a batch of B3 stock tickers to the repository.

        Args:
            b3_stock_tickers (list[B3StockTicker]): The list of B3 stock tickers to save.
        """
