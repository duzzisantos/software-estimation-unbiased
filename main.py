from fastapi import FastAPI
from routes.software_tasks_routes import work_log_router
from routes.training_records import training_output_router

app = FastAPI()


app.include_router(work_log_router)
app.include_router(training_output_router)
