# Software Project Estimator — Data Service

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

**CRUD API for managing software work logs — the data backbone of the Software Project Estimator system.**

</div>

---

## Purpose

This service handles the collection, storage, retrieval, and management of work log data. Teams submit time logs for 29 standardized task categories, which are then consumed by the [Training Service](https://github.com/duzzisantos/python-data-training) for PERT analysis, LSTM forecasting, and regression modeling.

## Why It Matters

Accurate work log data is the foundation for evaluating software project estimation bias — without it, teams risk compounding the very problems they aim to solve:

- **Risky conclusions** — Incomplete or inconsistent data produces misleading model outputs. *Example: Missing logs for DevOps tasks cause the regression model to underweight infrastructure effort, leading managers to understaff deployments.*

- **Under or over-investment of resources** — Poor data quality distorts resource planning. *Example: A team logs frontend tasks inconsistently, inflating styling estimates by 40% and diverting budget from underfunded backend work.*

- **Missing deadlines** — Gaps in historical data weaken forecast accuracy. *Example: Without API integration logs from prior sprints, the LSTM model fails to flag a recurring 2-week bottleneck, and the team misses a release window.*

- **Encouraging realistic, resource-efficient estimations** — Structured, standardized data collection enables evidence-based planning. *Example: After enforcing consistent logging across all 29 task categories, a team's PERT forecasts improve from within 35% accuracy to within 12%.*

---

## Architecture

```
                    ┌───────────────────────────────────────┐
                    │           Client Applications         │
                    │     React Dashboard  ·  Swagger UI    │
                    └────────────────┬──────────────────────┘
                                     │
                          CRUD Operations
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
┌────────▼────────┐       ┌──────────▼──────────┐     ┌──────────▼──────────┐
│  Work Log CRUD  │       │  Training Results   │     │  Regression Results │
│                 │       │                     │     │                     │
│  Create         │       │  LSTM predictions   │     │  Coefficients       │
│  Read           │       │  per training run   │     │  R² scores          │
│  Update         │       │  Filterable by      │     │  Residuals          │
│  Delete         │       │  task category      │     │  Predictions        │
└────────┬────────┘       └──────────┬──────────┘     └──────────┬──────────┘
         │                           │                           │
         └───────────────────────────┼───────────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │      MongoDB        │
                          │      Atlas          │
                          │                     │
                          │  ┌───────────────┐  │
                          │  │ software_     │  │
                          │  │ work_log      │  │
                          │  │ (raw logs)    │  │
                          │  ├───────────────┤  │
                          │  │ training_     │  │
                          │  │ result        │  │
                          │  │ (LSTM output) │  │
                          │  ├───────────────┤  │
                          │  │ multiple-     │  │
                          │  │ regression    │  │
                          │  │ (coefficients)│  │
                          │  └───────────────┘  │
                          └─────────────────────┘
```

---

## Data Model

Each work log entry tracks time spent across **29 standardized subtask categories**:

```
┌─────────────────────── Backend Tasks ───────────────────────┐
│                                                              │
│   database          server_management     data_backup        │
│   security          api_setup             backend_testing    │
│   validation        api_integration       data_structure     │
│   dev_ops           machine_learning      scalability        │
│   optimization      cloud                                    │
│                                                              │
├─────────────────────── Frontend Tasks ──────────────────────┤
│                                                              │
│   styling           form_setup            data_visualization │
│   ui_ux             table_setup           access_control     │
│   frontend_testing  layout_setup          seo                │
│   api_logic         data_display          widget_setup       │
│   ci_cd             deployment            cms_integration    │
│                                                              │
├─────────────────────── Metadata ────────────────────────────┤
│                                                              │
│   last_updated      submitted_by                             │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

All task fields are optional integers (duration in minutes/hours), allowing partial log submissions.

---

## API Reference

### Work Logs

<details>
<summary><strong>GET /GetWorkLogs</strong></summary>

Retrieve all work log entries.

**Response:**
```json
[
  {
    "id": "665f1a...",
    "database_task": 120,
    "api_setup_task": 90,
    "styling_task": 45,
    "last_updated": "2024-06-27T10:00:00",
    "submitted_by": "dev-team-a"
  }
]
```

</details>

<details>
<summary><strong>GET /GetWorkLogById/{id}</strong></summary>

Retrieve a single work log by MongoDB ObjectId.

</details>

<details>
<summary><strong>POST /CreateWorkLog</strong></summary>

Submit a new work log entry. Only include the tasks that were worked on — all fields are optional.

**Request:**
```json
{
  "database_task": 120,
  "api_setup_task": 90,
  "backend_testing_task": 60,
  "styling_task": 45,
  "last_updated": "2024-06-27T10:00:00",
  "submitted_by": "dev-team-a"
}
```

**Response:**
```json
{ "id": "665f1a2b..." }
```

</details>

<details>
<summary><strong>PUT /UpdateWorklog/{id}</strong></summary>

Update an existing work log entry by ID.

**Request:** Same schema as `POST /CreateWorkLog`.

</details>

<details>
<summary><strong>DELETE /DeleteWorkLogById/{id}</strong></summary>

Delete a work log entry by ID.

**Response:**
```json
{ "status": "ok", "data": [] }
```

</details>

### Training Results

<details>
<summary><strong>GET /GetTrainedWorkLogs</strong></summary>

Retrieve all stored LSTM time-series predictions across training runs.

**Response:**
```json
[
  {
    "task_categories": ["database_task", "api_setup_task"],
    "predicted_durations": [115.3, 88.7],
    "training_date": "2024-06-27T10:00:00"
  }
]
```

</details>

<details>
<summary><strong>GET /GetSpecificTrainedWorkLogs/{categories}</strong></summary>

Filter predictions by task category. Categories are joined with `+`.

**Example:** `/GetSpecificTrainedWorkLogs/database_task+api_setup_task`

</details>

### Regression Results

<details>
<summary><strong>GET /GetRegressionResults</strong></summary>

Retrieve stored multilinear regression results.

**Response:**
```json
[
  {
    "task_categories": ["database_task", "api_setup_task", "..."],
    "coefficients": [1.23, 0.87, "..."],
    "intercept": 5.67,
    "r_squared": 0.92,
    "predicted_totals": [245, 310, "..."],
    "actual_totals": [250, 300, "..."],
    "residuals": [-5, 10, "..."],
    "sample_count": 48,
    "training_date": "2024-06-27T10:00:00"
  }
]
```

</details>

---

## Data Flow

```
Team submits work log
        │
        ▼
  POST /CreateWorkLog
        │
        ▼
┌───────────────────┐
│  software_work_log│ ◄──── Raw time data per task
│  (MongoDB)        │
└────────┬──────────┘
         │
         │  Consumed by Training Service
         │  (scheduled retraining)
         ▼
┌───────────────────┐     ┌───────────────────┐
│  training_result  │     │ multiple-regression│
│  (LSTM output)    │     │ (regression model) │
└────────┬──────────┘     └────────┬──────────┘
         │                         │
         ▼                         ▼
  GET /GetTrainedWorkLogs   GET /GetRegressionResults
         │                         │
         └────────┬────────────────┘
                  │
                  ▼
         Dashboard renders
         charts & analysis
```

---

## Quick Start

```bash
# 1. Clone and install
git clone <repo-url> && cd software-estimation-data
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Configure environment
# Set MONGO_URL and WEBSITE_URL in .env

# 3. Run
uvicorn main:app --port 8000 --reload
# → http://localhost:8000/docs
```

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MONGO_URL` | Yes | MongoDB Atlas connection string |
| `WEBSITE_URL` | Yes | Frontend origin for CORS |

---

## System Context

This service is one of three components in the Software Project Estimator:

```
┌─────────────────────────────────────────────────────────┐
│              Software Project Estimator                  │
│                                                          │
│   ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│   │    Data      │  │   Training   │  │  Dashboard   │  │
│   │   Service    │  │   Service    │  │  (React)     │  │
│   │  ──────────  │  │  ──────────  │  │  ──────────  │  │
│   │  CRUD API    │  │  PERT        │  │  PERT tab    │  │
│   │  Work logs   │  │  LSTM        │  │  TimeSeries  │  │
│   │  Results     │◄─┤  Regression  │  │  Regression  │  │
│   │  retrieval   │  │  Monte Carlo │  │  Charts      │  │
│   │             ─┼──┤►            ─┼──┤►             │  │
│   └─────────────┘  └──────────────┘  └──────────────┘  │
│         │                                    │          │
│         └────────────── MongoDB ─────────────┘          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## License

[MIT](LICENSE)
