# ConversationPbxCall

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_sid** | **str** | Twilio account SID | [optional] 
**agents** | [**list[ConversationPbxCallAgent]**](ConversationPbxCallAgent.md) | List of agents who participated in this call | [optional] 
**ai_agent_engagements** | [**list[ConversationPbxCallAiEngagement]**](ConversationPbxCallAiEngagement.md) | List of AI agent engagements during the call | [optional] 
**call_sid** | **str** | Twilio call SID for the primary (customer) call leg | [optional] 
**call_uuid** | **str** | Unique identifier for this call record | [optional] 
**caller** | [**ConversationPbxCallCaller**](ConversationPbxCallCaller.md) |  | [optional] 
**conference_sid** | **str** | Twilio conference SID if this call used conferencing | [optional] 
**created_at_dts** | **str** | Timestamp when the call record was created | [optional] 
**customer_name** | **str** | Customer name associated with this call | [optional] 
**customer_profile_oid** | **str** | UltraCart customer profile OID if the caller was matched to a customer | [optional] 
**disposition** | **str** | Call disposition describing how the call ended | [optional] 
**email** | **str** | Email address of the caller if known | [optional] 
**financial** | [**ConversationPbxCallFinancial**](ConversationPbxCallFinancial.md) |  | [optional] 
**holds** | [**list[ConversationPbxCallHold]**](ConversationPbxCallHold.md) | List of hold events during the call | [optional] 
**merchant_id** | **str** | Merchant identifier | [optional] 
**recording_sids** | **list[str]** | List of all Twilio recording SIDs associated with this call | [optional] 
**recordings** | [**list[ConversationPbxCallRecording]**](ConversationPbxCallRecording.md) | List of recordings made during the call | [optional] 
**routing** | [**ConversationPbxCallRouting**](ConversationPbxCallRouting.md) |  | [optional] 
**status** | **str** | Final status of the call | [optional] 
**timeline** | [**ConversationPbxCallTimeline**](ConversationPbxCallTimeline.md) |  | [optional] 
**transfers** | [**list[ConversationPbxCallTransfer]**](ConversationPbxCallTransfer.md) | List of transfer events during the call | [optional] 
**updated_at_dts** | **str** | Timestamp when the call record was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


