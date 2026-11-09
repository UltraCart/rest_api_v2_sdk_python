# SfvbTrackingHtmlRenderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_sha256** | **str** | The SHA-256 of the HTML rendered, before rendering, as the slot would store it.  For a draft, the hash a tracking_html.put approval binds. | [optional] 
**html** | **str** | The rendered HTML, with order tokens filled and Velocity run, as the receipt would inject it.  Empty when the slot is empty. | [optional] 
**order_id** | **str** | The test order rendered against. | [optional] 
**provides** | **[str]** | The Velocity references the render provides.  Any other reference the receipt page has is left as written. | [optional] 
**size_bytes** | **int** | The size of html in UTF-8 bytes. | [optional] 
**slot** | **str** | The slot rendered.  Always conversion. | [optional] 
**source** | **str** | stored when the slot&#39;s saved HTML was rendered, draft when the request&#39;s content was. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | What the render left out or could not do, such as tokens it doesn&#39;t fill. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


