def software_estimate_serializer(estimate) -> dict:
    return {
        "id": str(estimate["_id"]),
        "database_task": estimate["database_task"],
        "security_task": estimate["security_task"],
        "validation_task": estimate["validation_task"],
        "dev_ops_task": estimate["validation_task"],
        "server_management_task": estimate["server_management_task"],
        "api_setup_task": estimate["api_setup_task"],
        "api_integration_task": estimate["api_integration_task"],
        "data_backup_task": estimate["data_backup_task"],
        "backend_testing_task": estimate["backend_testing_task"],
        "data_structure_task": estimate["data_structure_task"],
        "machine_learning_task": estimate["machine_learning_task"],
        "scalability_task": estimate["scalability_task"],
        "optimization_task": estimate["optimization_task"],
        "cloud_task": estimate["cloud_task"],
        "styling_task": estimate["styling_task"],
        "ui_ux_task": estimate["ui_ux_task"],
        "frontend_testing_task": estimate["frontend_test_task"],
        "api_logic_task": estimate["api_logic_task"],
        "form_setup_task": estimate["form_setup_task"],
        "table_setup_task": estimate["table_setup_task"],
        "layout_setup_task": estimate["layout_setup_task"],
        "data_display_task": estimate["data_display_task"],
        "data_visualization_task": estimate["data_visualization_task"],
        "access_control_task": estimate[""],
        "seo_task": estimate["seo_task"],
        "widget_setup": estimate["widget_setup_task"],
        "ci_cd_task": estimate["ci_cd_task"],
        "deployment_task": estimate["deployment_task"],
        "cms_integration_task": estimate["cms_integration_task"],
    }


def software_estimates_serializer(estimates) -> list:
    return [software_estimate_serializer(estimate) for estimate in estimates]
