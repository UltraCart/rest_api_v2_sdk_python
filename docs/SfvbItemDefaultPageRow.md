# SfvbItemDefaultPageRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_sha256** | **str** | The dry run&#39;s current_sha256 for the item.  Required on an apply. | [optional] 
**expected_current_path** | **str** | Dry run only - the default page the row expects now.  A different default makes the row stale. | [optional] 
**merchant_item_id** | **str** | The item&#39;s id.  Send this or merchant_item_oid. | [optional] 
**merchant_item_oid** | **int** | The item&#39;s oid.  Required on an apply. | [optional] 
**page_oid** | **int** | The page to make the default, by oid.  Required on an apply. | [optional] 
**page_path** | **str** | The page to make the default, by path.  Send this or page_oid. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


