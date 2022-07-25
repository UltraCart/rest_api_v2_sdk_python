# ConversationWebsocketMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** | Conversation UUID if the websocket message is tied to a specific conversation | [optional] 
**event_conversation_closed** | [**Conversation**](Conversation.md) |  | [optional] 
**event_new_conversation** | [**Conversation**](Conversation.md) |  | [optional] 
**event_new_message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**event_queue_position** | [**ConversationEventQueuePosition**](ConversationEventQueuePosition.md) |  | [optional] 
**event_type** | **str** | Type of event | [optional] 
**event_updated_message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**type** | **str** | Type of message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


