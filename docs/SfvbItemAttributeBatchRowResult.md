# SfvbItemAttributeBatchRowResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_present** | **bool** | Whether the item had the attribute before this batch. | [optional] 
**current_sha256** | **str** | The hash of the value before this batch.  Send it back with the row to apply. | [optional] 
**current_value** | **str** | The value before this batch, for a backup.  Empty when the item has no such attribute. | [optional] 
**merchant_item_id** | **str** | The item&#39;s merchant item id.  Absent when not_found. | [optional] 
**merchant_item_oid** | **int** | The item.  Absent when not_found. | [optional] 
**message** | **str** | Why a row is invalid, stale or error. | [optional] 
**name** | **str** | The attribute name as sent. | [optional] 
**result** | **str** | change or unchanged from a dry run, updated after an apply, stale (the value differs from expected_value or changed since the dry run), not_found, invalid, or error when the item could not be saved. | [optional] 
**row** | **int** | The row&#39;s position in the request, from 1. | [optional] 
**type** | **str** | The type the value is checked and stored as - the declaring template&#39;s, else the one sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


