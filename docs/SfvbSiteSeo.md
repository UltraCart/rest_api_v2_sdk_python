# SfvbSiteSeo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_needed** | **bool** | On a change, true when it needs an approved site_seo.change request. | [optional] 
**canonical** | **bool** | True when pages output canonical links. | [optional] 
**changed** | **bool** | On a change, true when anything was saved, or would be on a dry run. | [optional] 
**changes** | [**[SfvbSiteSeoChange]**](SfvbSiteSeoChange.md) | On a change, each switch it changed, or would change on a dry run. | [optional] 
**description** | **str** | The default meta description, the storefrontSEODescription site attribute. | [optional] 
**dry_run** | **bool** | True when nothing was saved because the request was a dry run. | [optional] 
**hash_sha256** | **str** | The hash of the three switches.  Send it as If-Match on a change. | [optional] 
**keywords** | **str** | The default meta keywords, the storefrontSEOKeywords site attribute. | [optional] 
**notes** | **[str]** | What a person should know about these settings. | [optional] 
**prevent_indexing** | **bool** | True when every page tells search engines not to index it.  For a development store only. | [optional] 
**schema_org** | **bool** | True when pages output Schema.org structured data. | [optional] 
**storefront_oid** | **int** | The storefront. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


