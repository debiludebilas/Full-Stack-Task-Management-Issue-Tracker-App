from fastapi import FastAPI
from database import engine, Base
from routers import tasks

app = FastAPI(title="FlowForge API")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Flowforge API works"}


