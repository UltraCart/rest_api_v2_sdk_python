# SfvbItemChildCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copied_cost** | **str** | The cost copied from the parent. | [optional] 
**copied_dimensions** | **str** | Length, width and height copied from the parent. | [optional] 
**copied_folder_id** | **int** | The parent&#39;s item folder the new item is filed in, 0 for the top. | [optional] 
**copied_weight** | **str** | The weight copied from the parent. | [optional] 
**description** | **str** | The new item&#39;s description. | [optional] 
**dry_run** | **bool** | True when nothing was created. | [optional] 
**merchant_item_id** | **str** | The new item&#39;s id. | [optional] 
**merchant_item_oid** | **int** | The new item&#39;s oid.  Absent on a dry run. | [optional] 
**next** | **str** | What to do next. | [optional] 
**parent** | [**SfvbItemVariationChild**](SfvbItemVariationChild.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


