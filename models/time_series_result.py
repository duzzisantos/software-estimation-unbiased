from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


class TimeSeriesResult(BaseModel):
    task_categories: List[str]
    predicted_durations: List[Union[float, int]]
    training_date: datetime = datetime.now()


class RegressionResult(BaseModel):
    task_categories: List[str]
    coefficients: List[float]
    intercept: float
    r_squared: float
    predicted_totals: List[float]
    actual_totals: List[float]
    residuals: List[float]
    sample_count: int
    training_date: datetime = datetime.now()
