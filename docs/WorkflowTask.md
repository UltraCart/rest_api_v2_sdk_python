# WorkflowTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_to_group** | **str** | Assigned to group | [optional] 
**assigned_to_group_id** | **int** | Assigned to group ID | [optional] 
**assigned_to_user** | **str** | Assigned to user | [optional] 
**assigned_to_user_id** | **int** | Assigned to user ID | [optional] 
**attachments** | [**list[WorkflowAttachment]**](WorkflowAttachment.md) | Attachments to the Workflow Task | [optional] 
**created_by** | [**WorkflowUser**](WorkflowUser.md) |  | [optional] 
**created_dts** | **str** | Date/time that the workflow task was created | [optional] 
**delay_until_dts** | **str** | Date/time that the workflow task should delay until | [optional] 
**dependant_workflow_task_uuid** | **str** | Dependant Workflow Task UUID (must be completed before this task can be completed) | [optional] 
**due_dts** | **str** | Date/time that the workflow task is due | [optional] 
**expiration_dts** | **str** | Date/time that the workflow task will expire and be closed.  This is set by system generated tasks. | [optional] 
**histories** | [**list[WorkflowTaskHistory]**](WorkflowTaskHistory.md) | Array of history records for the task | [optional] 
**last_update_dts** | **str** | Date/time that the workflow task was last updated | [optional] 
**merchant_id** | **str** | Merchant ID | [optional] 
**notes** | [**list[WorkflowNote]**](WorkflowNote.md) | Notes on the Workflow Task | [optional] 
**object_email** | **str** | Object is associated with customer email | [optional] 
**object_id** | **str** | Object ID | [optional] 
**object_type** | **str** | Object Type | [optional] 
**object_url** | **str** | Object URL | [optional] 
**priority** | **str** | Priority | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | Properties | [optional] 
**related_workflow_task_uuid** | **str** | Related Workflow Task UUID | [optional] 
**status** | **str** | Status of the workflow task | [optional] 
**system_task_type** | **str** | Constant for the type of system generated task | [optional] 
**tags** | **list[str]** | Tags | [optional] 
**task_context** | **str** | User friendly string of the task context | [optional] 
**task_details** | **str** | Task Details | [optional] 
**task_name** | **str** | Task Name | [optional] 
**workflow_task_uuid** | **str** | Workflow Task UUID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


