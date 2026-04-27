# ConversationAgentStatusTimelineResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_events** | [**[ConversationAgentCallEvent]**](ConversationAgentCallEvent.md) | PBX call records for the agent on the requested day | [optional] 
**chat_events** | [**[ConversationAgentChatEvent]**](ConversationAgentChatEvent.md) | Chat conversations for the agent on the requested day | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**status_events** | [**[ConversationAgentStatusEvent]**](ConversationAgentStatusEvent.md) | Status transitions for the agent on the requested day | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**summary** | [**TimelineSummary**](TimelineSummary.md) |  | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


