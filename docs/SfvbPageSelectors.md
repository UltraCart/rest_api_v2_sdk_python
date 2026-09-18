# SfvbPageSelectors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog_post_selectors** | [**[SfvbPageBlogPostSelector]**](SfvbPageBlogPostSelector.md) | The conditions that choose the page&#39;s blog posts. | [optional] 
**item_selectors** | [**[SfvbPageItemSelector]**](SfvbPageItemSelector.md) | The conditions that choose the page&#39;s items.  While there are any, the page&#39;s items are recalculated from them and cannot be assigned by hand. | [optional] 
**match_all_blog_post_selectors** | **bool** | True when a blog post must meet every blog post selector, false when any one is enough. | [optional] 
**match_all_item_selectors** | **bool** | True when an item must meet every item selector, false when meeting any one is enough. | [optional] 
**path** | **str** | The page path.  Read only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


