from fastapi import APIRouter
from typing import Optional
from app.schemas.irrigation import IrrigationAdvice
from app.schemas.common import Source

router = APIRouter()

@router.get("/recommendation/irrigation", response_model=IrrigationAdvice)
async def irrigation(
    field_id: Optional[str] = None,
    crop: Optional[str] = None,
    stage: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
) -> IrrigationAdvice:
    # Mock logic
    return IrrigationAdvice(
        action="Delay",
        next_window="In 24–36 hours",
        reasoning="High rain chance in next 48h and adequate soil moisture proxy.",
        sources=[Source(title="IMD 48h Forecast")],
        confidence=85,
    )