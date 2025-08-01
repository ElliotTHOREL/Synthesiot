from fastapi import FastAPI
from app.routes.summarizer import router

app = FastAPI(title="Synthesiot")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.start_api:app", host="127.0.0.1", port=3506, reload=True)