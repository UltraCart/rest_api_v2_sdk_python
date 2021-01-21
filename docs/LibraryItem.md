# LibraryItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**list[LibraryItemAsset]**](LibraryItemAsset.md) |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**content** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**industries** | **list[str]** |  | [optional] 
**library_item_oid** | **int** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**my_purchased_version** | **int** | If this is a public item and the merchant has already purchased it, this is their version.  If not yet purchased, this will be zero.  This value will only be populated during a searchPublicItems() call. | [optional] 
**original_object_id** | **str** | This id points to the original object that was added to the library. For flows and campaigns, this is a uuid string.  For upsells, it is an oid integer.  For transactional_emails, it is an email name. | [optional] 
**price** | **float** | The price of the published item.  Null for any private library items. | [optional] 
**price_formatted** | **str** | The formatted price of the published item.  Null for any private library items. | [optional] 
**published** | **bool** | True if this library item is a published item (not source) | [optional] 
**published_dts** | **object** | The timestamp of the last published version | [optional] 
**published_from_library_item_oid** | **int** | The source item used to publish this item.  This allows for comparisons between source and published | [optional] 
**published_meta** | [**LibraryItemPublishedMeta**](LibraryItemPublishedMeta.md) |  | [optional] 
**published_version** | **int** | The source version when this item was published.  This allows for out-of-date alerts to be shown when there is a difference between source and published | [optional] 
**purchased** | **bool** | True if this library item has been purchased | [optional] 
**purchased_from_library_item_oid** | **int** | The published item that was purchased to make this item.  This allows for comparisons between published and purchased | [optional] 
**purchased_meta** | [**LibraryItemPurchasedMeta**](LibraryItemPurchasedMeta.md) |  | [optional] 
**purchased_version** | **int** | The published version when this item was purchased.  This allows for out-of-date alerts to be shown when there is a difference between published and purchased | [optional] 
**rejected** | **bool** | Any published library reviewed by UltraCart staff for malicious or inappropriate content will have this flag set to true.  This is always false for non-published items | [optional] 
**rejected_reason** | **str** | Any rejected published item will have this field populated with the reason. | [optional] 
**release_notes** | **str** | Release notes specific to each published version and only appearing on public items. | [optional] 
**release_version** | **int** | This counter records how many times a library item has been published.  This is used to show version history. | [optional] 
**reviewed** | **bool** | Any published library items must be reviewed by UltraCart staff for malicious content.  This flag shows the status of that review.  This is always false for non-published items | [optional] 
**reviewed_dts** | **object** | This is the timestamp for a published items formal review by UltraCart staff for malicious content. | [optional] 
**screenshots** | [**list[LibraryItemScreenshot]**](LibraryItemScreenshot.md) |  | [optional] 
**share_with_accounts** | [**list[LibraryItemAccount]**](LibraryItemAccount.md) |  | [optional] 
**share_with_other_emails** | [**list[LibraryItemEmail]**](LibraryItemEmail.md) |  | [optional] 
**shared** | **bool** | True if this item is shared from another merchant account | [optional] 
**source** | **bool** | True if this library item has been published | [optional] 
**source_to_library_item_oid** | **int** | This oid points to the published library item, if there is one. | [optional] 
**source_version** | **int** | The version of this item.  Increment every time the item is saved. | [optional] 
**style** | **str** |  | [optional] 
**times_purchased** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**under_review** | **bool** | True if this library item was published but is awaiting review from UltraCart staff. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


