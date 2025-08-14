# backend/app/routers/admin/ops.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/metrics")
async def metrics():
    # placeholder; wire Prometheus later
    return {"uptime": "mock", "requests": "mock"}
