from fastapi import APIRouter
from app.schemas.market import MarketTrend, PricePoint
from app.schemas.common import Source

router = APIRouter()

@router.get("/market/price", response_model=MarketTrend)
async def market_price(commodity: str, market_id: str) -> MarketTrend:
    # Mock price series
    series = [
        PricePoint(date="2025-08-10", price=2560.0),
        PricePoint(date="2025-08-11", price=2585.0),
        PricePoint(date="2025-08-12", price=2590.0),
        PricePoint(date="2025-08-13", price=2605.0),
        PricePoint(date="2025-08-14", price=2610.0),
    ]
    return MarketTrend(
        latest_price=series[-1].price,
        trend=series,
        suggestion="Hold",
        sources=[Source(title="eNAM Market Feed", excerpt=f"{commodity} in {market_id}")],
        confidence=78,
    )