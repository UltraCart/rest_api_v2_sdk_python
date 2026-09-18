# SfvbPageSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog_post_template** | **str** | Template that renders the blog posts under this page. | [optional] 
**description** | **str** | The page description.  Null or empty clears it. | [optional] 
**exclude_from_sitemap** | **bool** | Leave the page out of the sitemap and mark it noindex. | [optional] 
**group_template** | **str** | Template that renders the page, a name from the template list. | [optional] 
**item_template** | **str** | Template that renders the item pages under this page. | [optional] 
**items_per_page** | **int** | Items per page on a template that paginates.  Null returns to the template&#39;s default. | [optional] 
**page_type** | **str** | S for a static page, D for a dynamic one. | [optional] 
**review_template** | **str** | Template that renders the item review pages under this page. | [optional] 
**sort_order** | **int** | Position among its siblings when the parent sorts child pages by a custom order.  Null clears it. | [optional] 
**sort_order_child_groups** | **str** | How the pages under this one are ordered.  TA or TD by title, DA or DD by description, C custom. | [optional] 
**sort_order_child_items** | **str** | How the page&#39;s items are ordered.  IA or ID by item id, DA or DD by description, SA or SD by manufacturer SKU, PA or PD by price, RA or RD by review, NA or ND by inventory, C custom. | [optional] 
**title** | **str** | The page title. | [optional] 
**visible** | **bool** | False hides the page, so it answers 404 to shoppers.  The root page cannot be hidden. | [optional] 
**visible_dts** | **str** | Keep the page hidden until this time (ISO 8601).  Null or empty clears it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


