# backend/app/core/stats.py

import time
from dataclasses import dataclass

@dataclass
class Stats:
    start_ts: float = time.time()
    requests_total: int = 0
    requests_success: int = 0
    requests_error: int = 0
    last_request_ms: int | None = None

stats = Stats()
