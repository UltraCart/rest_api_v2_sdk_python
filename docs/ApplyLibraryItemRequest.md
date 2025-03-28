# ApplyLibraryItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_uuid** | **str** | Normal emails are applied to an existing email object, so when requesting a library item to be applied to an email, supply the email uuid.  This is only for normal emails.  Transactional emails do not have a uuid. | [optional] 
**library_item_oid** | **int** | Library item oid that you wish to apply to the given StoreFront | [optional] 
**postcard_uuid** | **str** | The postcard uuid you wish to apply to a given StoreFront. | [optional] 
**storefront_oid** | **int** | StoreFront oid where content originates necessary for tracking down relative assets | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


