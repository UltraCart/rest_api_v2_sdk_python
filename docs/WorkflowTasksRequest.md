# WorkflowTasksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_to_group_id** | **int** | Assigned to group ID | [optional] 
**assigned_to_me** | **bool** | Tasks are assigned to me either by direct user id or a group that the user is a member of | [optional] 
**assigned_to_user_id** | **int** | Assigned to user ID | [optional] 
**created_by** | [**WorkflowUser**](WorkflowUser.md) |  | [optional] 
**created_dts_begin** | **str** | Date/time that the workflow task was created | [optional] 
**created_dts_end** | **str** | Date/time that the workflow task was created | [optional] 
**delay_until_dts** | **str** | Date/time that the workflow task should delay until | [optional] 
**due_dts_begin** | **str** | Date/time that the workflow task is due | [optional] 
**due_dts_end** | **str** | Date/time that the workflow task is due | [optional] 
**last_update_dts_begin** | **str** | Date/time that the workflow task was last updated | [optional] 
**last_update_dts_end** | **str** | Date/time that the workflow task was last updated | [optional] 
**object_email** | **str** | Object is associated with customer email | [optional] 
**object_type** | **str** | Object Type | [optional] 
**priority** | **str** | Priority | [optional] 
**status** | **str** | Status of the workflow task | [optional] 
**unassigned** | **bool** | Tasks that are unassigned to a user or group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


