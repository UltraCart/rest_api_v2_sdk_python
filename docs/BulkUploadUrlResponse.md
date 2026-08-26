# BulkUploadUrlResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**expires_at** | **str** | When the presigned URL expires | [optional] 
**max_records** | **int** | Per-job record cap | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**s3_key** | **str** | Opaque reference to pass back on POST /rest/v2/bulk/{object} | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**upload_url** | **str** | Presigned S3 PUT URL (short-lived) | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


