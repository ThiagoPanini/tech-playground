import os
import json
from uuid import uuid4

import boto3

from app.src.features.cross.utils.decorators import timing_decorator
from app.src.features.cross.utils.log_utils import (
    setup_logger,
    log_loop_status
)
from app.src.features.get_b3_stock_tickers.domain.interfaces.queue_adapter_interface import (
    IQueueAdapter
)
from app.src.features.get_b3_stock_tickers.domain.entities.b3_stock_ticker import B3StockTicker


class SQSQueueAdapter(IQueueAdapter):
    def __init__(self):
        self.logger = setup_logger(__name__)
        self.sqs_client = boto3.client("sqs", region_name=boto3.session.Session().region_name)


    @timing_decorator
    def batch_send_messages(self, b3_stock_tickers: list[B3StockTicker]) -> None:
        """
        Sends a batch of B3 stock tickers to the queue.

        Args:
            b3_stock_tickers (list[B3StockTicker]): The list of B3 stock tickers to send.
        """
        
        # Preparing messages to be sent in batches
        try:
            entries = [
                {
                    "Id": str(uuid4()),
                    "MessageBody": json.dumps({
                        "code": ticker.code,
                        "company_name": ticker.company_name,
                        "web_site": ticker.web_site.value,
                        "request_config": ticker.request_config.to_dict(),
                        "date_extracted": ticker.date_extracted
                    })
                }
                for ticker in b3_stock_tickers
            ]

        except Exception as e:
            self.logger.error(f"Error preparing messages for batch send: {e}")
            raise
        
        try:
            # Sending messages in batches of 10 messages per batch
            for i in range(0, len(entries), 10):
                batch_entries = entries[i:i + 10]

                _ = self.sqs_client.send_message_batch(
                    QueueUrl=os.environ.get("SQS_QUEUE_NAME"),
                    Entries=batch_entries
                )

                # Logging the status of the loop
                log_loop_status(
                    logger=self.logger,
                    loop_idx=i // 10,
                    total_elements=len(b3_stock_tickers) // 10,
                    log_pace=20,
                    log_msg="Sent <loop_idx> batches of 10 messages each to queue."
                )

        except Exception as e:
            self.logger.error(f"Error sending batch messages to SQS: {e}")
            raise
