# ReportDataSetPage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_uuid** | **str** | A unique identifier assigned to the data set that is returned. | [optional] 
**merchant_id** | **str** | Merchant that owns this data set | [optional] 
**next_page_token** | **str** |  | [optional] 
**next_start_index** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**row_count** | **int** |  | [optional] 
**rows** | [**[ReportDataSetRow]**](ReportDataSetRow.md) | Rows returned for the data set | [optional] 
**rows_s3_url** | **str** | Signed S3 URL where the page rows can be downloaded from | [optional] 
**start_index** | **int** | Zero based index of the starting row | [optional] 
**table_id** | **str** | The BigQuery destination table id that contains the result. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


