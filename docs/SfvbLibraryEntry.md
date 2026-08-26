# SfvbLibraryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarked** | **bool** | True when the calling user has bookmarked this entry. | [optional] 
**cjson** | **str** | The fragment&#39;s CJSON.  Omitted from search results to keep them terse; fetch a single entry to get it. | [optional] 
**description** | **str** | What this fragment is for. | [optional] 
**library_oid** | **int** | Library entry oid. | [optional] 
**name** | **str** | Entry name. | [optional] 
**owned** | **bool** | True when the calling user owns this entry. | [optional] 
**referenced_files** | **[str]** | Storefront file paths this fragment references.  Installing the fragment copies them into the storefront; reading it does not. | [optional] 
**screenshot_key** | **str** | S3 listing key for the large screenshot, when one has been generated. | [optional] 
**share_with_account** | **bool** | True when the entry is shared across the merchant account. | [optional] 
**thumbnail_key** | **str** | S3 listing key for the medium thumbnail, when one has been generated.  Thumbnails are produced asynchronously and can lag a save by a minute or two. | [optional] 
**widget_type** | **str** | Element type at the root of the fragment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


