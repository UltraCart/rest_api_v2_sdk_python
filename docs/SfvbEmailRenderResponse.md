# SfvbEmailRenderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** | True when an unsaved draft was rendered. | [optional] 
**html** | **str** | The HTML body. | [optional] 
**order_id** | **str** | The order the email rendered with, when it used one. | [optional] 
**order_source** | **str** | Where that order came from.  test (the order given), dummy (made up) or none. | [optional] 
**preview_text** | **str** | The preview text an inbox shows after the subject, when the email has one. | [optional] 
**subject** | **str** | The subject line. | [optional] 
**text** | **str** | The plain text body. | [optional] 
**validation** | [**SfvbValidationResponse**](SfvbValidationResponse.md) |  | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Problems a real send would hit, such as a missing required footer token, and placeholders used in place of values a send creates. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


