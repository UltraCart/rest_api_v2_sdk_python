# AddLibraryItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[LibraryItemAttribute]**](LibraryItemAttribute.md) | Attributes associated with the library item to contain additional configuration. | [optional] 
**cjson** | **str** | Cjson to be added to library | [optional] 
**content_type** | **str** | flow, campaign, cjson, email, transactional_email, postcard or upsell | [optional] 
**description** | **str** | description of library item | [optional] 
**email_name** | **str** | Required if content_type is transactional_email. This is the name of the email template (html, not text).  This name should have a .vm file extension.  An example is auto_order_cancel_html.vm | [optional] 
**email_path** | **str** | Required if content_type is transactional_email. This is the full path to the email template stored in the file system.  This defines which StoreFront contains the desired email template.  An example is /themes/Elements/core/emails/auto_order_cancel_html.vm | [optional] 
**screenshots** | [**[LibraryItemScreenshot]**](LibraryItemScreenshot.md) | Screenshot urls for display | [optional] 
**storefront_oid** | **int** | StoreFront oid where content originates necessary for tracking down relative assets | [optional] 
**title** | **str** | title of library item, usually the name of the flow or campaign, or description of cjson | [optional] 
**upsell_offer_oid** | **int** | Required if content_type is upsell. This is object identifier of a StoreFront Upsell Offer. | [optional] 
**uuid** | **str** | UUID of communication flow, campaign, email, postcard, or null if this item is something else. transactional_email do not have a uuid because they are singleton objects within a storefront and easily identifiable by name | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


