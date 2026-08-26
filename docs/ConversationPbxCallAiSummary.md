# ConversationPbxCallAiSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_items** | **[str]** | Action items identified during the call | [optional] 
**call_category** | **str** | Category of the call (e.g. support, sales, billing) | [optional] 
**completion_tokens** | **int** | Number of output tokens used to generate the summary | [optional] 
**cost** | **float** | Cost of generating the summary in the specified currency | [optional] 
**cost_currency** | **str** | Currency code for the summary cost (always USD) | [optional] 
**generated_at_dts** | **str** | Timestamp when the summary was generated | [optional] 
**key_topics** | **[str]** | Key topics discussed during the call | [optional] 
**model** | **str** | AI model used to generate the summary (e.g. grok-4.1-fast) | [optional] 
**prompt_tokens** | **int** | Number of input tokens used to generate the summary | [optional] 
**sentiment** | **str** | Overall sentiment of the call | [optional] 
**summary** | **str** | 2-3 sentence synopsis of the call | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


