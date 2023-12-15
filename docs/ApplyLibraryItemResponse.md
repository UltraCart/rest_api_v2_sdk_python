# ApplyLibraryItemResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[LibraryItemAttribute]**](LibraryItemAttribute.md) | Attributes from the library item | [optional] 
**cjson** | **str** | Cjson from library item, only populated if this library item was a cjson snippet or marketing email (not transactional) | [optional] 
**content_type** | **str** | flow, campaign, cjson, upsell, postcard, transactional_email or email | [optional] 
**email_template_vm_path** | **str** | If a marketing email was applied, this is the path to the template encapsulating the cjson.  This is needed for the UltraCart UI. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**storefront_oid** | **int** | StoreFront oid where content originates necessary for tracking down relative assets | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**title** | **str** | title of library item, usually the name of the flow or campaign, or description of cjson | [optional] 
**uuid** | **str** | UUID of marketing email or communication flow/campaign if this library item was an email, campaign or flow | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


