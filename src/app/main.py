from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, Base

from app.books import router
# import settings
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Books API", openapi_url=f"/api/v1/openapi.json",
)

app.include_router(router.books_router, prefix="/api/v1")