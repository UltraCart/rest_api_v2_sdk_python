# SfvbSearchFacetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_facets** | **[str]** | After a change, the facets it changed. | [optional] 
**cost_price_points** | **[int]** | The Cost facet price breaks, smallest first. | [optional] 
**dry_run** | **bool** | True when nothing was saved. | [optional] 
**facets** | [**[SfvbSearchFacet]**](SfvbSearchFacet.md) | Every facet the storefront can offer, in the fixed order shoppers see them. | [optional] 
**hash_sha256** | **str** | Hash of the facets and price points.  Send it as If-Match on a change. | [optional] 
**price_points_changed** | **bool** | After a change, true when the price points changed. | [optional] 
**rebuild** | **str** | After a change, the search index rebuild it started.  none, quick (minutes, small catalogs), slow (the regular rebuild cycle) or failed (the change is saved but the rebuild could not be started; save again or contact support). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


