# SfvbMenu


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The menu&#39;s code, which is the value a menu element&#39;s menuName refers to.  Compare case insensitively. | [optional] 
**hash_sha256** | **str** | Content hash of the menu as stored.  Send it back as If-Match when writing. | [optional] 
**item_count** | **int** | How many entries the menu holds in total, counting every level of the tree. | [optional] 
**items** | [**[SfvbMenuItem]**](SfvbMenuItem.md) | The menu&#39;s entries, in the order they render.  Omitted from the list endpoint, which returns each menu&#39;s identity and counts only. | [optional] 
**title** | **str** | The menu&#39;s own label, shown in the store admin rather than on the storefront.  Trimmed to 250 characters. | [optional] 
**unconfigured** | **bool** | True when a template names this code but no menu has been created for it.  Such a code renders an empty list today.  Write it to create it. | [optional] 
**undeclared** | **bool** | True when no template on the storefront names this code.  The menu is stored and editable, but nothing renders it, which usually means a menu element&#39;s menuName is misspelled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


