from fastapi import APIRouter, HTTPException
from config.database import training_result
from models.time_series_result import TimeSeriesResult
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from typing import List


training_output_router = APIRouter()


# Retrieves existing data, trains and returns predictive values
@training_output_router.get(
    "/GetTrainedWorkLogs", response_model=List[TimeSeriesResult]
)
async def get_trained_logs():
    output_cursor = training_result.find()
    output = list(output_cursor)

    for item in output:
        item["id"] = str(item["_id"])
    return output


## Retrieves only a few results of interest based on task categories joined as single string separated by
## + sign from the client
@training_output_router.get(
    "/GetSpecificTrainedWorkLogs/{joinedCategories}",
    response_model=List[TimeSeriesResult],
)
async def get_narrow_trained_logs(joinedCategories: str):
    queryResult = []

    for each in joinedCategories.split("+"):
        output_cursor = training_result.find({"category": each})
        queryResult.append(output_cursor)

    return queryResult
