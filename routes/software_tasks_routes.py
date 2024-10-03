from fastapi import APIRouter, HTTPException
from config.database import collection_name
from models.software_tasks import SoftwareTasks
from pymongo.errors import DuplicateKeyError
from bson import ObjectId, raw_bson
from typing import List


##Create an API router
work_log_router = APIRouter()


# Retrieves instances of task/work logs
@work_log_router.get("/GetWorkLogs", response_model=List[SoftwareTasks])
async def get_work_logs():
    work_logs_cursor = collection_name.find()
    work_logs = list(work_logs_cursor)

    for log in work_logs:
        log["id"] = str(log["_id"])

    return work_logs


## Retrieves one instance of task/work logs
@work_log_router.get("/GetWorkLogById/{id}")
async def get_work_log(id: str):
    work_log_cursor = collection_name.find({"id": ObjectId(id)})
    work_log = dict(work_log_cursor)
    # use bson ObjectId to format id input from client

    return work_log


# Create one new instance of work/task log from the client
@work_log_router.post("/CreateWorkLog")
async def create_log(task: SoftwareTasks):

    try:
        result = collection_name.insert_one(dict(task))
        print(result)

        return {"id": str(result.inserted_id)}
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="You cannot submit duplicate tasks")


# Update a work log
@work_log_router.put("/UpdateWorklog/{id}")
async def update_work_log(id: str, log: SoftwareTasks):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(log)})

    work_log = collection_name.find({"_id": ObjectId(id)})
    return work_log


# Delete one work log by ID
@work_log_router.delete("/DeleteWorkLogById/{id}")
async def delete_one_log(id: str, log: SoftwareTasks):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

    return {"status": "ok", "data": []}
