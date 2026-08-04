# ConversationPbxCallSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **[str]** | Filter by agent IDs | [optional] 
**customer_name** | **str** | Filter by customer name | [optional] 
**direction** | **str** | Filter by call direction (inbound/outbound) | [optional] 
**disposition** | **str** | Filter by call disposition | [optional] 
**end_date** | **str** | Filter calls created on or before this date (ISO 8601) | [optional] 
**has_ai_engagement** | **bool** | Filter to calls with AI agent engagement | [optional] 
**has_recording** | **bool** | Filter to calls that have a recording | [optional] 
**has_transcript** | **bool** | Filter to calls that have a transcript | [optional] 
**max_duration_seconds** | **int** | Filter by maximum call duration in seconds | [optional] 
**min_duration_seconds** | **int** | Filter by minimum call duration in seconds | [optional] 
**phone_number** | **str** | Filter by phone number (partial match supported) | [optional] 
**queue_uuids** | **[str]** | Filter by queue UUIDs | [optional] 
**search_term** | **str** | Free text search term - smart-routed based on content (phone, email, UUID, or general text) | [optional] 
**start_date** | **str** | Filter calls created on or after this date (ISO 8601) | [optional] 
**statuses** | **[str]** | Filter by call statuses | [optional] 
**transcript_search** | **str** | Search within transcript text | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


