# ApplyLibraryItemResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | Cjson from library item, only populated if this library item was a cjson snippet | [optional] 
**content_type** | **str** | flow, campaign, cjson, or upsell | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**storefront_oid** | **int** | StoreFront oid where content originates necessary for tracking down relative assets | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**title** | **str** | title of library item, usually the name of the flow or campaign, or description of cjson | [optional] 
**uuid** | **str** | UUID of communication flow or campaign if this library item was a campaign or flow | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


