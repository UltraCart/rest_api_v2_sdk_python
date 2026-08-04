# ConversationAgentStatusSummaryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**[AgentSummary]**](AgentSummary.md) | Per-agent enriched summary (status totals + activity metrics) | [optional] 
**avg_available_pct** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**status_breakdown** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total seconds-in-status across all agents, keyed by status name | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**total_agents** | **int** | Distinct agents with at least one transition in the range | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


