from fastapi import APIRouter
import time
from app.core.stats import stats

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/metrics")
async def metrics():
    uptime_sec = int(time.time() - stats.start_ts)
    return {
        "uptime_sec": uptime_sec,
        "requests_total": stats.requests_total,
        "requests_success": stats.requests_success,
        "requests_error": stats.requests_error,
        "last_request_ms": stats.last_request_ms,
    }
