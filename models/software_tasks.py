from pydantic import BaseModel
from typing import Optional


# from datetime import datetime
# import bson


class SoftwareTasks(BaseModel):

    ## Backend tasks
    database_task: Optional[int] = None
    security_task: Optional[int] = None
    validation_task: Optional[int] = None
    dev_ops_task: Optional[int] = None
    server_management_task: Optional[int] = None
    api_setup_task: Optional[int] = None
    api_integration_task: Optional[int] = None
    data_backup_task: Optional[int] = None
    backend_testing_task: Optional[int] = None
    data_structure_task: Optional[int] = None
    machine_learning_task: Optional[int] = None
    scalability_task: Optional[int] = None
    optimization_task: Optional[int] = None
    cloud_task: Optional[int] = None

    ## Frontend tasks
    styling_task: Optional[int] = None
    ui_ux_task: Optional[int] = None
    frontend_testing_task: Optional[int] = None
    api_logic_task: Optional[int] = None
    form_setup_task: Optional[int] = None
    table_setup_task: Optional[int] = None
    layout_setup_task: Optional[int] = None
    data_display_task: Optional[int] = None
    data_visualization_task: Optional[int] = None
    access_control_task: Optional[int] = None
    seo_task: Optional[int] = None
    widget_setup_task: Optional[int] = None
    ci_cd_task: Optional[int] = None
    deployment_task: Optional[int] = None
    cms_integration_task: Optional[int] = None
    last_updated: str
    submitted_by: Optional[str] = None
