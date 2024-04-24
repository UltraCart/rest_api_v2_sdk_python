# ConversationPbxQueue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announce_queue_position** | **bool** | If true, the customer is told their queue position upon entering the queue | [optional] 
**conversation_pbx_queue_uuid** | **str** | Conversation Pbx Queue unique identifier | [optional] 
**conversation_voicemail_mailbox_uuid** | **str** | The voicemail mailbox associated with this queue | [optional] 
**hold_conversation_pbx_audio_uuid** | **str** | The audio to play while holding in a queue | [optional] 
**max_hold_seconds** | **int** | The maximum number of seconds for a customer to hold in a queue | [optional] 
**members** | [**ConversationPbxQueueMembers**](ConversationPbxQueueMembers.md) |  | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**name** | **str** | Name of queue | [optional] 
**no_agent_available_play_audio_uuid** | **str** | When no agent is available after the max_hold_seconds, say this | [optional] 
**no_agent_available_say** | **str** | When no agent is available after the max_hold_seconds, say this | [optional] 
**no_agent_available_say_voice** | **str** | The type of voice used to say text when no agent is available | [optional] 
**play_audio_uuid** | **str** | Audio played when customer enters a queue | [optional] 
**record_call** | **bool** | If true, any calls in this queue are recorded | [optional] 
**say** | **str** | Say text when a customer enters queue | [optional] 
**say_voice** | **str** | The type of voice to use when say text is spoken | [optional] 
**twilio_taskrouter_workflow_sid** | **str** | Twilio taskrouter workflow sid | [optional] 
**twilio_workspace_queue_sid** | **str** | Twilio workspace queue sid | [optional] 
**voicemail** | **bool** | If true, this queue has a voicemail associated with it | [optional] 
**wait_critical_seconds** | **int** | Wait time in seconds before critical | [optional] 
**wait_warning_seconds** | **int** | Wait time in seconds before warning | [optional] 
**wrap_up_seconds** | **int** | Wrap up time in seconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


