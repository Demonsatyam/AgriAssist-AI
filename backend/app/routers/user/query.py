from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.schemas.common import Source

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(payload: QueryRequest) -> QueryResponse:
    # Hardcoded mock response
    return QueryResponse(
        answer="Delay irrigation for 24–36 hours.",
        reasoning=(
            "Rain probability is ~70% in the next 48 hours; conserving water now is advised."
        ),
        sources=[
            Source(title="IMD 48h Forecast", excerpt="Rain chance ~70%"),
            Source(title="Wheat Irrigation Guide", excerpt="Avoid irrigating before rainfall"),
        ],
        confidence=82,
    )