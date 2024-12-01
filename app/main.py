from fastapi import FastAPI
from app.routes.analyze import router as analyze_router


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Stock Market RAG API"}

app.include_router(analyze_router, prefix="/analyze")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
