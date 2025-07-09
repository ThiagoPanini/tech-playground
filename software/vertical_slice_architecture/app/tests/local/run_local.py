from app.src.features.get_b3_stock_tickers.presentation import get_b3_stock_tickers_presentation


# Building handlers
get_b3_stock_tickers_handler = get_b3_stock_tickers_presentation.handler


"""
FEATURE: Get B3 Stock Tickers

DESCRIPTION:
    This feature provides functionality to scrape and retrieve stock tickers from the B3 (Brazilian
    Stock Exchange) using a web scraping adapter. It includes the necessary entities, interfaces,
    and use cases to facilitate the retrieval of stock data.
"""

response = get_b3_stock_tickers_handler(event=None, context=None)
print(response[0])
