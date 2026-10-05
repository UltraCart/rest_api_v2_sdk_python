# SfvbLibraryEntryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The fragment, one widget and its children.  Not a whole container. | [optional] 
**description** | **str** | What the fragment is for, at most 1024 characters. | [optional] 
**name** | **str** | Entry name, at most 100 characters. | [optional] 
**parameters** | [**[SfvbLibraryParameter]**](SfvbLibraryParameter.md) | Named values the fragment expects its installer to supply. | [optional] 
**screenshot** | [**SfvbLibraryScreenshotRequest**](SfvbLibraryScreenshotRequest.md) |  | [optional] 
**share_with_account** | **bool** | True to let the other users on this merchant account see the published revision. | [optional] 
**taxonomy** | [**SfvbLibraryTaxonomy**](SfvbLibraryTaxonomy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


