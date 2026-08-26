# SfvbTheme


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True when this theme is the one serving live traffic.  Writing to an active theme requires the sfvb_publish scope. | [optional] 
**description** | **str** | What the theme is, where the author supplied a description. | [optional] 
**fs_directory_oid** | **int** | Oid of the theme root directory in the storefront file system. | [optional] 
**path** | **str** | Root path of the theme in the storefront file system, for example /themes/mytheme/ | [optional] 
**storefront_oid** | **int** | StoreFront oid this theme belongs to. | [optional] 
**theme_name** | **str** | Theme name. | [optional] 
**theme_oid** | **int** | StoreFront theme oid. | [optional] 
**upgrade_available** | **bool** | True when a newer version of this theme exists.  Relevant because an upgrade is what produces the merge conflicts that block activation. | [optional] 
**valid** | **bool** | False when the theme contains templates that failed validation.  Worth checking before choosing a theme to work in. | [optional] 
**version** | **str** | Theme version. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


