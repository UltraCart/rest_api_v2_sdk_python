# SfvbItemAttributeBatchRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_sha256** | **str** | The current_sha256 the dry run answered for this row.  Required to apply; a row whose value changed since is skipped as stale. | [optional] 
**expected_value** | **str** | For a dry run, the value the caller believes the item holds now.  A different current value makes the row stale. | [optional] 
**merchant_item_id** | **str** | The item by its merchant item id, for a dry run.  Send this or merchant_item_oid, not both. | [optional] 
**merchant_item_oid** | **int** | The item.  Required to apply; the dry run answers it for a row that named merchant_item_id. | [optional] 
**name** | **str** | The attribute name, matched without regard to case. | [optional] 
**type** | **str** | The attribute type, used only when no template on the item&#39;s pages declares the name. | [optional] 
**value** | **str** | The new value.  An empty string clears the attribute. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


