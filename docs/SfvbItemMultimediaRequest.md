# SfvbItemMultimediaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attach under this image code, the value an itemimage element&#39;s itemImageCode names. | [optional] 
**default** | **bool** | Attach as the item&#39;s default image, which is what an itemimage element with no code renders.  Name exactly one of this or code. | [optional] 
**description** | **str** | Stored with the image and rendered as its alt text.  Left out, the slot keeps the description it already had. | [optional] 
**path** | **str** | Storefront file system path of the image to attach, such as /assets/img/mug-front.jpg.  Upload it with files/upload first.  Unlike a page image this does not have to sit in any particular folder, because an item has no folder of its own - the bytes are copied into the item&#39;s own storage on attach. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


