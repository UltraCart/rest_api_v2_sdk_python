# SfvbBlogPostDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_comments** | **bool** | Whether shoppers may comment. | [optional] 
**author** | **str** | The post author. | [optional] 
**blog_post_oid** | **int** | The blog post&#39;s oid.  This is what a page&#39;s blog post assignment names. | [optional] 
**body** | **str** | The post body as HTML, exactly as stored. | [optional] 
**created_dts** | **str** | When the post was created (ISO 8601, UTC). | [optional] 
**excerpt** | **str** | The post excerpt as HTML, exactly as stored. | [optional] 
**images** | [**[SfvbBlogPostImage]**](SfvbBlogPostImage.md) | The post&#39;s images, the default image first. | [optional] 
**last_modified_dts** | **str** | When the post was last changed (ISO 8601, UTC), or null if it never was. | [optional] 
**publication_dts** | **str** | When the post is published (ISO 8601, UTC), or null for a draft. | [optional] 
**tags** | **[str]** | The post&#39;s tags. | [optional] 
**title** | **str** | The post title. | [optional] 
**unassigned** | **bool** | True when no page shows this post yet. | [optional] 
**url_part** | **str** | The post&#39;s name in its URL. | [optional] 
**view_url** | **str** | The post&#39;s address on the storefront, or null until a page shows it. | [optional] 
**visibility** | **str** | P public, L logged in customers only, D draft. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


