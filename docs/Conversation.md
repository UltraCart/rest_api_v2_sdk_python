# Conversation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_language_iso_code** | **str** | The base language iso code for the StoreFront that everything is translated into | [optional] 
**closed** | **bool** |  | [optional] 
**conversation_arn** | **str** |  | [optional] 
**conversation_uuid** | **str** |  | [optional] 
**customer_first_message_unresponded_to_dts** | **str** | Date/time of the first customer message that is unresponded to. | [optional] 
**last_conversation_message_body** | **str** |  | [optional] 
**last_conversation_participant_arn** | **str** |  | [optional] 
**last_conversation_participant_name** | **str** |  | [optional] 
**last_interactive_message_dts** | **str** | Last interactive message date/time | [optional] 
**last_message_dts** | **str** | Last message date/time | [optional] 
**medium** | **str** | The communication medium of the customer. | [optional] 
**merchant_id** | **str** |  | [optional] 
**message_count** | **int** |  | [optional] 
**messages** | [**[ConversationMessage]**](ConversationMessage.md) |  | [optional] 
**participants** | [**[ConversationParticipant]**](ConversationParticipant.md) |  | [optional] 
**sentiment** | [**ConversationSentiment**](ConversationSentiment.md) |  | [optional] 
**start_dts** | **str** | Start of the conversation date/time | [optional] 
**unread_messages** | **bool** |  | [optional] 
**virtual_agent** | **bool** | True if a virtual agent answered the conversation | [optional] 
**virtual_agent_cost** | **float** | The cost of this conversation performed by the virtual agent | [optional] 
**visible** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


