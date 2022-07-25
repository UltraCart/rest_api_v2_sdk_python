# ConversationWebsocketMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** | Conversation UUID if the websocket message is tied to a specific conversation | [optional] 
**event_conversation_closed** | [**Conversation**](Conversation.md) |  | [optional] 
**event_new_conversation** | [**Conversation**](Conversation.md) |  | [optional] 
**event_new_message** | [**Conversation**](Conversation.md) |  | [optional] 
**event_queue_position** | [**ConversationEventQueuePosition**](ConversationEventQueuePosition.md) |  | [optional] 
**event_type** | **str** | Type of event | [optional] 
**event_updated_message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**type** | **str** | Type of message | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


