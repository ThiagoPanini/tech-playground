from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class HTTPClientRetryConfig:
    """
    Represents the retry configuration for an HTTP client request.

    Attributes:
        num_retries (int): The number of times to retry the request.
        backoff_factor (float): A factor to apply to the delay between retries.
        status_forcelist (list[int]): A list of HTTP status codes that should trigger a retry.
    """

    num_retries: int = 3
    backoff_factor: float = 0.1
    status_forcelist: Optional[list[int]] = field(default_factory=lambda: [500, 502, 503, 504])
