# SfvbPageCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The page description, for templates that show one. | [optional] 
**exclude_from_sitemap** | **bool** | Leave the page out of the sitemap and mark it noindex.  Usual for ad landing pages. | [optional] 
**group_template** | **str** | Template that renders the page, a name from the template list.  When omitted the page inherits its parent&#39;s templates, or catalog_group.vm directly under the root. | [optional] 
**item_template** | **str** | Template that renders the item pages under this page.  Inherited or defaulted like group_template. | [optional] 
**page_type** | **str** | S for a static page, D for a dynamic one.  Defaults to D, as in the admin. | [optional] 
**path** | **str** | Path of the new page, for example /lp/spring-sale/.  The parent page must already exist, and the last part may only contain letters, digits, hyphens and underscores. | [optional] 
**title** | **str** | The page title. | [optional] 
**visible** | **bool** | False creates the page hidden, so it answers 404 to shoppers until it is shown. | [optional] 
**visible_dts** | **str** | Keep the page hidden until this time (ISO 8601). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


