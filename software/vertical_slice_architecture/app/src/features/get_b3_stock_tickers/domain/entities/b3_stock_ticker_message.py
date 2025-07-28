from dataclasses import dataclass, field
from uuid import uuid4
from typing import Any


@dataclass
class B3StockTickerMessageBody:
    """
    Represents the body of a B3 stock ticker message.
    This class is used to serialize B3 stock ticker data for publishing to a topic.
    
    Attributes:
        code (str): The stock ticker code.
        company_name (str): The name of the company associated with the stock ticker.
        date_extracted (str): The date when the stock ticker was extracted.
    """

    code: str
    company_name: str
    date_extracted: str


@dataclass
class B3StockTickerMessage:
    """
    Represents a message containing B3 stock ticker symbols.
    This class is used to serialize B3 stock ticker data for publishing to a topic.
    """
    message_body: B3StockTickerMessageBody
    message_id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict[str, Any]:
        """
        Converts the B3 stock ticker message to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the message.
        """
        return {
            "message_id": self.message_id,
            "message_body": self.message_body,
        }