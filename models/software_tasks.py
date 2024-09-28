from pydantic import BaseModel


class SoftwareTasks(BaseModel):

    ## Backend tasks
    database_task: dict[str, str]
    security_task: dict[str, str]
    validation_task: dict[str, str]
    dev_ops_task: dict[str, str]
    server_management_task: dict[str, str]
    api_setup_task: dict[str, str]
    api_integration_task: dict[str, str]
    data_backup_task: dict[str, str]
    backend_testing_task: dict[str, str]
    data_structure_task: dict[str, str]
    machine_learning_task: dict[str, str]
    scalability_task: dict[str, str]
    optimization_task: dict[str, str]
    cloud_task: dict[str, str]

    ## Frontend tasks
    styling_task: dict[str, str]
    ui_ux_task: dict[str, str]
    frontend_testing_task: dict[str, str]
    api_logic_task: dict[str, str]
    form_setup_task: dict[str, str]
    table_setup_task: dict[str, str]
    layout_setup_task: dict[str, str]
    data_display_task: dict[str, str]
    data_visualization_task: dict[str, str]
    access_control_task: dict[str, str]
    seo_task: dict[str, str]
    widget_setup_task: dict[str, str]
    ci_cd_task: dict[str, str]
    deployment_task: dict[str, str]
    cms_integration_task: dict[str, str]
