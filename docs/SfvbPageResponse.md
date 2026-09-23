# SfvbPageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[SfvbPageAttribute]**](SfvbPageAttribute.md) | Every attribute this page has, including ones a template declares but nothing has set yet.  These are what the pageattribute element renders.  Sorted by name. | [optional] 
**description** | **str** | The page description, the text a page template renders as the page&#39;s description.  Omitted when empty. | [optional] 
**exclude_from_sitemap** | **bool** | True when the page is left out of the sitemap and marked noindex. | [optional] 
**group_template** | **str** | Template file that renders the page itself, a bare .vm name found anywhere in the active theme. | [optional] 
**item_template** | **str** | Template file that renders the item pages under this page. | [optional] 
**multimedia** | [**[SfvbPageMultimedia]**](SfvbPageMultimedia.md) | The page&#39;s images, including codes a template declares but nothing has attached yet.  These are what the pageimage element renders - the default image when pageImageCode is empty, otherwise the image with that code.  The default image comes first. | [optional] 
**path** | **str** | The page path, normalized to begin and end with a slash. | [optional] 
**title** | **str** | The page title. | [optional] 
**visible** | **bool** | False when the page is hidden.  A hidden page answers 404 to shoppers. | [optional] 
**visible_dts** | **str** | When set, the page stays hidden until this time (ISO 8601, UTC). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


