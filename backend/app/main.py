from fastapi import FastAPI
from app.routes import query

app = FastAPI(title="AI Travel Assistant")

app.include_router(query.router)
