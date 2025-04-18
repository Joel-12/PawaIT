from fastapi import APIRouter, HTTPException
from app.schemas.query_schema import QueryRequest, QueryResponse
from app.services.gemini_client import get_llm_response



router = APIRouter(prefix="/api", tags=["Query"])

@router.post("/ask", response_model=QueryResponse)
async def ask_question(query: QueryRequest):
    try:
        response = await get_llm_response(query.question)
        return QueryResponse(answer=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
