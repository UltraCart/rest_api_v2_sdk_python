# BulkRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | On an upsert success, whether the record was inserted or updated | [optional] 
**error_code** | **str** | Error code on a failed record | [optional] 
**error_message** | **str** | Human-readable detail on a failed record | [optional] 
**line_number** | **int** | Original NDJSON line number | [optional] 
**merchant_record_id** | **str** | The merchant-supplied dedupe key for this record | [optional] 
**status** | **str** | Per-record verdict | [optional] 
**uc_id** | **str** | UltraCart-side id created on success or matched on duplicate | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


