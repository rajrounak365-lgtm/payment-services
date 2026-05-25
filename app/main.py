from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Payment Service")

app.include_router(router)

@app.get("/")
def root():
    return {"service": "payment-service", "status": "running"}
