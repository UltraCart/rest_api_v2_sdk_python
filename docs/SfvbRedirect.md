# SfvbRedirect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dts** | **str** | When SFVB created the rule, ISO 8601.  Empty for rules created in the admin. | [optional] 
**exclude_from_sitemap** | **bool** | Whether the source is left out of the generated sitemap. | [optional] 
**hash_sha256** | **str** | Send back as If-Match to update or delete the rule. | [optional] 
**modified_dts** | **str** | When SFVB last changed the rule, ISO 8601. | [optional] 
**note** | **str** | Why the rule exists. | [optional] 
**pinned_page_path** | **str** | When the rule is pinned to a page, that page&#39;s current path.  The target follows the page. | [optional] 
**redirect_id** | **int** | The rule&#39;s id. | [optional] 
**source** | **str** | The path the rule catches, as stored.  A trailing /* catches everything below it. | [optional] 
**status** | **str** | 301, 302 (to another site, admin rules only) or rewrite (an admin rule serving the target at the source with a 200).  Rules written through SFVB are always 301. | [optional] 
**target** | **str** | Where the rule sends the shopper. | [optional] 
**target_invalid** | **bool** | True when the target is a page or item that does not exist. | [optional] 
**target_invalid_message** | **str** | Why the target is invalid. | [optional] 
**type** | **str** | exact or pattern. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


