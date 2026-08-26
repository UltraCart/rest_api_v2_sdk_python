# ConversationAgentStatusEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_identifier** | **str** | Agent identifier â€” voice_identity for PBX (e.g. &#39;client:login&#39;), participant_arn for chat, synthetic &#39;ai:&lt;user_id&gt;&#39; for AI flag events. Stable across an agent&#39;s events; participates in DDB pk and GSI1 sk. | [optional] 
**agent_name** | **str** | Agent display name at the time of the event | [optional] 
**agent_type** | **str** | Agent type | [optional] 
**agent_user_id** | **str** | Agent user id (links across channels) | [optional] 
**channel** | **str** | Channel | [optional] 
**custom_status_name** | **str** | Custom status name (when applicable) | [optional] 
**custom_status_uuid** | **str** | Custom status uuid (when applicable) | [optional] 
**duration_in_previous_seconds** | **int** | Time spent in the previous status, in seconds | [optional] 
**event_dts** | **str** | Event timestamp (ISO 8601) | [optional] 
**event_uuid** | **str** | Event UUID (natural key for ES + BQ) | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**new_routing_effect** | **str** | Canonical new routing semantic | [optional] 
**new_status** | **str** | Channel-native new status name | [optional] 
**parent_merchant_id** | **str** | Parent merchant id (denormalized for ES routing parity) | [optional] 
**previous_routing_effect** | **str** | Canonical previous routing semantic | [optional] 
**previous_status** | **str** | Channel-native previous status name | [optional] 
**trigger** | **str** | What triggered the transition | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


