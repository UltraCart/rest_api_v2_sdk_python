# BulkJobRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Mutation mode - insert (create only) or upsert (create or update). Defaults to insert. This is always a mutation verb â€” the bulk surface writes only and has no read / query mode. upsert is currently supported for customer only. | [optional] 
**s3_key** | **str** | The s3_key returned by the upload-url endpoint | [optional] 
**webhook_secret** | **str** | Optional shared secret echoed in the completion POST&#39;s Authorization header | [optional] 
**webhook_url** | **str** | Optional URL to POST once, on completion | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


