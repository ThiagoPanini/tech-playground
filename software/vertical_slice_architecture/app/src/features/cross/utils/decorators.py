import os
import time
from functools import wraps

from app.src.features.cross.utils.log_utils import setup_logger


logger = setup_logger(__name__)


def timing_decorator(method):
    """
    Decorator to measure the execution time of a method.
    If the environment variable ENABLE_TIMING_DECORATOR is set to "1",
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        enable_timing = os.getenv("ENABLE_TIMING_DECORATOR", "0") == "1"
        if enable_timing and logger:
            start_time = time.time()
            result = method(self, *args, **kwargs)
            elapsed_time = time.time() - start_time
            logger.info(f"{method.__name__} executed in {elapsed_time:.2f} seconds")
            return result
        else:
            return method(self, *args, **kwargs)

    return wrapper
