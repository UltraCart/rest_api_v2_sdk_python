# ConversationAgentStatusRollup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_name** | **str** | Agent display name | [optional] 
**agent_user_id** | **str** | Agent user id | [optional] 
**availability_pct** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**available_seconds** | **int** | Seconds spent Available (incl. Busy per OVERVIEW reporting convention) | [optional] 
**calls_taken** | **int** | Calls handled by the agent on this day (PBX channel only) | [optional] 
**channel** | **str** | Channel | [optional] 
**chats_handled** | **int** | Chats handled by the agent on this day (chat channel only) | [optional] 
**rollup_date** | **str** | Day this rollup covers (YYYY-MM-DD) | [optional] 
**status_breakdown** | **bool, date, datetime, dict, float, int, list, str, none_type** | Per-status duration breakdown in seconds (status name -&gt; seconds) | [optional] 
**total_tracked_seconds** | **int** | Total seconds tracked across all statuses for the day | [optional] 
**unavailable_seconds** | **int** | Seconds spent Unavailable | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


