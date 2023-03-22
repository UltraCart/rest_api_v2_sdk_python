# ReportExecuteQueriesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_uuid** | **str** | Unique UUID assigned to this client during the auth.  This will be used to locate the websocket connect id. | [optional] 
**connection_id** | **str** | The websocket connection id that should receive back notices of query completion. | [optional] 
**default_dataset_id** | **str** |  | [optional] 
**default_project_id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**queries** | [**list[ReportDataSetQuery]**](ReportDataSetQuery.md) | An array of queries that we want the lambda function to execute. | [optional] 
**security_level** | **str** | Security level to execute report under | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


