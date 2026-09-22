# SfvbItemResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[SfvbItemAttribute]**](SfvbItemAttribute.md) | Every attribute a template declares for this item plus every one stored on it, so the list answers what can be set as well as what is set. | [optional] 
**description** | **str** | What an itemdescription element renders, the item&#39;s extended description.  Like title this is the catalog&#39;s own field rather than a storefront copy of it. | [optional] 
**groups** | **[str]** | The page paths this item is assigned to on this storefront.  The templates behind those pages are what the attribute and image declarations were reconciled against, so an empty list is why an item can report no declared attributes at all. | [optional] 
**merchant_item_id** | **str** | The item id a storefront carries, and the one data-context-item-id holds. | [optional] 
**merchant_item_oid** | **int** | The item&#39;s internal oid, which appears nowhere on a rendered storefront. | [optional] 
**multimedia** | [**[SfvbItemMultimedia]**](SfvbItemMultimedia.md) | Every image slot a template declares plus every image attached to the item. | [optional] 
**seo** | [**SfvbItemSeo**](SfvbItemSeo.md) |  | [optional] 
**title** | **str** | What an itemtitle element renders.  This is the item&#39;s short description in the catalog, not a storefront only field, so changing it changes the item everywhere. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


