# SfvbRenderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Why the render failed.  Always populated when success is false. | [optional] 
**html** | **str** | Rendered HTML. | [optional] 
**pending_translation_count** | **int** | Number of strings still awaiting translation in the requested language. | [optional] 
**success** | **bool** | True when HTML was produced. | [optional] 
**truncated** | **bool** | True when the HTML was cut short. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Quality warnings about the rendered node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


