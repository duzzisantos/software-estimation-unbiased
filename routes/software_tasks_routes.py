from fastapi import APIRouter
from config.database import collection_name
from models.software_tasks import SoftwareTasks

from schemas.software_tasks_schema import (
    software_estimate_serializer,
    software_estimates_serializer,
)


##Create an API router
work_log_router = APIRouter()


# Retrieves instances of task/work logs
@work_log_router.get("/")
async def get_work_logs():
    work_logs = software_estimate_serializer(collection_name.find())
    return {"status": "ok", "data": work_logs}
