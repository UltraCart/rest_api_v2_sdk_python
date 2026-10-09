# SfvbItemRelatedItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_item_id** | **str** | The related item.  On a write, send this or merchant_item_oid. | [optional] 
**merchant_item_oid** | **int** | The related item&#39;s oid. | [optional] 
**type** | **str** | user (the default on a write), addon or complementary.  system marks one UltraCart calculated and other a kind this API does not change.  Both are read only and kept by a write. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


