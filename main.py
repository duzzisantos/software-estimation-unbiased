from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.software_tasks_routes import work_log_router
from routes.training_records import training_output_router
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

website_url = os.getenv("WEBSITE_URL")
origins = [
    "http://localhost:5173",
    website_url,
    ##and other origins: eg production, staging etc
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*", "POST", "GET", "DELETE"],
    allow_headers=["*"],
)


app.include_router(work_log_router)
app.include_router(training_output_router)


@app.get("/", dependencies=[Depends(RateLimiter(times=5, seconds=10))])
async def index():
    return {"message": "Too many requests"}


@app.post("/", dependencies=[Depends(RateLimiter(times=5, seconds=10))])
async def index():
    return {"message": "Too many requests"}
