# ConversationAgentTestSessionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_profile_oid** | **int** | Customer profile to converse as.  The cart is established as a soft login for this customer, so the agent sees their real order history. | [optional] 
**question** | **str** | Optional opening question, the same way a customer types one before joining the queue. | [optional] 
**queue_name** | **str** | Webchat queue to join.  The agent is selected explicitly, so this does not have to be a queue the agent is assigned to. | [optional] 
**storefront_host_name** | **str** | Host name of the storefront to test against, with no protocol prefix.  Determines which catalog the agent searches. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


