# SfvbThemeDuplicateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | Directory name for the new theme under /themes/.  Letters and numbers, one path segment.  Used verbatim - anything that is not already a valid directory name is refused rather than adjusted, because this call does not return the new theme&#39;s oid and you find your copy by matching the target_path you asked for.  Must not already exist - a collision is refused rather than resolved, because silently creating a differently named theme leaves you unsure what you made. | [optional] 
**target_storefront_oid** | **int** | Storefront to create the copy on.  Defaults to the storefront in the path.  Supply it only when copying a theme between storefronts you own. | [optional] 
**theme_name** | **str** | Ignored.  A theme is named by its settings.json themeName, which the copy keeps from the source, so the copy has the source&#39;s name.  Edit themeName in the copy&#39;s settings.json to rename it.  Kept so existing callers still work. | [optional] 
**upgrade_to_version** | **str** | Upgrade the copy to this theme version after copying it, as the admin&#39;s Duplicate and Upgrade does.  Only the copy is upgraded - the source theme is never touched.  Must be one of the available_versions from getSfvbThemeUpgradeCheck, which also predicts the merge conflicts.  Omit for a plain copy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


