from fastapi import FastAPI
from routes.software_tasks_routes import work_log_router

app = FastAPI()


app.include_router(work_log_router)
