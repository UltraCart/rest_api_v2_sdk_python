# ConversationAgentStatusConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the status is active and selectable. DELETE soft-deactivates by setting this to false. | [optional] 
**channel** | **str** | Channel this status applies to | [optional] 
**color** | **str** | Hex color for UI (e.g. &#39;#FF5733&#39;) | [optional] 
**conversation_status_uuid** | **str** | Conversation agent status unique identifier | [optional] 
**created_at** | **str** | Created at | [optional] 
**icon** | **str** | Icon name | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**name** | **str** | Display name shown to agents | [optional] 
**parent_status** | **str** | Channel-native parent status | [optional] 
**routing_effect** | **str** | Canonical routing semantic. Derived server-side from (channel, parent_status). | [optional] 
**sort_order** | **int** | Sort order in lists; lower &#x3D; first | [optional] 
**twilio_activity_sid** | **str** | Twilio TaskRouter Activity SID (PBX-only; null for chat-only statuses) | [optional] 
**updated_at** | **str** | Updated at | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


