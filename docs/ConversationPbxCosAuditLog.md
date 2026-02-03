# ConversationPbxCosAuditLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action taken | [optional] 
**agent_login** | **str** | Login of the agent who attempted the call | [optional] 
**audit_log_uuid** | **str** | Audit log entry unique identifier | [optional] 
**class_of_service_name** | **str** | Name of the class of service (denormalized for display) | [optional] 
**class_of_service_uuid** | **str** | UUID of the class of service that was evaluated | [optional] 
**destination** | **str** | Phone number the agent tried to dial | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**rule_triggered** | **str** | Rule that triggered the action | [optional] 
**supervisor_login** | **str** | Login of supervisor who approved/denied (null for timeouts and direct blocks) | [optional] 
**timestamp** | **str** | ISO 8601 timestamp of the event | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


