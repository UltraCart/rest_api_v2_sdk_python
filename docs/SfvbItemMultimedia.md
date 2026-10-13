# SfvbItemMultimedia


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The image code, which is what an itemimage element&#39;s itemImageCode refers to.  Empty for the default image. | [optional] 
**declared** | **bool** | True when a template declares this code.  A slot that is attached but not declared is an image nothing on the page is asking for. | [optional] 
**default** | **bool** | True for the image an itemimage element with no code renders.  Default is per media type, so an item may have one default image and one default PDF at the same time. | [optional] 
**description** | **str** | The merchant&#39;s description, stored with the image and rendered as its alt text.  When it is empty the render falls back to rekognition_description or to text built from the item&#39;s title, depending on the element, so an empty value here is not an empty alt attribute. | [optional] 
**description_sha256** | **str** | SHA-256 of description (empty when there is none).  Send it as current_sha256 when changing the description so a change made since you read it is not overwritten. | [optional] 
**description_source** | **str** | Where the alt text comes from now.  merchant when description is set, rekognition when only rekognition_description is, none otherwise. | [optional] 
**dimensions** | **str** | Width x height in pixels, when the storage measured the file. | [optional] 
**exclude_from_gallery** | **bool** | True when the storage marks this image as kept out of the item gallery. | [optional] 
**filename** | **str** | The stored file&#39;s name.  Empty when the slot is declared and nothing is attached. | [optional] 
**merchant_item_multimedia_oid** | **int** | The stored image&#39;s id.  Name it to change this image&#39;s description when it has no code. | [optional] 
**rekognition_description** | **str** | The machine description image recognition produced for the stored image, if any.  It is used only while description is empty, and a description written here or in the admin always takes its place. | [optional] 
**type** | **str** | The media type the storage recorded. | [optional] 
**view_url** | **str** | Where the stored image is served.  Absent when nothing is attached to the slot. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


