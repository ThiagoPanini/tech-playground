from abc import ABC, abstractmethod
from typing import Any

from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


class IQueueAdapter(ABC):
    """
    Interface for the B3 stock tickers queue adapter.
    This interface defines methods for sending messages to a queue.
    """
    
    @abstractmethod
    def batch_send_messages(self, b3_stock_tickers: list[B3StockTicker]) -> None:
        """
        Sends a batch of B3 stock tickers to the queue.

        Args:
            b3_stock_tickers (list[B3StockTicker]): The list of B3 stock tickers to send.
        """
