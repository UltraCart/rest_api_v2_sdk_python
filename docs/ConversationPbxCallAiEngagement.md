# ConversationPbxCallAiEngagement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_name** | **str** | Display name of the AI agent | [optional] 
**agent_uuid** | **str** | UUID of the AI agent configuration used | [optional] 
**cost** | [**ConversationPbxCallAiCost**](ConversationPbxCallAiCost.md) |  | [optional] 
**ended_at_dts** | **str** | Timestamp when the AI engagement ended | [optional] 
**engagement_type** | **str** | Type of AI engagement | [optional] 
**session_uuid** | **str** | Unique identifier for this AI engagement session | [optional] 
**started_at_dts** | **str** | Timestamp when the AI engagement started | [optional] 
**status** | **str** | Status of the AI engagement | [optional] 
**tool_calls** | [**list[ConversationPbxCallAiToolCall]**](ConversationPbxCallAiToolCall.md) | List of tool calls made by the AI agent during this engagement | [optional] 
**whispers** | [**list[ConversationPbxCallAiWhisper]**](ConversationPbxCallAiWhisper.md) | List of coaching whispers sent during this engagement | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


