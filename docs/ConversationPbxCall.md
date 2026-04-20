# ConversationPbxCall


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_sid** | **str** | Twilio account SID | [optional] 
**agents** | [**[ConversationPbxCallAgent]**](ConversationPbxCallAgent.md) | List of agents who participated in this call | [optional] 
**ai_agent_engagements** | [**[ConversationPbxCallAiEngagement]**](ConversationPbxCallAiEngagement.md) | List of AI agent engagements during the call | [optional] 
**ai_summary** | [**ConversationPbxCallAiSummary**](ConversationPbxCallAiSummary.md) |  | [optional] 
**call_sid** | **str** | Twilio call SID for the primary (customer) call leg | [optional] 
**call_uuid** | **str** | Unique identifier for this call record | [optional] 
**caller** | [**ConversationPbxCallCaller**](ConversationPbxCallCaller.md) |  | [optional] 
**conference_sid** | **str** | Twilio conference SID if this call used conferencing | [optional] 
**context_merchant_id** | **str** | Optional child merchant ID this call is attributed to. Null &#x3D; no child attribution (parent-level call). | [optional] 
**created_at_dts** | **str** | Timestamp when the call record was created | [optional] 
**customer_name** | **str** | Customer name associated with this call | [optional] 
**customer_profile_oid** | **str** | UltraCart customer profile OID if the caller was matched to a customer | [optional] 
**disposition** | **str** | Call disposition describing how the call ended | [optional] 
**email** | **str** | Email address of the caller if known | [optional] 
**financial** | [**ConversationPbxCallFinancial**](ConversationPbxCallFinancial.md) |  | [optional] 
**holds** | [**[ConversationPbxCallHold]**](ConversationPbxCallHold.md) | List of hold events during the call | [optional] 
**merchant_id** | **str** | Merchant identifier | [optional] 
**recording_sids** | **[str]** | List of all Twilio recording SIDs associated with this call | [optional] 
**recordings** | [**[ConversationPbxCallRecording]**](ConversationPbxCallRecording.md) | List of recordings made during the call | [optional] 
**routing** | [**ConversationPbxCallRouting**](ConversationPbxCallRouting.md) |  | [optional] 
**status** | **str** | Final status of the call | [optional] 
**timeline** | [**ConversationPbxCallTimeline**](ConversationPbxCallTimeline.md) |  | [optional] 
**transfers** | [**[ConversationPbxCallTransfer]**](ConversationPbxCallTransfer.md) | List of transfer events during the call | [optional] 
**updated_at_dts** | **str** | Timestamp when the call record was last updated | [optional] 
**zoho_desk_ticket_id** | **str** | Zoho Desk ticket ID if a ticket was created for this call | [optional] 
**zoho_desk_ticket_url** | **str** | URL to the Zoho Desk ticket if a ticket was created for this call | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


