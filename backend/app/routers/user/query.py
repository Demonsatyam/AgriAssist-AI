from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.services.orchestrator import answer_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(payload: QueryRequest) -> QueryResponse:
    result = answer_query(payload.text, payload.locale, payload.farm_id)
    return QueryResponse(**result)
