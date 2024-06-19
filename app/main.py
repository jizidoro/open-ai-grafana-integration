from fastapi import FastAPI
from app.scheduler import start_scheduler

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/")
async def read_root():
    return {"message": "OpenAI Grafana Integration is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)