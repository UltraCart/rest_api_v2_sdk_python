# SfvbSitemapsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The host the sitemaps are built for. | [optional] 
**notes** | **[str]** | What a person should know about these sitemaps, such as when they are rebuilt. | [optional] 
**prevent_indexing** | **bool** | True when the storefront&#39;s Prevent Indexing setting is on.  The sitemaps are still served, but every page tells search engines not to index it. | [optional] 
**robots_txt** | [**SfvbRobotsTxt**](SfvbRobotsTxt.md) |  | [optional] 
**sitemaps** | [**[SfvbSitemap]**](SfvbSitemap.md) | The sitemaps that exist, sitemaps.org first.  Empty until the nightly build has run. | [optional] 
**storefront_oid** | **int** | The storefront. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


