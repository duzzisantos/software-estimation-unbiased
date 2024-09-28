from pydantic import BaseModel
from models.task_model import TaskModel
from datetime import datetime


class SoftwareTasks(BaseModel):

    ## Backend tasks
    database_task: list[TaskModel]
    security_task: list[TaskModel]
    validation_task: list[TaskModel]
    dev_ops_task: list[TaskModel]
    server_management_task: list[TaskModel]
    api_setup_task: list[TaskModel]
    api_integration_task: list[TaskModel]
    data_backup_task: list[TaskModel]
    backend_testing_task: list[TaskModel]
    data_structure_task: list[TaskModel]
    machine_learning_task: list[TaskModel]
    scalability_task: list[TaskModel]
    optimization_task: list[TaskModel]
    cloud_task: list[TaskModel]

    ## Frontend tasks
    styling_task: list[TaskModel]
    ui_ux_task: list[TaskModel]
    frontend_testing_task: list[TaskModel]
    api_logic_task: list[TaskModel]
    form_setup_task: list[TaskModel]
    table_setup_task: list[TaskModel]
    layout_setup_task: list[TaskModel]
    data_display_task: list[TaskModel]
    data_visualization_task: list[TaskModel]
    access_control_task: list[TaskModel]
    seo_task: list[TaskModel]
    widget_setup_task: list[TaskModel]
    ci_cd_task: list[TaskModel]
    deployment_task: list[TaskModel]
    cms_integration_task: list[TaskModel]

    ## Time stamps
    last_updated: datetime = datetime.now()
