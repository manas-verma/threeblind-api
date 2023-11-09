from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import router as router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/")
async def welcome():
    return "Welcome to Three Blind API"
