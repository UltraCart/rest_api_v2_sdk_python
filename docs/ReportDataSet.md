# ReportDataSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_query_uuid** | **str** | A unique identifier assigned to the data set query that is returned. | [optional] 
**data_set_uuid** | **str** | A unique identifier assigned to the data set that is returned. | [optional] 
**destination_table_id** | **str** | The BigQuery destination table id that contains the result. | [optional] 
**error_message** | **str** | Error message if the query failed. | [optional] 
**executed_sql** | **str** |  | [optional] 
**for_object_id** | **str** | An identifier that can be used to help match up the returned data set | [optional] 
**for_object_type** | **str** | The type of object this data set is for | [optional] 
**initial_pages** | [**[ReportDataSetPage]**](ReportDataSetPage.md) | Initial pages returned in the dataset | [optional] 
**max_results** | **int** | The total number of results | [optional] 
**merchant_id** | **str** | Merchant that owns this data set | [optional] 
**page_count** | **int** | The total number of pages in the result set | [optional] 
**page_size** | **int** | The size of the pages | [optional] 
**schema** | [**[ReportDataSetSchema]**](ReportDataSetSchema.md) | The schema associated with the data set. | [optional] 
**security_level** | **str** | Security level this dataset was read from. | [optional] 
**timezone** | **str** |  | [optional] 
**user_data** | **str** | Any other data that needs to be returned with the response to help the UI | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


