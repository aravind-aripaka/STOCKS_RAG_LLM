from fastapi import FastAPI
from app.routes import analyze, recommend, sentiment

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Stock Market RAG API"}

app.include_router(analyze.router, prefix="/analyze")
app.include_router(recommend.router, prefix="/recommend")
app.include_router(sentiment.router, prefix="/sentiment")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
