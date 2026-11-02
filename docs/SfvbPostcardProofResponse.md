# SfvbPostcardProofResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_html** | **str** | The back as the send renders it, after the name tokens are filled. | [optional] 
**back_image_url** | **str** | The back as the PNG image the print vendor prints from.  A public url. | [optional] 
**back_thumbnail_url** | **str** | The print vendor thumbnail of the back. | [optional] 
**front_html** | **str** | The front as the send renders it, after the name tokens are filled. | [optional] 
**front_image_url** | **str** | The front as the PNG image the print vendor prints from.  A public url. | [optional] 
**front_thumbnail_url** | **str** | The print vendor thumbnail of the front. | [optional] 
**order_source** | **str** | Where the order came from.  test for the order_id given, dummy for a made up one, none for no order. | [optional] 
**postcard_uuid** | **str** | The postcard the step mails. | [optional] 
**rendered_pdf_url** | **str** | The print vendor proof PDF of both sides. | [optional] 
**vendor_rendered** | **bool** | True when the print vendor rendered the card, so the image and PDF urls are set. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Where the proof differs from a send, such as a placeholder coupon code or a sample address, and anything that would make a send skip the card. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


