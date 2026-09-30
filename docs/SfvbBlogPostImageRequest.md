# SfvbBlogPostImageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog_post_multimedia_oid** | **int** | Detach only.  The oid of the image to remove, as the post&#39;s images report it. | [optional] 
**code** | **str** | An image code.  On attach it replaces any image with that code.  Leave out both code and default_image on attach to add an image used only in the body. | [optional] 
**default_image** | **bool** | True for the post&#39;s default image, which a blogpostimage element and og image use.  On attach it replaces any existing default. | [optional] 
**description** | **str** | Attach only.  Stored with the image and used as its alt text, as plain text. | [optional] 
**filename** | **str** | Attach only.  The image&#39;s name in its address, for example hero.png, with the same extension the upload was requested with.  Letters, digits, dots, hyphens, underscores and parentheses, and not already used by another image on the post. | [optional] 
**key** | **str** | Attach only.  The key files/upload_url returned for the image&#39;s bytes.  A JPEG, PNG, GIF or WebP image.  Attaching redeems the key, so it cannot be used again. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


