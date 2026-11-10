# SfvbItemPreorderChildrenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**[SfvbItemPreorderChildRow]**](SfvbItemPreorderChildRow.md) | The variations to change, 1 to 100, each named once. | [optional] 
**clear_eta** | **bool** | True to remove the ETA from every variation named.  Not with eta. | [optional] 
**eta** | **str** | The expected date for every variation named, YYYY-MM-DD.  Not with clear_eta. | [optional] 
**preorder** | **bool** | True to put the variations on pre-order, false to take them off.  Needs an approved item.preorder request when it changes any of them. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


