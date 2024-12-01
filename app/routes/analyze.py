from fastapi import APIRouter
from app.services.data_retrieval import fetch_stock_data
from app.services.lllm_interface import generate_response
router = APIRouter()

@router.get("/stock/{symbol}")
async def get_stock_data(symbol: str):
    data = fetch_stock_data(symbol)
    return data

@router.get("/test-llm")
async def test_llm(query: str = "Explain stock trends"):
    response = generate_response(query)
    return {"query": query, "response": response}
