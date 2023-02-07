# ConversationWebsocketMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_arn** | **str** | Conversation ARN | [optional] 
**conversation_uuid** | **str** | Conversation UUID if the websocket message is tied to a specific conversation | [optional] 
**event_add_coupon** | [**ConversationEventAddCoupon**](ConversationEventAddCoupon.md) |  | [optional] 
**event_add_item** | [**ConversationEventAddItem**](ConversationEventAddItem.md) |  | [optional] 
**event_conversation_closed** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_engage_customer** | [**ConversationWebchatQueueStatusQueueEntry**](ConversationWebchatQueueStatusQueueEntry.md) |  | [optional] 
**event_new_conversation** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_new_message** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_participant_join** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_participant_join_participant** | [**ConversationParticipant**](ConversationParticipant.md) |  | [optional] 
**event_participant_left** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_participant_left_participant** | [**ConversationParticipant**](ConversationParticipant.md) |  | [optional] 
**event_participant_update** | [**ConversationSummary**](ConversationSummary.md) |  | [optional] 
**event_queue_new_member** | [**ConversationWebchatQueueStatusQueueEntry**](ConversationWebchatQueueStatusQueueEntry.md) |  | [optional] 
**event_queue_position** | [**ConversationEventQueuePosition**](ConversationEventQueuePosition.md) |  | [optional] 
**event_queue_status_update** | [**ConversationWebchatQueueStatus**](ConversationWebchatQueueStatus.md) |  | [optional] 
**event_read_message** | [**ConversationEventReadMessage**](ConversationEventReadMessage.md) |  | [optional] 
**event_rrweb** | [**ConversationEventRRWeb**](ConversationEventRRWeb.md) |  | [optional] 
**event_type** | **str** | Type of event | [optional] 
**event_typing** | [**ConversationEventTyping**](ConversationEventTyping.md) |  | [optional] 
**event_updated_message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**event_webchat_context** | [**ConversationEventWebchatContext**](ConversationEventWebchatContext.md) |  | [optional] 
**message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**type** | **str** | Type of message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


