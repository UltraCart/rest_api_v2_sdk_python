# SfvbUpsellItemLogic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[SfvbUpsellItemLogicItem]**](SfvbUpsellItemLogicItem.md) | The items this logic looks at.  Every item id must exist on the merchant account. | [optional] 
**logic** | **str** | How items is read.  contains_any, contains_all, all, any or total.  Omitted or null means no item logic. | [optional] 
**total_quantity_comparison** | **int** | For total only.  The quantity the summed quantity is compared with. | [optional] 
**total_quantity_operator** | **str** | For total only.  The comparison applied to the summed quantity.  One of &lt;, &lt;&#x3D;, &#x3D;, &gt;&#x3D;, &gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


